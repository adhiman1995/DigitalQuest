import React, { useEffect, useRef, useState } from 'react';
import Icon from '../Icons.jsx';

let topZ = 60;

// A small window that floats over the page and can be dragged by its title bar.
// On narrow screens CSS turns it into a bottom sheet and dragging is ignored.
export default function FloatPanel({ title, icon, width, initial, onClose, children, className = '' }) {
  const ref = useRef(null);
  const [pos, setPos] = useState(() => initial());
  const [z, setZ] = useState(() => ++topZ);
  const drag = useRef(null);

  const clamp = (x, y) => {
    const el = ref.current;
    const w = el?.offsetWidth || width, h = el?.offsetHeight || 300;
    return { x: Math.min(Math.max(8, x), window.innerWidth - w - 8), y: Math.min(Math.max(8, y), window.innerHeight - Math.min(h, 120)) };
  };

  useEffect(() => {
    const onResize = () => setPos((p) => clamp(p.x, p.y));
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const down = (e) => {
    if (e.button !== 0 || e.target.closest('button') || window.innerWidth <= 640) return;
    drag.current = { dx: e.clientX - pos.x, dy: e.clientY - pos.y };
    e.currentTarget.setPointerCapture(e.pointerId);
  };
  const move = (e) => { if (drag.current) setPos(clamp(e.clientX - drag.current.dx, e.clientY - drag.current.dy)); };
  const up = () => { drag.current = null; };

  return (
    <div
      ref={ref}
      className={`fpanel ${className}`}
      style={{ left: pos.x, top: pos.y, width, zIndex: z }}
      onPointerDownCapture={() => setZ(++topZ)}
      role="dialog"
      aria-label={title}
    >
      <div className="fpanel-bar" onPointerDown={down} onPointerMove={move} onPointerUp={up} onPointerCancel={up}>
        <Icon name={icon} size={15} />
        <span>{title}</span>
        <button className="fpanel-x" onClick={onClose} aria-label={`Close ${title}`}><Icon name="close" size={15} /></button>
      </div>
      <div className="fpanel-body">{children}</div>
    </div>
  );
}
