// Official ESE 2027 dates as reported from the UPSC notification of 16 Sep 2026.
// Users can override them (stored in progress.prefs); check upsc.gov.in for changes.
export const OFFICIAL = { prelimsDate: '2027-01-31', mainsDate: '2027-06-18' };

export const EXAMS = [
  { key: 'prelimsDate', label: 'ESE Prelims', short: 'Prelims', tone: 'prelims' },
  { key: 'mainsDate', label: 'ESE Mains', short: 'Mains', tone: 'mains' },
];

// 'YYYY-MM-DD' <-> local Date at midnight (no timezone drift)
export const parseDay = (s) => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); };
export const dayKey = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
export const today = () => { const d = new Date(); d.setHours(0, 0, 0, 0); return d; };
export const daysUntil = (s) => Math.round((parseDay(s) - today()) / 86400000);

export function examDates(prefs = {}) {
  return EXAMS.map((e) => ({ ...e, date: prefs[e.key] || OFFICIAL[e.key], custom: !!prefs[e.key] && prefs[e.key] !== OFFICIAL[e.key] }));
}

export const fmtLong = (s) => parseDay(s).toLocaleDateString(undefined, { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' });
