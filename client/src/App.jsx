import React, { useEffect, useMemo, useState } from 'react';
import Tracker from './Tracker.jsx';
import Library from './Library.jsx';
import Exam from './Exam.jsx';
import { useProgress } from './useProgress.js';
import { useAuth, AuthBar } from './Auth.jsx';

const initialView = () => (location.hash.startsWith('#library') ? 'library' : location.hash.startsWith('#exam') ? 'exam' : 'tracker');

export default function App() {
  const [syllabus, setSyllabus] = useState(null);
  const [questions, setQuestions] = useState(null);
  const [error, setError] = useState('');
  const [view, setView] = useState(initialView);
  const auth = useAuth();
  const progress = useProgress(auth.user);
  const signOut = async () => { await progress.clearLocalAfterFlush(); await auth.logout(); };

  useEffect(() => {
    fetch('/api/syllabus').then((r) => r.json()).then(setSyllabus).catch(() => setError('Could not load syllabus from the server.'));
    fetch('/api/questions').then((r) => r.json()).then(setQuestions).catch(() => setQuestions([]));
  }, []);

  const totals = useMemo(() => {
    if (!syllabus) return { done: 0, total: 0 };
    let total = 0, done = 0;
    for (const s of syllabus.subjects)
      for (const c of s.chapters)
        for (const t of c.topics) {
          total++;
          if (progress.state.done[t.id]) done++;
        }
    return { done, total };
  }, [syllabus, progress.state.done]);

  if (error) return <p className="center">{error}</p>;
  if (!syllabus) return <p className="center">Loading…</p>;

  const pct = totals.total ? Math.round((totals.done / totals.total) * 100) : 0;
  const inExam = !!progress.state.session;

  return (
    <div className="app">
      <header>
        <div>
          <h1>ESE ECE · Stage 1</h1>
          <p className="muted">
            {totals.done}/{totals.total} topics covered · {pct}% overall
          </p>
        </div>
        <AuthBar auth={auth} sync={progress.sync} onLogout={signOut} />
        <nav>
          <button className={view === 'tracker' ? 'on' : ''} onClick={() => setView('tracker')}>Coverage tracker</button>
          <button className={view === 'library' ? 'on' : ''} onClick={() => setView('library')}>Question library</button>
          <button className={view === 'exam' ? 'on' : ''} onClick={() => setView('exam')}>
            Exam mode{inExam && <span className="live-dot" title="Exam in progress" />}
          </button>
        </nav>
      </header>
      {auth.ready && !auth.user && (auth.config?.googleClientId || auth.config?.devLogin) && (
        <p className="guestnote">You're browsing as a guest: progress is saved on this device only. Sign in to keep it across devices.</p>
      )}
      <div className="bar big"><span style={{ width: `${pct}%` }} /></div>

      {view === 'tracker' && <Tracker syllabus={syllabus} progress={progress} />}
      {view === 'library' && <Library syllabus={syllabus} questions={questions} progress={progress} />}
      {view === 'exam' && <Exam syllabus={syllabus} questions={questions} progress={progress} />}
    </div>
  );
}
