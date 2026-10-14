import React, { useState } from 'react';
import Icon from '../Icons.jsx';
import FloatPanel from './FloatPanel.jsx';
import Calculator from './Calculator.jsx';
import Timer, { useTimer, fmtTimer } from './Timer.jsx';
import Calendar from './Calendar.jsx';

const KEY = 'dq-tools-open';
const loadOpen = () => { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch { return {}; } };

// Floating toolbar for practice: GATE-style calculator, timer and exam calendar.
export default function ToolDock({ progress }) {
  const [open, setOpenRaw] = useState(loadOpen);
  const timer = useTimer();
  const setOpen = (k, v) => setOpenRaw((o) => {
    const next = { ...o, [k]: v ?? !o[k] };
    try { localStorage.setItem(KEY, JSON.stringify(next)); } catch { /* ignore */ }
    return next;
  });

  const W = () => window.innerWidth, H = () => window.innerHeight;
  const timerBadge = timer.running || timer.rang || timer.elapsed > 0;

  return (
    <>
      <div className="dock" role="toolbar" aria-label="Practice tools">
        <button className={open.calc ? 'on' : ''} onClick={() => setOpen('calc')} aria-pressed={!!open.calc}>
          <Icon name="calculator" /><span>Calculator</span>
        </button>
        <button className={`${open.timer ? 'on' : ''} ${timer.rang ? 'ring' : ''}`} onClick={() => setOpen('timer')} aria-pressed={!!open.timer}>
          <Icon name="exam" />
          {timerBadge ? <span className="dock-time">{fmtTimer(timer.mode === 'countdown' ? Math.ceil(timer.display) : timer.display)}</span> : <span>Timer</span>}
          {timer.running && <i className="dock-live" />}
        </button>
        <button className={open.cal ? 'on' : ''} onClick={() => setOpen('cal')} aria-pressed={!!open.cal}>
          <Icon name="calendar" /><span>Calendar</span>
        </button>
      </div>

      {open.calc && (
        <FloatPanel title="Scientific calculator" icon="calculator" width={560} className="fp-calc" onClose={() => setOpen('calc', false)}
          initial={() => ({ x: Math.max(8, W() - 560 - 24), y: Math.max(8, H() - 560) })}>
          <Calculator />
        </FloatPanel>
      )}
      {open.timer && (
        <FloatPanel title="Timer" icon="exam" width={300} onClose={() => { setOpen('timer', false); timer.dismiss(); }}
          initial={() => ({ x: Math.max(8, W() - 300 - 24), y: 90 })}>
          <Timer timer={timer} />
        </FloatPanel>
      )}
      {open.cal && (
        <FloatPanel title="Exam calendar" icon="calendar" width={340} onClose={() => setOpen('cal', false)}
          initial={() => ({ x: Math.max(8, W() - 340 - 340), y: 90 })}>
          <Calendar progress={progress} />
        </FloatPanel>
      )}
    </>
  );
}
