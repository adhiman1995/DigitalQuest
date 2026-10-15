# Detailed solutions, chapter 2 (time response analysis), 2.61-2.90.
# number -> (answer, concept, solution, [points to take care of])
D = {
"2.61": ("C", r"Sensitivity of $T$ to $K$: $S_K^T=\dfrac{K}{T}\cdot\dfrac{dT}{dK}$.",
r"""**Step 1 – Differentiate (quotient rule).**
$$\dfrac{dT}{dK}=\dfrac{2(3+4K)-4(1+2K)}{(3+4K)^2}=\dfrac{6+8K-4-8K}{(3+4K)^2}=\dfrac{2}{(3+4K)^2}$$

**Step 2 – Multiply by $K/T$.**
$$S_K^T=\dfrac{K(3+4K)}{1+2K}\cdot\dfrac{2}{(3+4K)^2}=\dfrac{2K}{(1+2K)(3+4K)}$$

**Step 3 – Expand.** $(1+2K)(3+4K)=3+4K+6K+8K^2=3+10K+8K^2$
$$S_K^T=\dfrac{2K}{3+10K+8K^2}$$

Answer: **(c)**""",
[r"Shortcut for a bilinear $T=\dfrac{a+bK}{c+dK}$: $S_K^T=\dfrac{K(bc-ad)}{(a+bK)(c+dK)}$. Here $bc-ad=6-4=2$.",
 r"Do not forget the factor $K/T$. $dT/dK$ alone is not the sensitivity."]),

"2.62": ("C", r"From the overshoot: $\xi=\dfrac{\ln(1/M_p)}{\sqrt{\pi^2+\ln^2(1/M_p)}}$. Then $t_p=\dfrac{\pi}{\omega_n\sqrt{1-\xi^2}}$.",
r"""**Step 1 – $\xi$ from $M_p=0.3$.** $\ln(1/0.3)=1.204$.
$$\xi=\dfrac{1.204}{\sqrt{9.870+1.450}}=\dfrac{1.204}{3.364}=0.358$$

**Step 2 – Damped frequency.**
$$\omega_d=10\sqrt{1-0.358^2}=10\times0.934=9.34\ \text{rad/s}$$

**Step 3 – Peak time.**
$$t_p=\dfrac{\pi}{9.34}=0.336\ \text{s}$$

Answer: **(c)**""",
[r"The options differ only in digit order (0.36, 0.363, 0.336, 0.633). Compute carefully to three significant figures.",
 r"Remember $\xi\approx0.36$ for 30% overshoot, $0.46$ for 20%, and $0.59$ for 10%."]),

"2.63": ("D", r"Overshoot depends only on $\xi$. The smaller $\xi$, the larger the overshoot.",
r"""Each has the form $\dfrac{\omega_n^2}{s^2+2s+\omega_n^2}$, so $2\xi\omega_n=2\Rightarrow\xi=\dfrac{1}{\omega_n}$.

- (a) $\omega_n=3$: $\xi=0.333$
- (b) $\omega_n=4$: $\xi=0.25$
- (c) $\omega_n=5$: $\xi=0.2$
- (d) $\omega_n=6$: $\xi=0.167$ (smallest)

The smallest $\xi$ gives the largest overshoot ($M_p=e^{-\pi\xi/\sqrt{1-\xi^2}}$, about 59% for (d)).

Answer: **(d)**""",
[r"With $\xi\omega_n$ fixed (same $s$ coefficient), a higher $\omega_n$ means a lower $\xi$ and more overshoot, but the same settling time.",
 r"Overshoot does not depend on $\omega_n$ directly; it is a function of $\xi$ alone."]),

"2.64": ("D", r"Closed-loop poles are the roots of $1+G(s)=0$, not the open-loop poles.",
r"""**Step 1 – Characteristic equation.**
$$1+\dfrac{1}{(s+2)^2}=0\ \Rightarrow\ (s+2)^2+1=0$$

**Step 2 – Solve.** $(s+2)^2=-1\Rightarrow s+2=\pm j\Rightarrow s=-2\pm j1$

(Expanded: $s^2+4s+5=0$.)

Answer: **(d)**""",
[r"Option (a) gives the *open-loop* poles. The question asks for the closed-loop poles.",
 r"Closing the loop around a double real pole splits it into a complex pair. This is the root locus breaking away from $-2$."]),

"2.65": ("C", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$.",
r"""**Step 1 – Parameters.** $\omega_n=\sqrt{100}=10$ rad/s, and $2\xi\omega_n=10\Rightarrow\xi\omega_n=5$ (and $\xi=0.5$).

**Step 2 – Settling time.**
$$t_s=\dfrac{4}{5}=0.8\ \text{s}$$

Answer: **(c)**""",
[r"When no tolerance is given, use the 2% criterion, $4/(\xi\omega_n)$. The 5% value, 0.6 s, is not an option here.",
 r"$\xi\omega_n$ is half the coefficient of $s$ (here $10/2=5$)."]),

"2.66": ("C", r"DC gain $=G(0)$. Treating $G$ as the overall transfer function, the step error is $1-G(0)$.",
r"""**Step 1 – DC gain.**
$$G(0)=\dfrac{0+1}{0+0+1}=1$$

**Step 2 – Steady-state step response.** The poles of $s^2+s+1$ are in the LHP, so the system is stable:
$$c(\infty)=\lim_{s\to0}s\cdot G(s)\cdot\dfrac1s=G(0)=1$$

**Step 3 – Error.** $e_{ss}=1-c(\infty)=1-1=0$

Answer: **(c)**""",
[r"The question treats $G(s)$ as the system's (closed-loop) transfer function. If it were an open-loop function in a unity loop, $e_{ss}=\dfrac1{1+K_p}=0.5$, which is not an option.",
 r"A DC gain of exactly 1 means the output follows a step with zero error."]),

"2.67": ("D", r"Compare $\ddot x+2\xi\omega_n\dot x+\omega_n^2x$: $\omega_n=\sqrt{\text{coefficient of }x}$ and $\xi=\dfrac{\text{coefficient of }\dot x}{2\omega_n}$.",
r"""**Step 1 – Natural frequency.** $\omega_n^2=7\Rightarrow\omega_n=\sqrt7=2.646$ rad/s

**Step 2 – Damping ratio.**
$$2\xi\omega_n=5\ \Rightarrow\ \xi=\dfrac{5}{2\sqrt7}=\dfrac{5}{5.29}=0.945\approx0.94$$

Answer: **(d)**""",
[r"The equation is already normalised (coefficient of $\ddot x$ is 1), so read the values directly.",
 r"$\xi=0.94<1$: the system is underdamped, but only slightly."]),

"2.68": ("D", r"Total response = zero-input response (from the initial conditions, input = 0) + zero-state response (from the input, initial conditions = 0).",
r"""**Statement (I).** The zero-*input* response is the response with the **input set to zero**, driven only by the *initial conditions*. The statement says 'with zero initial conditions', which is wrong. With zero input *and* zero initial conditions the response would be identically zero. False.

**Statement (II).** The zero-*state* response is the response to the given input with **zero initial conditions** (zero initial state). True.

Answer: **(d)**""",
[r"Mnemonic: the name says what is zero. Zero-*input* → input is zero. Zero-*state* → initial state is zero.",
 r"The transfer function gives only the zero-state response."]),

"2.69": ("A", r"Damped frequency $\omega_d=\omega_n\sqrt{1-\xi^2}$.",
r"""With $\xi=0$:
$$\omega_d=\omega_n\sqrt{1-0}=\omega_n$$
An undamped system oscillates at exactly its natural frequency.

Answer: **(a)**""",
[r"For $0<\xi<1$, $\omega_d<\omega_n$. For $\xi\ge1$ there is no oscillation, so $\omega_d$ is not defined (imaginary).",
 r"Do not confuse this with the resonant frequency $\omega_r=\omega_n\sqrt{1-2\xi^2}$, which is lower still."]),

"2.70": ("B", r"Type-0 unity feedback with a step input: $e_{ss}=\dfrac{1}{1+K_p}$, $K_p=G(0)$.",
r"""**Step 1 – Position constant.**
$$K_p=G(0)=\dfrac{12K}{14\times18}=\dfrac{12K}{252}=\dfrac{K}{21}$$

**Step 2 – Impose 10% error.**
$$\dfrac{1}{1+K_p}=0.1\ \Rightarrow\ 1+K_p=10\ \Rightarrow\ K_p=9$$

**Step 3 – Solve for $K$.** $\dfrac{K}{21}=9\Rightarrow K=189$

Answer: **(b)**""",
[r"10% error means $e_{ss}=0.1$, so $K_p=9$, not 10. Setting $1/K_p=0.1$ gives $K=210$, which is not an option.",
 r"Include the zero: $G(0)$ has $12$ in the numerator. Dropping it gives $K=2268$."]),

"2.71": ("B", r"Closed loop $s^2+10s+K$: $2\xi\omega_n=10$ and $\omega_n^2=K$.",
r"""**Step 1 – Characteristic equation.** $s^2+10s+K=0$

**Step 2 – With $\xi=0.5$.** $2(0.5)\omega_n=10\Rightarrow\omega_n=10$ rad/s

**Step 3 – $K$.** $K=\omega_n^2=100$

Answer: **(b)**""",
[r"Formula: $K=\left(\dfrac{a}{2\xi}\right)^2=\left(\dfrac{10}{1}\right)^2=100$ for $G=\dfrac{K}{s(s+a)}$."]),

"2.72": ("A", r"The underdamped impulse response has the form $Ae^{-\xi\omega_nt}\sin\omega_dt$, with $\omega_n^2=(\xi\omega_n)^2+\omega_d^2$.",
r"""**Step 1 – Read the exponent and frequency.** $e^{-0.8t}\sin0.6t$ gives $\xi\omega_n=0.8$ and $\omega_d=0.6$.

**Step 2 – Natural frequency.** The poles are at $-0.8\pm j0.6$, so
$$\omega_n=|s|=\sqrt{0.8^2+0.6^2}=\sqrt{1}=1\ \text{rad/s}$$

**Step 3 – Damping ratio.** $\xi=\dfrac{0.8}{1}=0.8$

Answer: **(a)**""",
[r"$\omega_n$ is the *distance* of the pole from the origin, not its imaginary part. Using $0.6^2+0.8^2$ under a square root is the key step.",
 r"The amplitude $\frac16$ does not affect $\omega_n$ or $\xi$; it only scales the response.",
 r"Option (b), $0.64$, comes from forgetting the square root or using $0.8^2$ alone."]),

"2.73": ("C", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$.",
r"""**Step 1 – Parameters.** $\omega_n=5$ rad/s, and $2\xi\omega_n=5\Rightarrow\xi\omega_n=2.5$ (and $\xi=0.5$).

**Step 2 – Settling time.**
$$t_s=\dfrac{4}{2.5}=1.6\ \text{s}$$

Answer: **(c)**""",
[r"This is the same system as question 2.55. The option order differs, so read the letters carefully.",
 r"The 5% band would give 1.2 s, which is the distractor (a)."]),

"2.74": ("D", r"Settling time: the time after which the response stays within a tolerance band (2% or 5%) of its final value.",
r"""- Delay time: the time to reach 50% of the final value.
- Rise time: 10% to 90% (overdamped) or 0 to 100% (underdamped) of the final value.
- **Settling time:** the time to reach and *stay* within a specified percentage band of the final value.

The phrase 'decrease and stay within a specified percentage' describes the settling time.

Answer: **(d)**""",
[r"The key word is 'stay'. Rise time and delay time are about reaching a level, not staying near it.",
 r"'Lag time' is not a standard time-domain specification."]),

"2.75": ("B", r"Rise time × bandwidth ≈ constant. For a first-order low-pass filter, $t_r=\dfrac{2.2}{\omega_H}=\dfrac{0.35}{f_H}$.",
r"""**Step 1 – First-order low-pass.** Step response $1-e^{-t/\tau}$. The 10–90% rise time is $t_r=2.2\tau$.

**Step 2 – Bandwidth.** The $-3$ dB frequency is $f_H=\dfrac{1}{2\pi\tau}$, so $\tau=\dfrac{1}{2\pi f_H}$.

**Step 3 – Combine.**
$$t_r=\dfrac{2.2}{2\pi f_H}=\dfrac{0.35}{f_H}$$
Rise time is inversely proportional to bandwidth.

Answer: **(b)**""",
[r"Remember $t_r\cdot f_H\approx0.35$. It is used widely in electronics and control.",
 r"A wider bandwidth gives a faster response (smaller rise time)."]),

"2.76": ("C", r"DC gain $=G(0)$; high-frequency gain $=\lim_{s\to\infty}G(s)$.",
r"""**DC gain.** $G(0)=\dfrac{1}{0+1}=1$

**High-frequency gain.** As $\omega\to\infty$, $|G(j\omega)|=\dfrac{1}{\sqrt{1+4\omega^2}}\to0$

This is a first-order low-pass system with corner frequency $0.5$ rad/s.

Answer: **(c)**""",
[r"A strictly proper transfer function (denominator order > numerator order) always has zero high-frequency gain.",
 r"A transfer function like $\dfrac{2s}{2s+1}$ would be high-pass: DC gain 0, high-frequency gain 1."]),

"2.77": ("A", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$.",
r"""**Step 1 – Parameters.** $\omega_n=10$ rad/s, and $2\xi\omega_n=10\Rightarrow\xi\omega_n=5$.

**Step 2 – Settling time.**
$$t_s=\dfrac{4}{5}=0.8\ \text{s}$$

Answer: **(a)**""",
[r"This is the same system as question 2.65.",
 r"The 5% band would give $3/5=0.6$ s."]),

"2.78": ("C", r"An overdamped step response $1+Ae^{-p_1t}+Be^{-p_2t}$ has poles $-p_1,-p_2$. Build the characteristic polynomial $(s+p_1)(s+p_2)$.",
r"""**Step 1 – Poles from the exponentials.** $e^{-60t}$ and $e^{-10t}$ give poles at $-60$ and $-10$.

**Step 2 – Characteristic polynomial.**
$$(s+10)(s+60)=s^2+70s+600$$
(The final value of 1 confirms that the DC gain is 1, so $T=\dfrac{600}{s^2+70s+600}$.)

**Step 3 – Parameters.**
$$\omega_n=\sqrt{600}=24.5\ \text{rad/s},\qquad\xi=\dfrac{70}{2\times24.5}=1.43$$

Answer: **(c)**""",
[r"$\omega_n=\sqrt{p_1p_2}$ (geometric mean) and $\xi=\dfrac{p_1+p_2}{2\sqrt{p_1p_2}}$ (arithmetic mean over geometric mean, always $\ge1$).",
 r"You do not need the coefficients 0.2 and −1.2. The exponents alone give the poles."]),

"2.79": ("C", r"Peak time $t_p=\dfrac{\pi}{\omega_d}$, with $\omega_d=\omega_n\sqrt{1-\xi^2}$ from the closed-loop characteristic equation.",
r"""**Step 1 – Closed loop.** $s^2+6s+25=0$

**Step 2 – Parameters.** $\omega_n=5$, $\xi\omega_n=3\Rightarrow\xi=0.6$
$$\omega_d=5\sqrt{1-0.36}=5\times0.8=4\ \text{rad/s}$$
(Poles at $-3\pm j4$, so $\omega_d$ is the imaginary part, 4.)

**Step 3 – Peak time.**
$$t_p=\dfrac{\pi}{4}=0.785\ \text{s}$$

Answer: **(c)**""",
[r"$\omega_d$ is just the imaginary part of the closed-loop poles. Completing the square, $(s+3)^2+16$, gives it immediately.",
 r"Use the closed-loop characteristic equation, not $G(s)$'s poles."]),

"2.80": ("A", r"For unity feedback, $G=\dfrac{T}{1-T}$. Then $K_v=\lim_{s\to0}sG(s)$.",
r"""**Step 1 – Recover $G$.** Using $G=\dfrac{N}{D-N}$:
$$G(s)=\dfrac{\omega_n^2}{s^2+2\xi\omega_ns}=\dfrac{\omega_n^2}{s(s+2\xi\omega_n)}$$

**Step 2 – Velocity constant.**
$$K_v=\lim_{s\to0}s\cdot\dfrac{\omega_n^2}{s(s+2\xi\omega_n)}=\dfrac{\omega_n^2}{2\xi\omega_n}=\dfrac{\omega_n}{2\xi}$$

Answer: **(a)**""",
[r"The standard second-order closed loop comes from the type-1 loop $\dfrac{\omega_n^2}{s(s+2\xi\omega_n)}$. Remember this pairing.",
 r"Ramp error of the standard system: $e_{ss}=\dfrac{1}{K_v}=\dfrac{2\xi}{\omega_n}$."]),

"2.81": ("C", r"$\xi=1$ gives repeated real roots at $s=-\omega_n$.",
r"""$$s=-\xi\omega_n\pm\omega_n\sqrt{\xi^2-1}\ \xrightarrow{\ \xi=1\ }\ s=-\omega_n,\,-\omega_n$$
The poles are **equal, negative and real**: critically damped.

Answer: **(c)**""",
[r"This is the same as question 2.58. Option (d), unequal real roots, describes $\xi>1$."]),

"2.82": ("C", r"Peak (maximum) overshoot: the largest deviation of the output above its final value during the transient.",
r"""For an underdamped step response, the output first exceeds the input (final value) and reaches its largest deviation at the peak time $t_p$. This maximum deviation is the **peak overshoot**:
$$M_p=\dfrac{c(t_p)-c(\infty)}{c(\infty)}\times100\%$$

By the given key, the largest error between reference and output during the transient is called the peak overshoot.

Answer: **(c)**""",
[r"$M_p$ depends only on $\xi$: $M_p=e^{-\pi\xi/\sqrt{1-\xi^2}}$.",
 r"'Transient overshoot', 'peak error' and 'transient deviation' are not standard terms. Learn the standard names: $M_p$, $t_p$, $t_r$, $t_d$, $t_s$."]),

"2.83": (None, r"Type-1 unity-feedback system: $K_p=\infty$, $K_v$ finite, $K_a=0$. Step error $=0$ and ramp error $=1/K_v$.",
r"""Take $G(s)=\dfrac{1}{s\,(\dots)}$ with unity gain, so $K_v=1$.

**Statement 1.** $K_p=\lim_{s\to0}G(s)=\infty$ for type 1, not zero. **False as written.**

**Statement 2.** $K_a=\lim_{s\to0}s^2G(s)=0$ for type 1. **True.**

**Statement 3.** The step-input error is $\dfrac{1}{1+K_p}=0$, not 1. **False as written.**
(The *ramp*, or velocity, input error is $\dfrac{1}{K_v}=1$.)

Only statement 2 is correct as transcribed, and no option says '2 only'. The source question most likely read '$K_p$ is infinite' and 'per unit-step **velocity** input', in which case all three would be true and the answer would be (a). Because the transcription does not support that, the answer key is left unset.""",
[r"Memorise the table: type 0 → $(K_p,K_v,K_a)=(K,0,0)$; type 1 → $(\infty,K,0)$; type 2 → $(\infty,\infty,K)$.",
 r"'Unit-step velocity input' means a unit ramp. Read input descriptions carefully: displacement = step, velocity = ramp, acceleration = parabola."]),

"2.84": (None, r"With non-unity feedback $H=K$, the closed-loop DC gain is $T(0)=\dfrac{1}{K}$ when $G$ has an integrator. The error is $e_{ss}=1-T(0)$.",
r"""**Step 1 – Closed-loop DC gain.**
$$T(s)=\dfrac{G}{1+GH}=\dfrac{10}{s(s+5)+10K}\ \Rightarrow\ T(0)=\dfrac{10}{10K}=\dfrac1K$$

**Step 2 – Steady-state error** (input minus output, unit step):
$$e_{ss}=1-\dfrac{1}{K}$$

**Step 3 – Require $|e_{ss}|<0.05$.**
$$0.95<\dfrac1K<1.05\ \Rightarrow\ 0.9524<K<1.0526$$

**Step 4 – Check the options.** $0.913$ ✗, $0.927$ ✗, $0.953$ ✓, $1.050$ ✓

Two options satisfy the condition. If only $K<1$ is considered (output overshooting the input is excluded), the intended answer is probably $0.953$, option (c). Because two options are valid, no answer key is set.""",
[r"With non-unity feedback, define the error as $r-c$ (the true error), not as the actuating signal $r-Hc$. The actuating signal goes to zero here for any $K$.",
 r"$T(0)=1/H(0)$ whenever $G$ has an integrator. The output tracks $r/H$, not $r$.",
 r"Check both sides of an absolute-value inequality. Forgetting $K>1$ hides the second valid option."]),

"2.85": (None, r"Settling time is governed by the dominant (slowest) pole: $t_s\approx4\tau_{dominant}$ for the 2% band.",
r"""**Step 1 – Poles.** $-10$ ($\tau=0.1$ s) and $-100$ ($\tau=0.01$ s). The pole at $-10$ is 10 times slower and dominates.

**Step 2 – Step response.**
$$c(t)=0.002\left[1-\dfrac{10}{9}e^{-10t}+\dfrac{1}{9}e^{-100t}\right]$$

**Step 3 – 2% settling.** Ignoring the fast term:
$$\dfrac{10}{9}e^{-10t_s}=0.02\ \Rightarrow\ t_s=\dfrac{\ln55.6}{10}=0.40\ \text{s}$$
The rule of thumb $4\tau=0.4$ s gives the same result.

None of the options (20, 2, 0.2, 0.02 s) equals 0.4 s, so the answer key is left unset. (Option (c), 0.2 s, is the closest, but it corresponds to $2\tau$, which is not a standard settling criterion.)""",
[r"For a system with well-separated real poles, the settling time is set by the slowest pole: $t_s\approx4/|p_{slow}|$.",
 r"The DC gain (here 0.002) does not affect the settling time. Settling is measured relative to the final value."]),

"2.86": ("C", r"Normalise, then $\xi=\dfrac{b}{2\sqrt c}$ for $s^2+bs+c$. $\xi<1$ means underdamped.",
r"""**Step 1 – Normalise.** $2s^2+6s+6=0\Rightarrow s^2+3s+3=0$

**Step 2 – Parameters.** $\omega_n=\sqrt3=1.732$ rad/s
$$\xi=\dfrac{3}{2\sqrt3}=\dfrac{\sqrt3}{2}=0.866$$

**Step 3 – Nature.** $0<\xi<1$, so the system is underdamped (discriminant $9-12<0$, complex roots $-1.5\pm j0.866$).

Answer: **(c)**""",
[r"Discriminant check: $b^2-4ac=36-48<0$ means complex roots, so underdamped. There is no need to normalise for this test.",
 r"$\xi=0.866$ still gives a small overshoot, about 0.4%."]),

"2.87": ("A", r"Error constants: $K_p=\lim G$, $K_v=\lim sG$, $K_a=\lim s^2G$ as $s\to0$. Type 2 gives $K_p=K_v=\infty$ and $K_a$ finite.",
r"""**Step 1 – Type.** $s^2$ in the denominator means two integrators: type 2.

**Step 2 – $K_p$ and $K_v$.**
$K_p=\lim_{s\to0}G(s)=\infty$ and $K_v=\lim_{s\to0}sG(s)=\infty$

**Step 3 – $K_a$.**
$$K_a=\lim_{s\to0}s^2G(s)=\dfrac{K(0+2)}{0+0+12}=\dfrac{2K}{12}=\dfrac{K}{6}$$

Answer: **(a)**""",
[r"Factorise or simply evaluate at $s=0$: $s^2+7s+12\to12$. Do not drop the zero's contribution $(s+2)\to2$.",
 r"Option (c) is the type-0 pattern and (b) has zeros where there should be infinities. Check the type first."]),

"2.88": ("B", r"Settling time is measured with respect to the final (steady-state) value.",
r"""Settling time $t_s$ is the time after which the response remains within a specified tolerance band (usually 2% or 5%) **of its final value**.

The tolerance is not measured relative to the peak value, the input amplitude (the final value differs from the input when $e_{ss}\ne0$), or the error.

Answer: **(b)**""",
[r"When there is a steady-state error, the final value differs from the input. Settling is still judged against the *final value*."]),

"2.89": ("D", r"Underdamped means complex-conjugate closed-loop poles, i.e. a negative discriminant of $s^2+as+K$.",
r"""**Step 1 – Characteristic equation.** $s(s+a)+K=0\Rightarrow s^2+as+K=0$

**Step 2 – Condition for complex roots.**
$$a^2-4K<0\ \Rightarrow\ K>\dfrac{a^2}{4}$$
(Equivalently, $\xi=\dfrac{a}{2\sqrt K}<1$.)

Summary:
- $K<a^2/4$: overdamped
- $K=a^2/4$: critically damped
- $K>a^2/4$: underdamped

Answer: **(d)**""",
[r"Increasing $K$ decreases $\xi$. Underdamping needs a *large enough* gain.",
 r"$K=0$ gives open-loop poles at $0$ and $-a$, which is not underdamped."]),

"2.90": ("B", r"Settling time (2%): $t_s=\dfrac{4}{\xi\omega_n}$, with $\xi\omega_n$ = half the $s$ coefficient of the closed-loop characteristic equation.",
r"""**Step 1 – Closed loop.** $s(s+6)+25=0\Rightarrow s^2+6s+25=0$

**Step 2 – Real part.** $\xi\omega_n=\dfrac62=3$ (and $\omega_n=5$, $\xi=0.6$)

**Step 3 – Settling time.**
$$t_s=\dfrac{4}{3}=1.33\ \text{s}$$

Answer: **(b)**""",
[r"For a 5% band: $3/3=1$ s. Read which band the question asks for.",
 r"For $G=\dfrac{K}{s(s+a)}$, $\xi\omega_n=a/2$ regardless of $K$, so the settling time does not depend on $K$ (as long as the system is underdamped)."]),
}
