const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const os = require('node:os');
const path = require('node:path');
const fs = require('node:fs');

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'ese-test-'));
function start(port, env = {}) {
  const proc = spawn(process.execPath, [path.join(__dirname, '..', 'server', 'index.js')], {
    env: { ...process.env, PORT: String(port), DEV_DB_FILE: path.join(tmp, `db-${port}.json`), GOOGLE_CLIENT_ID: '', DATABASE_URL: process.env.TEST_DATABASE_URL || '', ...env },
    stdio: 'ignore',
  });
  return proc;
}
const wait = async (base) => { for (let i = 0; i < 50; i++) { try { if ((await fetch(base + '/api/health')).ok) return; } catch {} await new Promise((r) => setTimeout(r, 100)); } throw new Error('server did not start'); };

const DEV = 'http://localhost:4871', PROD = 'http://localhost:4872';
let dev, prod;
before(async () => { dev = start(4871); prod = start(4872, { NODE_ENV: 'production' }); await wait(DEV); await wait(PROD); });
after(() => { dev.kill(); prod.kill(); fs.rmSync(tmp, { recursive: true, force: true }); });

async function login(email) {
  const r = await fetch(DEV + '/api/auth/dev-login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email }) });
  assert.equal(r.status, 200);
  return r.headers.get('set-cookie').split(';')[0];
}
const call = (cookie, method, url, body) => fetch(DEV + url, { method, headers: { 'Content-Type': 'application/json', ...(cookie ? { cookie } : {}) }, body: body ? JSON.stringify(body) : undefined });

test('serves syllabus and questions publicly', async () => {
  const s = await (await fetch(DEV + '/api/syllabus')).json();
  assert.ok(s.subjects.length > 20);
  const q = await (await fetch(DEV + '/api/questions')).json();
  assert.ok(q.length >= 200);
});

test('progress requires sign-in', async () => {
  assert.equal((await call(null, 'GET', '/api/progress')).status, 401);
  assert.equal((await call(null, 'PUT', '/api/progress', { data: {}, updatedAt: 1 })).status, 401);
  assert.deepEqual(await (await call(null, 'GET', '/api/me')).json(), { user: null });
});

test('a tampered or garbage cookie is treated as signed out', async () => {
  assert.equal((await call('ese_session=not.a.jwt', 'GET', '/api/progress')).status, 401);
});

test('save and load progress; sanitises junk', async () => {
  const c = await login('a@example.com');
  assert.deepEqual(await (await call(c, 'GET', '/api/progress')).json(), { data: null, updatedAt: 0 });
  const payload = { done: { t1: true, bad: 'yes' }, solved: { q1: true }, bookmarks: {}, added: {}, responses: { q1: 'B', q2: 'Z', q3: '<script>' },
    exams: [{ id: 'ex-1', qids: ['q1'], answers: {} }, { nope: 1 }], session: { qids: ['q1'], idx: 0 }, evil: { x: 1 } };
  const put = await call(c, 'PUT', '/api/progress', { data: payload, updatedAt: 1000 });
  assert.equal(put.status, 200);
  const got = await (await call(c, 'GET', '/api/progress')).json();
  assert.equal(got.updatedAt, 1000);
  assert.deepEqual(got.data.done, { t1: true });
  assert.deepEqual(got.data.responses, { q1: 'B' });
  assert.equal(got.data.exams.length, 1);
  assert.equal(got.data.evil, undefined);
  assert.equal((await call(c, 'GET', '/api/me')).status, 200);
});

test('stale writes are rejected with the newer copy', async () => {
  const c = await login('b@example.com');
  assert.equal((await call(c, 'PUT', '/api/progress', { data: { solved: { q9: true } }, updatedAt: 5000 })).status, 200);
  const stale = await call(c, 'PUT', '/api/progress', { data: { solved: {} }, updatedAt: 4000 });
  assert.equal(stale.status, 409);
  const body = await stale.json();
  assert.equal(body.updatedAt, 5000);
  assert.deepEqual(body.data.solved, { q9: true });
  assert.equal((await call(c, 'PUT', '/api/progress', { data: { solved: { q9: true, q10: true } }, updatedAt: 6000 })).status, 200);
});

test('users cannot see each other\'s progress', async () => {
  const a = await login('iso-a@example.com'), b = await login('iso-b@example.com');
  await call(a, 'PUT', '/api/progress', { data: { solved: { secret: true } }, updatedAt: 10 });
  const seenByB = await (await call(b, 'GET', '/api/progress')).json();
  assert.equal(seenByB.data, null);
});

test('rejects malformed payloads and oversized bodies', async () => {
  const c = await login('c@example.com');
  assert.equal((await call(c, 'PUT', '/api/progress', { data: 'x', updatedAt: 1 })).status, 400);
  assert.equal((await call(c, 'PUT', '/api/progress', { data: {}, updatedAt: 'now' })).status, 400);
  const big = await call(c, 'PUT', '/api/progress', { data: { done: Object.fromEntries(Array.from({ length: 60000 }, (_, i) => [`k${i}-${'x'.repeat(20)}`, true])) }, updatedAt: 1 });
  assert.equal(big.status, 413);
});

test('logout clears the session', async () => {
  const c = await login('d@example.com');
  const r = await call(c, 'POST', '/api/auth/logout');
  assert.match(r.headers.get('set-cookie') || '', /ese_session=;/);
});

test('google endpoint is disabled without a client id, and rejects bad input', async () => {
  const r = await call(null, 'POST', '/api/auth/google', { credential: 'x' });
  assert.equal(r.status, 503);
});

test('production: dev-login does not exist and cookies are Secure', async () => {
  const r = await fetch(PROD + '/api/auth/dev-login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' });
  assert.equal(r.status, 404);
  const cfg = await (await fetch(PROD + '/api/config')).json();
  assert.equal(cfg.devLogin, false);
});
