// Adds digitized questions and records their source images as processed.
// Usage: node scripts/ingest.js batch.json
//
// batch.json: [{ "image": "<path relative to question-bank/>", "questions": [ Question, ... ] }]
// Question = {
//   number: "2.107", year: 2022, topic: "Steady-State Error", page: 19, book: "MADE EASY",
//   text:    "LaTeX-typeset text: inline $x$, display $$x$$, **bold**",
//   options: ["$5$", "$7$", "$10$", "$14$"],
//   lists?:  [{ title, items: [[key, text], ...] }]      // match-the-following lists
//   table?:  { head: [...], rows: [[...], ...] }
//   figure?: { type: 'block' | 'plot' | 'grid', ... }     // vector diagram spec, see scripts/authoring/
//   after?:  "text shown below the figure/table",
//   answer?: "B"      // ONLY when verified against the book's printed answer key
//   marked?: "B"      // pen mark seen in the book (NOT a verified answer)
// }
// Questions are never stored as images. The source image is only hashed, so it is never re-processed.
const fs = require('fs');
const path = require('path');
const { BANK, LOG, QUESTIONS, folders, readJson, writeJson, sha1 } = require('./bank');

const batch = readJson(process.argv[2], null);
if (!Array.isArray(batch)) { console.error('Usage: node scripts/ingest.js batch.json (array expected)'); process.exit(1); }

const byDir = new Map(folders().map((f) => [f.dir, f]));
const log = readJson(LOG, { images: {} });
const questions = readJson(QUESTIONS, []);
const hashes = new Set(Object.values(log.images).map((x) => x.sha1));
let added = 0, skipped = 0;

for (const item of batch) {
  const abs = path.join(BANK, item.image);
  if (!fs.existsSync(abs)) { console.error(`missing image: ${item.image}`); process.exit(1); }
  const folder = byDir.get(path.dirname(item.image));
  if (!folder) { console.error(`image is not inside a known chapter folder: ${item.image}`); process.exit(1); }
  const hash = sha1(abs);
  if (hashes.has(hash)) { skipped++; console.log(`skip (already processed): ${item.image}`); continue; }

  const ids = (item.questions || []).map((q, i) => {
    if (!q.text || !Array.isArray(q.options)) { console.error(`question ${q.number}: text and options are required`); process.exit(1); }
    const id = `${hash.slice(0, 10)}-${i + 1}`;
    questions.push({
      id,
      number: q.number ?? null,
      year: q.year ?? null,
      subjectId: folder.subject.id,
      chapterId: folder.chapter.id,
      topic: q.topic ?? null,
      book: q.book ?? null,
      page: q.page ?? null,
      text: q.text,
      ...(q.lists && { lists: q.lists }),
      ...(q.table && { table: q.table }),
      ...(q.figure && { figure: q.figure }),
      ...(q.after && { after: q.after }),
      options: q.options,
      answer: q.answer || null,
      marked: q.marked || null,
    });
    added++;
    return id;
  });
  log.images[item.image] = { sha1: hash, processedAt: new Date().toISOString(), questionIds: ids };
  hashes.add(hash);
}

writeJson(QUESTIONS, questions);
writeJson(LOG, log);
console.log(`added ${added} question(s), skipped ${skipped} already-processed image(s).`);
