import { useCallback, useEffect, useRef, useState } from 'react';

const KEY = 'ese-ece-progress-v1';
const EMPTY = {
  owner: null,    // account id this local copy belongs to (null = guest)
  updatedAt: 0,   // ms timestamp of the last change; drives last-write-wins sync
  done: {},       // syllabus topic id -> true
  solved: {},     // question id -> true
  bookmarks: {},  // question id -> true
  added: {},      // question id -> true (practice set)
  responses: {},  // question id -> 'A'..'D' (option chosen in practice mode)
  exams: [],      // finished exam attempts
  session: null,  // exam currently in progress
};
const MAPS = ['done', 'solved', 'bookmarks', 'added', 'responses'];

const load = () => {
  try {
    return { ...EMPTY, ...JSON.parse(localStorage.getItem(KEY) || '{}') };
  } catch {
    return { ...EMPTY };
  }
};
const hasData = (s) => MAPS.some((k) => Object.keys(s[k] || {}).length) || (s.exams || []).length > 0 || !!s.session;

// Union of two copies (used once, when a guest who already has progress signs in).
function merge(local, remote) {
  const out = { ...EMPTY };
  for (const k of MAPS) out[k] = k === 'responses' ? { ...(remote[k] || {}), ...(local[k] || {}) } : { ...(remote[k] || {}), ...(local[k] || {}) };
  const byId = new Map([...(remote.exams || []), ...(local.exams || [])].map((e) => [e.id, e]));
  out.exams = [...byId.values()].sort((a, b) => a.finishedAt - b.finishedAt);
  const sessions = [local.session, remote.session].filter(Boolean);
  out.session = sessions.sort((a, b) => b.startedAt - a.startedAt)[0] || null;
  return out;
}

const api = async (method, url, body) => {
  const r = await fetch(url, { method, headers: body ? { 'Content-Type': 'application/json' } : undefined, body: body ? JSON.stringify(body) : undefined, keepalive: method === 'PUT' });
  let json = null;
  try { json = await r.json(); } catch { /* empty body */ }
  return { status: r.status, ok: r.ok, json };
};

