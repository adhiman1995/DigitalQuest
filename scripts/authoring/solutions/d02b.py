# Detailed solutions, chapter 2 (time response analysis), 2.31-2.60.
# number -> (answer, concept, solution, [points to take care of])
D = {
"2.31": ("A", r"The impulse response is the derivative of the step response. Differentiating removes the constant (forced) term.",
r"""**Step 1 – Structure of the step response.**
$$c_{step}(t)=\underbrace{K}_{\text{forced/particular}}+\underbrace{\textstyle\sum A_ie^{p_it}}_{\text{natural}}$$

**Step 2 – Differentiate.**
$$g(t)=\dfrac{d}{dt}c_{step}(t)=\sum A_ip_ie^{p_it}$$
The constant $K$ disappears. The exponentials remain with the same exponents (the system poles) but new coefficients $A_ip_i$.

**Step 3 – Conclusion.** The impulse response contains only natural-response terms, so (A) is true. (R) describes exactly the mechanism (differentiation removes the constant and only rescales the exponentials), so it explains (A).

Answer: **(a)**""",
[r"An impulse acts only at $t=0$. Afterwards the input is zero, so only the free (natural) response remains. This is another way to see (A).",
 r"Impulse response = $\dfrac{d}{dt}$(step response) and step response = $\int$(impulse response). This holds only for LTI systems with zero initial conditions."]),

"2.32": ("B", r"Forced (steady) response to a constant input: set all derivatives to zero.",
r"""**Step 1 – Forced response to a constant.** For $x(t)=k$, try $y_f=A$ (a constant), so $\dot y_f=0$.

**Step 2 – Substitute.** $0+3A=k\Rightarrow A=\dfrac k3$

**Check with the transfer function.** $H(s)=\dfrac{1}{s+3}$ and the DC gain is $H(0)=\dfrac13$, so $y_f=\dfrac{k}{3}$ ✓

Answer: **(b)**""",
[r"Forced response to a constant input = DC gain × input = $H(0)\cdot k$.",
 r"The complete response also has a natural term $Ce^{-3t}$, but the question asks only for the forced part."]),

"2.33": ("B", r"Steady-state error falls as the static error constants ($K_p,K_v,K_a$) rise, and these are proportional to the open-loop gain.",
r"""For unity feedback:
- step: $e_{ss}=\dfrac{1}{1+K_p}$
- ramp: $e_{ss}=\dfrac{1}{K_v}$
- parabola: $e_{ss}=\dfrac{1}{K_a}$

All error constants are proportional to the open-loop gain $K$, so increasing the system gain reduces $e_{ss}$.

- (a) Decreasing the type *increases* the error.
- (c) Decreasing the error constant *increases* the error.
- (d) A larger input gives a proportionally larger error.

Answer: **(b)**""",
[r"Raising the gain reduces $e_{ss}$ but lowers $\xi$, increasing overshoot, and may destabilise the system. The stability limit applies.",
 r"Increasing the *type* (adding an integrator) is the other way to reduce error, often making it zero."]),

"2.34": ("D", r"Normalise so that the coefficient of $\ddot y$ is 1, then compare with $\ddot y+2\xi\omega_n\dot y+\omega_n^2y$.",
r"""**Step 1 – Normalise.** Divide by 2:
$$\ddot y+2\dot y+4y=4x$$

**Step 2 – Compare.** $\omega_n^2=4\Rightarrow\omega_n=2$ rad/s, and $2\xi\omega_n=2\Rightarrow\xi=\dfrac{2}{2\times2}=0.5$.

Answer: **(d)**""",
[r"Always divide through by the leading coefficient first. Using $4/(2\sqrt8)$ from the raw equation gives $0.707$, which is wrong.",
 r"Direct formula for $a\ddot y+b\dot y+cy$: $\xi=\dfrac{b}{2\sqrt{ac}}=\dfrac{4}{2\sqrt{16}}=0.5$ ✓"]),

"2.35": ("B", r"With $\xi=0$, the characteristic equation becomes $s^2+\omega_n^2=0$.",
r"""$$s^2+2(0)\omega_ns+\omega_n^2=0\ \Rightarrow\ s=\pm j\omega_n$$
The poles are purely imaginary, on the $j\omega$ axis. The step response is an undamped oscillation $1-\cos\omega_nt$.

Answer: **(b)**""",
[r"$\xi=0$: undamped, poles on the $j\omega$ axis, marginally stable.",
 r"Poles move from the $j\omega$ axis ($\xi=0$) towards the real axis ($\xi=1$) along a circle of radius $\omega_n$."]),

"2.36": ("C", r"A type-2 system has $K_v=\infty$, so it follows a ramp with zero steady-state error, provided the closed loop is stable.",
r"""**Step 1 – Type.** $G=\dfrac{10}{s^2(s+4)}$ has two poles at the origin, so it is type 2.

**Step 2 – Velocity constant.** $K_v=\lim_{s\to0}sG(s)=\lim_{s\to0}\dfrac{10}{s(s+4)}=\infty$

**Step 3 – Error for $r=10t$.** $e_{ss}=\dfrac{10}{K_v}=0$

**Note on stability.** The characteristic equation $s^3+4s^2+0\cdot s+10=0$ has a missing $s$ term, so the closed loop is actually *unstable* and strictly no steady state exists. The question intends the error-constant answer, zero.

Answer: **(c)** (as intended by the question)""",
[r"Strictly, error constants are meaningful only for a stable closed loop. Always check stability. Here $s^3+4s^2+10=0$ fails the Routh test.",
 r"In exams, if all options assume a steady state, give the error-constant answer, but be aware of the stability catch.",
 r"The input slope (10) does not matter when $K_v=\infty$."]),

"2.37": ("D", r"Normalise the characteristic equation, then read $\omega_n$ and $\xi$. $\xi>1$ means overdamped.",
r"""**Step 1 – Normalise.** $4s^2+6s+1=0\Rightarrow s^2+1.5s+0.25=0$

**Step 2 – Parameters.** $\omega_n=\sqrt{0.25}=0.5$ rad/s, so (R) is true. Then $2\xi\omega_n=1.5\Rightarrow\xi=\dfrac{1.5}{1}=1.5$.

**Step 3 – Nature.** $\xi=1.5>1$ means overdamped, with no oscillation. (A) is false.

Answer: **(d)**""",
[r"Check with the discriminant: $6^2-4(4)(1)=20>0$ gives real roots, so it is overdamped.",
 r"Do not judge damping from the size of $\omega_n$. Only $\xi$ (or the discriminant) decides it."]),

"2.38": ("B", r"Poles $-\sigma\pm j\omega_d$ with no finite zeros: $H(s)=\dfrac{K}{(s+\sigma)^2+\omega_d^2}$. The steady-state step output is the DC gain $H(0)$.",
r"""**Step 1 – Pole location from the figure.** The poles are at a radius of $\sqrt2$ and $45^\circ$ from the negative real axis:
$$s=-\sqrt2\cos45^\circ\pm j\sqrt2\sin45^\circ=-1\pm j1$$

**Step 2 – Transfer function.** No finite zeros, with a numerator of 1 for the sensor model:
$$H(s)=\dfrac{1}{(s+1)^2+1}=\dfrac{1}{s^2+2s+2}$$

**Step 3 – Steady-state deformation for a unit step pressure.** By the FVT,
$$y_{ss}=\lim_{s\to0}s\cdot H(s)\cdot\dfrac1s=H(0)=\dfrac12=0.5$$

Answer: **(b)**""",
[r"$45^\circ$ from the negative real axis means $\xi=\cos45^\circ=0.707$, and the radius is $\omega_n=\sqrt2$.",
 r"The answer depends on assuming a numerator of 1. With a normalised model $\omega_n^2/(\dots)$ the DC gain would be 1. Follow the convention the options imply.",
 r"The steady-state step output is always $H(0)$ for a stable system."]),

"2.39": ("C", r"Time to the first overshoot (peak time): $t_p=\dfrac{\pi}{\omega_d}=\dfrac{\pi}{\omega_n\sqrt{1-\xi^2}}$.",
r"""**Step 1 – Parameters.** $\omega_n^2=16\Rightarrow\omega_n=4$ rad/s, and $2\xi\omega_n=4\Rightarrow\xi=0.5$.

**Step 2 – Damped frequency.**
$$\omega_d=4\sqrt{1-0.25}=4\cdot\dfrac{\sqrt3}{2}=2\sqrt3\ \text{rad/s}$$

**Step 3 – Peak time.**
$$t_p=\dfrac{\pi}{\omega_d}=\dfrac{\pi}{2\sqrt3}\ \text{s}\approx0.907\ \text{s}$$

Answer: **(c)**""",
[r"Use $\omega_d$, not $\omega_n$. Using $\omega_n$ gives $\pi/4$, which is not an option.",
 r"$t_p$ is half a damped period: $T_d/2=\pi/\omega_d$. Option (b) uses $\omega_d=\sqrt3$, an arithmetic slip."]),

"2.40": ("A", r"Dominant poles are those closest to the $j\omega$ axis. Poles and zeros far to the left affect the response only briefly.",
r"""**Step 1 – Compare distances from the $j\omega$ axis.**
- $p_1=-0.5$ gives $e^{-0.5t}$, time constant 2 s (slowest).
- $p_2=-1$ gives $e^{-t}$, time constant 1 s.
- $p_3=-5$ and $p_4=-10$ give time constants of 0.2 s and 0.1 s, which die out quickly.

**Step 2 – Zeros.** $z_1=-6$ and $z_2=-8$ are far left. They sit near the fast poles and mainly affect those fast terms.

**Step 3 – Approximation.** $p_3$ and $p_4$ are at least 5 times further left than $p_2$, so the response is governed by $p_1$ and $p_2$.

Answer: **(a)**""",
[r"Rule of thumb: neglect poles and zeros that are more than about 5 times further from the $j\omega$ axis than the dominant poles.",
 r"When neglecting the far poles and zeros, keep the DC gain the same.",
 r"A zero near a pole roughly cancels it. Zeros near the dominant poles must not be ignored."]),

"2.41": ("D", r"$\mathcal L^{-1}\left\{\dfrac{\omega}{s^2+\omega^2}\right\}=\sin\omega t$. The FVT does not apply when there are poles on the $j\omega$ axis.",
r"""**Step 1 – Time function.** $f(t)=\sin\omega t$

**Step 2 – Behaviour as $t\to\infty$.** $\sin\omega t$ keeps oscillating between $-1$ and $+1$ and never settles, so it has no limit.

**Step 3 – Why the FVT fails.** Blindly applying it gives $\lim_{s\to0}\dfrac{s\omega}{s^2+\omega^2}=0$, which is wrong. $sF(s)$ has poles at $\pm j\omega$ on the imaginary axis, so the theorem is not valid.

The function stays bounded between $-1$ and $+1$.

Answer: **(d)**""",
[r"Check the conditions before using the FVT: all poles of $sF(s)$ must be strictly in the LHP.",
 r"Option (a), zero, is exactly the trap of applying the FVT blindly."]),

"2.42": ("D", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$. For $s^2+as+b$, $\xi\omega_n=a/2$.",
r"""**Step 1 – Closed-loop characteristic equation.**
$$s^2+0.4s+4=0$$

**Step 2 – Parameters.** $\omega_n=2$ rad/s and $2\xi\omega_n=0.4\Rightarrow\xi\omega_n=0.2$ (and $\xi=0.1$).

**Step 3 – Settling time.**
$$t_s=\dfrac{4}{\xi\omega_n}=\dfrac{4}{0.2}=20\ \text{s}$$

Answer: **(d)**""",
[r"Shortcut: $\xi\omega_n$ is half the coefficient of $s$. There is no need to find $\xi$ separately.",
 r"For a 5% band it would be $3/0.2=15$ s, which is not offered."]),

"2.43": ("D", r"An underdamped response is an oscillation with an exponentially *decaying* envelope $e^{-\xi\omega_nt}$.",
r"""Examine each plot.
- **(a), (b):** smooth curves with no oscillation. These are not underdamped.
- **(c):** an oscillation whose envelope *grows* with time. That means negative damping, an unstable system.
- **(d):** an oscillation inside a decaying exponential envelope. This is the underdamped free response $Ae^{-\xi\omega_nt}\cos(\omega_dt)$.

Answer: **(d)**""",
[r"Underdamped ($0<\xi<1$) means oscillation *and* decay. Both features are needed.",
 r"A physical spring-mass-damper with positive damping can never produce a growing oscillation like (c)."]),

"2.44": ("B", r"Design compromise: lower $\xi$ gives a fast but oscillatory response, higher $\xi$ gives a sluggish one. $\xi\approx0.4$ to $0.7$ is the practical range.",
r"""- $\xi<0.4$: large overshoot ($M_p>25\%$) and long oscillation. Poor relative stability.
- $\xi>0.8$: little overshoot, but the rise is slow.
- $\xi=0.4$ to $0.7$: overshoot between about 25% and 5%, with a fast rise and settling.

$\xi\approx0.707$ is often taken as the optimum (about 4.3% overshoot, maximally flat frequency response).

Answer: **(b)**""",
[r"Remember the overshoot values: $\xi=0.4\to25\%$, $\xi=0.5\to16\%$, $\xi=0.6\to9.5\%$, $\xi=0.707\to4.3\%$.",
 r"Critical damping ($\xi=1$) is the fastest response *without overshoot*, not the fastest overall."]),

"2.45": ("B", r"Integral action raises the system type, reducing steady-state error. Derivative action adds damping, reducing overshoot.",
r"""**(A)** Increasing the integral gain $K_i$ strengthens the integral action, which drives the steady-state error towards zero. True.

**(R)** Increasing the derivative gain $K_d$ adds the term $K_ds$, which increases the effective damping. Overshoot is reduced. True.

**Relation.** (R) is about transient behaviour (overshoot) while (A) is about steady-state error. They are separate effects, so (R) does not explain (A).

Answer: **(b)**""",
[r"Integral (I) → steady state. Derivative (D) → transient (damping, overshoot). Proportional (P) → both, with a trade-off.",
 r"Too much integral gain *increases* overshoot and can destabilise the loop."]),

"2.46": ("A", r"BIBO stability of an LTI system: a bounded input gives a bounded output if and only if all characteristic roots have negative real parts.",
r"""**Step 1 – Assertion.** For a linear system that is stable, a bounded input gives a bounded output. That is the definition of BIBO stability. Read in this intended sense, (A) is true.

**Step 2 – Reason.** (R) states the stability condition: all roots of the characteristic equation in the LHP, so the response to initial conditions decays to zero. True.

**Step 3 – Link.** Because all the roots have negative real parts, the impulse response is absolutely integrable, and that is precisely why a bounded input gives a bounded output. (R) explains (A).

Answer: **(a)** (derived; the source has no printed key for this question)""",
[r"Strictly, (A) is not true for *every* linear system. An integrator $\frac1s$ turns a bounded step into an unbounded ramp. The assertion is meant for a stable system, and (R) supplies that condition.",
 r"For LTI systems, asymptotic stability (initial-condition response decays) and BIBO stability are equivalent when there are no hidden pole-zero cancellations.",
 r"BIBO condition in the time domain: $\int_0^\infty|g(t)|\,dt<\infty$."]),

"2.47": ("B", r"Closed-loop transfer function $T=\dfrac{G}{1+GH}$. The final value of the step response is $T(0)$.",
r"""**Step 1 – Identify the blocks.** Forward path $G=10\cdot\dfrac{1}{s+1}=\dfrac{10}{s+1}$. Feedback path $H=\dfrac1s$, an integrator.

**Step 2 – Closed loop.**
$$T=\dfrac{\frac{10}{s+1}}{1+\frac{10}{s(s+1)}}=\dfrac{10s}{s^2+s+10}$$

**Step 3 – Final value.** The poles of $s^2+s+10$ are in the LHP, so the FVT is valid:
$$c(\infty)=\lim_{s\to0}s\cdot\dfrac{10s}{s^2+s+10}\cdot\dfrac1s=T(0)=0$$

Answer: **(b)**""",
[r"An integrator in the *feedback* path puts a zero at the origin in $T$. The output then settles to zero for a step input.",
 r"An integrator in the forward path removes the step error. In the feedback path it does the opposite: the output follows the *derivative* of the input at DC.",
 r"System type is still 1 here, since $GH$ has one integrator, but the output is not unity-feedback-like."]),

"2.48": ("B", r"System type = number of poles at the origin in the open-loop transfer function $G(s)H(s)$.",
r"""$$G(s)H(s)=\dfrac{2}{s^2+2s+2}\cdot\dfrac{1}{s}=\dfrac{2}{s(s^2+2s+2)}$$
There is one pole at $s=0$, so the system is type 1.

Answer: **(b)**""",
[r"Count integrators in the whole loop, $GH$, not just in $G$. The integrator here is in the feedback path.",
 r"With non-unity feedback, the meaning of 'error' changes, so be careful applying error constants. The type definition is still based on $GH$."]),

"2.49": ("B", r"Write the first-order equation as $\tau\dot x+x=Kf(t)$. The coefficient of $\dot x$ is then the time constant.",
r"""**Step 1 – Normalise.** Divide by the coefficient of $x$, which is 2:
$$20\dfrac{dx}{dt}+x=\dfrac{1}{2}f(t)$$

**Step 2 – Read $\tau$.** $\tau=20$ s (and the static gain is $K=0.5$).

Equivalently, $X(s)/F(s)=\dfrac{1}{40s+2}=\dfrac{0.5}{20s+1}$, with the pole at $-0.05$, so $\tau=1/0.05=20$.

Answer: **(b)**""",
[r"Divide by the coefficient of $x$, not of $\dot x$. Reading 40 directly is the common mistake.",
 r"$\tau=1/|\text{pole}|$ is a quick cross-check."]),

"2.50": ("B", r"Settling time fixes the real part of the poles; $\xi$ fixes the angle. Poles are at $-\xi\omega_n\pm j\omega_n\sqrt{1-\xi^2}$.",
r"""**Step 1 – Real part from $t_s$ (5%).**
$$t_s=\dfrac{3}{\xi\omega_n}=0.6\ \Rightarrow\ \xi\omega_n=5$$

**Step 2 – $\omega_n$ from $\xi$.** $\omega_n=\dfrac{5}{0.707}=7.07$ rad/s

**Step 3 – Imaginary part.**
$$\omega_d=\omega_n\sqrt{1-\xi^2}=7.07\times0.707=5$$

**Poles:** $-5\pm j5$

Answer: **(b)**""",
[r"$\xi=0.707$ means the poles are at $45^\circ$, so the real and imaginary parts are equal. Once you have $\sigma=5$, the answer is $-5\pm j5$ straight away.",
 r"Use $3/(\xi\omega_n)$ for the 5% band. Using 4 (the 2% value) gives $\sigma=6.67$, which matches no option."]),

"2.51": ("C", r"Closed-loop characteristic equation $s^2+6s+K$: $\omega_n=\sqrt K$ and $\xi=\dfrac{6}{2\sqrt K}$.",
r"""**Step 1 – Characteristic equation.** $s(s+6)+K=0\Rightarrow s^2+6s+K=0$

**Step 2 – Compare.** $2\xi\omega_n=6\Rightarrow\xi\omega_n=3$, and $\omega_n=\sqrt K$.

**Step 3 – Impose $\xi=0.75$.**
$$\dfrac{3}{\sqrt K}=0.75\ \Rightarrow\ \sqrt K=4\ \Rightarrow\ K=16$$

Answer: **(c)**""",
[r"$K=\left(\dfrac{a}{2\xi}\right)^2$ for $G=\dfrac{K}{s(s+a)}$: $(6/1.5)^2=16$.",
 r"Do not stop at $\sqrt K=4$, which is option (b)."]),

"2.52": ("A", r"An impulse contains all frequencies with equal strength. A second-order system responds selectively, ringing at its own (natural) frequency.",
r"""**Statement (I).** The impulse response of an underdamped second-order system is
$$g(t)=\dfrac{\omega_n}{\sqrt{1-\xi^2}}e^{-\xi\omega_nt}\sin\omega_dt$$
The system oscillates at its own natural frequency of oscillation, $\omega_d\approx\omega_n$ for light damping. True.

**Statement (II).** $\mathcal F\{\delta(t)\}=1$, a flat spectrum, so the impulse contains all frequencies from $-\infty$ to $+\infty$. True.

**Link.** Because the impulse contains every frequency, it necessarily excites the system's natural frequency. The system picks that frequency out and rings at it, like a bell struck by a hammer. So (II) explains (I).

Answer: **(a)** (derived; the source has no printed key for this question)""",
[r"Strictly, the ringing frequency is the *damped* frequency $\omega_d=\omega_n\sqrt{1-\xi^2}$. 'Natural frequency' in (I) is used loosely.",
 r"This is why an impulse (hammer) test is used to find natural frequencies of structures: one test excites all the modes."]),

"2.53": ("A", r"For a prototype second-order system with fixed $\xi$: $t_r\propto\dfrac{1}{\omega_n}$ and $\omega_{BW}\propto\omega_n$, so $t_r\cdot\omega_{BW}$ is constant.",
r"""**Statement (I).** For a given $\xi$:
$$t_r=\dfrac{\pi-\cos^{-1}\xi}{\omega_n\sqrt{1-\xi^2}}\propto\dfrac1{\omega_n},\qquad\omega_{BW}=\omega_n\sqrt{1-2\xi^2+\sqrt{4\xi^4-4\xi^2+2}}\propto\omega_n$$
So $t_r\propto\dfrac{1}{\omega_{BW}}$. True.

**Statement (II).** Increasing $\omega_n$ increases $\omega_{BW}$ and reduces $t_r$. True.

**Link.** Both quantities depend on $\omega_n$ in opposite ways, and that is exactly why they are inversely proportional. (II) explains (I).

Answer: **(a)**""",
[r"A useful rule: $t_r\times\text{BW}\approx$ constant (about 0.35 for $t_r$ in seconds and BW in Hz for a first-order system).",
 r"Wider bandwidth means a faster response, but also more noise passed through."]),

"2.54": ("B", r"System type = number of open-loop poles at the origin ($s^N$ in the denominator of $G(s)H(s)$).",
r"""Write the open-loop transfer function as
$$G(s)H(s)=\dfrac{K\prod(s+z_i)}{s^N\prod(s+p_j)}$$
$N$, the number of **poles at the origin of the open-loop transfer function**, is the system type. The static error constants $K_p,K_v,K_a$ are evaluated from this form, and their finite or infinite values depend directly on $N$.

Answer: **(b)**""",
[r"Type is defined on the *open-loop* function. The closed-loop function of a stable system never has poles at the origin.",
 r"Type and order are different: order is the total number of poles, type counts only those at $s=0$."]),

"2.55": ("B", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$.",
r"""**Step 1 – Parameters.** $\omega_n^2=25\Rightarrow\omega_n=5$, and $2\xi\omega_n=5\Rightarrow\xi\omega_n=2.5$ (and $\xi=0.5$).

**Step 2 – Settling time.**
$$t_s=\dfrac{4}{\xi\omega_n}=\dfrac{4}{2.5}=1.6\ \text{s}$$

Answer: **(b)**""",
[r"$\xi\omega_n$ is half the coefficient of $s$: $5/2=2.5$.",
 r"The 5% band would give $3/2.5=1.2$ s, option (a). Read the tolerance band carefully."]),

"2.56": ("D", r"Standard transient specifications for a step input: delay time $t_d$, rise time $t_r$, peak time $t_p$, maximum overshoot $M_p$, settling time $t_s$.",
r"""Check each item.
1. Maximum overshoot ✓ (transient)
2. Maximum undershoot ✗ (not a standard specification)
3. Overall gain ✗ (a steady-state/DC property)
4. Delay time ✓ (transient)
5. Rise time ✓ (transient)
6. Fall time ✗ (not used for a step response)

So 1, 4 and 5. Answer: **(d)**""",
[r"Memorise the five standard time-domain specifications: $t_d,t_r,t_p,M_p,t_s$.",
 r"Gain, steady-state error and the error constants are *steady-state* measures, never transient ones."]),

"2.57": ("B", r"Type = number of poles at the origin of $G(s)H(s)$.",
r"""$$G(s)H(s)=\dfrac{4}{s(s+3)}\cdot\dfrac{1}{s}=\dfrac{4}{s^2(s+3)}$$
Two poles at the origin: **type 2**.

Answer: **(b)**""",
[r"Include the integrators in $H(s)$ as well. Counting only $G$ gives type 1, which is the trap.",
 r"This closed loop ($s^3+3s^2+4=0$, missing the $s$ term) is actually unstable. Type is still defined, but error constants would be meaningless."]),

"2.58": ("C", r"$\xi=1$: $s=-\xi\omega_n\pm\omega_n\sqrt{\xi^2-1}=-\omega_n$ (repeated).",
r"""$$s_{1,2}=-\omega_n\pm\omega_n\sqrt{1-1}=-\omega_n,\ -\omega_n$$
The poles are **equal, negative and real**: critically damped.

Option (d), 'negative and real', is also true of the poles, but it does not capture that they are *equal*. Option (c) is the complete answer.

Answer: **(c)**""",
[r"When two options are both true, choose the more specific one, the one that fully describes the case.",
 r"Negative, real and *unequal* poles mean overdamped ($\xi>1$)."]),

"2.59": ("B", r"Order reduction: neglecting a fast (non-dominant) pole while keeping the DC gain removes a small lag from the model.",
r"""This is the same as question 2.8.

**Step 1.** The third-order model has a far pole $p$ that adds a small lag to the response.

**Step 2.** Dropping it with DC gain preserved, $\dfrac{p}{s+p}\to1$, removes that lag, so the second-order approximation responds faster.

**Step 3.** Its rise time is therefore *smaller* than the original system's. Rise time is a system property, measured with the standard step input, so the result holds whatever input is later applied.

Answer: **(b)** (derived; the source has no printed key for this question)""",
[r"Every extra LHP pole adds lag. Removing it makes the model respond faster.",
 r"The approximation is valid only if the neglected pole is far from the dominant ones (5–10 times their real part)."]),

"2.60": ("A", r"DC gain = $G(0)$, the steady-state output for a unit step input.",
r"""$$G(0)=\dfrac{2(0)+5}{(0+5)(0+4)}=\dfrac{5}{20}=0.25$$

Answer: **(a)**""",
[r"DC gain means setting $s=0$. Do not cancel $(2s+5)$ with $(s+5)$; they are different factors.",
 r"The DC gain is finite because there is no pole at the origin. A pole at $s=0$ would make it infinite."]),
}
