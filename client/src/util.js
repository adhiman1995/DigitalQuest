export const LETTERS = 'ABCD';

const order = (n) => (n || '').split('.').map(Number);
export const byNumber = (a, b) => {
  const [a1, a2] = order(a.number), [b1, b2] = order(b.number);
  return a1 - b1 || a2 - b2;
};

export const shuffle = (arr) => {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
};

export const fmtClock = (secs) => {
  const s = Math.max(0, Math.ceil(secs));
  return `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
};

export const fmtDuration = (secs) => {
  const s = Math.round(secs);
  if (s < 60) return `${s}s`;
  const m = Math.floor(s / 60);
  return m < 60 ? `${m}m ${s % 60}s` : `${Math.floor(m / 60)}h ${m % 60}m`;
};
