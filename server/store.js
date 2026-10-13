// Persistence for users and their progress.
//  - DATABASE_URL set  -> PostgreSQL (production / Render)
//  - otherwise         -> a JSON file under server/data (local development only)
const fs = require('fs');
const path = require('path');

function postgresStore(url) {
  const { Pool } = require('pg');
  // Render's managed Postgres requires TLS; local Postgres usually does not.
  const ssl = /localhost|127\.0\.0\.1/.test(url) ? false : { rejectUnauthorized: false };
  const pool = new Pool({ connectionString: url, ssl, max: 5 });
  // Several instances can start at once during a deploy; the advisory lock makes schema creation safe.
  const ready = (async () => {
    const c = await pool.connect();
    try {
      await c.query('BEGIN');
      await c.query('SELECT pg_advisory_xact_lock(727401)');
      await c.query(`
        CREATE TABLE IF NOT EXISTS users (
          id         TEXT PRIMARY KEY,
          email      TEXT NOT NULL,
          name       TEXT,
          picture    TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
          last_login TIMESTAMPTZ NOT NULL DEFAULT now()
        )`);
      await c.query(`
        CREATE TABLE IF NOT EXISTS progress (
          user_id    TEXT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
          data       JSONB NOT NULL,
          updated_at BIGINT NOT NULL
        )`);
      await c.query('COMMIT');
    } catch (e) {
      await c.query('ROLLBACK').catch(() => {});
      throw e;
    } finally {
      c.release();
    }
  })();
  return {
    kind: 'postgres',
    ready,
    async upsertUser(u) {
      await pool.query(
        `INSERT INTO users (id, email, name, picture) VALUES ($1,$2,$3,$4)
         ON CONFLICT (id) DO UPDATE SET email=$2, name=$3, picture=$4, last_login=now()`,
        [u.id, u.email, u.name, u.picture]
      );
    },
    async getUser(id) {
      const r = await pool.query('SELECT id, email, name, picture FROM users WHERE id=$1', [id]);
      return r.rows[0] || null;
    },
    async getProgress(id) {
      const r = await pool.query('SELECT data, updated_at FROM progress WHERE user_id=$1', [id]);
      return r.rows[0] ? { data: r.rows[0].data, updatedAt: Number(r.rows[0].updated_at) } : null;
    },
    // Last-write-wins: only accept the write if it is not older than what is stored.
    async putProgress(id, data, updatedAt) {
      const r = await pool.query(
        `INSERT INTO progress (user_id, data, updated_at) VALUES ($1,$2,$3)
         ON CONFLICT (user_id) DO UPDATE SET data=$2, updated_at=$3 WHERE progress.updated_at <= $3
         RETURNING updated_at`,
        [id, data, updatedAt]
      );
      return r.rowCount > 0;
    },
  };
}

function fileStore(file) {
  const load = () => { try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch { return { users: {}, progress: {} }; } };
  const save = (db) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, JSON.stringify(db)); };
  return {
    kind: 'file',
    ready: Promise.resolve(),
    async upsertUser(u) { const db = load(); db.users[u.id] = { ...db.users[u.id], ...u }; save(db); },
    async getUser(id) { return load().users[id] || null; },
    async getProgress(id) { return load().progress[id] || null; },
    async putProgress(id, data, updatedAt) {
      const db = load();
      const cur = db.progress[id];
      if (cur && cur.updatedAt > updatedAt) return false;
      db.progress[id] = { data, updatedAt };
      save(db);
      return true;
    },
  };
}

module.exports = process.env.DATABASE_URL
  ? postgresStore(process.env.DATABASE_URL)
  : fileStore(process.env.DEV_DB_FILE || path.join(__dirname, 'data', 'dev-db.json'));
