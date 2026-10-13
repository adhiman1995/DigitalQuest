import React, { useId } from 'react';
import { texHtml, RichText } from './tex.jsx';

// All figures are drawn as vector graphics from a small JSON spec stored with the question:
//   { type: 'block',  w, h, nodes, edges, dots, labels }   control-system block diagram
//   { type: 'plot',   w, h, x:[min,max], y:[min,max], ... } s-plane / time-response plots (curves are computed)
//   { type: 'grid',   cols, items:[{cap, fig}] }            several figures laid out together

const INK = 'var(--fig-ink)';
const FONT = 'var(--fig-font)';

function SvgTeX({ x, y, tex, anchor = 'middle', size = 15, w = 220, h = 70 }) {
  const ox = anchor === 'middle' ? x - w / 2 : anchor === 'end' ? x - w : x;
  const justify = anchor === 'middle' ? 'center' : anchor === 'end' ? 'flex-end' : 'flex-start';
  return (
    <foreignObject x={ox} y={y - h / 2} width={w} height={h} style={{ overflow: 'visible', pointerEvents: 'none' }}>
      <div
        xmlns="http://www.w3.org/1999/xhtml"
        style={{ display: 'flex', alignItems: 'center', justifyContent: justify, height: '100%', fontSize: size, color: INK, whiteSpace: 'nowrap' }}
        dangerouslySetInnerHTML={{ __html: texHtml(tex) }}
      />
    </foreignObject>
  );
}

function Label({ x, y, tex, text, anchor = 'middle', size = 15 }) {
  if (tex) return <SvgTeX x={x} y={y} tex={tex} anchor={anchor} size={size} />;
  return (
    <text x={x} y={y} textAnchor={anchor} dominantBaseline="middle" fill={INK} fontSize={size - 2} fontFamily={FONT}>
      {text}
    </text>
  );
}

function Arrowhead({ id }) {
  return (
    <marker id={id} viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill={INK} />
    </marker>
  );
}

// ---------------------------------------------------------------- block diagram
function BlockDiagram({ spec }) {
  const id = useId().replace(/:/g, '');
  const mk = `ah${id}`;
  const signPos = { l: (n) => [n.x - n.r - 9, n.y - 11], t: (n) => [n.x + 11, n.y - n.r - 7], b: (n) => [n.x + 12, n.y + n.r + 12], r: (n) => [n.x + n.r + 9, n.y - 11] };
  return (
    <svg viewBox={`0 0 ${spec.w} ${spec.h}`} className="fig-svg" style={{ maxWidth: spec.w * (spec.scale || 1.15), minWidth: Math.min(spec.w, 560) }} role="img" aria-label={spec.alt || 'block diagram'}>
      <defs><Arrowhead id={mk} /></defs>
      {spec.edges.map((e, i) =>
        e.q ? (
          <path key={i} d={`M${e.p[0].join(',')} Q${e.q.join(',')} ${e.p[1].join(',')}`} fill="none" stroke={INK} strokeWidth="1.5" markerEnd={e.arrow ? `url(#${mk})` : undefined} />
        ) : (
          <polyline key={i} points={e.p.map((q) => q.join(',')).join(' ')} fill="none" stroke={INK} strokeWidth="1.5" markerEnd={e.arrow ? `url(#${mk})` : undefined} />
        )
      )}
      {(spec.dots || []).map((d, i) => <circle key={i} cx={d[0]} cy={d[1]} r="3.2" fill={INK} />)}
      {spec.nodes.map((n, i) =>
        n.k === 'pt' ? (
          <circle key={i} cx={n.x} cy={n.y} r="4.5" fill="var(--fig-fill)" stroke={INK} strokeWidth="1.5" />
        ) : n.k === 'box' ? (
          <g key={i}>
            <rect x={n.x - n.w / 2} y={n.y - n.h / 2} width={n.w} height={n.h} fill="var(--fig-fill)" stroke={INK} strokeWidth="1.5" />
            <Label x={n.x} y={n.y} tex={n.tex} size={n.size || 16} />
          </g>
        ) : (
          <g key={i}>
            <circle cx={n.x} cy={n.y} r={n.r} fill="var(--fig-fill)" stroke={INK} strokeWidth="1.5" />
            <line x1={n.x - n.r * 0.7} y1={n.y - n.r * 0.7} x2={n.x + n.r * 0.7} y2={n.y + n.r * 0.7} stroke={INK} strokeWidth="1.3" />
            <line x1={n.x - n.r * 0.7} y1={n.y + n.r * 0.7} x2={n.x + n.r * 0.7} y2={n.y - n.r * 0.7} stroke={INK} strokeWidth="1.3" />
            {(n.signs || []).map((s, j) => {
              const [sx, sy] = signPos[s.at]({ ...n, r: n.r });
              return <text key={j} x={sx} y={sy} textAnchor="middle" dominantBaseline="middle" fill={INK} fontSize="15" fontFamily={FONT}>{s.t}</text>;
            })}
          </g>
        )
      )}
      {(spec.labels || []).map((l, i) => <Label key={i} {...l} />)}
    </svg>
  );
}

