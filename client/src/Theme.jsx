import React, { useEffect, useState } from 'react';
import Icon from './Icons.jsx';

const KEY = 'dq-theme';
const systemDark = () => window.matchMedia?.('(prefers-color-scheme: dark)').matches;
const current = () => document.documentElement.getAttribute('data-theme') || (systemDark() ? 'dark' : 'light');

// Light/dark switch. The choice is remembered in this browser; until it is used the system setting applies.
export default function ThemeSwitch() {
  const [theme, setTheme] = useState(current);
  useEffect(() => {
    const mq = window.matchMedia?.('(prefers-color-scheme: dark)');
    const onChange = () => { if (!document.documentElement.hasAttribute('data-theme')) setTheme(current()); };
    mq?.addEventListener?.('change', onChange);
    return () => mq?.removeEventListener?.('change', onChange);
  }, []);
  const toggle = () => {
    const next = theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch { /* storage unavailable */ }
    setTheme(next);
  };
  return (
    <button type="button" className="themeswitch" role="switch" aria-checked={theme === 'dark'} aria-label="Dark theme" onClick={toggle}>
      <span className="track"><Icon name="sun" className="ico sun" size={14} /><Icon name="moon" className="ico moon" size={14} /></span>
      <span className="lbl">{theme === 'dark' ? 'Dark' : 'Light'} theme</span>
    </button>
  );
}
