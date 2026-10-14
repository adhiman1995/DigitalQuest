// Expression engine for the GATE-style calculator. A small tokenizer + precedence-climbing parser
// (no eval), so only arithmetic and the listed functions can ever run.

const FUNCS = {
  sin: (x, d) => Math.sin(d ? (x * Math.PI) / 180 : x),
  cos: (x, d) => Math.cos(d ? (x * Math.PI) / 180 : x),
  tan: (x, d) => {
    if (d && Math.abs(((x % 180) + 180) % 180 - 90) < 1e-12) throw new Error('Math error');
    return Math.tan(d ? (x * Math.PI) / 180 : x);
  },
  asin: (x, d) => toAngle(Math.asin(x), d),
  acos: (x, d) => toAngle(Math.acos(x), d),
  atan: (x, d) => toAngle(Math.atan(x), d),
  sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
  asinh: Math.asinh, acosh: Math.acosh, atanh: Math.atanh,
  ln: Math.log, log: Math.log10, log2: Math.log2,
  sqrt: Math.sqrt, cbrt: Math.cbrt, abs: Math.abs, exp: Math.exp,
};
const toAngle = (r, d) => (d ? (r * 180) / Math.PI : r);

// binary operators: precedence, right-assoc, implementation
const BIN = {
  '+': [1, false, (a, b) => a + b],
  '-': [1, false, (a, b) => a - b],
  '*': [2, false, (a, b) => a * b],
  '/': [2, false, (a, b) => { if (b === 0) throw new Error('Cannot divide by zero'); return a / b; }],
  mod: [2, false, (a, b) => { if (b === 0) throw new Error('Cannot divide by zero'); return a - b * Math.floor(a / b); }],
  '^': [4, true, (a, b) => a ** b],
  yroot: [4, true, (a, b) => (a < 0 && Math.abs(b % 2) === 1 ? -((-a) ** (1 / b)) : a ** (1 / b))],
  logbase: [4, true, (a, b) => Math.log(a) / Math.log(b)],
};

function factorial(n) {
  if (n < 0 || !Number.isInteger(n)) throw new Error('n! needs a whole number ≥ 0');
  if (n > 170) return Infinity;
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
}

export function tokenize(src) {
  const out = [];
  let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (c === ' ') { i++; continue; }
    const num = /^(\d+\.?\d*|\.\d+)(E[+-]?\d+)?/.exec(src.slice(i));
    if (num) { out.push({ t: 'num', v: parseFloat(num[0].replace('E', 'e')) }); i += num[0].length; continue; }
    const word = /^[a-z][a-z0-9]*/.exec(src.slice(i));
    if (word) {
      const w = word[0];
      if (w === 'pi') out.push({ t: 'num', v: Math.PI });
      else if (w === 'e') out.push({ t: 'num', v: Math.E });
      else if (w === 'ans') out.push({ t: 'ans' });
      else if (BIN[w]) out.push({ t: 'op', v: w });
      else if (FUNCS[w]) out.push({ t: 'fn', v: w });
      else throw new Error(`Unknown "${w}"`);
      i += w.length;
      continue;
    }
    if (c === 'π') { out.push({ t: 'num', v: Math.PI }); i++; continue; }
    if ('+-*/^'.includes(c)) { out.push({ t: 'op', v: c }); i++; continue; }
    if (c === '×') { out.push({ t: 'op', v: '*' }); i++; continue; }
    if (c === '÷') { out.push({ t: 'op', v: '/' }); i++; continue; }
    if (c === '(' || c === ')') { out.push({ t: c }); i++; continue; }
    if (c === '!' || c === '%') { out.push({ t: 'post', v: c }); i++; continue; }
    throw new Error(`Unexpected "${c}"`);
  }
  return out;
}

export function evaluate(src, { deg = true, ans = 0 } = {}) {
  const raw = tokenize(src);
  // auto-close open brackets, like the GATE calculator does
  let depth = 0;
  for (const t of raw) {
    if (t.t === '(') depth++;
    else if (t.t === ')' && --depth < 0) throw new Error('Unmatched )');
  }
  for (; depth > 0; depth--) raw.push({ t: ')' });

  // implicit multiplication: 2π, 2(3), (1)(2), 3sin(30), 5!2
  const toks = [];
  const ends = (t) => t && (t.t === 'num' || t.t === 'ans' || t.t === ')' || t.t === 'post');
  const starts = (t) => t && (t.t === 'num' || t.t === 'ans' || t.t === 'fn' || t.t === '(');
  raw.forEach((t, i) => { if (ends(raw[i - 1]) && starts(t)) toks.push({ t: 'op', v: '*' }); toks.push(t); });

  let p = 0;
  const peek = () => toks[p];

  function expr(minPrec) {
    let lhs = unary();
    for (;;) {
      const t = peek();
      if (!t || t.t !== 'op') break;
      const [prec, right, fn] = BIN[t.v];
      if (prec < minPrec) break;
      p++;
      lhs = fn(lhs, expr(right ? prec : prec + 1));
    }
    return lhs;
  }
  // unary minus binds looser than ^ (so -2^2 = -4) but tighter than × and ÷
  function unary() {
    const t = peek();
    if (t?.t === 'op' && (t.v === '-' || t.v === '+')) { p++; const x = expr(3); return t.v === '-' ? -x : x; }
    return primary();
  }
  function primary() {
    const t = toks[p++];
    if (!t) throw new Error('Incomplete expression');
    let v;
    if (t.t === 'num') v = t.v;
    else if (t.t === 'ans') v = ans;
    else if (t.t === '(') { v = expr(0); if (toks[p++]?.t !== ')') throw new Error('Missing )'); }
    else if (t.t === 'fn') v = FUNCS[t.v](peek()?.t === '(' ? primary() : unary(), deg);
    else throw new Error('Syntax error');
    while (peek()?.t === 'post') v = toks[p++].v === '!' ? factorial(v) : v / 100;
    return v;
  }

  const v = expr(0);
  if (p < toks.length) throw new Error('Syntax error');
  if (Number.isNaN(v)) throw new Error('Math error');
  return v;
}

// Display like a scientific calculator: up to 12 significant digits, exponent form when huge/tiny.
export function format(v) {
  if (!Number.isFinite(v)) return v > 0 ? 'Infinity' : v < 0 ? '-Infinity' : 'Math error';
  if (v === 0) return '0';
  const a = Math.abs(v);
  if (a >= 1e12 || a < 1e-9) return v.toExponential(9).replace(/\.?0+e/, 'e').replace('e+', 'E').replace('e-', 'E-');
  return String(parseFloat(v.toPrecision(12)));
}