// ---------------------------------------------------------------- plots
function curvePoints(c, xr, n = 240) {
  const [x0, x1] = c.t || xr;
  const out = [];
  for (let i = 0; i <= n; i++) {
    const t = x0 + ((x1 - x0) * i) / n;
    let y;
    if (c.fn === 'expsin') y = (c.c || 0) + (c.A ?? 1) * Math.exp((c.sigma || 0) * t) * Math.sin((c.omega ?? 1) * t + (c.phi || 0));
    else if (c.fn === 'sumexp') y = (c.c || 0) + c.terms.reduce((s, [a, k]) => s + a * Math.exp(k * t), 0);
    else y = 0;
    out.push([t, y]);
  }
  return out;
}

// Catmull-Rom -> cubic Bezier through hand-sketched points
function smoothPath(pts) {
  if (pts.length < 3) return 'M' + pts.map((p) => p.join(',')).join(' L');
  let d = `M${pts[0][0]},${pts[0][1]}`;
  for (let i = 0; i < pts.length - 1; i++) {
    const p0 = pts[i - 1] || pts[i], p1 = pts[i], p2 = pts[i + 1], p3 = pts[i + 2] || p2;
    const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
    const c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
    d += ` C${c1.join(',')} ${c2.join(',')} ${p2.join(',')}`;
  }
  return d;
}

