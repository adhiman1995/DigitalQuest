"""Figure-spec builders (JSON consumed by client/src/Figure.jsx)."""

def box(x, y, w, h, tex, size=16):
    return {"k": "box", "x": x, "y": y, "w": w, "h": h, "tex": tex, "size": size}

def sumn(x, y, signs, r=15):
    return {"k": "sum", "x": x, "y": y, "r": r, "signs": [{"at": a, "t": t} for a, t in signs]}

def edge(*pts, arrow=True):
    return {"p": [list(p) for p in pts], "arrow": arrow}

def lab(x, y, tex=None, text=None, anchor="middle", size=15):
    d = {"x": x, "y": y, "anchor": anchor, "size": size}
    if tex: d["tex"] = tex
    if text: d["text"] = text
    return d


def ufb(G, boxw=150, boxh=60, fb=None, fbw=64, rin="R(s)", cout="C(s)", elabel=False, size=16):
    """Single-loop negative feedback: R -> (+/-) -> G -> C, feedback from C back to the junction."""
    cy, sxc = 70, 100
    bx = 165 + boxw / 2
    right = 165 + boxw
    tap = right + 45
    ox = right + 90
    fy = 70 + 100
    nodes = [sumn(sxc, cy, [("l", "+"), ("b", "−")]), box(bx, cy, boxw, boxh, G, size)]
    edges = [
        edge((22, cy), (sxc - 15, cy)),
        edge((sxc + 15, cy), (165, cy)),
        edge((right, cy), (ox, cy)),
    ]
    labels = [lab(8, cy - 26, tex=rin, anchor="start"), lab(ox + 8, cy, tex=cout, anchor="start")]
    if elabel:
        labels.append(lab((sxc + 15 + 165) / 2, cy - 22, tex="E(s)"))
    if fb:
        fx = (sxc + tap) / 2
        nodes.append(box(fx, fy, fbw, 46, fb, size))
        edges += [edge((tap, cy), (tap, fy), (fx + fbw / 2, fy)), edge((fx - fbw / 2, fy), (sxc, fy), (sxc, cy + 15))]
    else:
        edges.append(edge((tap, cy), (tap, fy), (sxc, fy), (sxc, cy + 15)))
    return {"type": "block", "w": ox + 70, "h": fy + 30, "nodes": nodes, "edges": edges, "dots": [[tap, cy]], "labels": labels}


def disturbance_loop():
    """Q2.20: R -> o -> G1 -> o(+D) -> G2 -> C, unity feedback."""
    cy, fy = 100, 200
    nodes = [sumn(100, cy, [("l", "+"), ("b", "−")]), box(215, cy, 90, 54, "G_1(s)"),
             sumn(330, cy, [("l", "+"), ("t", "+")]), box(445, cy, 90, 54, "G_2(s)")]
    edges = [
        edge((22, cy), (85, cy)), edge((115, cy), (170, cy)), edge((260, cy), (315, cy)),
        edge((345, cy), (400, cy)), edge((490, cy), (600, cy)),
        edge((330, 36), (330, cy - 15)),
        edge((545, cy), (545, fy), (100, fy), (100, cy + 15)),
    ]
    labels = [lab(8, cy - 26, tex="R(s)", anchor="start"), lab(608, cy, tex="C(s)", anchor="start"),
              lab(330, 20, tex="D(s) = \\text{disturbance}", size=14)]
    return {"type": "block", "w": 680, "h": 230, "nodes": nodes, "edges": edges, "dots": [[545, cy]], "labels": labels}


def q247():
    cy, fy = 70, 170
    nodes = [sumn(100, cy, [("l", "+"), ("b", "−")]), box(190, cy, 56, 44, "10"), box(310, cy, 90, 58, "\\dfrac{1}{s+1}"),
             box(250, fy, 56, 52, "\\dfrac{1}{s}")]
    edges = [edge((22, cy), (85, cy)), edge((115, cy), (162, cy)), edge((218, cy), (265, cy)),
             edge((355, cy), (450, cy)),
             edge((410, cy), (410, fy), (278, fy)), edge((222, fy), (100, fy), (100, cy + 15))]
    labels = [lab(8, cy - 26, tex="R(s)", anchor="start"), lab(458, cy, tex="C(s)", anchor="start")]
    return {"type": "block", "w": 530, "h": 210, "nodes": nodes, "edges": edges, "dots": [[410, cy]], "labels": labels}


