import React, { useEffect, useState } from 'react';

const count = (topics, done) => topics.filter((t) => done[t.id]).length;

export default function Tracker({ syllabus, progress, initialSubject }) {
  const { state, toggle, setMany, exportData, importData } = progress;
  const [paper, setPaper] = useState(() => syllabus.subjects.find((s) => s.id === initialSubject)?.paper || 'p2');
  const [activeId, setActiveId] = useState(initialSubject || null);

  const subjects = syllabus.subjects.filter((s) => s.paper === paper);
  const active = syllabus.subjects.find((s) => s.id === activeId);

  return (
    <section>
      <div className="row">
        <div className="tabs">
          {syllabus.papers.map((p) => {
            const topics = syllabus.subjects
              .filter((s) => s.paper === p.id)
              .flatMap((s) => s.chapters.flatMap((c) => c.topics));
            const pct = Math.round((count(topics, state.done) / topics.length) * 100) || 0;
            return (
              <button key={p.id} className={paper === p.id ? 'on' : ''} onClick={() => setPaper(p.id)}>
                {p.name} · {p.title} <small>({p.marks} marks · {pct}%)</small>
              </button>
            );
          })}
        </div>
        <div className="actions">
          <button onClick={exportData}>Export progress</button>
          <label className="btn">
            Import
            <input
              type="file"
              accept="application/json"
              hidden
              onChange={(e) => e.target.files[0] && importData(e.target.files[0]).catch(() => alert('Invalid file'))}
            />
          </label>
        </div>
      </div>

      <div className="grid">
        {subjects.map((s) => {
          const topics = s.chapters.flatMap((c) => c.topics);
          const d = count(topics, state.done);
          const pct = Math.round((d / topics.length) * 100) || 0;
          return (
            <article className="card" key={s.id}>
              <button className="card-head" onClick={() => setActiveId(s.id)}>
                <span className="title">{s.name}</span>
                <span className="muted">{d}/{topics.length} · {pct}%</span>
              </button>
              <div className="bar"><span style={{ width: `${pct}%` }} /></div>
              <p className="muted">{s.chapters.length} chapters</p>
            </article>
          );
        })}
      </div>

      {active && (
        <SubjectModal
          subject={active}
          state={state}
          toggle={toggle}
          setMany={setMany}
          onClose={() => setActiveId(null)}
        />
      )}
    </section>
  );
}

function SubjectModal({ subject: s, state, toggle, setMany, onClose }) {
  useEffect(() => {
    const onKey = (e) => e.key === 'Escape' && onClose();
    document.addEventListener('keydown', onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', onKey);
      document.body.style.overflow = prev;
    };
  }, [onClose]);

  const topics = s.chapters.flatMap((c) => c.topics);
  const d = count(topics, state.done);
  const pct = Math.round((d / topics.length) * 100) || 0;

  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" role="dialog" aria-modal="true" onClick={(e) => e.stopPropagation()}>
        <div className="modal-head">
          <div>
            <h2>{s.name}</h2>
            <p className="muted">{d}/{topics.length} topics · {pct}% covered</p>
          </div>
          <button onClick={onClose} aria-label="Close">✕</button>
        </div>
        <div className="bar"><span style={{ width: `${pct}%` }} /></div>
        <div className="modal-body">
          {s.chapters.map((c) => {
            const cd = count(c.topics, state.done);
            const all = cd === c.topics.length;
            return (
              <div className="chapter" key={c.id}>
                <label className="chapter-head">
                  <input
                    type="checkbox"
                    checked={all}
                    ref={(el) => el && (el.indeterminate = cd > 0 && !all)}
                    onChange={() => setMany('done', c.topics.map((t) => t.id), !all)}
                  />
                  <strong>{c.name}</strong>
                  <span className="muted">{cd}/{c.topics.length}</span>
                </label>
                <ul>
                  {c.topics.map((t) => (
                    <li key={t.id}>
                      <label>
                        <input type="checkbox" checked={!!state.done[t.id]} onChange={() => toggle('done', t.id)} />
                        <span className={state.done[t.id] ? 'strike' : ''}>{t.name}</span>
                      </label>
                    </li>
                  ))}
                </ul>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
