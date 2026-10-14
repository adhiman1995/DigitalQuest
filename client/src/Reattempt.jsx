import React, { useMemo, useRef } from 'react';
import QuestionCard from './QuestionCard.jsx';
import { byNumber } from './util.js';

// Questions answered wrongly (in practice or in an exam). A question stays on screen after it is
// answered correctly so its solution can be read; it leaves the list on the next visit.
export default function Reattempt({ syllabus, questions, progress }) {
  const { state, toggle, setResponse, recordResult } = progress;
  const seen = useRef(new Set()); // ids shown in this visit, so a card doesn't vanish the moment it is solved
  for (const id of Object.keys(state.reattempt)) seen.current.add(id);

  const list = useMemo(
    () => (questions || []).filter((q) => seen.current.has(q.id)).sort(byNumber),
    [questions, state.reattempt], // eslint-disable-line react-hooks/exhaustive-deps
  );
  const subjectName = (id) => syllabus.subjects.find((s) => s.id === id)?.name || '';
  const left = Object.keys(state.reattempt).length;

  if (questions && list.length === 0) {
    return (
      <div className="empty">
        <h3>Nothing to reattempt</h3>
        <p>Questions you get wrong in the library or in an exam will show up here.</p>
      </div>
    );
  }
  return (
    <section>
      <p className="muted">{left} left to get right{list.length > left ? ` · ${list.length - left} cleared this visit` : ''}</p>
      {list.map((q) => (
        <QuestionCard key={q.id} q={q} subjectName={subjectName(q.subjectId)} state={state} toggle={toggle} setResponse={setResponse} recordResult={recordResult} />
      ))}
    </section>
  );
}
