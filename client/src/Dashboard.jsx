import React, { useMemo } from 'react';
import Icon from './Icons.jsx';
import { score } from './examLogic.js';
import { fmtDuration } from './util.js';
import Calendar from './tools/Calendar.jsx';
import { examDates, daysUntil, fmtLong } from './tools/examDates.js';

const pctOf = (a, b) => (b ? Math.round((a / b) * 100) : 0);

function Ring({ pct, size = 112, stroke = 10, label }) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  return (
    <div className="ring" style={{ width: size, height: size }}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle cx={size / 2} cy={size / 2} r={r} className="ring-track" strokeWidth={stroke} fill="none" />
        <circle cx={size / 2} cy={size / 2} r={r} className="ring-fill" strokeWidth={stroke} fill="none"
          strokeDasharray={c} strokeDashoffset={c * (1 - pct / 100)} strokeLinecap="round" transform={`rotate(-90 ${size / 2} ${size / 2})`} />
      </svg>
      <div className="ring-label"><b>{pct}%</b>{label && <span>{label}</span>}</div>
    </div>
  );
}

function Kpi({ icon, label, value, sub, tone }) {
  return (
    <div className={`kpi ${tone || ''}`}>
      <span className="kpi-ico"><Icon name={icon} /></span>
      <div>
        <div className="kpi-label">{label}</div>
        <div className="kpi-value">{value}</div>
        {sub && <div className="kpi-sub">{sub}</div>}
      </div>
    </div>
  );
}

