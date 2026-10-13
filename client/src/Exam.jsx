import React, { useEffect, useMemo, useRef, useState } from 'react';
import { QuestionBody, OptionList } from './QuestionCard.jsx';
import { fmtClock, fmtDuration } from './util.js';

import { SECONDS_PER_QUESTION, SUBJECT_TEST_SIZE, buildSession, finish, step, reconcile, score } from './examLogic.js';

// ------------------------------------------------------------------ root
export default function ExamTab({ syllabus, questions, progress }) {
  const { state, setSession, addExam } = progress;
  const [reviewId, setReviewId] = useState(null);
  const byId = useMemo(() => Object.fromEntries((questions || []).map((q) => [q.id, q])), [questions]);

  if (!questions) return <p className="center">Loading…</p>;

  const start = (cfg) => {
    const s = buildSession({ ...cfg, questions });
    if (!s.qids.length) return;
    setReviewId(null);
    setSession(s);
  };

  if (state.session)
    return <Runner session={state.session} byId={byId} progress={progress} onDone={(id) => setReviewId(id)} />;

  const exam = reviewId && state.exams.find((e) => e.id === reviewId);
  if (exam)
    return (
      <Results
        exam={exam}
        byId={byId}
        syllabus={syllabus}
        onBack={() => setReviewId(null)}
        onRetake={() => start({ scope: exam.scope, subjectId: exam.subjectId, chapterId: exam.chapterId, shuffleChapter: false })}
      />
    );

  return <Setup syllabus={syllabus} questions={questions} progress={progress} onStart={start} onReview={setReviewId} />;
}

