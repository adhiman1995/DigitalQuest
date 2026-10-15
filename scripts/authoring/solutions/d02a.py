# Detailed solutions, chapter 2 (time response analysis), 2.1-2.30.
# number -> (answer, concept, solution, [points to take care of])
D = {
"2.1": ("A", r"For an underdamped second-order system, the $n$-th extremum of the step response occurs at $t_n=\dfrac{n\pi}{\omega_d}$ and deviates from the final value by $e^{-n\xi\pi/\sqrt{1-\xi^2}}$.",
r"""**Step 1 – Step response.**
$$c(t)=1-\dfrac{e^{-\xi\omega_nt}}{\sqrt{1-\xi^2}}\sin(\omega_dt+\phi)$$
Setting $\dot c=0$ gives extrema at $t_n=n\pi/\omega_d$, $n=1,2,3,\dots$

**Step 2 – Size of each extremum.** At $t_n$:
$$|c(t_n)-1|=e^{-\xi\omega_nt_n}=e^{-n\xi\pi/\sqrt{1-\xi^2}}$$
Odd $n$ are overshoots (above 1) and even $n$ are undershoots (below 1). So (R) is true.

**Step 3 – Largest undershoot.** The undershoots are $n=2,4,6,\dots$ and they shrink with $n$, so the largest is $n=2$:
$$e^{-2\xi\pi/\sqrt{1-\xi^2}}$$
(A) is true, and it follows directly from (R) with $n=2$.

Answer: **(a)**""",
[r"The first undershoot is the square of the first overshoot: $M_{u1}=M_p^2$. Quick check: for $M_p=0.3$, the first undershoot is $0.09$.",
 r"Successive peaks fall by a constant ratio $e^{-\xi\pi/\sqrt{1-\xi^2}}$ every half-cycle. This is the basis of the logarithmic decrement.",
 r"Count $n$ correctly: $n=1$ is the first overshoot, $n=2$ the first undershoot, $n=3$ the second overshoot."]),

"2.2": ("A", r"Compare the denominator with $s^2+2\xi\omega_ns+\omega_n^2$. Critical damping means $\xi=1$, i.e. a repeated real pole.",
r"""For each option, $\omega_n^2=4\Rightarrow\omega_n=2$, so $\xi=\dfrac{b}{2\omega_n}=\dfrac{b}{4}$, where $b$ is the coefficient of $s$.

- $H_1$: $b=4$, $\xi=1$ → critically damped
- $H_2$: $b=3$, $\xi=0.75$ → underdamped
- $H_3$: $b=2$, $\xi=0.5$ → underdamped
- $H_4$: $b=1$, $\xi=0.25$ → underdamped

**Check:** $s^2+4s+4=(s+2)^2$, a repeated root at $-2$ ✓

Answer: **(a)**""",
[r"Quick test for critical damping: the quadratic is a perfect square, i.e. $b^2=4c$.",
 r"$\xi=\dfrac{b}{2\sqrt c}$ for $s^2+bs+c$. Always take $\sqrt c$, not $c$."]),

"2.3": ("C", r"The step response envelope is $e^{-\xi\omega_nt}$. Settling time is when the envelope falls within the tolerance band.",
r"""**Step 1 – Envelope condition.** The response stays within a $\pm2\%$ band once
$$e^{-\xi\omega_nt_s}\approx0.02$$
(ignoring the small factor $1/\sqrt{1-\xi^2}$).

**Step 2 – Solve.** $\xi\omega_nt_s=\ln50=3.91\approx4$
$$t_s=\dfrac{4}{\xi\omega_n}=4T,\qquad T=\dfrac{1}{\xi\omega_n}$$

For a 5% band, $\ln20=3.0$ gives $t_s=\dfrac{3}{\xi\omega_n}$.

Answer: **(c)**""",
[r"Know both: $t_s=4/(\xi\omega_n)$ for 2% and $3/(\xi\omega_n)$ for 5%. Option (b) is the 5% value.",
 r"Settling time depends only on the real part $\xi\omega_n$ of the poles. Poles on the same vertical line have the same $t_s$.",
 r"These formulas are envelope approximations, valid for underdamped systems (roughly $\xi<0.8$)."]),

"2.4": ("D", r"Non-interacting cascade: the transfer functions multiply. Two identical first-order lags give a repeated real pole, i.e. $\xi=1$.",
r"""**Step 1 – Overall transfer function.**
$$G(s)=\dfrac{1}{\tau s+1}\cdot\dfrac{1}{\tau s+1}=\dfrac{1/\tau^2}{\left(s+\frac1\tau\right)^2}$$

**Step 2 – Compare with the standard form.** $s^2+\dfrac2\tau s+\dfrac1{\tau^2}$ gives $\omega_n=\dfrac1\tau$ and $2\xi\omega_n=\dfrac2\tau\Rightarrow\xi=1$.

A repeated real pole means critical damping.

Answer: **(d)**""",
[r"Non-interacting means the second stage does not load the first, so you may multiply the transfer functions.",
 r"*Interacting* identical RC stages give $\dfrac{1}{\tau^2s^2+3\tau s+1}$ with $\xi=1.5$, which is overdamped. Do not mix the two cases.",
 r"Two *different* real first-order lags in cascade always give an overdamped system ($\xi>1$)."]),

"2.5": ("A", r"Output $Y(s)=H(s)X(s)$. Look for pole-zero cancellation, then use $\mathcal L^{-1}\left\{\dfrac{\omega}{(s+a)^2+\omega^2}\right\}=e^{-at}\sin\omega t$.",
r"""**Step 1 – Input transform.** $X(s)=\dfrac{1}{s+1}$

**Step 2 – Multiply.** Complete the square: $s^2+2s+2=(s+1)^2+1$.
$$Y(s)=\dfrac{s+1}{(s+1)^2+1}\cdot\dfrac{1}{s+1}=\dfrac{1}{(s+1)^2+1}$$

**Step 3 – Inverse transform.** With $a=1$ and $\omega=1$:
$$y(t)=e^{-t}\sin t\;u(t)$$

Answer: **(a)**""",
[r"Always complete the square in the quadratic. It shows the damped sinusoid immediately.",
 r"A numerator $s+a$ gives $e^{-at}\cos\omega t$ and a constant numerator $\omega$ gives $e^{-at}\sin\omega t$. Option (d) is what you get if you forget the cancellation.",
 r"Options with $u(t-1)$ are time-shifted results. There is no $e^{-s}$ factor here, so no delay."]),

"2.6": ("B", r"For unity feedback and a step input: $e_{ss}=\dfrac{1}{1+K_p}$, with $K_p=\lim_{s\to0}G(s)$.",
r"""**Step 1 – System type.** $G(s)=\dfrac{10}{s^2+14s+50}$ has no pole at the origin, so it is type 0 and the step error is finite.

**Step 2 – Position constant.** $K_p=G(0)=\dfrac{10}{50}=0.2$

**Step 3 – Error.**
$$e_{ss}=\dfrac{1}{1+K_p}=\dfrac{1}{1.2}=0.833$$

Answer: **(b)**""",
[r"Check closed-loop stability before using error constants. Here $s^2+14s+60$ is stable.",
 r"Do not use $1/K_p=5$. The step formula is $1/(1+K_p)$, while the ramp formula is $1/K_v$.",
 r"Type 0 gives a finite step error, type 1 or higher gives zero step error."]),

"2.7": ("C", r"Unit step input $R(s)=\frac1s$, so $T(s)=s\,C(s)$.",
r"""**Step 1 – Transform the response.**
$$C(s)=\dfrac1s-\dfrac{10}{s+1}=\dfrac{(s+1)-10s}{s(s+1)}=\dfrac{1-9s}{s(s+1)}$$

**Step 2 – Remove the step.**
$$T(s)=sC(s)=\dfrac{1-9s}{s+1}$$

**Checks:** $c(\infty)=T(0)=1$ ✓ and $c(0^+)=\lim_{s\to\infty}T(s)=-9$, which matches $1-10=-9$ ✓

Answer: **(c)**""",
[r"Option (d) is $C(s)$, not $T(s)$. Do not stop before multiplying by $s$.",
 r"The response starts at $-9$ and goes to $+1$, the opposite direction to the input first. That is the signature of an RHP zero (here at $s=1/9$), i.e. a non-minimum-phase system."]),

"2.8": ("B", r"Order reduction: neglecting a fast (non-dominant) pole while keeping the DC gain removes a small lag from the model.",
r"""**Step 1 – What the approximation does.** A third-order system, for example $\dfrac{p\,\omega_n^2}{(s+p)(s^2+2\xi\omega_ns+\omega_n^2)}$, is reduced by dropping the far pole: $\dfrac{p}{s+p}\to1$ (DC gain kept).

**Step 2 – Effect on speed.** The neglected pole adds an extra lag of roughly $1/p$ seconds and slows the rise of the original response. The reduced model has no such lag, so it rises faster.

**Step 3 – Conclusion.** The approximated second-order model has a *smaller* rise time than the original third-order system. Rise time is a property of the system, measured with the standard step input.

Answer: **(b)** (derived; the source has no printed key for this question)""",
[r"Every extra LHP pole adds lag. Removing it makes the model faster: smaller $t_r$ and $t_p$, and usually a slightly larger overshoot.",
 r"The approximation is valid only when the neglected pole is far left, at least 5–10 times the real part of the dominant poles.",
 r"Always keep the DC gain when dropping a pole: replace $\dfrac{p}{s+p}$ by $1$, not $\dfrac1{s+p}$ by $1$."]),

"2.9": ("B", r"The real part of a pole sets growth or decay ($\sigma<0$ decays, $\sigma=0$ sustains, $\sigma>0$ grows). The imaginary part sets oscillation.",
r"""Go through each pole-zero plot.

- **A.** All poles are real, and two of them ($\alpha_1$ and the pole at about $1.8$) are in the RHP. Terms like $e^{\alpha_1t}$ grow without oscillation → exponentially rising response, **4**.
- **B.** A conjugate pair on the $j\omega$ axis ($\pm j\omega$) → $\sin\omega t$ with constant amplitude, i.e. sustained oscillation, **3**.
- **C.** A conjugate pair at $\alpha\pm j\omega$ with $\alpha>0$ → $e^{\alpha t}\sin\omega t$, a growing oscillation, **2**.
- **D.** A conjugate pair in the LHP → $e^{-\alpha t}\sin\omega t$, a decaying oscillation, **1**.

A–4, B–3, C–2, D–1. Answer: **(b)**""",
[r"Read the real part for the envelope and the imaginary part for oscillation. One RHP pole is enough to make the response unbounded.",
 r"Simple poles on the $j\omega$ axis give sustained oscillation (marginally stable). Repeated poles there give a growing response.",
 r"Distinguish growing oscillation (complex RHP poles) from monotonic growth (real RHP poles)."]),

"2.10": ("A", r"A single pole at the origin, $G(s)=\dfrac{K}{s}$, is an integrator. Its impulse response is a step.",
r"""$$G(s)=\dfrac{K}{s}\ \Rightarrow\ g(t)=\mathcal L^{-1}\left\{\dfrac Ks\right\}=K\,u(t)$$
The impulse response is a constant $K$ for $t>0$.

Answer: **(a)**""",
[r"Pole at origin once → constant; twice → ramp ($\frac1{s^2}\to t$); a simple pair on the $j\omega$ axis → sinusoid.",
 r"A ramp, option (b), would need a *double* pole at the origin, or a single pole with a step input."]),

"2.11": ("B", r"Sensitivity of a quantity $e$ to a parameter $x$: $S_x^e=\dfrac{\partial e/e}{\partial x/x}=\dfrac{x}{e}\dfrac{\partial e}{\partial x}$.",
r"""**Step 1 – Ramp error.** $G=\dfrac{K}{s(s+a)}$ is type 1:
$$K_v=\lim_{s\to0}sG=\dfrac{K}{a}\ \Rightarrow\ e_{ss}=\dfrac1{K_v}=\dfrac{a}{K}$$

**Step 2 – Sensitivity to $K$.**
$$S_K^{e}=\dfrac{K}{e_{ss}}\cdot\dfrac{\partial}{\partial K}\left(\dfrac aK\right)=\dfrac{K}{a/K}\cdot\left(-\dfrac{a}{K^2}\right)=-1$$

**Step 3 – Sensitivity to $a$.**
$$S_a^{e}=\dfrac{a}{e_{ss}}\cdot\dfrac{1}{K}=\dfrac{a}{a/K}\cdot\dfrac1K=+1$$

Answer: **(b)**""",
[r"Shortcut: for a power law $e=cK^m a^n$, $S_K^e=m$ and $S_a^e=n$. Here $e=aK^{-1}$ gives $-1$ and $+1$ immediately.",
 r"The sign matters: increasing $K$ lowers the error (negative sensitivity) and increasing $a$ raises it (positive sensitivity).",
 r"Find $e_{ss}$ first (here for a ramp), then differentiate. Do not use the closed-loop gain sensitivity formula."]),

"2.12": ("B", r"For a unit step input, $H(s)=s\,Y(s)$. Laplace pair $\mathcal L\{t^ne^{-at}\}=\dfrac{n!}{(s+a)^{n+1}}$.",
r"""**Step 1 – Transform the output.** With $n=2$ and $a=1$:
$$Y(s)=\dfrac{2!}{(s+1)^3}=\dfrac{2}{(s+1)^3}$$

**Step 2 – Transfer function.**
$$H(s)=\dfrac{Y(s)}{1/s}=\dfrac{2s}{(s+1)^3}$$

**Check:** $y(\infty)=H(0)=0$, which matches $t^2e^{-t}\to0$ ✓

Answer: **(b)**""",
[r"Do not forget the $n!$ in the numerator. Writing $\dfrac{1}{(s+1)^3}$ leads to option (a).",
 r"A step response that returns to zero means $H(0)=0$, i.e. a zero at the origin. That rules out (c) and (d) immediately."]),

"2.13": ("A", r"Ramp error for unity feedback: $e_{ss}=\dfrac{1}{K_v}$ with $K_v=\lim_{s\to0}sG(s)$. $K_v=0$ for type 0, finite for type 1, and $\infty$ for type 2 and higher.",
r"""- Type 0: $K_v=0$ → $e_{ss}=\infty$ → **2**
- Type 1: $K_v=K$ → $e_{ss}=1/K$ → **4**
- Type 2: $K_v=\infty$ → $e_{ss}=0$ → **3**
- Type 3: $K_v=\infty$ → $e_{ss}=0$ → **3**

A–2, B–4, C–3, D–3. Answer: **(a)**""",
[r"Rule: a system of type $N$ follows an input of order $N-1$ with zero error, order $N$ with finite error, and order $N+1$ with infinite error. A ramp is order 1.",
 r"In match-the-list questions, an option may legitimately repeat a code (here 3 appears twice). Do not reject an option for that.",
 r"A type 3 system needs careful stability checking, but its error constants are still infinite."]),

"2.14": ("B", r"Total response = transient part + steady-state part. As $t\to\infty$, only the steady-state part remains.",
r"""The error $e(t)=r(t)-c(t)$ has a transient part, which dies out with time in a stable system, and a part that persists.

When the observation time is long, the transient has vanished and what is observed is the **steady-state error**, $e_{ss}=\lim_{t\to\infty}e(t)$.

Answer: **(b)**""",
[r"The position error constant $K_p$, option (d), is a constant used to *compute* the steady-state error. It is not a type of error.",
 r"The FVT form is $e_{ss}=\lim_{s\to0}sE(s)$, valid only for stable systems."]),

"2.15": ("D", r"First-order impulse response $g(t)=Ke^{-\alpha t}$. At $t=\tau=1/\alpha$ it falls to $e^{-1}K=0.37K$.",
r"""**Step 1 – Impulse response.** $g(t)=\mathcal L^{-1}\left\{\dfrac{K}{s+\alpha}\right\}=Ke^{-\alpha t}$

**Step 2 – Read the graph.** At $t=1/\alpha$, $g=Ke^{-1}=0.368K\approx0.37K$. The figure marks $0.37K$ at $t=t_2$, so
$$t_2=\dfrac{1}{\alpha}\ \Rightarrow\ \alpha=\dfrac{1}{t_2}$$

($t_1$ is at the $0.63K$ level, which is $t=\tau\ln(1/0.63)\approx0.46\tau$, not $\tau$.)

Answer: **(d)**""",
[r"The 63% value belongs to the *step* response, $1-e^{-1}=0.63$. For a decaying *impulse* response, the time constant is at 37%. Using $t_1$ is the trap.",
 r"$\alpha$ is the reciprocal of the time constant, so pick $\dfrac1{t}$, not $t$."]),

"2.16": ("A", r"Find the closed-loop characteristic equation $1+G=0$ and look at its roots (or at $\xi$).",
r"""**Step 1 – Characteristic equation.** $s(s+18)+80=0\Rightarrow s^2+18s+80=0$

**Step 2 – Roots.** $(s+8)(s+10)=0\Rightarrow s=-8,\,-10$: real and distinct.

**Step 3 – Damping ratio (check).** $\omega_n=\sqrt{80}=8.94$ and $\xi=\dfrac{18}{2\times8.94}=1.006>1$.

Real, unequal, negative roots → overdamped.

Answer: **(a)**""",
[r"$\xi$ is very close to 1 here. Factorise to decide; do not round $\xi$ to 1 and choose critically damped.",
 r"Discriminant test: $b^2-4c=324-320=4>0$ → overdamped; $=0$ → critical; $<0$ → underdamped."]),

"2.17": ("B", r"Feedback reduces sensitivity, moves the poles (changing time constants and bandwidth), and reduces overall gain.",
r"""**1.** Sensitivity is divided by $1+GH$, and so are disturbances in the forward path. True.

**2.** For $G=\dfrac{K}{1+\tau s}$, unity feedback gives $\tau_{cl}=\dfrac{\tau}{1+K}$. The time constant changes. True.

**3.** Feedback *reduces* the overall gain from $G$ to $\dfrac{G}{1+GH}$. It does not increase the loop gain; the loop gain $GH$ is fixed by the blocks. False.

Only 1 and 2. Answer: **(b)**""",
[r"Feedback lowers overall gain; it does not raise it. Any statement claiming increased gain is the trap.",
 r"Changing the time constant is a direct consequence of feedback moving the closed-loop poles."]),

"2.18": ("C", r"$\xi=1$ gives the characteristic roots $s=-\xi\omega_n\pm\omega_n\sqrt{\xi^2-1}=-\omega_n,-\omega_n$.",
r"""Roots of $s^2+2\xi\omega_ns+\omega_n^2=0$:
$$s=-\xi\omega_n\pm\omega_n\sqrt{\xi^2-1}$$

- $\xi>1$: negative, real, unequal → overdamped.
- $\xi=1$: $s=-\omega_n$ (twice) → negative, real, **equal** → critically damped.
- $0<\xi<1$: complex conjugates → underdamped.

Answer: **(c)**""",
[r"Positive real equal roots (option (d)) would make the system unstable. Critical damping always means LHP roots.",
 r"Option (a) describes overdamping, which is the closest distractor."]),

"2.19": ("A", r"Read the poles from the modes in the output, use pole-zero cancellation for the missing input mode, and use the DC gain from the step response.",
r"""**Step 1 – Poles.** The step response contains $e^{-t}$ and $e^{-3t}$, so the system poles are at $-1$ and $-3$: $\{a,b\}=\{1,3\}$.

**Step 2 – Zero.** For $x=e^{-2t}u(t)$, $X(s)=\dfrac{1}{s+2}$ and
$$Y(s)=H\dfrac{s+c}{(s+1)(s+3)(s+2)}$$
The output has no $e^{-2t}$ term, so the input pole at $-2$ must be cancelled: $c=2$.

**Step 3 – Gain.** The constant term of the step response is the DC gain:
$$H(0)=H\dfrac{c}{ab}=H\cdot\dfrac{2}{3}=2\ \Rightarrow\ H=3$$

$c=2$ and $H=3$. Answer: **(a)**""",
[r"A mode missing from the output means a pole was cancelled by a zero. This is the key idea in the question.",
 r"The constant in a step response is $H(0)$, the DC gain, not $H$ itself.",
 r"$a$ and $b$ are interchangeable; only their product $ab=3$ matters here."]),

"2.20": ("C", r"Disturbance at the plant input: $\dfrac{C}{D}=\dfrac{G_2}{1+G_1G_2}$. The DC gain of the block *before* the disturbance sets the rejection.",
r"""**Step 1 – Transfer function from $D$ to $C$** (with $R=0$):
$$\dfrac{C}{D}=\dfrac{G_2}{1+G_1G_2}$$

**Step 2 – Steady-state output for a unit step disturbance.** By the FVT,
$$c_{ss}=\dfrac{G_2(0)}{1+G_1(0)G_2(0)}$$
The error is $e=-c$, since $R=0$.

**Step 3 – Effect of each gain.**
- Increasing $G_2(0)$: $c_{ss}\to\dfrac{1}{G_1(0)}$. It cannot go below this.
- Increasing $G_1(0)$: $c_{ss}\to0$. ✓
- Increasing the product does not help if the increase is in $G_2$.
- Removing feedback gives $c_{ss}=G_2(0)$, which is worse.

Answer: **(c)**""",
[r"To reject a disturbance, put gain (or an integrator) *before* the point where the disturbance enters.",
 r"An integrator in $G_1$ makes $G_1(0)=\infty$ and the steady-state error to a step disturbance becomes zero. An integrator only in $G_2$ does not.",
 r"Remember that the error is $-c$ when $R=0$."]),

"2.21": ("C", r"Extrema of an underdamped step response occur at $t_n=\dfrac{n\pi}{\omega_d}$. Odd $n$ are peaks (overshoots) and even $n$ are troughs (undershoots).",
r"""**Step 1 – Extremum times.** $\dot c(t)\propto e^{-\xi\omega_nt}\sin\omega_dt=0$ gives $t=\dfrac{n\pi}{\omega_d}$.

**Step 2 – Pick the peaks.**
- $n=1$: first peak (first overshoot), $t_p=\pi/\omega_d$.
- $n=2$: first undershoot (a trough).
- $n=3$: **second peak**, $t=3\pi/\omega_d$.

$$t=\dfrac{3\pi}{\omega_n\sqrt{1-\xi^2}}$$

Answer: **(c)**""",
[r"Peaks and troughs are both extrema. $2\pi/\omega_d$, option (b), is the first undershoot, not the second peak.",
 r"Successive peaks are one full damped period $T_d=\dfrac{2\pi}{\omega_d}$ apart.",
 r"Option (d) has no $\omega_n$, so it is dimensionally wrong (not a time)."]),

"2.22": ("B", r"With negative feedback, $S_G^M=\dfrac{1}{1+GH}$.",
r"""For an open-loop system, $S=1$: a 1% change in $G$ gives a 1% change in output.

With negative feedback:
$$S_G^M=\dfrac{1}{1+GH}$$
For $|1+GH|>1$, which is the normal operating case, this is less than 1. The sensitivity decreases, by the factor $1+GH$.

Answer: **(b)**""",
[r"Sensitivity becomes small but never exactly zero, since that would need infinite loop gain. Option (c) is a trap.",
 r"Positive feedback would *increase* sensitivity, because $|1-GH|<1$."]),

"2.23": ("C", r"Roots $s=-\xi\omega_n\pm j\omega_n\sqrt{1-\xi^2}$. With $\xi<0$ the real part $-\xi\omega_n$ is positive.",
r"""**Underdamped** means $|\xi|<1$, so the roots are a complex-conjugate pair.

**Negative damping** ($\xi<0$) makes the real part $-\xi\omega_n>0$.

So the roots are complex conjugates in the **right half** of the $s$-plane. The response is a growing oscillation and the system is unstable.

Answer: **(c)**""",
[r"The sign of $\xi$ decides the half-plane. Its magnitude relative to 1 decides real or complex roots.",
 r"Negative damping with $\xi<-1$ would give real positive roots, option (d). The word 'underdamped' rules that out."]),

"2.24": ("C", r"For $s^2+bs+c$: $\omega_n=\sqrt c$ and $\xi=\dfrac{b}{2\sqrt c}$.",
r"""- **A.** $\omega_n=\sqrt{400}=20$, $\xi=12/40=0.3$ → underdamped (3)
- **B.** $\omega_n=\sqrt{900}=30$, $\xi=90/60=1.5$ → overdamped (4)
- **C.** $\omega_n=\sqrt{225}=15$, $\xi=30/30=1$ → critically damped (2)
- **D.** $\omega_n=\sqrt{625}=25$, no $s$ term so $\xi=0$ → undamped (1)

A–3, B–4, C–2, D–1. Answer: **(c)**""",
[r"No $s$ term in the denominator means $\xi=0$: undamped, sustained oscillation.",
 r"Fast check for critical damping: $b^2=4c$. For C, $900=4\times225$ ✓"]),

"2.25": ("B", r"Closed-loop characteristic equation $s^2+as+K$ compared with $s^2+2\xi\omega_ns+\omega_n^2$.",
r"""**Step 1 – Characteristic equation.** $s(s+4)+K=0\Rightarrow s^2+4s+K=0$

**Step 2 – Compare.** $\omega_n=\sqrt K$ and $2\xi\omega_n=4$.

**Step 3 – Impose $\xi=0.5$.**
$$2(0.5)\sqrt K=4\ \Rightarrow\ \sqrt K=4\ \Rightarrow\ K=16$$

Answer: **(b)**""",
[r"For $G=\dfrac{K}{s(s+a)}$, the product $\xi\omega_n=a/2$ stays fixed when $K$ changes, so $\xi=\dfrac{a}{2\sqrt K}$.",
 r"Increasing $K$ lowers $\xi$, raising overshoot, but does not change the settling time $4/(\xi\omega_n)$.",
 r"Do not stop at $\sqrt K=4$. The question asks for $K$."]),

"2.26": ("A", r"Ramp input to a type-1 unity-feedback system: $e_{ss}=\dfrac{1}{K_v}$ with $K_v=\lim_{s\to0}sG(s)$.",
r"""**Step 1 – Type.** There is one pole at the origin, so the system is type 1 and the ramp error is finite.

**Step 2 – Velocity constant.**
$$K_v=\lim_{s\to0}s\cdot\dfrac{1}{s(s+1)}=1$$

**Step 3 – Error.** $e_{ss}=\dfrac{1}{K_v}=1$

Answer: **(a)**""",
[r"Check stability first: $s^2+s+1=0$ is stable, so the error formula applies.",
 r"For a ramp of slope $A$, $e_{ss}=A/K_v$. Here $A=1$."]),

"2.27": ("B", r"Peak overshoot gives $\xi$: $M_p=e^{-\pi\xi/\sqrt{1-\xi^2}}$. Then match $s^2+s+K$ with the standard form.",
r"""**Step 1 – $\xi$ from $M_p=0.5$.**
$$\dfrac{\pi\xi}{\sqrt{1-\xi^2}}=\ln\dfrac{1}{0.5}=0.693\ \Rightarrow\ \dfrac{\xi}{\sqrt{1-\xi^2}}=0.2206$$
$$\xi^2=\dfrac{0.0487}{1.0487}=0.0464\ \Rightarrow\ \xi=0.215$$

**Step 2 – Characteristic equation.** $s(1+s)+K=0\Rightarrow s^2+s+K=0$, so $2\xi\omega_n=1$ and $\omega_n^2=K$.

**Step 3 – $K$.**
$$\omega_n=\dfrac{1}{2\times0.215}=2.32\ \Rightarrow\ K=\omega_n^2=5.39\approx5.3$$

Answer: **(b)**""",
[r"Useful formula: $\xi=\dfrac{-\ln M_p}{\sqrt{\pi^2+(\ln M_p)^2}}=\dfrac{0.693}{\sqrt{9.87+0.48}}=0.215$.",
 r"Express $M_p$ as a fraction (0.5), not as a percentage (50), before taking the log.",
 r"Higher overshoot needs lower $\xi$, i.e. higher $K$. A 50% overshoot needs a large $K$, which makes 0.53 and 0.047 unreasonable."]),

"2.28": ("B", r"First-order system $\dfrac{1}{\tau s+1}$: pole at $-1/\tau$, step response $1-e^{-t/\tau}$.",
r"""**1.** The time constant describes how the transient decays, so it is a transient-response specification. True.

**2.** The pole is at $s=-1/\tau$, so $\tau=\dfrac{1}{|\text{pole}|}$. True.

**3.** Accuracy is a steady-state property, given by $e_{ss}$ and the error constants. $\tau$ says nothing about final accuracy. False.

**4.** Smaller $\tau$ means a faster response ($t_r=2.2\tau$, $t_s=4\tau$). True.

Only 1, 2 and 4. Answer: **(b)**""",
[r"Speed is a transient property ($\tau$, $t_r$, $t_s$). Accuracy is a steady-state property ($e_{ss}$). Keep the two separate.",
 r"First-order formulas: $t_r(10\text{–}90\%)=2.2\tau$, $t_s(2\%)=4\tau$, $c(\tau)=63.2\%$."]),

"2.29": ("D", r"A step response of the form $1-e^{-\omega_nt}(1+\omega_nt)$ is the critically damped second-order response. The impulse response is the derivative of the step response.",
r"""**Step 1 – Identify the system.**
$$C(s)=\dfrac1s-\dfrac1{s+5}-\dfrac{5}{(s+5)^2}=\dfrac{25}{s(s+5)^2}$$
So $T(s)=\dfrac{25}{(s+5)^2}=\dfrac{25}{s^2+10s+25}$.

**Step 2 – Parameters.** $\omega_n^2=25\Rightarrow\omega_n=5$ rad/s (statement 1 ✓), and $2\xi\omega_n=10\Rightarrow\xi=1$ (statement 2 ✓).

**Step 3 – Impulse response.**
$$\dfrac{d}{dt}\left(1-e^{-5t}-5te^{-5t}\right)=5e^{-5t}-5e^{-5t}+25te^{-5t}=25te^{-5t}$$
(statement 3 ✓). Equivalently, $\mathcal L^{-1}\left\{\dfrac{25}{(s+5)^2}\right\}=25te^{-5t}$.

All three are correct. Answer: **(d)**""",
[r"Recognise the pattern: $1-e^{-at}(1+at)$ ⇔ $\dfrac{a^2}{(s+a)^2}$, critically damped with $\omega_n=a$.",
 r"When differentiating $5te^{-5t}$, use the product rule: $5e^{-5t}-25te^{-5t}$, with a minus sign carried in front."]),

"2.30": ("B", r"Identify $T(s)=s\,C(s)$ and check the pole locations.",
r"""**Step 1 – Transform the step response.**
$$C(s)=\dfrac1s-\dfrac{1}{s+1}-\dfrac{1}{(s+1)^2}=\dfrac{(s+1)^2-s(s+1)-s}{s(s+1)^2}=\dfrac{1}{s(s+1)^2}$$

**Step 2 – Transfer function.** $T(s)=sC(s)=\dfrac{1}{(s+1)^2}$

**Step 3 – Stability.** A double pole at $s=-1$ is in the LHP, so the system is stable. ($\xi=1$: critically damped, non-oscillatory.)

The response also settles to the finite value $1$, which agrees.

Answer: **(b)**""",
[r"Repeated poles are a problem only *on* the $j\omega$ axis. Repeated LHP poles are perfectly stable.",
 r"'Critically stable' (marginally stable) is not the same as 'critically damped'. Do not be misled by the similar words.",
 r"A bounded step response that settles to a constant is a quick sign of stability."]),
}
