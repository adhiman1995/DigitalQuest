import React, { useCallback, useEffect, useState } from 'react';
import { evaluate, format } from './calcEngine.js';

// Scientific calculator laid out like the GATE / ESE online virtual calculator.
// The expression is kept as a list of pieces ({ d: shown text, s: engine source }) so ← removes whole tokens.

const P = (d, s = d, kind = 'op') => ({ d, s, kind });
const FN = (d, s) => P(d, s, 'fn'); // starts a fresh expression after "="

// left block: 6 columns
const LEFT = [
  [['Exp', P('E', 'E', 'num')], ['sinh', FN('sinh(', 'sinh(')], ['cosh', FN('cosh(', 'cosh(')], ['tanh', FN('tanh(', 'tanh(')], ['(', FN('(', '(')], [')', P(')', ')')]],
  [['|x|', FN('abs(', 'abs(')], ['sinh⁻¹', FN('sinh⁻¹(', 'asinh(')], ['cosh⁻¹', FN('cosh⁻¹(', 'acosh(')], ['tanh⁻¹', FN('tanh⁻¹(', 'atanh(')], ['log₂x', FN('log₂(', 'log2(')], ['ln', FN('ln(', 'ln(')]],
  [['π', P('π', 'pi', 'num')], ['e', P('e', 'e', 'num')], ['n!', P('!', '!')], ['logᵧx', P(' log base ', ' logbase ')], ['eˣ', FN('e^(', 'e^(')], ['log', FN('log(', 'log(')]],
  [['sin', FN('sin(', 'sin(')], ['cos', FN('cos(', 'cos(')], ['tan', FN('tan(', 'tan(')], ['xʸ', P('^', '^')], ['ʸ√x', P(' yroot ', ' yroot ')], ['10ˣ', FN('10^(', '10^(')]],
  [['sin⁻¹', FN('sin⁻¹(', 'asin(')], ['cos⁻¹', FN('cos⁻¹(', 'acos(')], ['tan⁻¹', FN('tan⁻¹(', 'atan(')], ['x²', P('²', '^2')], ['x³', P('³', '^3')], ['∛', FN('∛(', 'cbrt(')]],
];
const NUM = (n) => [n, P(n, n, 'num')];

