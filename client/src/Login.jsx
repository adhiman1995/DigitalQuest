import React, { useState } from 'react';
import { GoogleButton } from './Auth.jsx';
import ThemeSwitch from './Theme.jsx';
import Icon from './Icons.jsx';

export function Brand({ small }) {
  return (
    <div className={`brand ${small ? 'small' : ''}`}>
      <span className="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="100%" height="100%">
          <rect width="32" height="32" rx="9" fill="currentColor" />
          <path d="M9 9h6.5a7 7 0 0 1 0 14H9z" fill="none" stroke="#fff" strokeWidth="2.6" strokeLinejoin="round" />
          <path d="M19 19l4 4" stroke="#fff" strokeWidth="2.6" strokeLinecap="round" />
        </svg>
      </span>
      <span className="brand-name">Digital<b>Quest</b></span>
    </div>
  );
}

const FEATURES = [
  ['tracker', 'Syllabus coverage', 'Tick off every topic of ESE ECE Stage 1, paper by paper.'],
  ['library', 'Previous-year questions', 'Typeset questions with figures, filters and bookmarks.'],
  ['exam', 'Timed exam mode', 'One question at a time, a clock on each, full review after.'],
  ['devices', 'Synced everywhere', 'Sign in and your progress follows you to every device.'],
];

export default function Login({ auth, stats }) {
  const { config, error, loginWithGoogle, devLogin } = auth;
  const [email, setEmail] = useState('');
  const [busy, setBusy] = useState(false);

  const dev = async (e) => {
    e.preventDefault();
    setBusy(true);
    await devLogin(email || 'dev@example.com');
    setBusy(false);
  };

  return (
    <div className="login">
      <div className="login-theme"><ThemeSwitch /></div>
      <aside className="login-hero">
        <Brand />
        <div className="hero-copy">
          <h1>Prepare for ESE ECE with a plan you can see.</h1>
          <p>Track the syllabus, practise previous-year questions and take timed tests, all in one place.</p>
        </div>
        <ul className="hero-features">
          {FEATURES.map(([icon, title, text]) => (
            <li key={title}>
              <span className="hero-ico"><Icon name={icon} /></span>
              <div><strong>{title}</strong><span>{text}</span></div>
            </li>
          ))}
        </ul>
        {stats && (
          <div className="hero-stats">
            <div><b>{stats.topics}</b><span>topics</span></div>
            <div><b>{stats.subjects}</b><span>subjects</span></div>
            <div><b>{stats.questions}</b><span>questions</span></div>
          </div>
        )}
      </aside>

      <main className="login-main">
        <div className="login-card">
          <div className="login-brand-mobile"><Brand /></div>
          <h2>Welcome to DigitalQuest</h2>
          <p className="muted">Sign in with your Google account to continue.</p>

          <div className="login-actions">
            {config?.googleClientId && <GoogleButton clientId={config.googleClientId} onCredential={loginWithGoogle} width={320} />}
            {!config?.googleClientId && config?.devLogin && (
              <form className="devform" onSubmit={dev}>
                <p className="devnote">Google sign-in isn't configured on this local server (set <code>GOOGLE_CLIENT_ID</code> in <code>.env</code>). Use a test account instead:</p>
                <label htmlFor="dev-email">Email <span className="tag">local dev only</span></label>
                <input id="dev-email" type="email" placeholder="you@example.com" value={email} onChange={(e) => setEmail(e.target.value)} autoFocus />
                <button className="primary block" disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button>
              </form>
            )}
            {!config?.googleClientId && !config?.devLogin && <p className="autherr" role="alert">Sign-in is temporarily unavailable. Please try again later.</p>}
            {error && <p className="autherr" role="alert">{error}</p>}
          </div>

          <p className="fineprint">Your syllabus progress, answers, bookmarks and exam history are saved to your account and sync across your devices.</p>
        </div>
      </main>
    </div>
  );
}
