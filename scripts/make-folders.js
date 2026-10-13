// Creates question-bank/<paper>/<subject>/<chapter>/ for the whole syllabus. Safe to re-run.
const fs = require('fs');
const path = require('path');
const { BANK, folders } = require('./bank');

let made = 0;
for (const f of folders()) {
  const d = path.join(BANK, f.dir);
  if (!fs.existsSync(d)) { fs.mkdirSync(d, { recursive: true }); made++; }
}
console.log(`question-bank ready: ${folders().length} chapter folders (${made} newly created)`);
