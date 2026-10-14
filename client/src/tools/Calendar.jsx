import React, { useMemo, useState } from 'react';
import Icon from '../Icons.jsx';
import { OFFICIAL, examDates, dayKey, parseDay, today, daysUntil, fmtLong } from './examDates.js';

const WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

export function Countdown({ exam, compact }) {
  const n = daysUntil(exam.date);
  const text = n > 1 ? `${n} days` : n === 1 ? 'Tomorrow' : n === 0 ? 'Today' : 'Done';
  return (
    <div className={`cdown ${exam.tone} ${compact ? 'compact' : ''}`}>
      <span className="cdown-label">{exam.label}</span>
      <b>{text}</b>
      <span className="cdown-date">{fmtLong(exam.date)}</span>
    </div>
  );
}

// Month calendar with exam dates, today, and days you finished an exam.
export default function Calendar({ progress }) {
  const { state, setPref } = progress;
  const exams = examDates(state.prefs);
  const t0 = today();
  const [cursor, setCursor] = useState(() => new Date(t0.getFullYear(), t0.getMonth(), 1));
  const [picked, setPicked] = useState(null);
  const [editing, setEditing] = useState(false);

  const examByDay = Object.fromEntries(exams.map((e) => [e.date, e]));
  const attemptsByDay = useMemo(() => {
    const m = {};
    for (const e of state.exams) { const k = dayKey(new Date(e.finishedAt)); m[k] = (m[k] || 0) + 1; }
    return m;
  }, [state.exams]);

  // 6-week grid starting on Monday
  const first = new Date(cursor);
  const offset = (first.getDay() + 6) % 7;
  const cells = Array.from({ length: 42 }, (_, i) => new Date(cursor.getFullYear(), cursor.getMonth(), 1 - offset + i));
  const rows = cells.slice(35).every((d) => d.getMonth() !== cursor.getMonth()) ? cells.slice(0, 35) : cells;

  const shift = (n) => setCursor((c) => new Date(c.getFullYear(), c.getMonth() + n, 1));
  const jump = (s) => { const d = parseDay(s); setCursor(new Date(d.getFullYear(), d.getMonth(), 1)); setPicked(s); };
  const todayKey = dayKey(t0);
  const sel = picked && {
    exam: examByDay[picked],
    attempts: attemptsByDay[picked] || 0,
    diff: daysUntil(picked),
  };

  return (
    <div className="cal">
      <div className="cdowns">
        {exams.map((e) => <button key={e.key} className="cdown-btn" onClick={() => jump(e.date)} title="Show on calendar"><Countdown exam={e} compact /></button>)}
      </div>

      <div className="cal-head">
        <button className="iconbtn-sq" onClick={() => shift(-1)} aria-label="Previous month"><Icon name="chevron" size={16} style={{ transform: 'rotate(90deg)' }} /></button>
        <strong>{cursor.toLocaleDateString(undefined, { month: 'long', year: 'numeric' })}</strong>
        <button className="iconbtn-sq" onClick={() => shift(1)} aria-label="Next month"><Icon name="chevron" size={16} style={{ transform: 'rotate(-90deg)' }} /></button>
        <button className="linkbtn small" onClick={() => { setCursor(new Date(t0.getFullYear(), t0.getMonth(), 1)); setPicked(todayKey); }}>Today</button>
      </div>

      <div className="cal-grid" role="grid">
        {WEEK.map((w) => <div key={w} className="cal-wd">{w}</div>)}
        {rows.map((d) => {
          const k = dayKey(d);
          const ex = examByDay[k];
          const cls = ['cal-day', d.getMonth() !== cursor.getMonth() && 'out', k === todayKey && 'today', ex && `exam ${ex.tone}`, picked === k && 'picked', d < t0 && 'past'].filter(Boolean).join(' ');
          return (
            <button key={k} className={cls} onClick={() => setPicked(k)} title={ex ? ex.label : undefined} aria-label={`${fmtLong(k)}${ex ? `, ${ex.label}` : ''}`}>
              <span>{d.getDate()}</span>
              {attemptsByDay[k] && <i className="cal-dot" />}
            </button>
          );
        })}
      </div>

      <div className="cal-legend">
        <span><i className="sw prelims" />Prelims</span>
        <span><i className="sw mains" />Mains</span>
        <span><i className="sw today" />Today</span>
        <span><i className="sw dot" />Exam practised</span>
      </div>

      {sel && (
        <div className="cal-info">
          <strong>{fmtLong(picked)}</strong>
          <span className="muted">
            {sel.exam ? `${sel.exam.label} · ` : ''}
            {sel.diff === 0 ? 'today' : sel.diff > 0 ? `in ${sel.diff} day${sel.diff === 1 ? '' : 's'}` : `${-sel.diff} day${sel.diff === -1 ? '' : 's'} ago`}
            {sel.attempts ? ` · ${sel.attempts} practice exam${sel.attempts === 1 ? '' : 's'} finished` : ''}
          </span>
        </div>
      )}

      <div className="cal-edit">
        <button className="linkbtn small" onClick={() => setEditing((v) => !v)}>{editing ? 'Close' : 'Edit exam dates'}</button>
        {editing && (
          <div className="cal-edit-form">
            {exams.map((e) => (
              <label key={e.key}>
                <span>{e.label}</span>
                <input type="date" value={e.date} onChange={(ev) => setPref(e.key, ev.target.value && ev.target.value !== OFFICIAL[e.key] ? ev.target.value : null)} />
              </label>
            ))}
            <p className="fineprint">
              Defaults follow the UPSC ESE 2027 notification (16 Sep 2026): Prelims {fmtLong(OFFICIAL.prelimsDate)}, Mains {fmtLong(OFFICIAL.mainsDate)}. Check upsc.gov.in for changes.
              {exams.some((e) => e.custom) && <> <button className="linkbtn small" onClick={() => exams.forEach((e) => setPref(e.key, null))}>Reset to official dates</button></>}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
