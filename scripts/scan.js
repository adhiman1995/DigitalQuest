// Lists images that have NOT been processed yet (tracked by content hash, so renames/moves don't cause re-processing).
// Usage: node scripts/scan.js [--json]
const path = require('path');
const { BANK, LOG, folders, readJson, sha1, walkImages } = require('./bank');

const log = readJson(LOG, { images: {} });
const seen = new Set(Object.values(log.images).map((x) => x.sha1));
const json = process.argv.includes('--json');

const pending = [], rows = [];
for (const f of folders()) {
  const imgs = walkImages(path.join(BANK, f.dir));
  if (!imgs.length) continue;
  const todo = imgs.filter((p) => !seen.has(sha1(p)));
  todo.forEach((p) => pending.push(path.relative(BANK, p)));
  rows.push({ folder: f.dir, total: imgs.length, pending: todo.length });
}

if (json) { console.log(JSON.stringify(pending, null, 2)); process.exit(0); }
if (!rows.length) { console.log('No images found in question-bank/ yet.'); process.exit(0); }
for (const r of rows)
  console.log(`${r.pending === 0 ? '✓ done   ' : r.pending === r.total ? '○ new    ' : '◐ partial'}  ${r.folder}  (${r.total - r.pending}/${r.total} processed)`);
console.log(`\n${pending.length} image(s) pending.`);
