"""Figure builders for Frequency Response / Nyquist questions (ch. 5)."""
from figs import *

RE, IM = "\\mathrm{Re}", "\\mathrm{Img}"

def dashed(p, q, n=14):
    """Dashed straight line as short solid segments (plot 'lines')."""
    out = []
    for i in range(n):
        a, b = i / n, (i + 0.55) / n
        out.append({"from": [p[0] + (q[0] - p[0]) * a, p[1] + (q[1] - p[1]) * a],
                    "to": [p[0] + (q[0] - p[0]) * b, p[1] + (q[1] - p[1]) * b]})
    return out

def pts(*p, arrow=False, **kw):
    d = {"fn": "points", "pts": [list(x) for x in p]}
    if arrow: d["arrow"] = True
    d.update(kw)
    return d

def nyq(curves, labels=None, x=(-1.6, 1.6), y=(-1.3, 1.3), w=240, h=190, **kw):
    d = {"type": "plot", "w": w, "h": h, "x": list(x), "y": list(y), "xlabel": RE, "ylabel": IM, "ylabelDx": 8,
         "margin": {"l": 10, "r": 32, "t": 22, "b": 12}, "curves": curves, "labels": labels or [], "scale": 1}
    d.update(kw)
    return d

def minus1(x=-1.0, dy=-0.22):
    return {"x": x, "y": dy, "tex": "-1"}

def grid4(figs, cols=2):
    return {"type": "grid", "cols": cols, "items": [{"cap": f"({c})", "fig": f} for c, f in zip("abcd", figs)]}

# ---- 5.2  polar plot with unit circle, GM / PM
def q52():
    return {"type": "plot", "w": 400, "h": 300, "x": [-1.35, 2.0], "y": [-1.25, 1.25], "xlabel": "\\mathrm{Re}\\,G(j\\omega)", "ylabel": "\\mathrm{Img}\\,G(j\\omega)",
            "ylabelDx": 8, "margin": {"l": 10, "r": 90, "t": 24, "b": 12}, "scale": 1,
            "circle": {"r": 1, "cx": 0, "cy": 0}, "rays": [[1.55, -0.9]],
            "curves": [pts([1.5, 0.5], [1.15, -0.1], [0.8, -0.45], [0.3, -0.55], [-0.1, -0.4], [-0.28, -0.05], [-0.2, 0.2], [-0.05, 0.1], [0, -0.05], arrow=True)],
            "labels": [{"x": -1.0, "y": 0.14, "tex": "-1"}, {"x": -0.25, "y": 0.28, "tex": "-0.25"}, {"x": 1.0, "y": 0.14, "tex": "1"},
                       {"x": 0.12, "y": 1.1, "tex": "+j1"}, {"x": 0.12, "y": -1.1, "tex": "-j1"}, {"x": 0.62, "y": -0.2, "tex": "30^\\circ"}]}

# ---- 5.4  Nyquist plot with infinite-radius arc
def q54():
    return nyq([pts([-0.1, -1.6], [-0.1, -0.9], [-0.3, -0.2], [-0.27, 0.15], [-0.1, 0.9], [-0.1, 1.6], arrow=True)],
               x=(-0.7, 1.9), y=(-1.7, 1.7), w=330, h=250,
               circle={"r": 1.55, "cx": 0, "cy": 0}, margin={"l": 10, "r": 34, "t": 22, "b": 12})

# ---- 5.9  four candidate Nyquist sketches  (also reused geometry for 5.40)
def q59():
    m1 = [minus1()]
    a = nyq([pts([0.5, -0.05], [0.4, -0.38], [0.05, -0.5], [-0.28, -0.35], [-0.3, -0.05], arrow=True)], m1, y=(-0.9, 0.9), w=210, h=150)
    b = nyq([pts([-1.1, 0.0], [-0.85, 0.35], [-0.5, 0.5], [-0.2, 0.33], [0.0, 0.0], arrow=True)], m1, y=(-0.9, 0.9), w=210, h=150)
    c = nyq([pts([0.0, -1.5], [-0.08, -0.9], [-0.05, -0.2], [0.05, 0.5], [0.0, 1.0], [-0.2, 1.1], [-0.35, 0.6], [-0.35, 0.0], [-0.22, -0.45], arrow=True)], m1, y=(-1.6, 1.4), w=210, h=190)
    d = nyq([pts([1.0, 0.0], [0.8, 0.3], [0.45, 0.5], [0.15, 0.4], [0.0, 0.0], arrow=True)], m1, y=(-0.7, 0.9), w=210, h=150)
    return grid4([a, b, c, d])