export default function Dashboard({ syllabus, questions, progress, user, go, openSubject }) {
  const { state } = progress;
  const qs = questions || [];

  const data = useMemo(() => {
    const byId = Object.fromEntries(qs.map((q) => [q.id, q]));
    const qBySubject = {};
    for (const q of qs) qBySubject[q.subjectId] = (qBySubject[q.subjectId] || 0) + 1;

    let topics = 0, done = 0;
    const papers = syllabus.papers.map((p) => ({ ...p, topics: 0, done: 0 }));
    const subjects = syllabus.subjects.map((s) => {
      const ts = s.chapters.flatMap((c) => c.topics);
      const d = ts.filter((t) => state.done[t.id]).length;
      topics += ts.length; done += d;
      const p = papers.find((x) => x.id === s.paper);
      if (p) { p.topics += ts.length; p.done += d; }
      return { ...s, topics: ts.length, done: d, pct: pctOf(d, ts.length), questions: qBySubject[s.id] || 0 };
    });

    let attempted = 0, verified = 0, correct = 0;
    for (const [id, letter] of Object.entries(state.responses)) {
      const q = byId[id];
      if (!q) continue;
      attempted++;
      if (q.answer) { verified++; if (q.answer === letter) correct++; }
    }

    const exams = [...state.exams].sort((a, b) => b.finishedAt - a.finishedAt).map((e) => ({ ...e, sc: score(e, byId) }));
    const scored = exams.filter((e) => e.sc.verified);
    const avgExam = scored.length ? Math.round(scored.reduce((n, e) => n + e.sc.correct / e.sc.verified, 0) / scored.length * 100) : null;
    const bestExam = scored.length ? Math.max(...scored.map((e) => Math.round((e.sc.correct / e.sc.verified) * 100))) : null;

    // Subjects to work on next: least covered first, ties broken by more available questions.
    const focus = subjects.filter((s) => s.pct < 100).sort((a, b) => a.pct - b.pct || b.questions - a.questions).slice(0, 4);

    return { topics, done, papers, subjects, attempted, verified, correct, exams, avgExam, bestExam, focus };
  }, [syllabus, qs, state.done, state.responses, state.exams]);

  const nameOf = (id) => syllabus.subjects.find((s) => s.id === id)?.name || '';
  const chapterName = (id) => syllabus.subjects.flatMap((s) => s.chapters).find((c) => c.id === id)?.name || '';
  const overall = pctOf(data.done, data.topics);
  const accuracy = data.verified ? pctOf(data.correct, data.verified) : null;
  const first = user?.name?.split(' ')[0];
  const hour = new Date().getHours();
  const greet = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening';
  const session = state.session;
  const next = examDates(state.prefs).find((e) => daysUntil(e.date) >= 0);

  return (
    <section className="dash">
      <div className="page-head">
        <div>
          <h1>{greet}{first ? `, ${first}` : ''}</h1>
          <p className="muted">Here's where your ESE ECE Stage 1 preparation stands.</p>
        </div>
        <div className="actions">
          <button onClick={() => go('library')}><Icon name="library" size={16} /> Practise</button>
          <button className="primary" onClick={() => go('exam')}><Icon name="play" size={14} /> Start an exam</button>
        </div>
      </div>

      {session && (
        <div className="resume">
          <span className="live-dot" />
          <div>
            <strong>Exam in progress</strong>
            <span className="muted"> · {nameOf(session.subjectId)}{session.chapterId ? ` · ${chapterName(session.chapterId)}` : ' · random test'} · question {session.idx + 1} of {session.qids.length}</span>
          </div>
          <button className="primary" onClick={() => go('exam')}>Resume <Icon name="arrow" size={16} /></button>
        </div>
      )}

      {next && (
        <div className={`exam-banner ${next.tone}`}>
          <div className="eb-days"><b>{daysUntil(next.date)}</b><span>{daysUntil(next.date) === 1 ? 'day' : 'days'} to go</span></div>
          <div className="eb-text">
            <strong>{next.label} {next.date.slice(0, 4)}</strong>
            <span>{fmtLong(next.date)} · about {Math.max(0, Math.floor(daysUntil(next.date) / 7))} weeks left. {data.topics - data.done} topics still to cover{daysUntil(next.date) > 0 ? `, roughly ${Math.ceil((data.topics - data.done) / Math.max(1, daysUntil(next.date)))} a day` : ''}.</span>
          </div>
        </div>
      )}

      <div className="kpis">
        <Kpi icon="target" label="Syllabus covered" value={`${overall}%`} sub={`${data.done} of ${data.topics} topics`} tone="t1" />
        <Kpi icon="list" label="Questions attempted" value={data.attempted} sub={`of ${qs.length} in the library`} tone="t2" />
        <Kpi icon="check" label="Practice accuracy" value={accuracy === null ? '–' : `${accuracy}%`} sub={data.verified ? `${data.correct}/${data.verified} with answer keys` : 'Answer some questions to see it'} tone="t3" />
        <Kpi icon="trophy" label="Exams taken" value={data.exams.length} sub={data.avgExam === null ? 'No scored exams yet' : `avg ${data.avgExam}% · best ${data.bestExam}%`} tone="t4" />
      </div>

      <div className="dash-grid">
        <div className="panel">
          <div className="panel-head"><h2>Coverage by paper</h2><button className="linkbtn small" onClick={() => go('tracker')}>Open tracker</button></div>
          <div className="papers">
            {data.papers.map((p) => (
              <div className="paper" key={p.id}>
                <Ring pct={pctOf(p.done, p.topics)} />
                <div>
                  <strong>{p.name}</strong>
                  <div className="muted">{p.title}</div>
                  <div className="muted">{p.done}/{p.topics} topics · {p.marks} marks</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="panel">
          <div className="panel-head"><h2>Focus next</h2><span className="muted">least covered</span></div>
          {data.focus.length === 0 && <p className="muted">Every topic is ticked off. Time for full-length exams.</p>}
          <ul className="focus">
            {data.focus.map((s) => (
              <li key={s.id}>
                <button onClick={() => openSubject(s.id)}>
                  <div className="focus-top">
                    <span className="focus-name">{s.name}</span>
                    <span className="muted">{s.pct}%</span>
                  </div>
                  <div className="bar"><span style={{ width: `${s.pct}%` }} /></div>
                  <div className="muted tiny">{s.done}/{s.topics} topics{s.questions ? ` · ${s.questions} questions` : ''}</div>
                </button>
              </li>
            ))}
          </ul>
        </div>

        <div className="panel">
          <div className="panel-head"><h2>Exam calendar</h2><span className="muted">click a date</span></div>
          <Calendar progress={progress} />
        </div>

        <div className="panel">
          <div className="panel-head"><h2>Recent exams</h2>{data.exams.length > 0 && <button className="linkbtn small" onClick={() => go('exam')}>View all</button>}</div>
          {data.exams.length === 0 && (
            <div className="panel-empty">
              <p className="muted">No exams yet. A chapter exam is a quick way to check what has stuck.</p>
              <button onClick={() => go('exam')}>Set up an exam</button>
            </div>
          )}
          <ul className="recent">
            {data.exams.slice(0, 5).map((e) => {
              const p = e.sc.verified ? pctOf(e.sc.correct, e.sc.verified) : null;
              return (
                <li key={e.id}>
                  <div>
                    <strong>{nameOf(e.subjectId)}</strong>
                    <div className="muted tiny">{e.scope === 'subject' ? 'Random test' : chapterName(e.chapterId)} · {new Date(e.finishedAt).toLocaleDateString()} · {fmtDuration(e.sc.secs)}</div>
                  </div>
                  <span className={`score ${p === null ? '' : p >= 70 ? 'good' : p >= 40 ? 'mid' : 'low'}`}>{p === null ? `${e.sc.answered}/${e.sc.total}` : `${p}%`}</span>
                </li>
              );
            })}
          </ul>
        </div>

        <div className="panel wide">
          <div className="panel-head"><h2>All subjects</h2><span className="muted">{data.subjects.length} subjects</span></div>
          <div className="subj-table">
            {data.subjects.map((s) => (
              <button key={s.id} className="subj-row" onClick={() => openSubject(s.id)}>
                <span className={`paper-tag ${s.paper}`}>{s.paper.toUpperCase()}</span>
                <span className="subj-name">{s.name}</span>
                <span className="bar"><span style={{ width: `${s.pct}%` }} /></span>
                <span className="subj-pct">{s.pct}%</span>
              </button>
            ))}
          </div>
        </div>

        <div className="panel wide">
          <div className="panel-head"><h2>Your lists</h2></div>
          <div className="lists">
            <button onClick={() => go('library')}><Icon name="star" /><b>{Object.keys(state.bookmarks).length}</b><span>Bookmarked</span></button>
            <button onClick={() => go('library')}><Icon name="list" /><b>{Object.keys(state.added).length}</b><span>Practice set</span></button>
            <button onClick={() => go('library')}><Icon name="check" /><b>{Object.keys(state.results).length}</b><span>Answered correctly</span></button>
          </div>
        </div>
      </div>
    </section>
  );
}
