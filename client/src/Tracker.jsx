import React, { useEffect, useState } from 'react';
import Icon from './Icons.jsx';

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
          paper={syllabus.papers.find((p) => p.id === active.paper)}
          state={state}
          toggle={toggle}
          setMany={setMany}
          onClose={() => setActiveId(null)}
        />
      )}
    </section>
  );
}

function SubjectModal({ subject: s, paper, state, toggle, setMany, onClose }) {
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
  const chaptersDone = s.chapters.filter((c) => count(c.topics, state.done) === c.topics.length).length;
  const [filter, setFilter] = useState('all'); // all | todo | done
  // finished chapters start collapsed so the remaining work is what you see first
  const [open, setOpen] = useState(() => Object.fromEntries(s.chapters.map((c) => [c.id, count(c.topics, state.done) < c.topics.length])));
  const allOpen = s.chapters.every((c) => open[c.id]);
  const setAll = (v) => setOpen(Object.fromEntries(s.chapters.map((c) => [c.id, v])));
  const keep = (t) => filter === 'all' || (filter === 'done') === !!state.done[t.id];

  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal smodal" role="dialog" aria-modal="true" aria-labelledby="smodal-title" onClick={(e) => e.stopPropagation()}>
        <header className="smodal-head">
          <div className="smodal-title">
            {paper && <span className={`paper-tag ${s.paper}`}>{paper.name}</span>}
            <h2 id="smodal-title">{s.name}</h2>
            <p className="muted">{s.chapters.length} chapters · {topics.length} topics</p>
          </div>
          <button className="iconbtn-sq" onClick={onClose} aria-label="Close"><Icon name="close" /></button>
        </header>

        <div className="smodal-progress">
          <div className="smodal-pct"><b>{pct}%</b><span>covered</span></div>
          <div className="smodal-meter">
            <div className="bar big"><span style={{ width: `${pct}%` }} /></div>
            <div className="smodal-counts">
              <span><b>{d}</b>/{topics.length} topics</span>
              <span><b>{chaptersDone}</b>/{s.chapters.length} chapters complete</span>
            </div>
          </div>
        </div>

        <div className="smodal-tools">
          <div className="seg" role="tablist" aria-label="Show">
            {[['all', 'All'], ['todo', `To do · ${topics.length - d}`], ['done', `Done · ${d}`]].map(([k, label]) => (
              <button key={k} role="tab" aria-selected={filter === k} className={filter === k ? 'on' : ''} onClick={() => setFilter(k)}>{label}</button>
            ))}
          </div>
          <button className="linkbtn small" onClick={() => setAll(!allOpen)}>{allOpen ? 'Collapse all' : 'Expand all'}</button>
        </div>

        <div className="modal-body smodal-body">
          {s.chapters.map((c, i) => {
            const cd = count(c.topics, state.done);
            const all = cd === c.topics.length;
            const cp = Math.round((cd / c.topics.length) * 100) || 0;
            const shown = c.topics.filter(keep);
            if (!shown.length && filter !== 'all') return null;
            const isOpen = open[c.id] || filter !== 'all';
            return (
              <section className={`chap ${all ? 'complete' : ''} ${isOpen ? 'open' : ''}`} key={c.id}>
                <div className="chap-head">
                  <input
                    type="checkbox"
                    className="tick"
                    checked={all}
                    ref={(el) => el && (el.indeterminate = cd > 0 && !all)}
                    onChange={() => setMany('done', c.topics.map((t) => t.id), !all)}
                    aria-label={`Mark all of ${c.name} ${all ? 'not done' : 'done'}`}
                  />
                  <button className="chap-toggle" onClick={() => setOpen((o) => ({ ...o, [c.id]: !isOpen }))} aria-expanded={isOpen}>
                    <span className="chap-num">{String(i + 1).padStart(2, '0')}</span>
                    <span className="chap-name">{c.name}</span>
                    <span className="chap-mini"><span style={{ width: `${cp}%` }} /></span>
                    <span className="chap-count">{cd}/{c.topics.length}</span>
                    <Icon name="chevron" size={16} className="chev" />
                  </button>
                </div>
                {isOpen && (
                  <ul className="topics">
                    {shown.map((t) => (
                      <li key={t.id}>
                        <label className={state.done[t.id] ? 'done' : ''}>
                          <input type="checkbox" className="tick" checked={!!state.done[t.id]} onChange={() => toggle('done', t.id)} />
                          <span>{t.name}</span>
                        </label>
                      </li>
                    ))}
                  </ul>
                )}
              </section>
            );
          })}
          {filter !== 'all' && !topics.some(keep) && (
            <p className="smodal-empty">{filter === 'done' ? 'Nothing ticked off yet. Start with any topic below.' : 'Every topic in this subject is done. 🎉'}</p>
          )}
        </div>

        <footer className="smodal-foot">
          <button className="linkbtn small" disabled={!d} onClick={() => window.confirm(`Clear all ${d} ticked topics in ${s.name}?`) && setMany('done', topics.map((t) => t.id), false)}>Reset subject</button>
          <div className="actions">
            {d < topics.length && <button onClick={() => setMany('done', topics.map((t) => t.id), true)}>Mark all done</button>}
            <button className="primary" onClick={onClose}>Done</button>
          </div>
        </footer>
      </div>
    </div>
  );
}