def q2107():
    cy = 90
    nodes = [sumn(100, cy, [("l", "+"), ("b", "−")]), box(215, cy, 86, 58, "\\dfrac{K}{s}"),
             sumn(335, cy, [("l", "+"), ("b", "−")]), box(470, cy, 96, 58, "\\dfrac{10}{s}"),
             box(400, 165, 58, 40, "0.1"), box(380, 235, 40, 38, "1")]
    edges = [
        edge((22, cy), (85, cy)), edge((115, cy), (172, cy)), edge((258, cy), (320, cy)),
        edge((350, cy), (422, cy)), edge((518, cy), (690, cy)),
        edge((565, cy), (565, 165), (429, 165)), edge((371, 165), (335, 165), (335, cy + 15)),
        edge((640, cy), (640, 235), (400, 235)), edge((360, 235), (100, 235), (100, cy + 15)),
    ]
    labels = [lab(8, cy - 28, tex="V_r(s)", anchor="start"), lab(150, cy - 30, tex="E(s)"),
              lab(215, 36, text="Controller"), lab(470, 36, text="Motor"), lab(698, cy, tex="\\omega(s)", anchor="start"),
              lab(380, 270, text="Tachometer")]
    return {"type": "block", "w": 780, "h": 290, "nodes": nodes, "edges": edges, "dots": [[565, cy], [640, cy]], "labels": labels}


# ------------------------------------------------------------------ plots
def splane(poles=None, zeros=None, **kw):
    d = {"type": "plot", "w": 250, "h": 190, "x": [-3, 3], "y": [-2.2, 2.2], "xlabel": "\\sigma", "ylabel": "j\\omega",
         "poles": poles or [], "zeros": zeros or [], "scale": 1}
    d.update(kw)
    return d

def tplot(curves, **kw):
    d = {"type": "plot", "w": 250, "h": 170, "x": [0, 10], "y": [-1.4, 1.4], "xlabel": "t", "ylabel": "C",
         "margin": {"l": 26, "r": 30, "t": 24, "b": 20}, "curves": curves, "scale": 1}
    d.update(kw)
    return d

def q29():
    items = [
        ("A", splane(poles=[[-2.3, 0], [-1.3, 0], [0.8, 0], [1.8, 0]], y=[-1.6, 1.6], labels=[
            {"x": -2.3, "y": -0.5, "tex": "-\\alpha_3"}, {"x": -1.3, "y": -0.5, "tex": "-\\alpha_2"}, {"x": 0.8, "y": -0.5, "tex": "\\alpha_1"}])),
        ("B", splane(poles=[[0, 1.1], [0, -1.1]], labels=[{"x": 0.55, "y": 1.1, "tex": "j\\omega"}, {"x": 0.65, "y": -1.1, "tex": "-j\\omega"}])),
        ("C", splane(poles=[[1.1, 1.1], [1.1, -1.1]], vlines=[{"x": 1.1}], labels=[
            {"x": 1.7, "y": 1.1, "tex": "j\\omega"}, {"x": 1.1, "y": -0.45, "tex": "\\alpha"}, {"x": 1.8, "y": -1.1, "tex": "-j\\omega"}])),
        ("D", splane(poles=[[-1.1, 1.1], [-1.1, -1.1]], vlines=[{"x": -1.1}], labels=[
            {"x": -1.9, "y": 1.1, "tex": "j\\omega"}, {"x": -1.1, "y": -0.45, "tex": "-\\alpha"}, {"x": 1.4, "y": -0.45, "tex": "\\alpha"}, {"x": -1.9, "y": -1.1, "tex": "-j\\omega"}])),
    ]
    resp = [
        tplot([{"fn": "expsin", "A": 0.9, "sigma": -0.13, "omega": 2.3, "t": [0, 9]}], x=[0, 9]),
        tplot([{"fn": "expsin", "A": 0.35, "sigma": 0.2, "omega": 1.55, "t": [0, 9]}], x=[0, 9], y=[-1.4, 1.4]),
        tplot([{"fn": "expsin", "A": 0.8, "sigma": 0, "omega": 1.8, "t": [0, 9]}], x=[0, 9]),
        tplot([{"fn": "sumexp", "terms": [[1.25, -0.9], [0.05, 0.55]], "t": [0, 9]}], x=[0, 9], y=[-0.2, 1.6]),
    ]
    cells = []
    for i in range(4):
        cells.append({"cap": f"**{items[i][0]}.**", "fig": items[i][1]})
        cells.append({"cap": f"**{i + 1}.**", "fig": resp[i]})
    return {"type": "grid", "cols": 2, "items": cells}