# ---- 5.16 / 5.21 cardioid-type Nyquist plot
def q516():
    return nyq([pts([-0.1, 0.0], [-1.2, 0], [-2.2, 0]),
                pts([-0.1, 0.02], [-0.72, 0.15], [-0.92, 0.4], [-0.62, 0.8], [0, 0.93], [0.43, 0.7], [1, 0], arrow=True),
                pts([1, 0], [0.43, -0.7], [0, -0.93], [-0.62, -0.8], [-0.92, -0.4], [-0.72, -0.15], [-0.1, -0.02], arrow=False)],
               [{"x": 0.5, "y": 0.2, "tex": "\\omega=\\infty", "anchor": "end", "size": 12}, {"x": 1.02, "y": 0.2, "tex": "1.0", "anchor": "start", "size": 12},
                {"x": 1.02, "y": -0.2, "tex": "\\omega=0", "anchor": "start", "size": 12}],
               x=(-2.4, 1.9), y=(-1.25, 1.25), w=380, h=230, margin={"l": 10, "r": 34, "t": 22, "b": 12})

# ---- 5.18 / 5.82 / 5.85 / 5.86  Bode magnitude sketches
def bode(lines_, labels, xr, yr, w=340, h=250, ylabel="|G(j\\omega)H(j\\omega)|\\ \\mathrm{dB}", xlabel="\\omega\\ \\mathrm{rad/s}", **kw):
    ls = []
    for seg in lines_:
        ls.append({"from": list(seg[0]), "to": list(seg[1])})
    d = {"type": "plot", "w": w, "h": h, "x": list(xr), "y": list(yr), "xlabel": xlabel, "ylabel": ylabel, "ylabelDx": 8,
         "margin": {"l": 40, "r": 40, "t": 24, "b": 22}, "lines": ls, "labels": labels, "scale": 1}
    d.update(kw)
    return d

def q518():
    ls = [((0, 4.9), (3.2, 2.9)), ((3.2, 2.9), (5.2, 0)), ((5.2, 0), (5.55, -0.5))] + [(s["from"], s["to"]) for s in dashed((3.2, 2.9), (8.5, 0), 16)] + [(s["from"], s["to"]) for s in dashed((3.2, 2.9), (3.2, 0), 8)]
    return bode(ls, [{"x": 3.2, "y": -0.45, "tex": "\\omega_1"}, {"x": 5.2, "y": -0.45, "tex": "\\omega_2"}, {"x": 8.5, "y": -0.45, "tex": "\\omega_3"}, {"x": -0.35, "y": -0.3, "tex": "O"},
                   {"x": 5.3, "y": 4.2, "tex": "20\\ \\mathrm{dB/decade}"}, {"x": 7.3, "y": 2.2, "tex": "40\\ \\mathrm{dB/decade}"}],
                (0, 9.6), (-1.0, 5.4), ylabel="\\mathrm{Magnitude\\ (dB)}", xlabel="\\mathrm{Log}\\ \\omega", w=420, h=270, margin={"l": 14, "r": 44, "t": 24, "b": 22})

def q582():
    ls = [((0, 2.8), (1.2, 2.8)), ((1.2, 2.8), (3.6, 0)), ((3.6, 0), (4.3, -0.8))] + [(s["from"], s["to"]) for s in dashed((1.2, 2.8), (1.2, 0), 8)]
    return bode(ls, [{"x": -0.35, "y": 2.8, "tex": "20", "anchor": "end"}, {"x": -0.12, "y": 0.0, "tex": "0", "anchor": "end"}, {"x": 1.2, "y": -0.42, "tex": "1"},
                     {"x": 3.5, "y": 2.2, "tex": "-20\\ \\mathrm{dB/dec}"}], (-0.9, 5.2), (-1.2, 3.6), margin={"l": 30, "r": 70, "t": 24, "b": 22}, w=400, h=240)

def q585():
    k = 0.625
    y0 = 2.6; y2 = y0 - k * 1.5; y20 = y2 - 2 * k * 1.6
    ls = [((0, y0), (1.5, y2)), ((1.5, y2), (3.1, y20)), ((3.1, y20), (5.0, y20 - k * 1.9))] + [(s["from"], s["to"]) for s in dashed((1.5, y2), (1.5, 0), 7)] + [(s["from"], s["to"]) for s in dashed((3.1, y20), (3.1, 0), 5)]
    return bode(ls, [{"x": 1.5, "y": 0.4, "tex": "2"}, {"x": 3.1, "y": 0.45, "tex": "20", "size": 13},
                     {"x": 0.9, "y": 2.75, "tex": "-20\\ \\mathrm{dB/dec}", "anchor": "start", "size": 12}, {"x": 2.5, "y": 1.25, "tex": "-40\\ \\mathrm{dB/dec}", "anchor": "start", "size": 12},
                     {"x": 3.5, "y": -0.65, "tex": "-20\\ \\mathrm{dB/dec}", "anchor": "start", "size": 12}],
                (0, 6.4), (-1.5, 3.4), ylabel="G(j\\omega)H(j\\omega)\\ \\mathrm{dBs}", xlabel="\\omega\\,(\\mathrm{r/s})", w=420, h=260, margin={"l": 14, "r": 54, "t": 24, "b": 22})

