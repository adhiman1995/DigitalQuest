// Shared helpers: maps question-bank folders <-> syllabus subjects/chapters.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { PAPERS, subjects } = require('../server/data/syllabus');

const ROOT = path.join(__dirname, '..');
const BANK = path.join(ROOT, '..', 'question-bank');
const LOG = path.join(ROOT, 'server', 'data', 'processed.json');
const QUESTIONS = path.join(ROOT, 'server', 'data', 'questions.json');
const PUBLIC_IMG = path.join(ROOT, 'server', 'public', 'questions');
const IMG_RE = /\.(jpe?g|png|webp|heic|gif)$/i;

const slug = (s) => s.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const nn = (i) => String(i + 1).padStart(2, '0');

const paperDir = (p) => (p.id === 'p1' ? 'paper-1-general-studies' : 'paper-2-ece');

// [{ dir: 'paper-2-.../03-network-theory/02-network-theorems', subject, chapter }]
function folders() {
  const out = [];
  for (const p of PAPERS) {
    subjects.filter((s) => s.paper === p.id).forEach((s, si) => {
      s.chapters.forEach((c, ci) => {
        out.push({
          dir: path.join(paperDir(p), `${nn(si)}-${slug(s.name)}`, `${nn(ci)}-${slug(c.name)}`),
          subject: s,
          chapter: c,
        });
      });
    });
  }
  return out;
}

const readJson = (f, fallback) => { try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch { return fallback; } };
const writeJson = (f, v) => { fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, JSON.stringify(v, null, 2) + '\n'); };
const sha1 = (f) => crypto.createHash('sha1').update(fs.readFileSync(f)).digest('hex');

function walkImages(dir) {
  const out = [];
  for (const e of fs.existsSync(dir) ? fs.readdirSync(dir, { withFileTypes: true }) : []) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walkImages(p));
    else if (IMG_RE.test(e.name)) out.push(p);
  }
  return out;
}

module.exports = { ROOT, BANK, LOG, QUESTIONS, PUBLIC_IMG, folders, readJson, writeJson, sha1, walkImages, slug };
