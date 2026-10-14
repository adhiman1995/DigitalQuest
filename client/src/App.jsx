import React, { useEffect, useMemo, useState } from 'react';
import Dashboard from './Dashboard.jsx';
import Tracker from './Tracker.jsx';
import Library from './Library.jsx';
import Exam from './Exam.jsx';
import ThemeSwitch from './Theme.jsx';
import Reattempt from './Reattempt.jsx';
import Login, { Brand } from './Login.jsx';
import Icon from './Icons.jsx';
import { useProgress } from './useProgress.js';
import { useAuth, UserCard } from './Auth.jsx';

const VIEWS = [
  ['dashboard', 'Dashboard', 'dashboard'],
  ['tracker', 'Coverage tracker', 'tracker'],
  ['library', 'Question library', 'library'],
  ['reattempt', 'Reattempt questions', 'retry'],
  ['exam', 'Exam mode', 'exam'],
];
const viewFromHash = () => VIEWS.find(([id]) => location.hash.startsWith(`#${id}`))?.[0] || 'dashboard';

export default function App() {
  const [syllabus, setSyllabus] = useState(null);
  const [questions, setQuestions] = useState(null);
  const [error, setError] = useState('');
  const [view, setView] = useState(viewFromHash);
  const [focusSubject, setFocusSubject] = useState(null);
  const auth = useAuth();
  const progress = useProgress(auth.user);

  useEffect(() => {
    fetch('/api/syllabus').then((r) => r.json()).then(setSyllabus).catch(() => setError('Could not load syllabus from the server.'));
    fetch('/api/questions').then((r) => r.json()).then(setQuestions).catch(() => setQuestions([]));
  }, []);

  useEffect(() => {
    const onHash = () => setView(viewFromHash());
    window.addEventListener('hashchange', onHash);
    return () => window.removeEventListener('hashchange', onHash);
  }, []);

  const go = (v) => {
    setFocusSubject(null);
    setView(v);
    if (!location.hash.startsWith(`#${v}`)) history.replaceState(null, '', `#${v}`);
    window.scrollTo(0, 0);
  };
  const openSubject = (id) => { go('tracker'); setFocusSubject(id); };

  const signOut = async () => { await progress.clearLocalAfterFlush(); await auth.logout(); };

  const stats = useMemo(() => syllabus && {
    subjects: syllabus.subjects.length,
    topics: syllabus.subjects.reduce((n, s) => n + s.chapters.reduce((m, c) => m + c.topics.length, 0), 0),
    questions: questions?.length ?? '–',
  }, [syllabus, questions]);

  if (error) return <p className="center">{error}</p>;
  if (!syllabus || !auth.ready) return <div className="splash"><Brand /><div className="spinner" /></div>;

  if (!auth.user) return <Login auth={auth} stats={stats} />;

  const inExam = !!progress.state.session;
  const reCount = Object.keys(progress.state.reattempt).length;

  return (
    <div className="shell">
      <aside className="sidebar">
        <Brand small />
        <nav className="sidenav">
          {VIEWS.map(([id, label, icon]) => (
            <button key={id} className={view === id ? 'on' : ''} onClick={() => go(id)} aria-current={view === id ? 'page' : undefined}>
              <Icon name={icon} />
              <span>{label}</span>
              {id === 'reattempt' && reCount > 0 && <span className="navcount">{reCount}</span>}
              {id === 'exam' && inExam && <span className="live-dot" title="Exam in progress" />}
            </button>
          ))}
        </nav>
        <ThemeSwitch />
        <UserCard user={auth.user} sync={progress.sync} onLogout={signOut} />
      </aside>

      <main className="content">
        {view === 'dashboard' && <Dashboard syllabus={syllabus} questions={questions} progress={progress} user={auth.user} go={go} openSubject={openSubject} />}
        {view === 'tracker' && (
          <>
            <PageHead title="Coverage tracker" sub="Tick off topics as you finish them." />
            <Tracker key={focusSubject || 'all'} syllabus={syllabus} progress={progress} initialSubject={focusSubject} />
          </>
        )}
        {view === 'library' && (
          <>
            <PageHead title="Question library" sub="Previous-year questions, filterable by subject, chapter, topic and year." />
            <Library syllabus={syllabus} questions={questions} progress={progress} />
          </>
        )}
        {view === 'reattempt' && (
          <>
            <PageHead title="Reattempt questions" sub="Questions you answered incorrectly. Get one right to unlock its solution and concept." />
            <Reattempt syllabus={syllabus} questions={questions} progress={progress} />
          </>
        )}
        {view === 'exam' && (
          <>
            {!inExam && <PageHead title="Exam mode" sub="Timed, one question at a time." />}
            <Exam syllabus={syllabus} questions={questions} progress={progress} />
          </>
        )}
      </main>
    </div>
  );
}

function PageHead({ title, sub }) {
  return (
    <div className="page-head">
      <div>
        <h1>{title}</h1>
        {sub && <p className="muted">{sub}</p>}
      </div>
    </div>
  );
}
