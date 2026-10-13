import React, { useMemo } from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const cache = new Map();

export function texHtml(src, display = false) {
  const key = (display ? 'D:' : 'I:') + src;
  let html = cache.get(key);
  if (html === undefined) {
    html = katex.renderToString(src, { throwOnError: false, displayMode: display, strict: false });
    cache.set(key, html);
  }
  return html;
}

export function TeX({ children, display = false }) {
  return <span dangerouslySetInnerHTML={{ __html: texHtml(children, display) }} />;
}

// Text with inline $math$, display $$math$$ and **bold**. Newlines are preserved by CSS.
const TOKEN = /(\$\$[\s\S]+?\$\$|\$[^$]+?\$|\*\*[^*]+?\*\*)/g;

export function RichText({ text }) {
  const parts = useMemo(() => (text || '').split(TOKEN).filter((p) => p !== ''), [text]);
  return (
    <>
      {parts.map((p, i) => {
        if (p.startsWith('$$')) return <div key={i} className="math-block" dangerouslySetInnerHTML={{ __html: texHtml(p.slice(2, -2).trim(), true) }} />;
        if (p.startsWith('$') && /^\$[\d.,\s]+\$$/.test(p)) return <span key={i}>{p.slice(1, -1)}</span>;
        if (p.startsWith('$')) return <span key={i} dangerouslySetInnerHTML={{ __html: texHtml(p.slice(1, -1)) }} />;
        if (p.startsWith('**')) return <strong key={i}>{p.slice(2, -2)}</strong>;
        return <React.Fragment key={i}>{p}</React.Fragment>;
      })}
    </>
  );
}
