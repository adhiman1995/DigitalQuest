// Google sign-in (ID-token flow) + signed session cookie.
const jwt = require('jsonwebtoken');
const { OAuth2Client } = require('google-auth-library');
const store = require('./store');

const isProd = process.env.NODE_ENV === 'production';
const CLIENT_ID = process.env.GOOGLE_CLIENT_ID || '';
const SECRET = process.env.SESSION_SECRET || '';
const COOKIE = 'ese_session';
const MAX_AGE_S = 60 * 60 * 24 * 30;

if (isProd && CLIENT_ID && SECRET.length < 16) {
  console.error('SESSION_SECRET must be set (16+ chars) in production.');
  process.exit(1);
}
// Outside production a throwaway secret keeps local dev working; sessions reset on restart.
const secret = SECRET || require('crypto').randomBytes(32).toString('hex');
const google = CLIENT_ID ? new OAuth2Client(CLIENT_ID) : null;

const parseCookies = (header = '') =>
  Object.fromEntries(header.split(';').map((c) => c.trim().split(/=(.*)/s).slice(0, 2)).filter(([k]) => k));

const cookieOpts = () => ({ httpOnly: true, sameSite: 'lax', secure: isProd, maxAge: MAX_AGE_S * 1000, path: '/' });

function setSession(res, userId) {
  const token = jwt.sign({ sub: userId }, secret, { expiresIn: MAX_AGE_S });
  res.cookie(COOKIE, token, cookieOpts());
}

// Attach req.userId when a valid session cookie is present.
function session(req, _res, next) {
  const token = parseCookies(req.headers.cookie)[COOKIE];
  if (token) {
    try { req.userId = jwt.verify(token, secret).sub; } catch { /* expired or tampered: treat as signed out */ }
  }
  next();
}

const requireUser = (req, res, next) => (req.userId ? next() : res.status(401).json({ error: 'Not signed in' }));

function routes(app) {
  app.get('/api/config', (_req, res) => res.json({ googleClientId: CLIENT_ID || null, devLogin: !isProd }));

  app.get('/api/me', async (req, res) => {
    if (!req.userId) return res.json({ user: null });
    const user = await store.getUser(req.userId);
    res.json({ user });
  });

  app.post('/api/auth/google', async (req, res) => {
    if (!google) return res.status(503).json({ error: 'Google sign-in is not configured on this server' });
    const credential = req.body?.credential;
    if (typeof credential !== 'string' || credential.length > 4096) return res.status(400).json({ error: 'Missing credential' });
    try {
      const ticket = await google.verifyIdToken({ idToken: credential, audience: CLIENT_ID });
      const p = ticket.getPayload();
      if (!p?.sub || !p.email || !p.email_verified) return res.status(403).json({ error: 'Google account email is not verified' });
      const user = { id: `g:${p.sub}`, email: p.email, name: p.name || p.email, picture: p.picture || null };
      await store.upsertUser(user);
      setSession(res, user.id);
      res.json({ user });
    } catch (e) {
      console.warn('Google token rejected:', e.message);
      res.status(401).json({ error: 'Invalid Google credential' });
    }
  });

  // Local development only: lets you test accounts without Google credentials.
  if (!isProd) {
    app.post('/api/auth/dev-login', async (req, res) => {
      const email = String(req.body?.email || 'dev@example.com').slice(0, 100);
      const user = { id: `dev:${email}`, email, name: email.split('@')[0], picture: null };
      await store.upsertUser(user);
      setSession(res, user.id);
      res.json({ user });
    });
  }

  app.post('/api/auth/logout', (_req, res) => {
    res.clearCookie(COOKIE, { ...cookieOpts(), maxAge: undefined });
    res.json({ ok: true });
  });
}

module.exports = { session, requireUser, routes };
