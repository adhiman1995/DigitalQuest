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

// Practice-mode card: choose an option (saved automatically), reveal the answer when verified.
export default function QuestionCard({ q, subjectName, state, toggle, setResponse }) {
  const [reveal, setReveal] = useState(false);
  const selected = state.responses[q.id] || null;
  const verdict = reveal && q.answer && selected ? (selected === q.answer ? 'correct' : 'wrong') : null;

  return (
    <article className="qcard" id={`q-${q.number}`}>
      <header className="qhead">
        <h3 className="qnum">{q.number}</h3>
        {q.year && <span className="yearchip">ESE-{q.year}</span>}
        <span className="qpath">{subjectName}{q.topic ? ` · ${q.topic}` : ''}</span>
        <label className={`addpill ${state.added[q.id] ? 'on' : ''}`}>
          <input type="checkbox" checked={!!state.added[q.id]} onChange={() => toggle('added', q.id)} />
          Add
        </label>
      </header>

      <QuestionBody q={q} />
      <OptionList
        q={q}
        selected={selected}
        onSelect={(L) => setResponse(q.id, selected === L ? null : L)}
        correct={q.answer}
        showCorrect={reveal}
      />

      <footer className="qfoot">
        <div className="qfoot-left">
          {q.answer ? (
            <button className="linkbtn" onClick={() => setReveal(!reveal)}>
              {reveal ? `Answer: (${q.answer.toLowerCase()})` : 'Show answer'}
            </button>
          ) : (
            <span className="muted" title="Add the book's answer-key page to verify answers">Answer not verified yet</span>
          )}
          {selected && (
            <span className={`saved ${verdict || ''}`}>
              {verdict === 'correct' ? '✓ Correct' : verdict === 'wrong' ? '✗ Incorrect' : `✓ Saved (${selected.toLowerCase()})`}
              {' · '}
              <button className="linkbtn small" onClick={() => setResponse(q.id, null)}>clear</button>
            </span>
          )}
          <button className={`iconbtn ${state.solved[q.id] ? 'on' : ''}`} onClick={() => toggle('solved', q.id)}>
            {state.solved[q.id] ? '✓ Solved' : 'Mark solved'}
          </button>
          <button className={`iconbtn ${state.bookmarks[q.id] ? 'on' : ''}`} onClick={() => toggle('bookmarks', q.id)}>
            {state.bookmarks[q.id] ? '★' : '☆'}
          </button>
        </div>
        <span className="qsource">{[q.book, subjectName, q.page && `p. ${q.page}`].filter(Boolean).join(' · ')}</span>
      </footer>
    </article>
  );
}