def q215():
    t1, t2 = 0.462, 0.994
    return {"type": "plot", "w": 400, "h": 250, "x": [0, 3.2], "y": [-0.08, 1.12], "xlabel": "t", "ylabel": "K", "ylabelDx": -14,
            "margin": {"l": 54, "r": 30, "t": 28, "b": 36}, "scale": 1,
            "curves": [{"fn": "sumexp", "terms": [[1, -1]], "t": [0, 3.2]}],
            "guides": [{"x": t1, "y": 0.63, "xtex": "t_1", "ytex": "0.63K", "dot": True}, {"x": t2, "y": 0.37, "xtex": "t_2", "ytex": "0.37K"}],
            "annots": [{"at": [1.9, 0.78], "to": [1.15, 0.34], "tex": "\\text{Unit Impulse Response}", "anchor": "middle"}]}

def q238():
    return {"type": "plot", "w": 330, "h": 270, "x": [-2.8, 1.4], "y": [-2.1, 2.1], "xlabel": "\\mathrm{Re}", "ylabel": "\\mathrm{Img}", "scale": 1,
            "margin": {"l": 20, "r": 48, "t": 30, "b": 20},
            "poles": [[-1, 1], [-1, -1]], "circle": {"r": 1.4142}, "rays": [[-1.45, 1.45], [-1.45, -1.45]],
            "arcs": [{"r": 0.6, "from": 0, "to": 45}, {"r": 0.6, "from": 0, "to": -45}],
            "dims": [{"x": 0.45, "from": 0, "to": 1.4142, "tex": "1"}],
            "labels": [{"x": -0.98, "y": 0.28, "tex": "45^\\circ", "size": 12}, {"x": -0.98, "y": -0.28, "tex": "45^\\circ", "size": 12}]}

def q243():
    def p(pts, **kw):
        return {"type": "plot", "w": 300, "h": 190, "x": [0, 4.6], "y": [-1.25, 1.25], "xlabel": "\\text{Time}", "ylabel": "y(t)", "ylabelDx": -6,
                "margin": {"l": 40, "r": 56, "t": 26, "b": 20}, "origin": True, "curves": pts, "scale": 1, **kw}
    return {"type": "grid", "cols": 2, "items": [
        {"cap": "**(a)**", "fig": p([{"fn": "points", "pts": [[0, 1.0], [0.6, 0.62], [1.4, 0.42], [2.3, 0.35], [3.2, 0.4], [4.2, 0.5]]}])},
        {"cap": "**(b)**", "fig": p([{"fn": "points", "pts": [[0, -1.0], [0.6, -0.62], [1.4, -0.42], [2.3, -0.35], [3.2, -0.4], [4.2, -0.5]]}])},
        {"cap": "**(c)**", "fig": p([{"fn": "expsin", "A": 0.3, "sigma": 0.24, "omega": 5.2, "phi": 0.35, "t": [0, 4.6], "envelope": True}])},
        {"cap": "**(d)**", "fig": p([{"fn": "expsin", "A": 1.0, "sigma": -0.4, "omega": 5.4, "phi": 1.5708, "t": [0, 4.6], "envelope": True}])},
    ]}

