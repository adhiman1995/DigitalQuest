"""Merge worked solutions into server/data/questions.json.

Sources (a d*.py entry replaces the s*.py entry for the same question):
- scripts/authoring/solutions/s*.py: S = { "<number>": (answer_letter | None, concept, solution) }
- scripts/authoring/solutions/d*.py: detailed solutions,
  D = { "<number>": (answer_letter | None, concept, solution, [point, ...]) }
  The points are shown to the student under "Points to take care of".
- If the question already has a printed-key answer, the solution's answer must match it (mismatches are reported, nothing is changed).
- If it has none, the derived answer is stored with answerSource='derived' so the UI can say it is not from the book's key.
- An answer written as "D!" replaces a printed key that the solution shows to be wrong: answerSource='corrected'
  and the book's letter is kept in printedAnswer so the UI can say so.
Usage: python3 scripts/authoring/apply_solutions.py
"""
import glob, importlib.util, json, os, re, sys

here = os.path.dirname(__file__)
root = os.path.join(here, '..', '..')
qpath = os.path.join(root, 'server', 'data', 'questions.json')
qs = json.load(open(qpath))
by = {q['number']: q for q in qs}
bad = 0
n = 0
def load(f):
    spec = importlib.util.spec_from_file_location('s', f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, 'S', None) or getattr(m, 'D')

detailed = {}
for f in sorted(glob.glob(os.path.join(here, 'solutions', 'd*.py'))):
    detailed.update(load(f))
entries = {}
for f in sorted(glob.glob(os.path.join(here, 'solutions', 's*.py'))):
    entries.update({k: v for k, v in load(f).items() if k not in detailed})
entries.update(detailed)
for num, entry in entries.items():
    ans, concept, sol = entry[:3]
    points = entry[3] if len(entry) > 3 else None
    correct_key = bool(ans) and ans.endswith('!')  # "D!" overrides a printed key shown to be wrong
    ans = ans and ans.rstrip('!')
    q = by.get(num)
    if not q:
        print('unknown question', num); bad += 1; continue
    said = re.findall(r'\*\*\(([a-d])\)\*\*', sol)
    if ans and said and said[-1].upper() != ans:
        print(f'LETTER {num}: tuple says {ans} but the solution text ends with ({said[-1]})'); bad += 1; continue
    if correct_key:
        printed = q.get('printedAnswer') or q.get('answer')
        if q.get('answerSource') not in ('corrected', None) or not printed or printed == ans:
            print(f'BAD OVERRIDE {num}: "!" needs a printed key that differs from {ans}'); bad += 1; continue
        if q.get('answerSource') != 'corrected':
            print(f'CORRECTED {num}: printed key {printed} -> {ans}')
        q['answer'] = ans; q['answerSource'] = 'corrected'; q['printedAnswer'] = printed
    elif q.get('answer') and ans and q['answer'] != ans and q.get('answerSource') != 'derived':
        print(f'MISMATCH {num}: printed key {q["answer"]}, solution says {ans}'); bad += 1; continue
    elif ans and (not q.get('answer') or q.get('answerSource') == 'derived'):
        if q.get('answer') and q['answer'] != ans:
            print(f'CHANGED {num}: derived answer {q["answer"]} -> {ans}')
        q['answer'] = ans; q['answerSource'] = 'derived'
    q['concept'] = concept; q['solution'] = sol
    if points: q['points'] = points
    n += 1
json.dump(qs, open(qpath, 'w'), ensure_ascii=False, indent=2)
open(qpath, 'a').write('\n')
missing = [q['number'] for q in qs if not q.get('solution')]
nopoints = [q['number'] for q in qs if not q.get('points')]
print(f'applied {n}; problems {bad}; without a solution: {len(missing)}; without points: {len(nopoints)}')
sys.exit(1 if bad else 0)
