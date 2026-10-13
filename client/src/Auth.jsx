import React, { useCallback, useEffect, useRef, useState } from 'react';

const post = (url, body) =>
  fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body || {}) });

export function useAuth() {
  const [config, setConfig] = useState(null); // { googleClientId, devLogin }
  const [user, setUser] = useState(null);
  const [ready, setReady] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    Promise.all([
      fetch('/api/config').then((r) => r.json()).catch(() => ({})),
      fetch('/api/me').then((r) => r.json()).catch(() => ({ user: null })),
    ]).then(([c, me]) => {
      setConfig(c);
      setUser(me.user || null);
      setReady(true);
    });
  }, []);

  const loginWithGoogle = useCallback(async (credential) => {
    setError('');
    const r = await post('/api/auth/google', { credential }).catch(() => null);
    const j = r && (await r.json().catch(() => ({})));
    if (r?.ok) setUser(j.user);
    else setError(j?.error || 'Sign-in failed. Please try again.');
  }, []);

  const devLogin = useCallback(async (email) => {
    const r = await post('/api/auth/dev-login', { email });
    if (r.ok) setUser((await r.json()).user);
  }, []);

  const logout = useCallback(async () => {
    await post('/api/auth/logout');
    setUser(null);
  }, []);

  return { config, user, ready, error, loginWithGoogle, devLogin, logout };
}

// Google's own sign-in button (Google Identity Services). It returns a signed ID token that the server verifies.
function GoogleButton({ clientId, onCredential }) {
  const box = useRef(null);
  const cb = useRef(onCredential);
  cb.current = onCredential;

  useEffect(() => {
    let cancelled = false;
    const init = () => {
      if (cancelled || !window.google?.accounts?.id || !box.current) return;
      window.google.accounts.id.initialize({ client_id: clientId, callback: (resp) => cb.current(resp.credential), ux_mode: 'popup' });
      window.google.accounts.id.renderButton(box.current, { theme: 'outline', size: 'large', text: 'signin_with', shape: 'pill', logo_alignment: 'left' });
    };
    if (window.google?.accounts?.id) init();
    else {
      let s = document.querySelector('script[data-gsi]');
      if (!s) {
        s = document.createElement('script');
        s.src = 'https://accounts.google.com/gsi/client';
        s.async = true;
        s.defer = true;
        s.dataset.gsi = '1';
        document.head.appendChild(s);
      }
      s.addEventListener('load', init);
    }
    return () => { cancelled = true; };
  }, [clientId]);

  return <div ref={box} className="gbtn" />;
}

const SYNC_LABEL = { local: '', syncing: 'Saving…', saved: '✓ Saved', error: '⚠ Offline: will retry' };

export function AuthBar({ auth, sync, onLogout }) {
  const { config, user, ready, error, loginWithGoogle, devLogin } = auth;
  const [email, setEmail] = useState('');
  if (!ready) return <div className="authbar" />;

  if (user) {
    return (
      <div className="authbar">
        {user.picture ? <img className="avatar" src={user.picture} alt="" referrerPolicy="no-referrer" /> : <span className="avatar ph">{(user.name || '?')[0].toUpperCase()}</span>}
        <div className="who">
          <strong title={user.email}>{user.name}</strong>
          <span className={`sync ${sync}`}>{SYNC_LABEL[sync]}</span>
        </div>
        <button className="small" onClick={onLogout}>Sign out</button>
      </div>
    );
  }

  return (
    <div className="authbar col">
      {config?.googleClientId && <GoogleButton clientId={config.googleClientId} onCredential={loginWithGoogle} />}
      {!config?.googleClientId && config?.devLogin && (
        <form className="devlogin" onSubmit={(e) => { e.preventDefault(); devLogin(email || 'dev@example.com'); }}>
          <input placeholder="dev email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <button className="small">Dev sign-in</button>
        </form>
      )}
      {!config?.googleClientId && !config?.devLogin && <span className="muted">Sign-in is not configured</span>}
      {error && <span className="autherr">{error}</span>}
    </div>
  );
}