// Progress lives in localStorage (works offline, works for guests). When a user is signed in it is also
// saved to their account, so it follows them across devices.
export function useProgress(user) {
  const [state, setStateRaw] = useState(load);
  const [sync, setSync] = useState('local'); // local | syncing | saved | error
  const [pulled, setPulled] = useState(0);    // bumps when the initial pull finishes, so a pending upload starts
  const stateRef = useRef(state);
  stateRef.current = state;
  const pushed = useRef(0);   // updatedAt of the newest copy the server has confirmed
  const ready = useRef(false); // initial pull for this account has finished
  const timer = useRef(null);

  useEffect(() => {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch { /* storage unavailable */ }
  }, [state]);

  // every user-visible change goes through here so updatedAt always moves forward
  const update = useCallback((fn) => setStateRaw((s) => ({ ...fn(s), updatedAt: Math.max(Date.now(), s.updatedAt + 1) })), []);

  const adopt = useCallback((remote, userId) => {
    pushed.current = remote.updatedAt;
    setStateRaw({ ...EMPTY, ...remote.data, owner: userId, updatedAt: remote.updatedAt });
  }, []);

  // ---- pull when the signed-in account changes
  useEffect(() => {
    ready.current = false;
    if (!user) { setSync('local'); return undefined; }
    let cancelled = false;
    (async () => {
      setSync('syncing');
      const r = await api('GET', '/api/progress').catch(() => null);
      if (cancelled) return;
      if (!r?.ok) { setSync('error'); return; }
      const remote = r.json; // { data|null, updatedAt }
      const local = stateRef.current;
      const mine = local.owner === user.id;
      if (remote.data) {
        if (mine && local.updatedAt > remote.updatedAt) { pushed.current = remote.updatedAt; }
        else if (!mine && !local.owner && hasData(local)) {
          // a guest with progress just signed in: keep both
          setStateRaw({ ...merge(local, remote.data), owner: user.id, updatedAt: Date.now() });
          pushed.current = remote.updatedAt;
        } else adopt(remote, user.id);
      } else if (mine || (!local.owner && hasData(local))) {
        setStateRaw({ ...local, owner: user.id, updatedAt: Math.max(local.updatedAt, 1) });
        pushed.current = 0;
      } else {
        setStateRaw({ ...EMPTY, owner: user.id });
      }
      ready.current = true;
      setPulled((n) => n + 1);
      setSync('saved');
    })();
    return () => { cancelled = true; };
  }, [user?.id, adopt]); // eslint-disable-line react-hooks/exhaustive-deps

  // ---- push (debounced) whenever there is something newer than the server's copy
  const push = useCallback(async () => {
    const s = stateRef.current;
    if (!user || !ready.current || s.updatedAt <= pushed.current) return;
    setSync('syncing');
    const { owner, ...data } = s;
    const r = await api('PUT', '/api/progress', { data, updatedAt: s.updatedAt }).catch(() => null);
    if (!r) { setSync('error'); return; }
    if (r.ok) { pushed.current = Math.max(pushed.current, s.updatedAt); setSync(stateRef.current.updatedAt > pushed.current ? 'syncing' : 'saved'); }
    else if (r.status === 409 && r.json?.data) { adopt(r.json, user.id); setSync('saved'); }
    else if (r.status === 401) setSync('error');
    else setSync('error');
  }, [user, adopt]);

  useEffect(() => {
    if (!user || !ready.current || state.updatedAt <= pushed.current) return undefined;
    setSync('syncing');
    clearTimeout(timer.current);
    timer.current = setTimeout(push, 700);
    return () => clearTimeout(timer.current);
  }, [state.updatedAt, user, push, pulled, sync === 'error' && 'retry']); // eslint-disable-line react-hooks/exhaustive-deps

  // ---- pick up changes made on another device; flush on tab close; retry when back online
  useEffect(() => {
    if (!user) return undefined;
    const refresh = async () => {
      if (document.visibilityState !== 'visible' || !ready.current) return;
      if (stateRef.current.updatedAt > pushed.current) { push(); return; }
      const r = await api('GET', '/api/progress').catch(() => null);
      if (r?.ok && r.json.data && r.json.updatedAt > stateRef.current.updatedAt) adopt(r.json, user.id);
    };
    const flush = () => { if (stateRef.current.updatedAt > pushed.current) push(); };
    document.addEventListener('visibilitychange', refresh);
    window.addEventListener('online', refresh);
    window.addEventListener('pagehide', flush);
    return () => {
      document.removeEventListener('visibilitychange', refresh);
      window.removeEventListener('online', refresh);
      window.removeEventListener('pagehide', flush);
    };
  }, [user, push, adopt]);

  // ---- actions
  const toggle = useCallback((bucket, id) => {
    update((s) => {
      const next = { ...s[bucket] };
      if (next[id]) delete next[id];
      else next[id] = true;
      return { ...s, [bucket]: next };
    });
  }, [update]);

  const setMany = useCallback((bucket, ids, value) => {
    update((s) => {
      const next = { ...s[bucket] };
      for (const id of ids) {
        if (value) next[id] = true;
        else delete next[id];
      }
      return { ...s, [bucket]: next };
    });
  }, [update]);

  const setResponse = useCallback((id, letter) => {
    update((s) => {
      const next = { ...s.responses };
      if (letter) next[id] = letter;
      else delete next[id];
      return { ...s, responses: next };
    });
  }, [update]);

  const setSession = useCallback((session) => update((s) => ({ ...s, session })), [update]);
  const addExam = useCallback((exam) => update((s) => ({ ...s, exams: [...s.exams.filter((e) => e.id !== exam.id), exam] })), [update]);
  const deleteExam = useCallback((id) => update((s) => ({ ...s, exams: s.exams.filter((e) => e.id !== id) })), [update]);

  const exportData = useCallback(() => {
    const { owner, ...data } = stateRef.current;
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'ese-progress.json';
    a.click();
    URL.revokeObjectURL(a.href);
  }, []);

  const importData = useCallback(async (file) => {
    const parsed = JSON.parse(await file.text());
    update((s) => ({ ...EMPTY, ...parsed, owner: s.owner }));
  }, [update]);

  // Before signing out: make sure the server has the latest copy, then wipe this browser's copy
  // so the next person on a shared computer starts clean.
  const clearLocalAfterFlush = useCallback(async () => {
    clearTimeout(timer.current);
    await push();
    try { localStorage.removeItem(KEY); } catch { /* ignore */ }
    ready.current = false;
    pushed.current = 0;
    setStateRaw({ ...EMPTY });
  }, [push]);

  return { state, sync, toggle, setMany, setResponse, setSession, addExam, deleteExam, exportData, importData, clearLocalAfterFlush };
}
