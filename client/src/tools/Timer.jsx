import React, { useEffect, useRef, useState } from 'react';
import { fmtClock } from '../util.js';

const KEY = 'dq-timer-v1';
const PRESETS = [1, 2, 5, 10, 15, 30, 60];
const INITIAL = { mode: 'countdown', duration: 120, running: false, startedAt: 0, banked: 0, laps: [] };

const load = () => { try { return { ...INITIAL, ...JSON.parse(localStorage.getItem(KEY) || '{}') }; } catch { return { ...INITIAL }; } };

// seconds elapsed in the current run
const elapsedOf = (t, now) => t.banked + (t.running ? (now - t.startedAt) / 1000 : 0);

function beep() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    [0, 0.25, 0.5].forEach((at) => {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.frequency.value = 880; o.connect(g); g.connect(ctx.destination);
      g.gain.setValueAtTime(0.0001, ctx.currentTime + at);
      g.gain.exponentialRampToValueAtTime(0.25, ctx.currentTime + at + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + at + 0.2);
      o.start(ctx.currentTime + at); o.stop(ctx.currentTime + at + 0.22);
    });
  } catch { /* audio unavailable */ }
}

// Lives in the dock (not the panel) so the timer keeps going while its window is closed.
export function useTimer() {
  const [t, setT] = useState(load);
  const [now, setNow] = useState(Date.now());
  const [rang, setRang] = useState(false);
  const fired = useRef(false);

  useEffect(() => { try { localStorage.setItem(KEY, JSON.stringify(t)); } catch { /* ignore */ } }, [t]);
  useEffect(() => {
    if (!t.running) return undefined;
    const id = setInterval(() => setNow(Date.now()), 200);
    return () => clearInterval(id);
  }, [t.running]);

  const elapsed = elapsedOf(t, now);
  const remaining = Math.max(0, t.duration - elapsed);
  const finished = t.mode === 'countdown' && t.running && remaining <= 0;

  useEffect(() => {
    if (finished && !fired.current) {
      fired.current = true;
      beep();
      setRang(true);
      setT((x) => ({ ...x, running: false, banked: x.duration }));
    }
  }, [finished]);

  const api = {
    ...t, elapsed, remaining, rang,
    display: t.mode === 'countdown' ? remaining : elapsed,
    start: () => { fired.current = false; setRang(false); setNow(Date.now()); setT((x) => ({ ...x, running: true, startedAt: Date.now(), banked: x.mode === 'countdown' && x.banked >= x.duration ? 0 : x.banked })); },
    pause: () => { const n = Date.now(); setNow(n); setT((x) => ({ ...x, running: false, banked: elapsedOf(x, n) })); },
    reset: () => { fired.current = false; setRang(false); setT((x) => ({ ...x, running: false, banked: 0, laps: [] })); },
    lap: () => { const n = Date.now(); setT((x) => ({ ...x, laps: [elapsedOf(x, n), ...x.laps].slice(0, 30) })); },
    setMode: (mode) => { setRang(false); setT((x) => ({ ...INITIAL, duration: x.duration, mode })); },
    setDuration: (secs) => { fired.current = false; setRang(false); setT((x) => ({ ...x, duration: secs, running: false, banked: 0 })); },
    dismiss: () => setRang(false),
  };
  return api;
}

const fmtLong = (secs) => {
  const s = Math.max(0, Math.floor(secs));
  return s >= 3600 ? `${Math.floor(s / 3600)}:${fmtClock(s % 3600)}` : fmtClock(s);
};
export { fmtLong as fmtTimer };

export default function Timer({ timer: t }) {
  const [custom, setCustom] = useState('');
  const pct = t.mode === 'countdown' ? (t.duration ? (t.remaining / t.duration) * 100 : 0) : 100;
  const R = 74, C = 2 * Math.PI * R;
  const state = t.rang ? 'done' : t.mode === 'countdown' && t.running && t.remaining <= 10 ? 'danger' : t.mode === 'countdown' && t.running && t.remaining <= 30 ? 'warn' : '';
  const idle = !t.running && t.elapsed === 0;

  return (
    <div className="timerw">
      <div className="seg full" role="tablist" aria-label="Timer mode">
        <button role="tab" aria-selected={t.mode === 'countdown'} className={t.mode === 'countdown' ? 'on' : ''} onClick={() => t.setMode('countdown')}>Countdown</button>
        <button role="tab" aria-selected={t.mode === 'stopwatch'} className={t.mode === 'stopwatch' ? 'on' : ''} onClick={() => t.setMode('stopwatch')}>Stopwatch</button>
      </div>

      <div className={`tdial ${state}`}>
        <svg viewBox="0 0 170 170" width="170" height="170" aria-hidden="true">
          <circle cx="85" cy="85" r={R} className="tdial-track" />
          <circle cx="85" cy="85" r={R} className="tdial-fill" strokeDasharray={C} strokeDashoffset={C * (1 - pct / 100)} transform="rotate(-90 85 85)" />
        </svg>
        <div className="tdial-time">
          <b>{fmtLong(t.mode === 'countdown' ? Math.ceil(t.display) : t.display)}</b>
          <span>{t.rang ? "Time's up" : t.running ? 'running' : idle ? (t.mode === 'countdown' ? 'ready' : 'press start') : 'paused'}</span>
        </div>
      </div>

      {t.mode === 'countdown' && (
        <div className="tpresets">
          {PRESETS.map((m) => (
            <button key={m} className={!t.running && t.duration === m * 60 ? 'on' : ''} disabled={t.running} onClick={() => t.setDuration(m * 60)}>{m < 60 ? `${m}m` : '1h'}</button>
          ))}
          <form onSubmit={(e) => { e.preventDefault(); const m = parseFloat(custom); if (m > 0 && m <= 600) { t.setDuration(Math.round(m * 60)); setCustom(''); } }}>
            <input type="number" min="0.5" max="600" step="0.5" placeholder="min" value={custom} onChange={(e) => setCustom(e.target.value)} disabled={t.running} aria-label="Custom minutes" />
          </form>
        </div>
      )}

      <div className="tctl">
        <button onClick={t.reset} disabled={idle && !t.laps.length}>Reset</button>
        {t.mode === 'stopwatch' && <button onClick={t.lap} disabled={!t.running}>Lap</button>}
        {t.running
          ? <button className="primary" onClick={t.pause}>Pause</button>
          : <button className="primary" onClick={t.start}>{idle || t.rang ? 'Start' : 'Resume'}</button>}
      </div>

      {t.mode === 'stopwatch' && t.laps.length > 0 && (
        <ol className="laps">
          {t.laps.map((l, i) => {
            const prev = t.laps[i + 1] ?? 0;
            return <li key={t.laps.length - i}><span>Q{t.laps.length - i}</span><span>{fmtLong(l - prev)}</span><span className="muted">{fmtLong(l)}</span></li>;
          })}
        </ol>
      )}
      {t.mode === 'stopwatch' && <p className="fineprint">Tip: press <b>Lap</b> after each question to see how long it took.</p>}
    </div>
  );
}
