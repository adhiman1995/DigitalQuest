import React, { useMemo, useState } from 'react';
import QuestionCard from './QuestionCard.jsx';
import ToolDock from './tools/ToolDock.jsx';
import { byNumber } from './util.js';

export default function Library({ syllabus, questions: rawQuestions, progress }) {
  const { state, toggle, setResponse, recordResult } = progress;
  const loaded = rawQuestions !== null;
  const questions = useMemo(() => [...(rawQuestions || [])].sort(byNumber), [rawQuestions]);
  const [subject, setSubject] = useState('');
  const [chapter, setChapter] = useState('');
  const [topic, setTopic] = useState('');
  const [year, setYear] = useState('');
  const [q, setQ] = useState(() => decodeURIComponent((location.hash.split('/')[1] || '')));
  const [only, setOnly] = useState(''); // '', 'added', 'marked', 'unsolved'

  const subj = syllabus.subjects.find((s) => s.id === subject);
  const subjectName = (id) => syllabus.subjects.find((s) => s.id === id)?.name || '';
  const inScope = (x) => (!subject || x.subjectId === subject) && (!chapter || x.chapterId === chapter);
  const topics = useMemo(() => [...new Set(questions.filter(inScope).map((x) => x.topic).filter(Boolean))].sort(), [questions, subject, chapter]);
  const years = useMemo(() => [...new Set(questions.map((x) => x.year))].filter(Boolean).sort((a, b) => b - a), [questions]);
  const addedCount = Object.keys(state.added).length;

  const shown = questions.filter((x) => {
    if (!inScope(x)) return false;
    if (topic && x.topic !== topic) return false;
    if (year && String(x.year) !== year) return false;
    if (only === 'added' && !state.added[x.id]) return false;
    if (only === 'reattempt' && !state.reattempt[x.id]) return false;
    if (only === 'marked' && !state.bookmarks[x.id]) return false;
    if (only === 'unsolved' && state.solved[x.id]) return false;
    if (only === 'unattempted' && state.responses[x.id]) return false;
    if (q && !`${x.number} ${x.text} ${x.topic || ''}`.toLowerCase().includes(q.toLowerCase())) return false;
    return true;
  });

  return (
    <section>
      <div className="filters">
        <select value={subject} onChange={(e) => { setSubject(e.target.value); setChapter(''); setTopic(''); }}>
          <option value="">All subjects</option>
          {syllabus.subjects.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}
        </select>
        <select value={chapter} onChange={(e) => { setChapter(e.target.value); setTopic(''); }} disabled={!subj}>
          <option value="">All chapters</option>
          {subj?.chapters.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
        </select>
        <select value={topic} onChange={(e) => setTopic(e.target.value)} disabled={!topics.length}>
          <option value="">All topics</option>
          {topics.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
        <select value={year} onChange={(e) => setYear(e.target.value)}>
          <option value="">All years</option>
          {years.map((y) => <option key={y} value={y}>{y}</option>)}
        </select>
        <input placeholder="Search questions…" value={q} onChange={(e) => setQ(e.target.value)} />
      </div>
      <div className="filters">
        {[['', 'All'], ['unattempted', 'Not attempted'], ['unsolved', 'Unsolved'], ['reattempt', `Reattempt (${Object.keys(state.reattempt).length})`], ['marked', '★ Bookmarked'], ['added', `Practice set (${addedCount})`]].map(([k, label]) => (
          <button key={k} className={only === k ? 'on' : ''} onClick={() => setOnly(k)}>{label}</button>
        ))}
        <span className="muted" style={{ marginLeft: 'auto' }}>{shown.length} of {questions.length} questions</span>
      </div>

      {loaded && questions.length === 0 && (
        <div className="empty">
          <h3>No questions digitized yet</h3>
          <p>Questions appear here once images from <code>question-bank/</code> have been processed.</p>
        </div>
      )}

      {shown.map((x) => (
        <QuestionCard key={x.id} q={x} subjectName={subjectName(x.subjectId)} state={state} toggle={toggle} setResponse={setResponse} recordResult={recordResult} />
      ))}
      <ToolDock progress={progress} />
    </section>
  );
}