def q291():
    return {"type": "plot", "w": 420, "h": 260, "x": [0, 0.34], "y": [-0.3, 6.4], "xlabel": "t", "ylabel": "c(t)", "origin": True, "scale": 1,
            "margin": {"l": 52, "r": 30, "t": 28, "b": 34},
            "curves": [{"fn": "sumexp", "terms": [[-5, -10]], "c": 5, "t": [0, 0.34]}],
            "lines": [{"from": [0, 0], "to": [0.128, 6.4]}],
            "guides": [{"y": 5, "ytex": "5.0"}, {"x": 0.1, "y": 5, "xtex": "0.1\\,\\mathrm{s}", "dot": True}],
            "annots": [{"at": [0.215, 3.4], "to": [0.105, 4.9], "tex": "\\text{Slope at origin}", "anchor": "middle"}],
            "labels": [{"x": 0.29, "y": 2.0, "tex": "G(s)=\\dfrac{K}{s+a}", "size": 14}]}


# ------------------------------------------------------------------ added for chapters 1, 3, 4
def pt(x, y):
    return {"k": "pt", "x": x, "y": y}

def trim(a, b, t=6):
    """Shorten the end of a straight edge so the arrowhead stops at the node boundary."""
    import math
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = math.hypot(dx, dy) or 1
    return (b[0] - dx / d * t, b[1] - dy / d * t)

def chain_loop(boxes, fb=None, fbw=84, gap=46, rin="R(s)", cout="C(s)", size=16):
    """Negative feedback loop with several blocks in the forward path."""
    cy, sxc = 70, 100
    x = 165
    nodes = [sumn(sxc, cy, [("l", "+"), ("b", "−")])]
    edges = [edge((22, cy), (sxc - 15, cy))]
    prev = sxc + 15
    for tex, w in boxes:
        nodes.append(box(x + w / 2, cy, w, 60, tex, size))
        edges.append(edge((prev, cy), (x, cy)))
        prev = x + w
        x = x + w + gap
    tap, ox, fy = prev + 45, prev + 90, 170
    edges.append(edge((prev, cy), (ox, cy)))
    if fb:
        fx = (sxc + tap) / 2
        nodes.append(box(fx, fy, fbw, 50, fb, size))
        edges += [edge((tap, cy), (tap, fy), (fx + fbw / 2, fy)), edge((fx - fbw / 2, fy), (sxc, fy), (sxc, cy + 15))]
    else:
        edges.append(edge((tap, cy), (tap, fy), (sxc, fy), (sxc, cy + 15)))
    labels = [lab(8, cy - 26, tex=rin, anchor="start"), lab(ox + 8, cy, tex=cout, anchor="start")]
    return {"type": "block", "w": ox + 80, "h": fy + 30, "nodes": nodes, "edges": edges, "dots": [[tap, cy]], "labels": labels}

def series(boxes, rin="R(s)", cout="C(s)", gap=50, size=16):
    cy, x = 50, 100
    nodes, edges, prev = [], [edge((18, cy), (x, cy))], x
    for tex, w in boxes:
        nodes.append(box(x + w / 2, cy, w, 56, tex, size))
        x += w
        if len(nodes) < len(boxes):
            edges.append(edge((x, cy), (x + gap, cy)))
            x += gap
    edges.append(edge((x, cy), (x + 70, cy)))
    return {"type": "block", "w": x + 130, "h": 100, "nodes": nodes, "edges": edges,
            "labels": [lab(8, cy - 26, tex=rin, anchor="start"), lab(x + 78, cy, tex=cout, anchor="start")]}

