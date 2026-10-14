import React, { useState } from 'react';
import { RichText } from './tex.jsx';
import Figure from './Figure.jsx';
import { LETTERS } from './util.js';

// The question itself: text, match lists, table, figure and trailing text.
export function QuestionBody({ q }) {
  return (
    <>
      <div className="qtext"><RichText text={q.text} /></div>

      {q.lists && (
        <div className="qlists">
          {q.lists.map((l, i) => (
            <div key={i}>
              <div className="qlist-title"><RichText text={l.title} /></div>
              <ul>
                {l.items.map(([k, v], j) => (
                  <li key={j}><span className="qlist-key">{k}</span><RichText text={v} /></li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}

      {q.table && (
        <table className="qtable">
          <thead><tr>{q.table.head.map((h, i) => <th key={i}><RichText text={h} /></th>)}</tr></thead>
          <tbody>
            {q.table.rows.map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j}><RichText text={c} /></td>)}</tr>)}
          </tbody>
        </table>
      )}

      {q.figure && <div className="figbox"><Figure spec={q.figure} /></div>}
      {q.after && <div className="qtext"><RichText text={q.after} /></div>}
    </>
  );
}

// Options. Selectable when onSelect is given; `correct` is highlighted only when `showCorrect`.
export function OptionList({ q, selected, onSelect, correct, showCorrect }) {
  if (!q.options?.length) return null;
  return (
    <ul className="opts" role={onSelect ? 'radiogroup' : undefined}>
      {q.options.map((o, i) => {
        const L = LETTERS[i];
        const cls = [
          'opt',
          selected === L ? 'sel' : '',
          showCorrect && correct === L ? 'correct' : '',
          showCorrect && correct && selected === L && selected !== correct ? 'wrong' : '',
        ].join(' ');
        const inner = (
          <>
            <span className="optkey">({L.toLowerCase()})</span>
            <span><RichText text={o} /></span>
          </>
        );
        return (
          <li key={i}>
            {onSelect ? (
              <button type="button" className={cls} role="radio" aria-checked={selected === L} onClick={() => onSelect(L)}>{inner}</button>
            ) : (
              <div className={cls}>{inner}</div>
            )}
          </li>
        );
      })}
    </ul>
  );
}

// Practice-mode card: choose an option (saved automatically), then check it.
// Correct -> the answer, solution and concept are shown. Wrong -> nothing is revealed and the
// question is sent to the Reattempt list until it is answered correctly.
export default function QuestionCard({ q, subjectName, state, toggle, setResponse, recordResult }) {
  const selected = state.responses[q.id] || null;
  const passed = !!state.results[q.id] && selected === q.answer;
  const [tried, setTried] = useState(false); // a wrong check on the currently selected option
  const unlocked = !passed && !!state.revealed[q.id]; // wrong again on a reattempt
  const wrong = tried && !passed && !!selected && selected !== q.answer;
  const showSolution = passed || unlocked;

  const check = () => {
    if (!selected || !q.answer) return;
    setTried(true);
    recordResult(q.id, selected === q.answer);
  };
  const choose = (L) => { setTried(false); setResponse(q.id, selected === L ? null : L); };

  return (
    <article className="qcard" id={`q-${q.number}`}>
      <header className="qhead">
        <h3 className="qnum">{q.number}</h3>
        {q.year && <span className="yearchip">ESE-{q.year}</span>}
        <span className="qpath">{subjectName}{q.topic ? ` · ${q.topic}` : ''}</span>
        {state.reattempt[q.id] && <span className="rechip">Reattempt</span>}
        <label className={`addpill ${state.added[q.id] ? 'on' : ''}`}>
          <input type="checkbox" checked={!!state.added[q.id]} onChange={() => toggle('added', q.id)} />
          Add
        </label>
      </header>

      <QuestionBody q={q} />
      <OptionList
        q={q}
        selected={selected}
        onSelect={choose}
        correct={q.answer}
        showCorrect={showSolution}
      />

      {wrong && !unlocked && (
        <p className="verdict-note bad">Incorrect. This question has been added to <a href="#reattempt">Reattempt questions</a>. Pick another option and check again.</p>
      )}
      {unlocked && !passed && (
        <p className="verdict-note bad">Still incorrect on the reattempt, so the correct answer ({q.answer.toLowerCase()}) and solution are unlocked below. It stays in Reattempt until you answer it correctly.</p>
      )}

      {showSolution && (q.solution || q.concept) && (
        <div className="explain">
          {q.concept && (
            <div className="concept">
              <div className="explain-title">Concept</div>
              <RichText text={q.concept} />
            </div>
          )}
          {q.solution && (
            <div className="solution">
              <div className="explain-title">Solution</div>
              <RichText text={q.solution} />
            </div>
          )}
        </div>
      )}
      {showSolution && q.answerSource === 'derived' && (
        <p className="muted small-note">This answer was worked out in the solution above; the source book has no printed answer key for it.</p>
      )}
      {showSolution && !q.solution && !q.concept && <p className="muted">No written solution has been added for this question yet.</p>}

      <footer className="qfoot">
        <div className="qfoot-left">
          {q.answer ? (
            passed ? (
              <span className="saved">✓ Correct · answer ({q.answer.toLowerCase()})</span>
            ) : (
              <button className="primary small" disabled={!selected} onClick={check}>Check answer</button>
            )
          ) : (
            <span className="muted" title="The answer key for this question hasn't been added yet">Answer not verified yet</span>
          )}
          {selected && !passed && !wrong && !q.answer && <span className="saved">✓ Saved ({selected.toLowerCase()})</span>}
          {selected && (
            <button className="linkbtn small" onClick={() => { setTried(false); setResponse(q.id, null); }}>clear</button>
          )}
          <button className={`iconbtn ${state.solved[q.id] ? 'on' : ''}`} onClick={() => toggle('solved', q.id)}>
            {state.solved[q.id] ? '✓ Solved' : 'Mark solved'}
          </button>
          <button className={`iconbtn ${state.bookmarks[q.id] ? 'on' : ''}`} onClick={() => toggle('bookmarks', q.id)}>
            {state.bookmarks[q.id] ? '★' : '☆'}
          </button>
        </div>
        <span className="qsource">{subjectName}</span>
      </footer>
    </article>
  );
}