export default function Calculator() {
  const [pieces, setPieces] = useState([]);
  const [result, setResult] = useState('0');
  const [error, setError] = useState('');
  const [done, setDone] = useState(false); // last key was "="
  const [deg, setDeg] = useState(true);
  const [mem, setMem] = useState(null);
  const [last, setLast] = useState(0);

  const expr = pieces.map((p) => p.s).join('');

  const push = useCallback((piece) => {
    setError('');
    setPieces((ps) => {
      if (!done) return [...ps, piece];
      // after "=": numbers and functions start over, operators continue from the answer
      if (piece.kind === 'num' || piece.kind === 'fn') return [piece];
      return [P(format(last), format(last), 'num'), piece];
    });
    setDone(false);
  }, [done, last]);

  const calc = useCallback(() => {
    if (!pieces.length) return null;
    try {
      const v = evaluate(expr, { deg });
      setResult(format(v)); setLast(v); setError(''); setDone(true);
      return v;
    } catch (e) {
      setError(e.message); return null;
    }
  }, [pieces, expr, deg]);

  const clear = () => { setPieces([]); setResult('0'); setError(''); setDone(false); };
  const back = () => { setError(''); setDone(false); setPieces((ps) => ps.slice(0, -1)); };
  const negate = () => {
    setError('');
    if (done) { const v = -last; setLast(v); setResult(format(v)); setPieces([P(format(v), format(v), 'num')]); return; }
    setPieces((ps) => (ps[0]?.s === '-(' && ps.at(-1)?.s === ')' ? ps.slice(1, -1) : ps.length ? [P('-(', '-('), ...ps, P(')', ')')] : [P('-', '-')]));
  };
  // memory works on the shown result (evaluating the current expression first if needed)
  const current = () => (done || !pieces.length ? last : calc());
  const memOp = (op) => {
    if (op === 'MC') return setMem(null);
    if (op === 'MR') { if (mem !== null) push(P(format(mem), format(mem), 'num')); return; }
    const v = current();
    if (v === null || v === undefined) return;
    if (op === 'MS') setMem(v);
    if (op === 'M+') setMem((m) => (m ?? 0) + v);
    if (op === 'M-') setMem((m) => (m ?? 0) - v);
  };

  // keyboard input while the calculator is open (ignored while typing in a text field)
  useEffect(() => {
    const onKey = (e) => {
      if (e.target.closest?.('input, textarea, select') || e.metaKey || e.ctrlKey || e.altKey) return;
      const k = e.key;
      let handled = true;
      if (/^[0-9.]$/.test(k)) push(P(k, k, 'num'));
      else if ('+-*/^'.includes(k)) push(P(k === '*' ? '×' : k === '/' ? '÷' : k, k));
      else if (k === '(') push(FN('(', '('));
      else if (k === ')' || k === '!' || k === '%') push(P(k, k));
      else if (k === 'Enter' || k === '=') calc();
      else if (k === 'Backspace') back();
      else if (k === 'Escape' && (pieces.length || error)) clear();
      else handled = false;
      if (handled) e.preventDefault();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }); // re-bind each render so handlers see current state

  const key = (label, onClick, cls = '', extra = {}) => (
    <button key={label} type="button" className={`ck ${cls}`} onClick={onClick} {...extra}>{label}</button>
  );

  return (
    <div className="calc">
      <div className="calc-display" aria-live="polite">
        <div className="calc-expr" title={pieces.map((p) => p.d).join('')}>{pieces.map((p) => p.d).join('') || ' '}</div>
        <div className={`calc-result ${error ? 'err' : ''}`}>{error || result}</div>
        <div className="calc-flags">{mem !== null && <span>M</span>}<span>{deg ? 'DEG' : 'RAD'}</span></div>
      </div>

      <div className="calc-top">
        {key('mod', () => push(P(' mod ', ' mod ')), 'fn')}
        <div className="calc-angle" role="radiogroup" aria-label="Angle unit">
          <label><input type="radio" checked={deg} onChange={() => setDeg(true)} /> Deg</label>
          <label><input type="radio" checked={!deg} onChange={() => setDeg(false)} /> Rad</label>
        </div>
        <div className="calc-mem">{['MC', 'MR', 'MS', 'M+', 'M-'].map((m) => key(m, () => memOp(m), 'mem'))}</div>
      </div>

      <div className="calc-keys">
        <div className="calc-left">
          {LEFT.flat().map(([label, piece]) => key(label, () => push(piece), 'fn'))}
        </div>
        <div className="calc-right">
          {key('←', back, 'ctl', { 'aria-label': 'Backspace' })}
          {key('C', clear, 'ctl danger span2')}
          {key('+/-', negate, 'ctl')}
          {key('√', () => push(FN('√(', 'sqrt(')), 'ctl')}
          {[NUM('7'), NUM('8'), NUM('9')].map(([l, p]) => key(l, () => push(p), 'num'))}
          {key('/', () => push(P('÷', '/')), 'op')}
          {key('%', () => push(P('%', '%')), 'op')}
          {[NUM('4'), NUM('5'), NUM('6')].map(([l, p]) => key(l, () => push(p), 'num'))}
          {key('*', () => push(P('×', '*')), 'op')}
          {key('1/x', () => push(P('⁻¹', '^(-1)')), 'op')}
          {[NUM('1'), NUM('2'), NUM('3')].map(([l, p]) => key(l, () => push(p), 'num'))}
          {key('-', () => push(P('-', '-')), 'op')}
          {key('=', calc, 'eq rows2')}
          {key('0', () => push(P('0', '0', 'num')), 'num span2')}
          {key('.', () => push(P('.', '.', 'num')), 'num')}
          {key('+', () => push(P('+', '+')), 'op')}
        </div>
      </div>
    </div>
  );
}
