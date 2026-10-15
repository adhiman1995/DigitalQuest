# Detailed solutions, chapter 2 (time response analysis), 2.91-2.115.
# number -> (answer, concept, solution, [points to take care of])
D = {
"2.91": (None, r"First-order step response: $c(t)=\dfrac{K}{a}\left(1-e^{-at}\right)$. Final value $K/a$, time constant $1/a$, initial slope $K$.",
r"""**Step 1 – Read the graph.**
- Final value $=5$.
- The tangent at the origin reaches the final value at $t=0.1$ s, so the time constant is $\tau=0.1$ s.

**Step 2 – Match with $G(s)=\dfrac{K}{s+a}$.**
- $\tau=\dfrac1a=0.1\Rightarrow a=10$
- Final value $\dfrac{K}{a}=5\Rightarrow K=50$
- Check: initial slope $=K=50=\dfrac{5}{0.1}$ ✓

**Step 3 – Compare with the options.** $(K,a)=(50,10)$ is not offered.

If the plant were written in time-constant form, $G(s)=\dfrac{K}{\tau s+1}$ (or $\dfrac{Ka}{s+a}$), then $K$ would be the final value 5 and $a=10$, which is option (b). That is probably what was intended, but as transcribed no option matches, so the answer key is left unset.""",
[r"For $\dfrac{K}{s+a}$, the DC gain is $K/a$, not $K$. Check which form the transfer function is written in.",
 r"The tangent at $t=0$ always meets the final value at $t=\tau$. That is the fastest way to read $\tau$ from a graph.",
 r"Initial slope of a first-order step response $=\dfrac{\text{final value}}{\tau}$."]),

"2.92": ("A", r"Adding an integrator raises the type by one. The old $K_p$ becomes the new $K_v$ (for a unity-gain integrator).",
r"""**Step 1 – Original $K_p$.**
$$e_{ss}=\dfrac{1}{1+K_p}=0.2\ \Rightarrow\ K_p=4$$

**Step 2 – Remove the step error.** Insert a unity-gain **integrator** $\dfrac1s$. The new open loop is $G'(s)=\dfrac{G(s)}{s}$, which is type 1, so the step error becomes zero. (A differentiator would lower the type and make things worse.)

**Step 3 – New ramp error.**
$$K_v'=\lim_{s\to0}s\cdot\dfrac{G(s)}{s}=G(0)=K_p=4\ \Rightarrow\ e_{ss}=\dfrac{1}{K_v'}=0.25$$

Answer: **(a)**""",
[r"$K_p=4$, not $5$. From $1/(1+K_p)=0.2$, $1+K_p=5$.",
 r"The new ramp error equals $1/K_p$ of the old system, which is 0.25 and not 0.2.",
 r"Adding an integrator can reduce stability. In practice, check the new closed loop."]),

"2.93": ("C", r"Step response = integral of the impulse response, or in Laplace terms $C(s)=G(s)/s$.",
r"""**Step 1 – Transfer function.**
$$G(s)=\dfrac{16}{s+2}-\dfrac{8}{s+1}$$

**Step 2 – Divide by $s$ and split each term.** Use $\dfrac{a}{s(s+a)}=\dfrac1s-\dfrac{1}{s+a}$:
$$\dfrac{16}{s(s+2)}=\dfrac{8}{s}-\dfrac{8}{s+2},\qquad\dfrac{8}{s(s+1)}=\dfrac8s-\dfrac8{s+1}$$
$$C(s)=\left(\dfrac8s-\dfrac8{s+2}\right)-\left(\dfrac8s-\dfrac8{s+1}\right)=\dfrac{8}{s+1}-\dfrac{8}{s+2}$$

**Step 3 – Inverse transform.** $c(t)=8e^{-t}-8e^{-2t}$

**Check in the time domain.** $\int_0^t(16e^{-2\tau}-8e^{-\tau})d\tau=8(1-e^{-2t})-8(1-e^{-t})=8e^{-t}-8e^{-2t}$ ✓

Answer: **(c)**""",
[r"Integrate from 0 to $t$, including the lower limit. The constants $\pm8$ cancel here, which is easy to miss.",
 r"Check: $G(0)=8-8=0$, so the final value of the step response is 0. Options (a) and (b) end at 8, which is wrong."]),

"2.94": ("A", r"$Y(s)=G(s)R(s)$ with $R(s)=\dfrac5s$, then partial fractions.",
r"""**Step 1 – Output transform.**
$$Y(s)=\dfrac{5}{s(s+1)(s+2)}$$

**Step 2 – Residues (cover-up method).**
- At $s=0$: $\dfrac{5}{(1)(2)}=\dfrac52$
- At $s=-1$: $\dfrac{5}{(-1)(1)}=-5$
- At $s=-2$: $\dfrac{5}{(-2)(-1)}=\dfrac52$

**Step 3 – Inverse transform.**
$$y(t)=\left[\dfrac52-5e^{-t}+\dfrac52e^{-2t}\right]u(t)$$

**Check:** $y(0)=\frac52-5+\frac52=0$ ✓ and $y(\infty)=5G(0)=\frac52$ ✓

Answer: **(a)**""",
[r"Quick check: $y(0)$ must be 0, since the relative degree is 2. Only option (a) satisfies this.",
 r"Do not forget the input amplitude 5. It scales every residue."]),

"2.95": ("C", r"Type $N$ gives zero error for inputs of order up to $N-1$. Type 2 tracks both step and ramp with zero error.",
r"""For a type-2 system:
- $K_p=\lim_{s\to0}G=\infty$, so the step error is $\dfrac{1}{1+\infty}=0$
- $K_v=\lim_{s\to0}sG=\infty$, so the ramp error is $\dfrac{1}{\infty}=0$
- $K_a$ is finite, so the parabolic error is $1/K_a$, finite.

Answer: **(c)**""",
[r"Type 2 = two integrators: zero error for step and ramp, finite error for a parabola.",
 r"These results assume the closed loop is stable."]),

"2.96": ("D", r"Unit parabolic input: $r(t)=\dfrac{t^2}{2}u(t)$, $R(s)=\dfrac{1}{s^3}$.",
r"""**1.** Step ($t^0$) → ramp ($t^1$) → parabola ($t^2$). Each is the integral of the previous one, so a parabola is one degree faster than a ramp. True.

**2.** The unit parabola is defined as $t^2/2$ for $t>0$, so that its second derivative is a unit step. True.

**3.** $\mathcal L\left\{\dfrac{t^2}{2}\right\}=\dfrac12\cdot\dfrac{2!}{s^3}=\dfrac1{s^3}$. True.

All three. Answer: **(d)**""",
[r"The factor $\frac12$ in the definition is what makes the transform exactly $1/s^3$.",
 r"Standard inputs: step $1/s$, ramp $1/s^2$, parabola $1/s^3$. Each needs one more integrator in $G$ for zero error."]),

"2.97": ("A", r"First-order step response: $C(s)=\dfrac{1}{s(1+\tau s)}$, so $c(t)=1-e^{-t/\tau}$.",
r"""**Step 1.** $C(s)=\dfrac{1}{s(1+\tau s)}$

**Step 2 – Partial fractions.**
$$C(s)=\dfrac1s-\dfrac{\tau}{1+\tau s}=\dfrac1s-\dfrac{1}{s+1/\tau}$$

**Step 3 – Inverse transform.** $c(t)=1-e^{-t/\tau}$

Answer: **(a)**""",
[r"Check $c(0)=0$ and $c(\infty)=1$. Option (b) starts at 2, and (c) and (d) blow up.",
 r"Key values: $c(\tau)=0.632$, $c(4\tau)=0.982$."]),

"2.98": ("B", r"Continuous-time step response = running *integral* of the impulse response. The running *sum* is the discrete-time version.",
r"""**1.** By definition, the step response is the output for a unit-step input. True.

**2.** A running sum of the impulse response gives the step response of a *discrete-time* system. In the context here, it is not the continuous-time definition. False.

**3.** For a continuous-time system, $s(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$. True.

1 and 3 only. Answer: **(b)**""",
[r"Continuous time: integral and derivative. Discrete time: running sum and first difference.",
 r"Statement 2 would be true for a discrete-time system. Read the context carefully."]),

"2.99": ("B", r"Type 1: step error $=0$ and ramp error $=1/K_v$. In time-constant form, $K_v$ is simply the gain $K$.",
r"""**Step 1 – Type.** One pole at the origin: type 1.

**Step 2 – Step input.** $K_p=\infty$, so $e_{ss}=0$.

**Step 3 – Ramp input.**
$$K_v=\lim_{s\to0}s\cdot\dfrac{1}{s(0.5s+1)(0.2s+1)}=1\ \Rightarrow\ e_{ss}=\dfrac1{K_v}=1$$

Answer: **(b)**""",
[r"In time-constant (Bode) form $\dfrac{K}{s(1+T_1s)(1+T_2s)}$, $K_v=K$ directly.",
 r"Check stability first: $0.1s^3+0.7s^2+s+1=0$ satisfies Routh ($0.7\times1>0.1\times1$), so it is stable."]),

"2.100": ("B", r"Extrema of the underdamped step response occur at $t=\dfrac{n\pi}{\omega_d}$. $n=1$ is the first overshoot and $n=2$ the first undershoot.",
r"""$\dot c(t)\propto e^{-\xi\omega_nt}\sin\omega_dt=0$ at $t=\dfrac{n\pi}{\omega_d}$.

- $n=1$: $t=\pi/\omega_d$, the first overshoot (maximum).
- $n=2$: $t=2\pi/\omega_d$, the **first undershoot** (minimum).

Answer: **(b)**""",
[r"Overshoots are at odd multiples of $\pi/\omega_d$ and undershoots at even multiples.",
 r"Option (a) is the peak time, not the undershoot time."]),

"2.101": ("D", r"Parabolic input needs $K_a=\lim_{s\to0}s^2G(s)$. Type 1 gives $K_a=0$, so $e_{ss}=\infty$.",
r"""Input $r=\dfrac{t^2}{2}$, so $R(s)=\dfrac1{s^3}$.
$$e_{ss}=\dfrac{1}{K_a},\qquad K_a=\lim_{s\to0}s^2\cdot\dfrac{K(\dots)}{s(\dots)}=0$$
$$e_{ss}=\infty$$
The type-1 system cannot keep up with a parabolic input, and the error grows without limit.

Answer: **(d)**""",
[r"Rule: a type-$N$ system has infinite error for inputs of order greater than $N$. A parabola is order 2 and type 1 is less than 2.",
 r"Infinite error means a growing error. The system does not become unstable."]),

"2.102": ("A", r"A higher-order system can be approximated as second order if the extra closed-loop poles are far away, or if they nearly cancel nearby closed-loop zeros (pole-zero dipoles).",
r"""For a valid second-order approximation, the response must be governed by the dominant pole pair alone. Two things can spoil this:
1. A zero close to the dominant pair. It changes the overshoot significantly.
2. Higher-order poles close to the dominant pair. They add significant slow terms.

Both problems disappear if each such zero is nearly cancelled by a higher-order pole sitting very close to it (a pole-zero dipole has almost zero residue).

Option (a) states exactly this: zeros near the dominant pair are nearly cancelled by nearby higher-order poles.

Answer: **(a)**""",
[r"A pole-zero pair very close together (a dipole) contributes almost nothing to the response, so both can be dropped.",
 r"An *uncancelled* zero near the dominant poles increases overshoot and invalidates the approximation. That is option (c), the opposite case."]),

"2.103": ("D", r"Superposition of errors: for $r=A+Bt$, $e_{ss}=\dfrac{A}{1+K_p}+\dfrac{B}{K_v}$.",
r"""**Step 1 – Error constants.** One integrator: type 1.
- $K_p=\infty$
- $K_v=\lim_{s\to0}s\cdot\dfrac{K(2s+1)}{s(4s+1)(s+1)^2}=\dfrac{K(1)}{(1)(1)}=K$

**Step 2 – Error for $r=1+5t$.**
$$e_{ss}=\dfrac{1}{1+\infty}+\dfrac{5}{K}=\dfrac5K$$

**Step 3 – Condition.** $\dfrac{5}{K}<0.1\Rightarrow K>50$

Answer: **(d)**""",
[r"Multiply the ramp error by the slope (5). Forgetting it gives $K>10$.",
 r"In time-constant form, every factor $(1+Ts)\to1$ at $s=0$, so $K_v$ is just $K$.",
 r"In practice, also check that $K>50$ keeps the loop stable. The exam question ignores this."]),

"2.104": ("D", r"Type-1 system, so a finite steady-state error refers to a ramp input: $e_{ss}=\dfrac1{K_v}$.",
r"""**Step 1 – Type.** One integrator: type 1. The step error would be zero, so '10% error' must refer to a unit ramp.

**Step 2 – Velocity constant.**
$$K_v=\lim_{s\to0}s\cdot\dfrac{K(s+5)}{s(s+6)(s+7)(s+8)}=\dfrac{5K}{6\times7\times8}=\dfrac{5K}{336}$$

**Step 3 – Impose 10% error.**
$$\dfrac{1}{K_v}=0.1\ \Rightarrow\ K_v=10\ \Rightarrow\ K=\dfrac{3360}{5}=672$$

Answer: **(d)**""",
[r"When the system type makes the step error zero, a nonzero error requirement must be for a ramp.",
 r"Include the zero: $(s+5)\to5$ at $s=0$."]),

"2.105": ("A", r"Rise time: 10% to 90% of the final value (commonly 0 to 100% for underdamped systems).",
r"""- **Rise time $t_r$:** the time to rise from 10% to 90% of the final value. For underdamped systems, 0–100% is also used.
- Peak time: the time to the first peak.
- Settling time: the time to stay within a 2% or 5% band.

0.1 → 0.9 of the final value is the rise time.

Answer: **(a)**""",
[r"Underdamped: $t_r$ (0–100%) $=\dfrac{\pi-\theta}{\omega_d}$ with $\theta=\cos^{-1}\xi$.",
 r"'Final time' is not a standard specification."]),

"2.106": ("A", r"For $G=\dfrac{K}{s(\tau s+1)}$: $\xi=\dfrac{1}{2\sqrt{K\tau}}\propto\dfrac{1}{\sqrt K}$.",
r"""**Step 1 – Characteristic equation.** $\tau s^2+s+K=0\Rightarrow s^2+\dfrac1\tau s+\dfrac K\tau=0$

**Step 2 – Damping ratio.** $\omega_n=\sqrt{K/\tau}$ and $2\xi\omega_n=\dfrac1\tau$
$$\xi=\dfrac{1}{2\tau\sqrt{K/\tau}}=\dfrac{1}{2\sqrt{K\tau}}$$

**Step 3 – Ratio.**
$$\dfrac{\xi_2}{\xi_1}=\sqrt{\dfrac{K_1}{K_2}}=\dfrac{0.75}{0.25}=3\ \Rightarrow\ \dfrac{K_2}{K_1}=\dfrac19=0.1111$$

Answer: **(a)**""",
[r"To *increase* damping, the gain must be *reduced*. The factor must be less than 1, which rules out (b) and (d).",
 r"$\xi\propto1/\sqrt K$, so tripling $\xi$ needs $K/9$, not $K/3$. Option (c) is the trap."]),

"2.107": ("D", r"Reduce the inner (back-emf) loop first, then find $K_v$ of the outer loop. Ramp error $=1/K_v$.",
r"""**Step 1 – Inner loop.** Motor $\dfrac{10}{s}$ with feedback $0.1$:
$$\dfrac{10/s}{1+0.1\cdot10/s}=\dfrac{10}{s+1}$$

**Step 2 – Outer open loop** (tachometer gain 1):
$$G(s)=\dfrac{K}{s}\cdot\dfrac{10}{s+1}=\dfrac{10K}{s(s+1)}$$
This is type 1.

**Step 3 – Ramp error.**
$$K_v=\lim_{s\to0}sG=10K\ \Rightarrow\ e_{ss}=\dfrac{1}{10K}<0.01\ \Rightarrow\ K>10$$

**Step 4 – Options.** Only $K=14$ is greater than 10 ($K=10$ gives exactly 0.01, not *less than*).

Answer: **(d)**""",
[r"Always collapse inner loops before computing error constants.",
 r"'Less than 0.01' is strict. $K=10$ gives exactly 0.01 and fails.",
 r"The inner back-emf loop turns the pure integrator $10/s$ into a first-order lag $10/(s+1)$. This is why the controller must supply the integrator."]),

"2.108": ("B", r"Standard definitions: delay time = 0 to 50%; rise time = 10–90% (or 0–100%); peak time = first peak; settling time = within 2% or 5% of the *final* value.",
r"""**1.** 10–90%, 5–95% or 0–100% of the final value is the definition of **rise time**, not delay time. Delay time is the time to reach 50% of the final value. Incorrect.

**2.** Peak time is the time to reach the first peak of the overshoot. Correct.

**3.** Settling time uses a 2% or 5% band of the **final** value, not 3% or 5% of the *initial* value. Incorrect.

Not correct: 1 and 3. Answer: **(b)**""",
[r"The question asks which are **not** correct. Read the negation carefully.",
 r"Delay time is 50%, rise time is 10–90%. These are often swapped in trick questions."]),

"2.109": ("B", r"Settling time (5%): $t_s=\dfrac{3}{\xi\omega_n}$.",
r"""**Step 1 – Parameters.** $\omega_n=5$ rad/s, and $2\xi\omega_n=8\Rightarrow\xi\omega_n=4$ (and $\xi=0.8$).

**Step 2 – Settling time (5%).**
$$t_s=\dfrac{3}{4}\ \text{s}$$

Answer: **(b)**""",
[r"5% band → 3, 2% band → 4. For 2% the answer would be 1 s, which is not offered.",
 r"For $\xi=0.8$ the envelope formula is less exact, but it is the accepted exam approach."]),

"2.110": ("D", r"Underdamped step response: $1-\dfrac{e^{-\xi\omega_nt}}{\sqrt{1-\xi^2}}\sin(\omega_dt+\theta)$, $\theta=\cos^{-1}\xi$. Read $\xi\omega_n$ and $\omega_d$ from it.",
r"""**Step 1 – Read the decay and frequency.** $e^{-t}$ gives $\xi\omega_n=1$. $\cos(\sqrt3t-\dots)$ gives $\omega_d=\sqrt3$.

**Step 2 – $\omega_n$ and $\xi$.**
$$\omega_n=\sqrt{(\xi\omega_n)^2+\omega_d^2}=\sqrt{1+3}=2,\qquad\xi=\dfrac12$$

**Step 3 – Confirm with the amplitude and phase.**
- Amplitude $\dfrac{1}{\sqrt{1-0.25}}=\dfrac{2}{\sqrt3}$ ✓
- $\cos(\omega_dt-\pi/6)=\sin(\omega_dt+\pi/3)$, and $\theta=\cos^{-1}0.5=\pi/3$ ✓

**Step 4 – Transfer function.**
$$T(s)=\dfrac{\omega_n^2}{s^2+2\xi\omega_ns+\omega_n^2}=\dfrac{4}{s^2+2s+4}$$

Answer: **(d)**""",
[r"Pole $=-\xi\omega_n\pm j\omega_d=-1\pm j\sqrt3$, and $(s+1)^2+3=s^2+2s+4$ follows directly.",
 r"Option (c) uses $\omega_d^2=3$ as $\omega_n^2$. Remember that $\omega_n^2=\sigma^2+\omega_d^2$."]),

"2.111": ("C", r"Critically damped step response: $c(t)=1-(1+\omega_nt)e^{-\omega_nt}$. Solve numerically for the required level.",
r"""**Step 1 – Step response.** $G=\dfrac{1}{(s+1)^2}$ with $\omega_n=1$ and $\xi=1$:
$$c(t)=1-(1+t)e^{-t}$$

**Step 2 – Condition for 94%.** $(1+t)e^{-t}=0.06$

**Step 3 – Trial values.**
- $t=4.5$: $5.5\times0.01111=0.0611$
- $t=4.52$: $5.52\times0.01089=0.0601$
- $t=4.53$: $5.53\times0.01078=0.0596$

So $t\approx4.52$ s, and the nearest option is 4.50.

Answer: **(c)**""",
[r"With answer options, test them directly: plug each option into $(1+t)e^{-t}$ and see which gives about 0.06.",
 r"Do not use the underdamped settling-time formula. This system is critically damped."]),

"2.112": ("D", r"Peaks (maxima) of an underdamped step response occur at odd multiples of $\pi/\omega_d$: $t=\pi/\omega_d,\ 3\pi/\omega_d,\dots$",
r"""**Step 1 – Parameters.** $\omega_n=5$ and $2\xi\omega_n=8\Rightarrow\xi=0.8$
$$\omega_d=5\sqrt{1-0.64}=5\times0.6=3\ \text{rad/s}$$
(Poles at $-4\pm j3$.)

**Step 2 – Peak times.**
- First peak: $\dfrac{\pi}{3}$ s
- First undershoot: $\dfrac{2\pi}{3}$ s
- **Second peak:** $\dfrac{3\pi}{3}=\pi$ s

Answer: **(d)**""",
[r"'Second peak' means the second *maximum*, at $3\pi/\omega_d$. $2\pi/\omega_d$ is a trough. Option (b) is the trap.",
 r"$\omega_d$ is the imaginary part of the poles: $(s+4)^2+9$ gives 3."]),

"2.113": ("C", r"Error constants for $\dfrac{10}{s(1+0.1s)}$ (type 1): $K_p=\infty$, $K_v=10$, $K_a=0$.",
r"""- $K_p=\lim_{s\to0}G(s)=\infty$
- $K_v=\lim_{s\to0}sG(s)=\dfrac{10}{1}=10$
- $K_a=\lim_{s\to0}s^2G(s)=0$

The question asks for them in the order **acceleration, velocity, position**: $0,\ 10,\ \infty$.

Answer: **(c)**""",
[r"Read the order asked for. Here it is reversed ($K_a$, $K_v$, $K_p$). Option (d) uses the usual order with wrong values.",
 r"In Bode form, $K_v$ equals the gain constant for a type-1 system."]),

"2.114": ("D", r"Peak time $t_p=\dfrac{\pi}{\omega_n\sqrt{1-\xi^2}}$.",
r"""**Step 1 – Find $\omega_n$.** $s^2+10s+K=0$ with $2\xi\omega_n=10$ and $\xi=0.5$ gives $\omega_n=10$ rad/s (and $K=100$).

**Step 2 – Damped frequency.** $\omega_d=10\sqrt{1-0.25}=10\times0.866=8.66$ rad/s

**Step 3 – Peak time.**
$$t_p=\dfrac{\pi}{8.66}=0.363\ \text{s}$$

Answer: **(d)**""",
[r"You do not need $K$ explicitly. $\xi\omega_n=5$ is fixed by the open-loop pole at $-10$.",
 r"$\sqrt{0.75}=0.866$ is worth remembering, since $\xi=0.5$ appears very often."]),

"2.115": ("B", r"Standard definitions: rise time 10–90% (or 0–100% for underdamped); $M_p$ indicates relative stability; settling band 2% or 5% of the final value.",
r"""**1.** Rise time for an underdamped system is 0–100% (or 10–90%), not 5–95%. Incorrect.

**2.** A larger $M_p$ means lower $\xi$ and poles closer to the $j\omega$ axis, so maximum overshoot is a direct measure of relative stability. Correct.

**3.** The settling band is 2% or 5% of the final value, not 3% or 6%. Incorrect.

Not correct: 1 and 3. Answer: **(b)**""",
[r"Again the question asks which are **not** correct.",
 r"Relative stability in the time domain is shown by $M_p$ (or $\xi$). In the frequency domain it is shown by the gain and phase margins."]),
}
