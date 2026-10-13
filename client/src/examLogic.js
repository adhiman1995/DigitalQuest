import { byNumber, shuffle } from './util.js';

// Exam rules, kept free of React so they can be unit-tested.
export const SECONDS_PER_QUESTION = 120;
export const SUBJECT_TEST_SIZE = 150;

// ------------------------------------------------------------------ session logic
// A session is plain JSON so it survives refreshes:
//   { scope, subjectId, chapterId, qids, idx, qStart, startedAt, seconds, answers, flash }
// The timer is derived from `qStart`, so refreshing or leaving the page never resets it.

export function buildSession({ scope, subjectId, chapterId, questions, shuffleChapter }) {
  const pool = questions.filter((q) => q.subjectId === subjectId && (scope === 'subject' || q.chapterId === chapterId));
  const picked = scope === 'subject' ? shuffle(pool).slice(0, SUBJECT_TEST_SIZE) : shuffleChapter ? shuffle(pool) : [...pool].sort(byNumber);
  const now = Date.now();
  return {
    scope, subjectId, chapterId: scope === 'chapter' ? chapterId : null,
    qids: picked.map((q) => q.id), idx: 0, qStart: now, startedAt: now,
    seconds: SECONDS_PER_QUESTION, answers: {}, flash: null,
  };
}

export function finish(s, answers, endMs, early = false) {
  const { idx, qStart, flash, ...rest } = s;
  return { ...rest, answers, id: `ex-${s.startedAt}`, finishedAt: endMs, early };
}

// Record the current question and move on (or finish the exam).
export function step(s, status, chosen, secs, nextStart) {
  const answers = { ...s.answers, [s.qids[s.idx]]: { status, chosen, secs: Math.round(secs) } };
  if (s.idx + 1 >= s.qids.length) return { exam: finish(s, answers, nextStart) };
  const flash = status === 'timeout' ? 'Time ran out on the previous question; it was marked unattempted.' : null;
  return { session: { ...s, answers, idx: s.idx + 1, qStart: nextStart, flash } };
}

// Apply any timeouts that have elapsed (also covers the page having been closed meanwhile).
export function reconcile(s, nowMs) {
  let cur = s, changed = false;
  while (cur && nowMs - cur.qStart >= cur.seconds * 1000) {
    const r = step(cur, 'timeout', null, cur.seconds, cur.qStart + cur.seconds * 1000);
    changed = true;
    if (r.exam) return { exam: r.exam, changed };
    cur = r.session;
  }
  return { session: cur, changed };
}

// ------------------------------------------------------------------ scoring (computed at view time from the current answer keys)
export function score(exam, byId) {
  let answered = 0, skipped = 0, timeout = 0, correct = 0, wrong = 0, verified = 0, secs = 0;
  for (const qid of exam.qids) {
    const a = exam.answers[qid];
    if (!a) continue;
    secs += a.secs || 0;
    if (a.status === 'answered') {
      answered++;
      const key = byId[qid]?.answer;
      if (key) { verified++; a.chosen === key ? correct++ : wrong++; }
    } else if (a.status === 'skipped') skipped++;
    else timeout++;
  }
  const reached = answered + skipped + timeout;
  return { total: exam.qids.length, answered, skipped, timeout, notReached: exam.qids.length - reached, correct, wrong, verified, secs };
}