// ------------------------------------------------------------------ setup
function Setup({ syllabus, questions, progress, onStart, onReview }) {
  const { state, deleteExam } = progress;
  const counts = useMemo(() => {
    const bySubject = {}, byChapter = {};
    for (const q of questions) {
      bySubject[q.subjectId] = (bySubject[q.subjectId] || 0) + 1;
      byChapter[q.chapterId] = (byChapter[q.chapterId] || 0) + 1;
    }
    return { bySubject, byChapter };
  }, [questions]);

  const withQuestions = syllabus.subjects.filter((s) => counts.bySubject[s.id]);
  const [subjectId, setSubjectId] = useState(withQuestions[0]?.id || '');
  const [scope, setScope] = useState('chapter');
  const subject = syllabus.subjects.find((s) => s.id === subjectId);
  const chapters = subject?.chapters.filter((c) => counts.byChapter[c.id]) || [];
  const [chapterId, setChapterId] = useState('');
  const [shuffleChapter, setShuffleChapter] = useState(false);
  const activeChapter = chapters.find((c) => c.id === chapterId) || chapters[0];

  const poolSize = scope === 'subject' ? counts.bySubject[subjectId] || 0 : counts.byChapter[activeChapter?.id] || 0;
  const n = scope === 'subject' ? Math.min(SUBJECT_TEST_SIZE, poolSize) : poolSize;
  const nameOf = (id) => syllabus.subjects.find((s) => s.id === id)?.name || '';
  const chapterName = (id) => syllabus.subjects.flatMap((s) => s.chapters).find((c) => c.id === id)?.name || '';

  return (
    <section>
      <div className="exam-setup card-plain">
        <h2>Exam mode</h2>
        <ul className="rules">
          <li>Questions appear <strong>one at a time</strong>, each with a <strong>{SECONDS_PER_QUESTION / 60}-minute</strong> timer.</li>
          <li>You can only move on after you <strong>submit an answer</strong> or <strong>skip</strong>. There is no going back.</li>
          <li>When the timer reaches zero, the question is marked unattempted and the next one opens.</li>
          <li>The timer keeps running if you refresh or leave the page.</li>
        </ul>

        <div className="setup-grid">
          <label>Subject
            <select value={subjectId} onChange={(e) => { setSubjectId(e.target.value); setChapterId(''); }}>
              {withQuestions.length === 0 && <option value="">No questions yet</option>}
              {withQuestions.map((s) => <option key={s.id} value={s.id}>{s.name} ({counts.bySubject[s.id]})</option>)}
            </select>
          </label>

          <fieldset>
            <legend>Exam type</legend>
            <label className="radio"><input type="radio" checked={scope === 'chapter'} onChange={() => setScope('chapter')} /> Chapter exam</label>
            <label className="radio"><input type="radio" checked={scope === 'subject'} onChange={() => setScope('subject')} /> Subject exam: random {SUBJECT_TEST_SIZE}-question test</label>
          </fieldset>

          {scope === 'chapter' && (
            <>
              <label>Chapter
                <select value={activeChapter?.id || ''} onChange={(e) => setChapterId(e.target.value)}>
                  {chapters.map((c) => <option key={c.id} value={c.id}>{c.name} ({counts.byChapter[c.id]})</option>)}
                </select>
              </label>
              <label className="radio"><input type="checkbox" checked={shuffleChapter} onChange={(e) => setShuffleChapter(e.target.checked)} /> Shuffle question order</label>
            </>
          )}
        </div>

        <p className="muted">
          {n} question{n === 1 ? '' : 's'} · up to {fmtDuration(n * SECONDS_PER_QUESTION)} in total
          {scope === 'subject' && poolSize < SUBJECT_TEST_SIZE && poolSize > 0 && ` · only ${poolSize} questions exist for this subject so far, so the test uses all of them in random order`}
        </p>
        <button className="primary" disabled={!n} onClick={() => onStart({ scope, subjectId, chapterId: activeChapter?.id, shuffleChapter })}>
          Start exam
        </button>
      </div>

      {state.exams.length > 0 && (
        <div className="exam-history">
          <h3>Previous attempts</h3>
          {[...state.exams].reverse().map((e) => {
            const sc = score(e, Object.fromEntries(questions.map((q) => [q.id, q])));
            return (
              <div key={e.id} className="hist-row">
                <div>
                  <strong>{e.scope === 'subject' ? `${nameOf(e.subjectId)} · random test` : `${nameOf(e.subjectId)} · ${chapterName(e.chapterId)}`}</strong>
                  <div className="muted">{new Date(e.finishedAt).toLocaleString()} · {sc.answered} answered, {sc.skipped + sc.timeout} unattempted of {sc.total}{e.early ? ' · ended early' : ''}</div>
                </div>
                <div className="hist-actions">
                  <button onClick={() => onReview(e.id)}>Review</button>
                  <button className="linkbtn small" onClick={() => window.confirm('Delete this attempt?') && deleteExam(e.id)}>delete</button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </section>
  );
}

// ------------------------------------------------------------------ runner
function Runner({ session, byId, progress, onDone }) {
  const { setSession, addExam } = progress;
  const sessionRef = useRef(session);
  sessionRef.current = session;
  const [now, setNow] = useState(Date.now());

  const apply = (r) => {
    if (r.exam) { addExam(r.exam); setSession(null); onDone(r.exam.id); }
    else setSession(r.session);
  };

  // tick: updates the clock and applies timeouts (also right after mount, to catch time spent away)
  useEffect(() => {
    const tick = () => {
      const t = Date.now();
      setNow(t);
      const r = reconcile(sessionRef.current, t);
      if (r.changed) apply(r);
    };
    tick();
    const id = setInterval(tick, 250);
    return () => clearInterval(id);
  }, []);

  const q = byId[session.qids[session.idx]];
  const remaining = Math.max(0, session.seconds - (now - session.qStart) / 1000);
  const total = session.qids.length;

  const submit = (choice) => apply(step(session, 'answered', choice, (Date.now() - session.qStart) / 1000, Date.now()));
  const skip = () => apply(step(session, 'skipped', null, (Date.now() - session.qStart) / 1000, Date.now()));
  const endEarly = () => {
    if (!window.confirm('End the exam now? Remaining questions will not be counted.')) return;
    apply({ exam: finish(session, session.answers, Date.now(), true) });
  };

  if (!q) return <p className="center">This exam references questions that no longer exist. <button onClick={() => setSession(null)}>Discard exam</button></p>;

  return (
    <section className="exam-run">
      <div className="exam-bar">
        <div>
          <strong>Question {session.idx + 1} of {total}</strong>
          <div className="bar"><span style={{ width: `${(session.idx / total) * 100}%` }} /></div>
        </div>
        <div className={`timer ${remaining <= 10 ? 'danger' : remaining <= 30 ? 'warn' : ''}`} aria-live="off" title="Time left for this question">
          {fmtClock(remaining)}
        </div>
      </div>
      <div className="timebar"><span style={{ width: `${(remaining / session.seconds) * 100}%` }} /></div>
      {session.flash && <div className="flash">{session.flash}</div>}

      <QuestionPane key={session.idx} q={q} onSubmit={submit} onSkip={skip} onEnd={endEarly} />
    </section>
  );
}

function QuestionPane({ q, onSubmit, onSkip, onEnd }) {
  const [choice, setChoice] = useState(null);
  return (
    <article className="qcard">
      <QuestionBody q={q} />
      <OptionList q={q} selected={choice} onSelect={setChoice} />
      <footer className="qfoot">
        <button className="linkbtn small" onClick={onEnd}>End exam</button>
        <div className="exam-actions">
          <button onClick={onSkip}>Skip</button>
          <button className="primary" disabled={!choice} onClick={() => onSubmit(choice)}>Submit answer →</button>
        </div>
      </footer>
    </article>
  );
}

// ------------------------------------------------------------------ results
function Results({ exam, byId, syllabus, onBack, onRetake }) {
  const sc = score(exam, byId);
  const nameOf = (id) => syllabus.subjects.find((s) => s.id === id)?.name || '';
  const chapter = syllabus.subjects.flatMap((s) => s.chapters).find((c) => c.id === exam.chapterId);
  const unverified = sc.answered - sc.verified;
  const pct = sc.verified ? Math.round((sc.correct / sc.verified) * 100) : null;
  const [rf, setRf] = useState('reached');
  const verdictOf = (q, a) => (a?.status === 'answered' && q.answer ? (a.chosen === q.answer ? 'correct' : 'wrong') : null);
  const FILTERS = [
    ['reached', 'Reached', (q, a) => !!a],
    ['answered', 'Answered', (q, a) => a?.status === 'answered'],
    ['unattempted', 'Skipped / timed out', (q, a) => a && a.status !== 'answered'],
    ['wrong', 'Incorrect', (q, a) => verdictOf(q, a) === 'wrong'],
    ['all', 'All questions', () => true],
  ];
  const keep = FILTERS.find((f) => f[0] === rf)[2];

  return (
    <section>
      <div className="results-head">
        <div>
          <h2>Results</h2>
          <p className="muted">{nameOf(exam.subjectId)} · {exam.scope === 'subject' ? 'random test' : chapter?.name} · {new Date(exam.finishedAt).toLocaleString()}{exam.early ? ' · ended early' : ''}</p>
        </div>
        <div className="actions">
          <button onClick={onBack}>Back</button>
          <button className="primary" onClick={onRetake}>Retake</button>
        </div>
      </div>

      <div className="stats">
        <Stat label="Questions" value={sc.total} />
        <Stat label="Answered" value={sc.answered} />
        <Stat label="Skipped" value={sc.skipped} />
        <Stat label="Timed out" value={sc.timeout} />
        {sc.notReached > 0 && <Stat label="Not reached" value={sc.notReached} />}
        <Stat label="Time spent" value={fmtDuration(sc.secs)} />
        <Stat label="Correct" value={sc.verified ? `${sc.correct}/${sc.verified}` : '–'} accent={pct !== null} sub={pct !== null ? `${pct}%` : undefined} />
      </div>
      <p className="muted">
        {sc.verified
          ? `Correct/incorrect is counted only for the ${sc.verified} answered question${sc.verified === 1 ? '' : 's'} that ${sc.verified === 1 ? 'has' : 'have'} a verified answer key.`
          : 'No answered question has a verified answer key yet, so correctness cannot be scored.'}
        {unverified > 0 && sc.verified > 0 ? ` ${unverified} other answered question${unverified === 1 ? ' has' : 's have'} no key yet.` : ''}
      </p>

      <h3>Review</h3>
      <div className="review-filters">
        {FILTERS.map(([k, label]) => <button key={k} className={rf === k ? 'on' : ''} onClick={() => setRf(k)}>{label}</button>)}
      </div>
      {exam.qids.map((qid, i) => {
        const q = byId[qid], a = exam.answers[qid];
        if (!q || !keep(q, a)) return null;
        const status = !a ? 'not reached' : a.status === 'timeout' ? 'timed out' : a.status;
        const verdict = a?.status === 'answered' && q.answer ? (a.chosen === q.answer ? 'correct' : 'wrong') : null;
        return (
          <article className="qcard" key={qid}>
            <header className="qhead">
              <h3 className="qnum">Q{i + 1}</h3>
              <span className={`status ${verdict || status.replace(' ', '-')}`}>{verdict === 'correct' ? '✓ correct' : verdict === 'wrong' ? '✗ incorrect' : status}</span>
              {q.year && <span className="yearchip">ESE-{q.year}</span>}
              <span className="qpath">{q.number} · {q.topic}</span>
              {a?.secs !== undefined && <span className="muted">{fmtDuration(a.secs)}</span>}
            </header>
            <QuestionBody q={q} />
            <OptionList q={q} selected={a?.chosen || null} correct={q.answer} showCorrect />
            {!q.answer && a?.chosen && <p className="muted">You chose ({a.chosen.toLowerCase()}). This question has no verified answer key yet.</p>}
          </article>
        );
      })}
    </section>
  );
}

function Stat({ label, value, sub, accent }) {
  return (
    <div className={`stat ${accent ? 'accent' : ''}`}>
      <div className="stat-value">{value}{sub && <small> {sub}</small>}</div>
      <div className="stat-label">{label}</div>
    </div>
  );
}