def dist_loop(g1, g2, g1w=60, g2w=100, dlabel="d(s)", rin="R(s)", cout="Y(s)"):
    cy, fy = 100, 200
    x2 = 215 + g1w / 2 + 70
    nodes = [sumn(100, cy, [("l", "+"), ("b", "−")]), box(215, cy, g1w, 54, g1),
             sumn(x2 + 0, cy, [("l", "+"), ("t", "+")]), box(x2 + 115, cy, g2w, 58, g2)]
    xe = x2 + 115 + g2w / 2
    edges = [edge((22, cy), (85, cy)), edge((115, cy), (215 - g1w / 2, cy)), edge((215 + g1w / 2, cy), (x2 - 15, cy)),
             edge((x2 + 15, cy), (x2 + 115 - g2w / 2, cy)), edge((xe, cy), (xe + 70, cy)),
             edge((x2, 36), (x2, cy - 15)), edge((xe + 30, cy), (xe + 30, fy), (100, fy), (100, cy + 15))]
    labels = [lab(8, cy - 26, tex=rin, anchor="start"), lab(xe + 78, cy, tex=cout, anchor="start"), lab(x2, 20, tex=dlabel, size=14)]
    return {"type": "block", "w": xe + 150, "h": 230, "nodes": nodes, "edges": edges, "dots": [[xe + 30, cy]], "labels": labels}

def q126():
    cy, cy2 = 80, 160
    nodes = [sumn(90, cy, [("l", "+"), ("b", "−")]), box(260, cy, 84, 56, "\\dfrac{1}{s+1}"),
             box(260, cy2, 84, 56, "\\dfrac{1}{s+1}"), sumn(380, cy2, [("t", "+"), ("l", "−")])]
    edges = [edge((18, cy), (75, cy)), edge((105, cy), (218, cy)), edge((302, cy), (460, cy)),
             edge((150, cy), (150, cy2), (218, cy2)), edge((302, cy2), (365, cy2)),
             edge((380, cy), (380, cy2 - 15)), edge((380, cy2 + 15), (380, 225), (90, 225), (90, cy + 15))]
    return {"type": "block", "w": 520, "h": 245, "nodes": nodes, "edges": edges, "dots": [[150, cy], [380, cy]],
            "labels": [lab(8, cy - 26, tex="R(s)", anchor="start"), lab(468, cy, tex="C(s)", anchor="start")]}

def q13_sfg():
    X1, N1, N2, X2, N3, N4 = (24, 60), (130, 60), (220, 60), (326, 60), (130, 150), (220, 150)
    def e(a, b, **k):
        return {"p": [list(a), list(trim(a, b))], "arrow": True, **k}
    edges = [e(X1, N1), e(N1, N2), e(N2, X2), e(X1, N3), e(N3, N4), e(N4, X2),
             {"p": [list(N2), list(N1)], "q": [175, -6], "arrow": True},
             {"p": [list(N4), list(N3)], "q": [175, 100], "arrow": True}]
    nodes = [pt(*X1), pt(*N1), pt(*N2), pt(*X2), pt(*N3), pt(*N4)]
    labels = [lab(24, 38, tex="x_1"), lab(326, 38, tex="x_2"), lab(78, 44, tex="r", size=14), lab(175, 76, tex="s", size=14),
              lab(273, 44, tex="u", size=14), lab(60, 118, tex="e", size=14), lab(175, 166, tex="f", size=14),
              lab(290, 118, tex="h", size=14), lab(175, 14, tex="t", size=14), lab(175, 120, tex="g", size=14)]
    return {"type": "block", "w": 360, "h": 185, "nodes": nodes, "edges": edges, "labels": labels, "scale": 1.2}

def rl_axes(**kw):
    d = {"type": "plot", "w": 330, "h": 250, "x": [-3, 1.2], "y": [-1.8, 1.8], "xlabel": "\\sigma", "ylabel": "j\\omega", "scale": 1,
         "margin": {"l": 14, "r": 34, "t": 24, "b": 18}, "poles": [], "zeros": [], "curves": []}
    d.update(kw)
    return d

def q44():
    return rl_axes(w=380, h=300, x=[-2.4, 3.2], y=[-2.2, 2.2], poles=[[-1.35, 0], [0, 0]],
                   curves=[{"fn": "points", "pts": [[-1.4, 0], [-1.95, 0]], "arrow": True},
                           {"fn": "points", "pts": [[0, 0], [-0.06, 0.55], [0.25, 1.15], [1.3, 1.4]], "arrow": True},
                           {"fn": "points", "pts": [[0, 0], [-0.06, -0.55], [0.25, -1.15], [1.3, -1.4]], "arrow": True}],
                   labels=[{"x": 0.95, "y": 0.95, "tex": "r_1"}, {"x": 0.95, "y": -0.95, "tex": "r_2"}, {"x": -1.95, "y": -0.35, "tex": "r_3"}])

