"""Merge worked solutions (scripts/authoring/solutions/s*.py) into server/data/questions.json.

Each file defines S = { "<number>": (answer_letter | None, concept, solution) }.
- If the question already has a printed-key answer, the solution's answer must match it (mismatches are reported, nothing is changed).
- If it has none, the derived answer is stored with answerSource='derived' so the UI can say it is not from the book's key.
Usage: python3 scripts/authoring/apply_solutions.py
"""
import glob, importlib.util, json, os, re, sys

root = os.path.join(os.path.dirname(__file__), '..', '..')
qpath = os.path.join(root, 'server', 'data', 'questions.json')
qs = json.load(open(qpath))
by = {q['number']: q for q in qs}
bad = 0
n = 0
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'solutions', 's*.py'))):
    spec = importlib.util.spec_from_file_location('s', f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for num, (ans, concept, sol) in m.S.items():
        q = by.get(num)
        if not q:
            print('unknown question', num); bad += 1; continue
        said = re.findall(r'\*\*\(([a-d])\)\*\*', sol)
        if ans and said and said[-1].upper() != ans:
            print(f'LETTER {num}: tuple says {ans} but the solution text ends with ({said[-1]})'); bad += 1; continue
        if q.get('answer') and ans and q['answer'] != ans:
            print(f'MISMATCH {num}: printed key {q["answer"]}, solution says {ans}'); bad += 1; continue
        if not q.get('answer') and ans:
            q['answer'] = ans; q['answerSource'] = 'derived'
        q['concept'] = concept; q['solution'] = sol; n += 1
json.dump(qs, open(qpath, 'w'), ensure_ascii=False, indent=2)
open(qpath, 'a').write('\n')
missing = [q['number'] for q in qs if not q.get('solution')]
print(f'applied {n}; problems {bad}; questions still without a solution: {len(missing)}')
sys.exit(1 if bad else 0)