function Plot({ spec }) {
  const id = useId().replace(/:/g, '');
  const mk = `ah${id}`;
  const { w, h } = spec;
  const M = spec.margin || { l: 34, r: 40, t: 26, b: 34 };
  const [xa, xb] = spec.x, [ya, yb] = spec.y;
  const sx = (v) => M.l + ((v - xa) / (xb - xa)) * (w - M.l - M.r);
  const sy = (v) => h - M.b - ((v - ya) / (yb - ya)) * (h - M.t - M.b);
  const ox = Math.min(Math.max(0, xa), xb), oy = Math.min(Math.max(0, ya), yb);
  const px = (p) => `${sx(p[0])},${sy(p[1])}`;
  const sc = (w - M.l - M.r) / (xb - xa); // px per x unit (for circles in s-plane, x and y share a scale)

  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="fig-svg" style={{ maxWidth: w * (spec.scale || 1.1), minWidth: Math.min(w, 300) }} role="img" aria-label={spec.alt || 'plot'}>
      <defs>
        <Arrowhead id={mk} />
        <clipPath id={`cp${id}`}><rect x={M.l - 2} y={M.t - 2} width={w - M.l - M.r + 4} height={h - M.t - M.b + 4} /></clipPath>
      </defs>

      {/* axes */}
      <line x1={sx(xa)} y1={sy(oy)} x2={sx(xb)} y2={sy(oy)} stroke={INK} strokeWidth="1.3" markerEnd={`url(#${mk})`} />
      <line x1={sx(ox)} y1={sy(ya)} x2={sx(ox)} y2={sy(yb)} stroke={INK} strokeWidth="1.3" markerEnd={`url(#${mk})`} />
      {spec.xlabel && <Label x={sx(xb) + 6} y={sy(oy) + (spec.xlabelDy || 0)} tex={spec.xlabel} anchor="start" size={14} />}
      {spec.ylabel && <Label x={sx(ox) + (spec.ylabelDx ?? 8)} y={M.t - 12} tex={spec.ylabel} anchor={spec.ylabelDx < 0 ? 'end' : 'start'} size={14} />}
      {spec.origin && <Label x={sx(ox) - 10} y={sy(oy) + 4} tex="0" anchor="end" size={13} />}

      <g clipPath={`url(#cp${id})`}>
        {(spec.circle ? [spec.circle] : []).map((c, i) => (
          <circle key={i} cx={sx(c.cx || 0)} cy={sy(c.cy || 0)} r={c.r * sc} fill="none" stroke={c.solid ? 'var(--fig-curve)' : INK} strokeWidth={c.solid ? 2 : 1} strokeDasharray={c.solid ? undefined : '4 3'} opacity={c.solid ? 1 : 0.8} />
        ))}
        {(spec.vlines || []).map((v, i) => <line key={i} x1={sx(v.x)} y1={sy(ya)} x2={sx(v.x)} y2={sy(yb)} stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />)}
        {(spec.rays || []).map((r, i) => <line key={i} x1={sx(0)} y1={sy(0)} x2={sx(r[0])} y2={sy(r[1])} stroke={INK} strokeWidth="1.5" />)}
        {(spec.curves || []).map((c, i) => {
          const pts = c.fn === 'points' ? c.pts : curvePoints(c, spec.x);
          const d = c.fn === 'points' ? smoothPath(pts.map((p) => [sx(p[0]), sy(p[1])])) : 'M' + pts.map(px).join(' L');
          const env = c.envelope && curvePoints({ ...c, fn: 'expsin', omega: 0, phi: Math.PI / 2 }, spec.x);
          return (
            <g key={i}>
              {env && (
                <>
                  <path d={'M' + env.map((p) => `${sx(p[0])},${sy(p[1])}`).join(' L')} fill="none" stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />
                  <path d={'M' + env.map((p) => `${sx(p[0])},${sy(-p[1] + 2 * (c.c || 0))}`).join(' L')} fill="none" stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />
                </>
              )}
              <path d={d} fill="none" stroke={c.color || 'var(--fig-curve)'} strokeWidth="2" strokeLinejoin="round" markerEnd={c.arrow ? `url(#${mk})` : undefined} />
            </g>
          );
        })}
        {(spec.lines || []).map((l, i) => <line key={i} x1={sx(l.from[0])} y1={sy(l.from[1])} x2={sx(l.to[0])} y2={sy(l.to[1])} stroke={INK} strokeWidth="1.5" />)}
      </g>

      {/* guides: dashed drop-lines with tick labels */}
      {(spec.guides || []).map((g, i) => (
        <g key={i}>
          {g.y !== undefined && g.x !== undefined && <line x1={sx(ox)} y1={sy(g.y)} x2={sx(g.x)} y2={sy(g.y)} stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />}
          {g.x !== undefined && <line x1={sx(g.x)} y1={sy(g.y ?? yb)} x2={sx(g.x)} y2={sy(oy)} stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />}
          {g.y !== undefined && g.x === undefined && <line x1={sx(ox)} y1={sy(g.y)} x2={sx(xb)} y2={sy(g.y)} stroke={INK} strokeWidth="1" strokeDasharray="4 3" opacity=".8" />}
          {g.ytex && <Label x={sx(ox) - 8} y={sy(g.y)} tex={g.ytex} anchor="end" size={13} />}
          {g.xtex && <Label x={sx(g.x)} y={sy(oy) + 16} tex={g.xtex} size={13} />}
          {g.dot && <circle cx={sx(g.x)} cy={sy(g.y)} r="3.5" fill={INK} />}
        </g>
      ))}

      {/* pole / zero markers */}
      {(spec.poles || []).map((p, i) => (
        <g key={'p' + i} stroke={INK} strokeWidth="2.2">
          <line x1={sx(p[0]) - 5} y1={sy(p[1]) - 5} x2={sx(p[0]) + 5} y2={sy(p[1]) + 5} />
          <line x1={sx(p[0]) - 5} y1={sy(p[1]) + 5} x2={sx(p[0]) + 5} y2={sy(p[1]) - 5} />
        </g>
      ))}
      {(spec.dots || []).map((p, i) => <circle key={'d' + i} cx={sx(p[0])} cy={sy(p[1])} r="4" fill={INK} />)}
      {(spec.zeros || []).map((p, i) => <circle key={'z' + i} cx={sx(p[0])} cy={sy(p[1])} r="5" fill="none" stroke={INK} strokeWidth="2" />)}

      {/* angle arcs (s-plane): { r, from, to } in degrees measured from the negative real axis */}
      {(spec.arcs || []).map((a, i) => {
        const r = a.r * sc, rad = (d) => (d * Math.PI) / 180;
        const p = (d) => [sx(0) - r * Math.cos(rad(d)), sy(0) - r * Math.sin(rad(d))];
        const [x1, y1] = p(a.from), [x2, y2] = p(a.to);
        return <path key={i} d={`M${x1},${y1} A${r},${r} 0 0 ${a.to > a.from ? 1 : 0} ${x2},${y2}`} fill="none" stroke={INK} strokeWidth="1" />;
      })}

      {/* dimension arrow */}
      {(spec.dims || []).map((d, i) => (
        <g key={i}>
          <line x1={sx(d.x)} y1={sy(d.from)} x2={sx(d.x)} y2={sy(d.to)} stroke={INK} strokeWidth="1.2" markerEnd={`url(#${mk})`} markerStart={`url(#${mk})`} />
          <line x1={sx(d.x) - 5} y1={sy(d.to)} x2={sx(d.x) + 5} y2={sy(d.to)} stroke={INK} strokeWidth="1.2" />
          {d.tex && <Label x={sx(d.x) + 10} y={(sy(d.from) + sy(d.to)) / 2} tex={d.tex} anchor="start" size={13} />}
        </g>
      ))}

      {/* annotation with leader arrow */}
      {(spec.annots || []).map((a, i) => (
        <g key={i}>
          <line x1={sx(a.at[0])} y1={sy(a.at[1])} x2={sx(a.to[0])} y2={sy(a.to[1])} stroke={INK} strokeWidth="1.1" markerEnd={`url(#${mk})`} />
          <Label x={sx(a.at[0])} y={sy(a.at[1]) + 12} tex={a.tex} anchor={a.anchor || 'middle'} size={13} />
        </g>
      ))}
      {(spec.labels || []).map((l, i) => <Label key={i} x={sx(l.x)} y={sy(l.y)} tex={l.tex} text={l.text} anchor={l.anchor} size={l.size || 13} />)}
    </svg>
  );
}

// ---------------------------------------------------------------- entry point
export default function Figure({ spec }) {
  if (!spec) return null;
  if (spec.type === 'block') return <BlockDiagram spec={spec} />;
  if (spec.type === 'plot') return <Plot spec={spec} />;
  if (spec.type === 'grid')
    return (
      <div className="fig-grid" style={{ gridTemplateColumns: `repeat(${spec.cols || 2}, minmax(0, 1fr))` }}>
        {spec.items.map((it, i) => (
          <figure key={i} className="fig-cell">
            <Figure spec={it.fig} />
            {it.cap && <figcaption><RichText text={it.cap} /></figcaption>}
          </figure>
        ))}
      </div>
    );
  return null;
}
