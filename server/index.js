const path = require('path');
const fs = require('fs');
const express = require('express');
const compression = require('compression');
const { subjects, PAPERS } = require('./data/syllabus');
const store = require('./store');
const auth = require('./auth');

const app = express();
const PORT = process.env.PORT || 3001;
const DATA_DIR = path.join(__dirname, 'data');
const QUESTIONS_FILE = path.join(DATA_DIR, 'questions.json');

app.set('trust proxy', 1); // Render terminates TLS in front of the app
app.disable('x-powered-by');
app.use((_req, res, next) => {
  res.set({ 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'strict-origin-when-cross-origin', 'X-Frame-Options': 'DENY' });
  next();
});
app.use(compression());
app.use(express.json({ limit: '1mb' }));
app.use(auth.session);

// Questions are static for the life of the process.
let questionsCache = null;
const questions = () => (questionsCache ??= JSON.parse(fs.readFileSync(QUESTIONS_FILE, 'utf8')));

app.get('/api/health', (_req, res) => res.json({ ok: true, db: store.kind }));
app.get('/api/syllabus', (_req, res) => res.json({ papers: PAPERS, subjects }));
app.get('/api/questions', (_req, res) => {
  res.set('Cache-Control', 'public, max-age=300');
  res.json(questions());
});

auth.routes(app);

// ---------------------------------------------------------------- progress
const MAPS = ['done', 'solved', 'bookmarks', 'added', 'responses', 'results', 'reattempt', 'revealed'];

// Accept only the expected shape so a client can never store arbitrary junk.
function clean(d) {
  if (!d || typeof d !== 'object') return null;
  const out = { exams: [], session: null, prefs: {} };
  for (const k of MAPS) {
    const m = d[k];
    out[k] = {};
    if (m && typeof m === 'object' && !Array.isArray(m)) {
      for (const [id, v] of Object.entries(m).slice(0, 20000)) {
        if (k === 'responses' ? /^[A-D]$/.test(v) : v === true) out[k][String(id).slice(0, 200)] = v;
      }
    }
  }
  if (Array.isArray(d.exams)) out.exams = d.exams.filter((e) => e && typeof e.id === 'string' && Array.isArray(e.qids) && e.answers && typeof e.answers === 'object').slice(-200);
  if (d.session && typeof d.session === 'object' && Array.isArray(d.session.qids)) out.session = d.session;
  // user settings: only exam dates (YYYY-MM-DD) for now
  if (d.prefs && typeof d.prefs === 'object') {
    for (const k of ['prelimsDate', 'mainsDate']) if (typeof d.prefs[k] === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(d.prefs[k])) out.prefs[k] = d.prefs[k];
  }
  return out;
}

app.get('/api/progress', auth.requireUser, async (req, res) => {
  res.set('Cache-Control', 'no-store');
  res.json((await store.getProgress(req.userId)) || { data: null, updatedAt: 0 });
});

app.put('/api/progress', auth.requireUser, async (req, res) => {
  const data = clean(req.body?.data);
  const updatedAt = Number(req.body?.updatedAt);
  if (!data || !Number.isFinite(updatedAt)) return res.status(400).json({ error: 'Invalid progress payload' });
  const ok = await store.putProgress(req.userId, data, updatedAt);
  if (ok) return res.json({ ok: true, updatedAt });
  // A newer copy exists (another device): tell the client to adopt it.
  res.status(409).json({ error: 'Stale write', ...(await store.getProgress(req.userId)) });
});

app.use('/api', (_req, res) => res.status(404).json({ error: 'Not found' }));

const CLIENT_DIST = path.join(__dirname, '..', 'client', 'dist');
if (fs.existsSync(CLIENT_DIST)) {
  app.use(express.static(CLIENT_DIST, { maxAge: '1h', index: false }));
  app.get('*', (_req, res) => res.sendFile(path.join(CLIENT_DIST, 'index.html')));
}

app.use((err, _req, res, _next) => {
  console.error(err);
  res.status(err.status || 500).json({ error: err.status === 413 ? 'Payload too large' : 'Server error' });
});

store.ready
  .then(() => app.listen(PORT, () => console.log(`ESE tracker on :${PORT} (storage: ${store.kind})`)))
  .catch((e) => { console.error('Database connection failed:', e.message); process.exit(1); });