def q586():
    ls = [((1.2, 0.3), (3.7, 2.5)), ((3.7, 2.5), (5.6, 0.0))] + [(s["from"], s["to"]) for s in dashed((0, 2.5), (6.2, 2.5), 22)] + [(s["from"], s["to"]) for s in dashed((3.7, 2.5), (3.7, 0), 8)]
    return bode(ls, [{"x": -0.15, "y": 2.5, "tex": "100\\ \\mathrm{dB}", "anchor": "end"}, {"x": 3.7, "y": -0.35, "tex": "10"},
                     {"x": 1.0, "y": 2.0, "tex": "40\\ \\mathrm{dB/dec}", "anchor": "start", "size": 12}, {"x": 4.4, "y": 1.9, "tex": "-60\\ \\mathrm{dB/dec}", "anchor": "start", "size": 12}],
                (-1.6, 6.4), (-0.8, 3.4), ylabel="G(j\\omega)H(j\\omega)\\ \\mathrm{dBs}", xlabel="\\omega\\,(\\mathrm{r/s})", w=420, h=260, margin={"l": 14, "r": 54, "t": 24, "b": 22})

# ---- 5.40 polar-plot candidates for 1/((jw)^2 (1+jwT))
def q540():
    lw = lambda t: {"x": -1.45, "y": 0.5, "tex": "0\\leftarrow\\omega", "size": 11}
    winf = lambda x, y: {"x": x, "y": y, "tex": "\\omega=\\infty", "anchor": "start", "size": 11}
    a = nyq([pts([0.75, 0.05], [0.6, -0.4], [0.1, -0.8], [-0.45, -0.55], [-0.65, 0.05], [-0.45, 0.4], [-0.1, 0.55], [0.03, 0.32], arrow=True)],
            [{"x": 0.3, "y": 0.2, "tex": "\\omega=0", "anchor": "start", "size": 11}], x=(-1.1, 1.3), y=(-1.0, 0.8), w=230, h=170)
    b = nyq([pts([-0.9, -1.1], [-0.8, -0.2], [-0.6, 0.35], [-0.35, 0.55], [-0.12, 0.4], [0, 0], arrow=True)], [winf(0.05, 0.22)], x=(-1.2, 1.3), y=(-1.2, 0.8), w=230, h=170)
    c = nyq([pts([-1.5, 0.12], [-1.0, 0.15], [-0.5, 0.3], [-0.2, 0.35], [0, 0], arrow=True)], [lw(0), winf(0.05, 0.25)], x=(-1.7, 1.2), y=(-0.5, 0.8), w=230, h=130)
    d = nyq([pts([-1.5, 0.1], [-0.9, 0.2], [-0.4, 0.5], [-0.05, 0.85], [0.3, 0.65], [0.3, 0.2], [0, 0], arrow=True)], [lw(0), winf(0.05, -0.2)], x=(-1.7, 1.2), y=(-0.5, 1.0), w=230, h=150)
    return grid4([a, b, c, d])

# ---- 5.44 gain-phase plot
def q544():
    ls = [(s["from"], s["to"]) for s in dashed((1.2, -1.15), (1.2, 1.15), 12)]
    return {"type": "plot", "w": 460, "h": 300, "x": [-0.7, 3.0], "y": [-1.2, 1.25], "xlabel": "\\text{Phase (degrees)}", "ylabel": "\\text{Gain (dB)}", "ylabelDx": 8,
            "margin": {"l": 10, "r": 100, "t": 24, "b": 12}, "scale": 1,
            "curves": [pts([0.45, -1.0], [0.6, -0.5], [0.85, -0.15], [1.1, 0.0], [1.25, 0.12], [1.6, 0.4], [2.1, 0.7], [2.3, 1.0])],
            "lines": [{"from": a, "to": b} for a, b in ls], "dots": [[1.1, 0.0]],
            "labels": [{"x": 0.3, "y": -0.16, "tex": "-270^\\circ"}, {"x": 1.2, "y": -0.16, "tex": "-180^\\circ", "anchor": "start"}, {"x": 2.1, "y": -0.16, "tex": "-90^\\circ"},
                       {"x": -0.1, "y": 0.8, "tex": "20\\,\\mathrm{dB}", "anchor": "end"}, {"x": -0.1, "y": -0.8, "tex": "-20\\,\\mathrm{dB}", "anchor": "end"},
                       {"x": 0.95, "y": -1.0, "tex": "\\omega=\\infty", "anchor": "start", "size": 12}, {"x": 0.7, "y": 0.28, "tex": "\\omega_{pc}", "size": 12}]}
