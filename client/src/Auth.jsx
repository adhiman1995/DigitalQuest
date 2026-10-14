import React, { useCallback, useEffect, useRef, useState } from 'react';
import Icon from './Icons.jsx';

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
    setError('');
    const r = await post('/api/auth/dev-login', { email }).catch(() => null);
    if (r?.ok) setUser((await r.json()).user);
    else setError('Dev sign-in failed.');
  }, []);

  const logout = useCallback(async () => {
    await post('/api/auth/logout');
    setUser(null);
  }, []);

  return { config, user, ready, error, loginWithGoogle, devLogin, logout };
}

// Google's own sign-in button (Google Identity Services). It returns a signed ID token that the server verifies.
export function GoogleButton({ clientId, onCredential, width = 300 }) {
  const box = useRef(null);
  const cb = useRef(onCredential);
  cb.current = onCredential;

  useEffect(() => {
    let cancelled = false;
    const init = () => {
      if (cancelled || !window.google?.accounts?.id || !box.current) return;
      window.google.accounts.id.initialize({ client_id: clientId, callback: (resp) => cb.current(resp.credential), ux_mode: 'popup' });
      window.google.accounts.id.renderButton(box.current, { theme: 'outline', size: 'large', text: 'continue_with', shape: 'pill', logo_alignment: 'center', width });
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
  }, [clientId, width]);

  return <div ref={box} className="gbtn" />;
}

const SYNC_LABEL = { local: '', syncing: 'Saving…', saved: 'Synced', error: 'Offline: will retry' };

// Account card at the bottom of the sidebar.
export function UserCard({ user, sync, onLogout }) {
  return (
    <div className="usercard">
      {user.picture
        ? <img className="avatar" src={user.picture} alt="" referrerPolicy="no-referrer" />
        : <span className="avatar ph">{(user.name || '?')[0].toUpperCase()}</span>}
      <div className="who">
        <strong title={user.email}>{user.name}</strong>
        <span className={`sync ${sync}`}><i className="sync-dot" />{SYNC_LABEL[sync]}</span>
      </div>
      <button className="iconbtn-sq" onClick={onLogout} title="Sign out" aria-label="Sign out"><Icon name="logout" /></button>
    </div>
  );
}
