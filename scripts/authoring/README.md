# Authoring digitized questions

Questions are stored as **data, not images**:

- Maths is LaTeX inside `$...$` (inline) or `$$...$$` (display), rendered with KaTeX.
- Diagrams are JSON specs drawn as vector graphics by `client/src/Figure.jsx`:
  - `block`: control block diagrams (`ufb(...)` in `figs.py` builds the common unity-feedback loop)
  - `plot`:  s-plane pole/zero plots and response curves (curves are computed from formulas:
             `expsin`, `sumexp`, or hand-sketched `points`)
  - `grid`:  several of the above in one figure
- `answer` is only set from the book's printed answer key. Pen marks go in `marked`.

`figs.py` holds the Python helpers used to generate the Time Response Analysis figures.
`node scripts/ingest.js batch.json` documents the full question format.