def q47():
    return rl_axes(w=380, h=270, x=[-4.4, 1.6], y=[-2.2, 2.2], xlabel="\\mathrm{Re}", ylabel="\\mathrm{Img}", ylabelDx=8,
                   circle={"r": 1.414, "cx": -2, "cy": 0, "solid": True}, dots=[[0, 0], [-1, 0], [-2, 0]],
                   curves=[{"fn": "points", "pts": [[0, 0], [-0.55, 0]], "arrow": True},
                           {"fn": "points", "pts": [[-1, 0], [-0.62, 0]], "arrow": True}],
                   labels=[{"x": -2, "y": -0.5, "tex": "-2"}, {"x": -1, "y": -0.5, "tex": "-1"}, {"x": 0.12, "y": -0.5, "tex": "0"}])

def q427():
    ticks = [{"from": [-2.12, y], "to": [-1.88, y]} for y in (-1.6, -0.9, 0.9, 1.6)]
    return rl_axes(w=360, h=280, x=[-3.8, 1.2], y=[-2.3, 2.3], poles=[[-3, 0], [-1, 0]],
                   lines=[{"from": [-2, -2.1], "to": [-2, 2.1]}] + ticks,
                   labels=[{"x": -3, "y": -0.5, "tex": "-3"}, {"x": -1, "y": -0.5, "tex": "-1"}])

def q417():
    def P(**kw):
        return rl_axes(w=330, h=230, x=[-2.6, 1.0], y=[-1.5, 1.5], margin={"l": 10, "r": 26, "t": 22, "b": 12}, **kw)
    p1 = P(poles=[[-0.45, 0.4], [-0.45, -0.4]], zeros=[[-1.1, 0]],
           curves=[{"fn": "points", "pts": [[-0.45, 0.4], [-0.9, 0.95], [-1.6, 0.7], [-1.85, 0], [-1.6, -0.7], [-0.9, -0.95], [-0.45, -0.4]]},
                   {"fn": "points", "pts": [[-1.85, 0], [-2.4, 0]], "arrow": True}])
    p2 = P(circle={"r": 0.75, "cx": -1.2, "cy": 0, "solid": True}, poles=[[-1.05, 0], [-0.2, 0]], zeros=[[-1.63, 0]],
           curves=[{"fn": "points", "pts": [[-0.2, 0], [-0.5, 0]], "arrow": True}, {"fn": "points", "pts": [[-1.95, 0], [-2.45, 0]], "arrow": True}])
    p3 = P(zeros=[[-1.65, 0]], poles=[[-0.45, 0], [-1.13, 0.73], [-1.13, -0.7]],
           curves=[{"fn": "points", "pts": [[-0.5, 0], [-1.0, 0]], "arrow": True},
                   {"fn": "points", "pts": [[-1.13, 0.73], [-0.9, 0.83], [-0.5, 1.1]], "arrow": True},
                   {"fn": "points", "pts": [[-1.13, -0.7], [-0.9, -0.83], [-0.4, -1.1]], "arrow": True}])
    p4 = P(circle={"r": 0.75, "cx": -1.1, "cy": 0, "solid": True}, zeros=[[-1.45, 0]], poles=[[-0.75, 0], [-0.02, 0], [-0.18, 0.72], [-0.18, -0.72]],
           curves=[{"fn": "points", "pts": [[-0.18, 0.72], [0.1, 0.9], [0.4, 1.1]], "arrow": True},
                   {"fn": "points", "pts": [[-0.18, -0.72], [0.1, -0.9], [0.4, -1.1]], "arrow": True}])
    return {"type": "grid", "cols": 2, "items": [{"cap": "**1.**", "fig": p1}, {"cap": "**2.**", "fig": p2}, {"cap": "**3.**", "fig": p3}, {"cap": "**4.**", "fig": p4}]}
