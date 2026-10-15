# Detailed solutions, chapter 5 (Nyquist stability).
# number -> (answer, concept, solution, [points to take care of])
D = {
"5.4": ("B", r"The low-frequency end of a Nyquist (polar) plot reveals the type: type $N$ starts at infinity with phase $-90^\circ\times N$.",
r"""**Step 1 – Read the low-frequency behaviour.** The plot comes in from infinity along a **vertical** direction (parallel to the imaginary axis, at $-j\infty$ for $\omega\to0^+$). Its mirror image comes from $+j\infty$ for $\omega\to0^-$, and the two are joined by a large semicircle.

**Step 2 – Link to type.** $G(j\omega)\approx\dfrac{K}{(j\omega)^N}$ as $\omega\to0$, so the starting phase is $-90^\circ N$.
- Type 0: starts at a finite point on the positive real axis.
- **Type 1: starts at $\infty\angle-90^\circ$ (along $-j\infty$).** ✓
- Type 2: starts at $\infty\angle-180^\circ$ (along the negative real axis).
- Type 3: starts at $\infty\angle-270^\circ$ (along $+j\infty$).

**Step 3 – Closing semicircle.** A single pole at the origin gives one infinite semicircle ($180^\circ$), as drawn.

Answer: **(b)**""",
[r"The number of infinite half-circles in the full Nyquist contour equals the number of poles at the origin.",
 r"A type-1 plot approaches a vertical asymptote at $\text{Re}=$ a finite value, not the imaginary axis itself (unless there are no other poles)."]),

"5.8": ("A", r"Find the phase at $\omega\to0$ and $\omega\to\infty$, then decide the quadrant from the exact angle (just above or just below a multiple of $90^\circ$).",
r"""$$G(j\omega)H(j\omega)=\dfrac{10}{(j\omega)^2(1+j0.5\omega)(1+j\omega)}$$
$$\phi(\omega)=-180^\circ-\tan^{-1}0.5\omega-\tan^{-1}\omega$$

**$\omega\to0$ (termination):** $\phi=-180^\circ-\epsilon$ with $|G|\to\infty$.
An angle slightly below $-180^\circ$ is the same as $+180^\circ-\epsilon$, which is in the **second quadrant**.

**$\omega\to\infty$ (start):** each $\tan^{-1}\to90^\circ$ from below, so $\phi\to-360^\circ+\epsilon$ with $|G|\to0$.
An angle slightly above $-360^\circ$ is the same as $+\epsilon$, which is in the **first quadrant**.

Starts ($\omega=\infty$) in the first quadrant and ends ($\omega=0$) in the second quadrant.

Answer: **(a)**""",
[r"The question uses 'start' for $\omega=\infty$ and 'terminate' for $\omega=0$, the reverse of the usual description. Read it carefully.",
 r"Convert angles to $(-180^\circ,180^\circ]$ before naming quadrants: $-180^\circ-\epsilon\equiv180^\circ-\epsilon$ (Q2) and $-360^\circ+\epsilon\equiv\epsilon$ (Q1).",
 r"Type 2 with two lags: the plot spirals clockwise from Q2 through Q1 as $\omega$ increases. The closed loop is unstable (it encircles $-1$)."]),

"5.9": ("C", r"Type 1 with two lags: the polar plot starts at $\infty\angle-90^\circ$ (from $-j\infty$) and ends at the origin with phase $-270^\circ$ (approaching from the $+j$ side).",
r"""**Step 1 – Low frequency.** $G\approx\dfrac{5}{j\omega}$, so $|G|\to\infty$ at $-90^\circ$. The plot comes in from $-j\infty$.

**Step 2 – High frequency.** $G\approx\dfrac{5}{(j\omega)(0.1j\omega)(0.01j\omega)}$, so $|G|\to0$ at $-270^\circ$. The plot reaches the origin from the $+j$ (second-quadrant) side.

**Step 3 – Negative real-axis crossing.** Phase $-180^\circ$ occurs when $\tan^{-1}0.1\omega+\tan^{-1}0.01\omega=90^\circ$, i.e. $0.1\omega\cdot0.01\omega=1\Rightarrow\omega_{pc}=31.6$ rad/s. There
$$|G(j\omega_{pc})|=\dfrac{K\,T_1T_2}{T_1+T_2}=\dfrac{5\times0.1\times0.01}{0.1+0.01}=0.045$$
The crossing is at $-0.045$, well between $0$ and $-1$ (stable, $GM\approx22$).

**Step 4 – Match.** Only plot (c) starts from $-j\infty$ (an integrator) and curls round to approach the origin from the upper-left, after crossing the negative real axis. Plots (a), (b), (d) start at finite points, which would be type 0.

Answer: **(c)**""",
[r"Useful formula: for $\dfrac{K}{s(1+sT_1)(1+sT_2)}$, the negative real-axis crossing is at $-\dfrac{KT_1T_2}{T_1+T_2}$ and $\omega_{pc}=\dfrac{1}{\sqrt{T_1T_2}}$.",
 r"Eliminate options by type first: any plot starting at a finite point cannot have an integrator."]),

"5.16": ("B", r"Match a Nyquist plot by its $\omega=0$ value (DC gain), its $\omega=\infty$ approach angle ($-90^\circ\times$ relative degree), and any axis crossings.",
r"""**Step 1 – $\omega=0$.** The plot starts at $+1$, so the DC gain is $G(0)=1$.
- (c) $\dfrac{1}{s^2+2s+2}$ has $G(0)=0.5$ ✗

**Step 2 – $\omega\to\infty$.** The plot reaches the origin tangent to the *negative real axis*, i.e. phase $\to-180^\circ$. So the relative degree is 2.
- (a) $\dfrac{1}{(s+1)^3}$ would end at $-270^\circ$ ✗
- (d) $\dfrac{1}{s+1}$ would end at $-90^\circ$ ✗

**Step 3 – Check (b).** $\dfrac{1}{(1+j\omega)^2}$: magnitude $\dfrac{1}{1+\omega^2}$, phase $-2\tan^{-1}\omega$. At $\omega=1$: $|G|=0.5$, $\angle=-90^\circ$, so it crosses the imaginary axis at $-j0.5$. It never reaches $-180^\circ$ at finite $\omega$, so it never crosses the negative real axis ✓.

Answer: **(b)**""",
[r"Three checks are usually enough: starting point, ending angle, and axis crossings.",
 r"A plot that touches $-180^\circ$ only at $\omega=\infty$ has infinite gain margin."]),

"5.21": ("B", r"Same plot as 5.16: DC value 1 and end phase $-180^\circ$ identify $\dfrac{1}{(s+1)^2}$.",
r"""This is the same figure and options as question 5.16.

- The start at $+1$ gives DC gain 1, which rules out $\dfrac{1}{s^2+2s+2}$ (DC gain 0.5).
- The approach to the origin along the negative real axis means relative degree 2, which rules out the first- and third-order options.
- $\dfrac{1}{(s+1)^2}$: $|G(j1)|=0.5$ at $-90^\circ$, consistent with the plot.

Answer: **(b)**""",
[r"Repeated question (ESE 2003 and 2004). The approach is the same, but always recheck the option order."]),

"5.37": ("B", r"Nyquist criterion: $Z=N+P$, using open-loop RHP poles $P$ and encirclements $N$ of $-1$ by the polar (Nyquist) plot.",
r"""**(A)** The Nyquist criterion determines closed-loop stability using
- $P$, the number of open-loop poles in the RHP (from the open-loop poles), and
- $N$, the encirclements of $-1+j0$ by the polar plot of $G(j\omega)H(j\omega)$.

Then $Z=N+P$ (clockwise $N$ positive) gives the number of closed-loop RHP poles. True.

**(R)** An unstable system has poles in the RHP. True, but it is just a general fact about instability. It does not explain *why* the open-loop poles and polar plot are sufficient (that comes from the argument principle).

Answer: **(b)**""",
[r"The theoretical basis of Nyquist is Cauchy's argument principle applied to $1+G(s)H(s)$.",
 r"Assertion–reason: if R is merely a general truth that does not *cause* A, choose (b)."]),

"5.42": ("A", r"A pure delay has $|e^{-j\omega T}|=1$. The Nyquist plot of $Ke^{-Ts}$ is a circle of radius $K$, so whether it reaches $-1$ depends only on $K$.",
r"""**Step 1 – Frequency response.**
$$G(j\omega)=Ke^{-j\omega T},\qquad|G|=K,\quad\angle G=-\omega T$$
As $\omega$ goes from $0$ to $\infty$, the plot goes round a circle of radius $K$ (clockwise, infinitely many times).

**Step 2 – Stability.**
- $K<1$: the circle stays inside the unit circle and never reaches $-1$. Stable.
- $K>1$: the circle encloses $-1$. Unstable.
- $K=1$: it passes through $-1$. Marginal.

**Step 3 – Check with the characteristic equation.** $1+Ke^{-sT}=0\Rightarrow e^{-sT}=-\frac1K$. Taking magnitudes, $e^{-\sigma T}=\frac1K\Rightarrow\sigma=\dfrac{\ln K}{T}$. $\sigma<0$ if and only if $K<1$, independent of $T$.

Stability depends on $K$ only.

Answer: **(a)**""",
[r"$T$ changes *where* (at which frequency) the plot crosses $-1$, but not *whether* it does.",
 r"In real systems, delay combined with other dynamics *does* reduce stability. This independence of $T$ holds only for a pure gain times delay."]),

"5.43": ("B", r"Gain margin from the negative-real-axis crossing at $-a$: $GM=\dfrac1a$, or $20\log\dfrac1a$ dB.",
r"""- **A.** No crossing of the negative real axis: $a=0$, so $GM=\infty$ (4).
- **B.** Crossing between $0$ and $-1$ ($0<a<1$): $GM>1$, i.e. $>0$ dB (3).
- **C.** Passing through $-1$ ($a=1$): $GM=1$, i.e. $0$ dB (2), marginal.
- **D.** Enclosing $-1$ ($a>1$): $GM<1$, i.e. $<0$ dB (1), unstable.

A–4, B–3, C–2, D–1. Answer: **(b)**""",
[r"Positive dB GM is stable, 0 dB is marginal and negative dB is unstable (for minimum-phase, open-loop-stable systems).",
 r"$GM=1/a$, not $a$. The closer the crossing is to $-1$, the smaller the margin."]),

"5.49": ("A", r"If the plot passes through $-1+j0$, then at that frequency $|GH|=1$ and $\angle GH=-180^\circ$ together. So $PM=0^\circ$ and $GM=0$ dB.",
r"""At the point $-1+j0$:
- $|G(j\omega)H(j\omega)|=1$, so this is the gain crossover frequency $\omega_{gc}$.
- $\angle G(j\omega)H(j\omega)=-180^\circ$, so this is also the phase crossover frequency $\omega_{pc}$.

$$PM=180^\circ+\angle GH(j\omega_{gc})=180^\circ-180^\circ=0^\circ$$
(and $GM=1$, i.e. 0 dB). The system is marginally stable.

Answer: **(a)**""",
[r"$\omega_{gc}=\omega_{pc}$ is the signature of marginal stability.",
 r"A PM of $180^\circ$ would mean the plot crosses the unit circle on the *positive* real axis, i.e. no lag at all."]),

"5.56": ("C", r"The Nyquist criterion relates the encirclements of $-1$ by the open-loop plot to the number of RHP **zeros of $1+GH$** (closed-loop poles) minus RHP **poles of $1+GH$** (open-loop poles).",
r"""**Statement (I).** The Nyquist criterion finds closed-loop stability from the open-loop frequency response $G(j\omega)H(j\omega)$, and it works even with delays and experimental data. True.

**Statement (II).** It claims the criterion relates the poles and zeros of the *closed-loop transfer function*. In fact it relates
$$N=Z-P$$
where $Z$ is the number of RHP zeros of $1+GH$ (the closed-loop poles) and $P$ is the number of RHP poles of $1+GH$ (the open-loop poles). Closed-loop zeros play no part. False.

Answer: **(c)**""",
[r"Zeros of $1+GH$ = closed-loop poles. Poles of $1+GH$ = open-loop poles. Knowing these two facts is the key to Nyquist questions.",
 r"Closed-loop zeros do not affect stability at all."]),

"5.87": (None, r"Nyquist criterion: $N=Z-P$ (clockwise encirclements positive). For a stable closed loop $Z=0$, so $N=-P$, i.e. $P$ counter-clockwise encirclements of $-1$.",
r"""**Step 1 – Required encirclement.** For stability $Z=0$, so the Nyquist plot must encircle $-1+j0$ **counter-clockwise** $P$ times, where $P$ is the number of open-loop poles in the RHP.

**Step 2 – Count $P$ from the description.** The sensible reading is: one pole in the LHP and one in the RHP (the phrase 'on the imaginary axis' appears to be a misprint for 'on the real axis'). Then $P=1$.

**Step 3 – Encirclement number.**
- With $N=Z-P$ (clockwise positive): $N=0-1=-1$, i.e. one counter-clockwise encirclement → option (a).
- With $N=P-Z$ (counter-clockwise positive), used by some textbooks: $N=+1$ → option (b).

Because the pole description is garbled and the answer depends on the sign convention, the answer key is left unset. Physically, the plot must make **one counter-clockwise encirclement** of $-1$.""",
[r"State your sign convention. 'One counter-clockwise encirclement' is unambiguous, while '$\pm1$' is not.",
 r"Poles *on* the $j\omega$ axis are not counted in $P$. The Nyquist contour detours around them with small semicircles.",
 r"Zeros of the open-loop function (here at the origin and in the LHP) do not enter the count $P$."]),

"5.100": ("A!", r"For an amplifier with loop gain $A\beta$: $|1+A\beta|>1$ (outside the unit circle centred at $-1$) means negative feedback, and $|1+A\beta|<1$ (inside it) means positive feedback. Enclosing $-1$ means instability.",
r"""**Step 1 – Gain with feedback.** $A_f=\dfrac{A}{1+A\beta}$
- If $|1+A\beta|>1$: $|A_f|<|A|$. The gain is reduced, so the feedback is **negative**.
- If $|1+A\beta|<1$: $|A_f|>|A|$. The gain is increased, so the feedback is **positive**.

**Step 2 – Geometry.** $|1+A\beta|=1$ is a circle of radius 1 centred at $-1+j0$, and $|1+A\beta|$ is the distance from $A\beta$ to $-1$.
- $A\beta$ outside this circle: negative feedback.
- $A\beta$ inside this circle: positive feedback.

**Step 3 – Check each option.**
- (a) $A\beta$ outside the circle → negative feedback. **True.**
- (b) Inside the circle, $|1+A\beta|<1$ → the feedback is *positive*, not negative. False.
- (c) Not enclosing $-1$ means *stable*, not unstable. False.
- (d) Inside the circle → positive feedback. False.

The source book's key gives (b), but as worded, (b) contradicts $A_f=A/(1+A\beta)$. The statement that is correct is (a).

Answer: **(a)**""",
[r"Remember the circle $|1+A\beta|=1$, centred at $-1$ with radius 1. Outside it is negative feedback, inside it is positive feedback.",
 r"Positive feedback is not automatically unstable. Instability needs the plot to *enclose* $-1$.",
 r"Test each statement with $A_f=A/(1+A\beta)$: if $|A_f|<|A|$ the feedback is negative."]),

"5.102": ("A", r"Phase crossover is where the polar plot cuts the **negative** real axis ($\angle GH=-180^\circ$). The gain margin measures how far that crossing is from $-1$.",
r"""**1.** The gain margin indicates how close the negative-real-axis crossing of the polar plot is to the critical point $(-1+j0)$: $GM=1/|GH(j\omega_{pc})|$. Correct. (The '$(-1+j)$' in the statement is a typo for $(-1+j0)$.)

**2.** The phase crossover point is where the plot intersects the **negative** real axis, not the positive real axis. **Not correct.**

**3.** The phase crossover frequency is where $\angle GH=\pm180^\circ$. Writing $180^\circ$ instead of $-180^\circ$ describes the same direction. Correct.

Only statement 2 is not correct.

Answer: **(a)**""",
[r"The question asks which are **not** correct.",
 r"Gain crossover: $|GH|=1$. Phase crossover: $\angle GH=-180^\circ$. Do not mix the two up."]),
}
