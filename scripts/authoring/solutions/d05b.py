# Detailed solutions, chapter 5 (frequency response), 5.36-5.70 (Nyquist questions are in d05n.py).
# number -> (answer, concept, solution, [points to take care of]); "X!" corrects a wrong printed key.
D = {
"5.36": ("D", r"A stable (minimum-phase) closed loop needs GM > 0 dB and PM > 0°.",
r"""- GM $>0$ dB: at the phase crossover, $|GH|<1$, so the plot crosses the negative real axis between $0$ and $-1$.
- PM $>0^\circ$: at the gain crossover, the phase is above $-180^\circ$.

Together these mean the Nyquist plot does not encircle $-1$, so the closed loop is stable.

Answer: **(d)**""",
[r"Repeat of 5.27 in different wording. The answer is valid for minimum-phase, open-loop-stable systems.",
 r"Good practice: GM ≥ 6 dB and PM ≥ 30°."]),

"5.38": ("B", r"A delay $e^{-sT}$ has $|e^{-j\omega T}|=1$ and phase $-\omega T$. It adds pure lag, which lowers the phase margin and also lowers the gain margin.",
r"""**Effect on the gain crossover.** The magnitude is unchanged, so $\omega_{gc}$ is the same.

**Phase margin.** At $\omega_{gc}$ the delay adds $-\omega_{gc}$ rad of phase:
$$PM_{delay}=PM-\omega_{gc}\cdot\dfrac{180^\circ}{\pi}<PM$$

**Gain margin.** The extra lag makes the total phase reach $-180^\circ$ at a *lower* frequency, $\omega_{pc}'<\omega_{pc}$. At a lower frequency the magnitude is *higher* (for a typical low-pass $GH$), so
$$GM_{delay}=\dfrac{1}{|GH(j\omega_{pc}')|}<GM$$

So both margins of $G(s)H(s)$ (without the delay) are larger.

Answer: **(b)**""",
[r"A delay never changes the magnitude plot. It only rotates the phase further clockwise as $\omega$ increases.",
 r"Option (c) is tempting, since GM 'seems' unaffected because magnitude is unchanged. But GM is measured at $\omega_{pc}$, which moves.",
 r"Delays are the main reason a high-gain loop becomes unstable in practice."]),

"5.39": (None, r"Relative stability in the frequency domain: PM relates closely to $\xi$; GM (in dB) is positive for a stable minimum-phase system.",
r"""**1.** The phase margin is directly related to the effective damping ($PM\approx100\xi$ for $\xi<0.7$). True.

**2.** It is the *phase margin*, not the gain margin, that gives the better estimate of the damping ratio. A system can have a large GM yet be poorly damped. False.

**3.** For a stable (minimum-phase) system, GM in dB is *positive*. False.

Only statement 1 is correct, and no option offers '1 only'. The question as transcribed has an error, so the answer key is left unset. (If statement 2 originally read 'Phase margin gives a better estimate of damping ratio than gain margin', the answer would be (a), 1 and 2.)""",
[r"PM ↔ damping ($\xi$). GM ↔ how much the gain can rise before instability.",
 r"GM in dB: positive is stable, negative is unstable (minimum-phase systems)."]),

"5.40": ("C", r"Polar plot of a type-2 system with one lag: starts at $\infty\angle-180^\circ$, ends at $0\angle-270^\circ$.",
r"""**Step 1 – Phase and magnitude.**
$$|G|=\dfrac{1}{\omega^2\sqrt{1+\omega^2T^2}},\qquad\angle G=-180^\circ-\tan^{-1}\omega T$$

**Step 2 – End points.**
- $\omega\to0$: $|G|\to\infty$ at $-180^\circ$, so the plot starts far out along the negative real axis.
- $\omega\to\infty$: $|G|\to0$ at $-270^\circ$ (equivalently $+90^\circ$), so it reaches the origin from the positive imaginary direction.

**Step 3 – Path.** The phase stays between $-180^\circ$ and $-270^\circ$, which is the **second quadrant** (negative real part, positive imaginary part). The plot never crosses either axis in between.

This matches plot (c): it comes in from the far left just above the real axis and curves into the origin from above.

Answer: **(c)**""",
[r"Type 2 means two integrators, so the start is at $-180^\circ$. Each extra lag adds up to $-90^\circ$ more by $\omega=\infty$.",
 r"A plot that starts at a finite point on the positive real axis is type 0, which rules out (a)."]),

"5.41": ("B", r"GM ≈ 1 (0 dB) or PM ≈ 0° means the Nyquist plot passes very close to $-1$. The closed loop is on the verge of instability, with very low damping.",
r"""If the margins are nearly zero, the Nyquist plot passes almost through $-1+j0$:
- the closed-loop poles are very close to the $j\omega$ axis,
- $\xi\approx0$, giving a highly oscillatory response with large overshoot and a large $M_r$.

Such a system is **oscillatory** (marginally or poorly stable), not 'relatively stable' or 'highly stable'.

Answer: **(b)**""",
[r"Small PM means small $\xi$, which means oscillatory behaviour. This link appears in many questions.",
 r"GM 'close to unity' means 0 dB, not 1 dB. Read the units."]),

"5.44": ("D", r"Gain-phase (Nichols-type) plot: PM is the horizontal distance from the 0 dB crossing to $-180^\circ$; GM is the vertical distance from the $-180^\circ$ crossing to 0 dB.",
r"""**Step 1 – Phase crossover ($-180^\circ$ line).** The curve crosses the $-180^\circ$ vertical line *above* the 0 dB level (positive gain). So at $\omega_{pc}$, $|GH|>1$:
$$GM=-|GH(j\omega_{pc})|_{dB}<0\ \text{dB}$$

**Step 2 – Gain crossover (0 dB line).** The curve crosses 0 dB at a phase *to the left of* $-180^\circ$ (more lag, about $-190^\circ$):
$$PM=180^\circ+\angle GH(j\omega_{gc})<0^\circ$$

Both margins are negative, so the closed loop is unstable.

Answer: **(d)**""",
[r"On a gain-phase plot: stable means the curve passes to the *right* of and *below* the critical point (0 dB, $-180^\circ$).",
 r"Check the axis directions. Here phase increases to the right, from $-270^\circ$ to $-90^\circ$."]),

"5.45": ("A", r"$GM=\dfrac{1}{|G(j\omega_{pc})|}$: the factor by which the gain can be increased before the plot reaches $-1$.",
r"""At phase crossover the plot is at $-a$ on the real axis. Multiplying the loop gain by $1/a$ moves this point exactly to $-1$, the stability limit. So
$$GM=\dfrac{1}{a}\qquad\left(GM_{dB}=20\log\dfrac1a\right)$$

Answer: **(a)**""",
[r"$a<1$ gives GM > 1 (stable). $a>1$ gives GM < 1 (unstable).",
 r"Option (d), $a$, is the magnitude at phase crossover, not the margin."]),

"5.46": ("C", r"$M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}$ for $\xi\le\dfrac{1}{\sqrt2}$. $M_r=1$ is the boundary where the resonance peak just disappears.",
r"""$$\dfrac{1}{2\xi\sqrt{1-\xi^2}}=1\ \Rightarrow\ 4\xi^2(1-\xi^2)=1\ \Rightarrow\ 4\xi^4-4\xi^2+1=0$$
$$(2\xi^2-1)^2=0\ \Rightarrow\ \xi=\dfrac{1}{\sqrt2}=0.707$$

At this damping, $\omega_r=\omega_n\sqrt{1-2\xi^2}=0$: the peak is at DC, so there is no peak above 1.

Answer: **(c)**""",
[r"For $\xi\ge0.707$, $M_r=1$ (no resonance). The formula should not be used beyond that point.",
 r"$\xi=0.707$ gives the maximally flat (Butterworth) response."]),

"5.47": ("A", r"Marginal stability from Routh: the $s^1$ row is zero, and the auxiliary equation gives $\omega$.",
r"""**Step 1 – Characteristic equation.**
$$s(s+1)(s+5)+K=s^3+6s^2+5s+K=0$$

**Step 2 – Routh.**
$$\begin{array}{c|cc} s^3 & 1 & 5\\ s^2 & 6 & K\\ s^1 & \frac{30-K}{6} & \\ s^0 & K & \end{array}$$
Marginal: $K=30$.

**Step 3 – Frequency.** $6s^2+30=0\Rightarrow s=\pm j\sqrt5$
$$\omega=\sqrt5\ \text{rad/s}\approx2.24\ \text{rad/s}$$

Answer: **(a)**""",
[r"Same system as 3.29. For $s^3+as^2+bs+K$, the oscillation frequency is $\sqrt b$.",
 r"Option (b), $\sqrt6$, uses the wrong coefficient."]),

"5.48": ("D", r"$PM=180^\circ+\angle G(j\omega_{gc})$.",
r"""$$PM=180^\circ+(-90^\circ)=+90^\circ$$
The plot crosses the unit circle on the negative imaginary axis, $90^\circ$ away from $-1$.

Answer: **(d)**""",
[r"Watch the sign: $\angle G=-90^\circ$ gives $PM=+90^\circ$, not $-90^\circ$.",
 r"A first-order type-1 loop $K/s$ always has $PM=90^\circ$."]),

"5.50": ("C", r"Evaluate $G(j\omega)$ at the given frequency. At the corner frequency of a first-order lag, $|G|=0.707$ (−3 dB) and $\angle G=-45^\circ$.",
r"""$$G(j1)=\dfrac{1}{1+j1}$$
- Magnitude: $\dfrac{1}{\sqrt{1^2+1^2}}=\dfrac{1}{\sqrt2}=0.707$ (i.e. $-3$ dB)
- Phase: $-\tan^{-1}\dfrac11=-45^\circ$

Answer: **(c)**""",
[r"Option (b) has the right magnitude ($-3$ dB) but the wrong phase sign: $+0.78$ rad is $+45^\circ$. A pole gives *lag*.",
 r"Option (a) has the wrong phase sign too."]),

"5.51": ("B", r"For $\dfrac{1}{1+sT}$, the corner frequency is $\omega_c=\dfrac{1}{T}$.",
r"""$$G(s)=\dfrac{1}{1+3s}\ \Rightarrow\ T=3\ \text{s}$$
$$\omega_c=\dfrac{1}{3}=0.33\ \text{rad/s}$$
(The pole is at $s=-1/3$.)

Answer: **(b)**""",
[r"The corner frequency equals the pole magnitude $|p|=1/T$, not $T$. Option (a) is the trap.",
 r"Put the factor in $(1+sT)$ form before reading $T$."]),

"5.52": ("B", r"A zero factor $(1+j\omega)$ has magnitude $\sqrt{1+\omega^2}$ and a phase *lead* $+\tan^{-1}\omega$.",
r"""$$G(j1)=1+j1$$
- Magnitude: $\sqrt{1+1}=\sqrt2=1.41$ (i.e. $+3$ dB)
- Phase: $+\tan^{-1}1=+45^\circ$

Answer: **(b)**""",
[r"A zero gives phase *lead* (+), a pole gives phase *lag* (−).",
 r"$|1+j|=\sqrt2$, not $1+1=2$ (and not 2.41, option (d))."]),

"5.53": ("D", r"Factorise the quadratic into $(1+sT_1)(1+sT_2)$. The corner frequencies are $1/T_1$ and $1/T_2$.",
r"""**Step 1 – Factorise.** Look for $T_1T_2=0.66$ and $T_1+T_2=2.33$. Trying $T_1=2$ and $T_2=0.33$: $2\times0.33=0.66$ ✓ and $2+0.33=2.33$ ✓
$$0.66s^2+2.33s+1=(1+2s)(1+0.33s)$$

**Step 2 – Corner frequencies.**
$$\omega_1=\dfrac12=0.5\ \text{rad/s},\qquad\omega_2=\dfrac{1}{0.33}\approx3\ \text{rad/s}$$

Answer: **(d)**""",
[r"The corner frequencies are the pole magnitudes: the roots of $0.66s^2+2.33s+1$ are $-0.5$ and $-3$.",
 r"Do not read corner frequencies off the coefficients directly. Option (a) uses $0.66$ and $0.33$."]),

"5.54": ("C", r"$GM_{dB}=-20\log|GH(j\omega_{pc})|$. Negative GM in dB means $|GH(j\omega_{pc})|>1$.",
r"""Negative GM in dB means the loop gain at the phase crossover exceeds 1. The Nyquist plot crosses the negative real axis *beyond* $-1$ and encircles it.

For a minimum-phase system this means the closed loop is **unstable**.

Answer: **(c)**""",
[r"0 dB GM is marginal, negative is unstable, positive is stable (minimum-phase systems).",
 r"Option (d) would apply only to non-minimum-phase or conditionally stable systems. The standard answer assumes minimum phase."]),

"5.55": ("B", r"Marginal stability: the Nyquist plot passes through $-1$, so $|GH|=1$ and $\angle GH=-180^\circ$ at the same frequency, i.e. $\omega_{gc}=\omega_{pc}$.",
r"""For a minimum-phase system:
- $\omega_{gc}<\omega_{pc}$: stable
- $\omega_{gc}=\omega_{pc}$: **marginally stable** (GM = 0 dB, PM = 0°)
- $\omega_{gc}>\omega_{pc}$: unstable

Answer: **(b)**""",
[r"Remember the order: stable systems reach gain crossover *before* phase crossover as $\omega$ increases.",
 r"Equal crossover frequencies also mean the closed loop oscillates at that frequency."]),

"5.57": ("D", r"Overshoot exists for all $\xi<1$, but a resonance peak ($M_r>1$) exists only for $\xi<0.707$.",
r"""**Statement (I).** A system with $0.707<\xi<1$ shows a (small) overshoot in its step response, but *no* resonance peak in its frequency response, since $M_r=1$ for $\xi\ge0.707$. So 'all systems which overshoot also show a resonance peak' is false.

**Statement (II).** $M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}$ and $M_p=e^{-\pi\xi/\sqrt{1-\xi^2}}$ both increase as $\xi$ falls. A large $M_r$ means a large overshoot. True.

Answer: **(d)**""",
[r"The range $0.707<\xi<1$ is the key counter-example: overshoot without resonance.",
 r"Both $M_r$ and $M_p$ depend only on $\xi$ (for the standard second-order system)."]),

"5.58": ("C", r"Changing the gain $K$ shifts the Bode magnitude plot vertically and leaves the phase plot unchanged. But $\omega_{gc}$ moves, so the PM changes.",
r"""**Statement (I).** $\angle KG(j\omega)=\angle G(j\omega)$ for $K>0$, so the phase plot is unaffected by gain. True.

**Statement (II).** Raising $K$ lifts the magnitude curve, so it crosses 0 dB at a *higher* $\omega_{gc}$. There the phase is more negative, so the PM *decreases*. Gain does affect PM. False.

Answer: **(c)**""",
[r"This is the basis of gain adjustment for a desired PM: pick the frequency where the phase is $-180^\circ+PM_{desired}$, then set $K$ so that $|KG|=1$ there.",
 r"GM also changes with gain (by the same number of dB as the gain change)."]),

"5.59": ("B", r"Phase crossover from $\angle G=-180^\circ$, then $GM=20\log\dfrac{1}{|G(j\omega_{pc})|}$.",
r"""**Step 1 – Phase crossover.**
$$-3\tan^{-1}\dfrac{\omega}{5}=-180^\circ\ \Rightarrow\ \tan^{-1}\dfrac{\omega}{5}=60^\circ\ \Rightarrow\ \omega_{pc}=5\sqrt3=8.66\ \text{rad/s}$$

**Step 2 – Magnitude.**
$$|G(j\omega_{pc})|=\dfrac{10}{\left(\sqrt{25+75}\right)^3}=\dfrac{10}{10^3}=0.01$$

**Step 3 – Gain margin.**
$$GM=20\log\dfrac{1}{0.01}=20\times2=40\ \text{dB}$$

Answer: **(b)**""",
[r"For a triple identical pole, each contributes $60^\circ$ at phase crossover, so $\omega_{pc}=a\tan60^\circ=a\sqrt3$.",
 r"Equivalent check: the critical gain is $8\times5^3=1000$, so $GM=1000/10=100=40$ dB."]),

"5.60": ("A", r"Gain crossover where $|G|=1$; $PM=180^\circ+\angle G(j\omega_{gc})$. ESE expects the asymptotic (straight-line) Bode value here.",
r"""**Step 1 – Asymptotic gain crossover.** $G=\dfrac{1}{s(1+s)}$. Below the corner at 1 rad/s, $|G|\approx\dfrac1\omega$, which reaches 0 dB at $\omega=1$. So $\omega_{gc}\approx1$ rad/s.

**Step 2 – Phase margin.**
$$\angle G(j1)=-90^\circ-\tan^{-1}1=-135^\circ\ \Rightarrow\ PM=180^\circ-135^\circ=45^\circ$$

**Exact values (for reference).** $\omega\sqrt{1+\omega^2}=1\Rightarrow\omega_{gc}=0.786$ rad/s and $PM=51.8^\circ$. The options are built on the asymptotic approximation.

Answer: **(a)**""",
[r"$135^\circ$ (options (c) and (d)) is $|\angle G|$, not the PM. $PM=180^\circ-135^\circ$.",
 r"If an exact answer is listed, prefer it; otherwise use the asymptotic Bode estimate."]),

"5.61": ("D", r"Low-frequency slope of the Bode magnitude plot $=-20N$ dB/decade, where $N$ is the system type.",
r"""For $\omega\to0$, $G(j\omega)\approx\dfrac{K}{(j\omega)^N}$, so
$$|G|_{dB}\approx20\log K-20N\log\omega$$
Type 1 ($N=1$): slope $=-20$ dB/decade (equivalently $-6$ dB/octave).

Answer: **(d)**""",
[r"$-20$ dB/decade $=-6$ dB/octave. Option (b) has the octave number with the wrong sign and unit.",
 r"Type 0: flat (0 dB/dec); type 2: $-40$ dB/dec."]),

"5.62": ("C", r"The forced (sinusoidal steady-state) response is zero at frequencies where $H(j\omega)=0$, i.e. at zeros on the $j\omega$ axis.",
r"""**Step 1 – Transfer function from the step response.**
$$Y(s)=\dfrac1s-\dfrac{3}{s+1}+\dfrac{3}{s+2}=\dfrac{(s+1)(s+2)-3s(s+2)+3s(s+1)}{s(s+1)(s+2)}=\dfrac{s^2+2}{s(s+1)(s+2)}$$
$$H(s)=sY(s)=\dfrac{s^2+2}{(s+1)(s+2)}$$

**Step 2 – Zeros.** $s^2+2=0\Rightarrow s=\pm j\sqrt2$, on the $j\omega$ axis.

**Step 3 – Interpretation.** $H(j\sqrt2)=0$, so a sinusoidal input at $\omega=\sqrt2$ rad/s produces zero forced response (a notch).

Answer: **(c)**""",
[r"Expand the numerator carefully: $s^2+3s+2-3s^2-6s+3s^2+3s=s^2+2$.",
 r"Zeros on the $j\omega$ axis act as perfect notch filters at that frequency."]),

"5.63": ("D", r"For a standard second-order loop, $PM\approx100\,\xi$ (degrees) for $\xi\lesssim0.7$: increasing, and zero when $\xi=0$.",
r"""From the exact relation
$$PM=\tan^{-1}\dfrac{2\xi}{\sqrt{\sqrt{1+4\xi^4}-2\xi^2}}$$
- PM increases with $\xi$ and is roughly proportional to it, $PM\approx100\xi$. Statement 1 ✓
- At $\xi=0$, $PM=\tan^{-1}0=0^\circ$. Statement 4 ✓
- It is neither inversely proportional to nor independent of $\xi$. Statements 2 and 3 ✗

Correct: 1 and 4. Answer: **(d)**""",
[r"'Directly proportional' is an approximation valid for $\xi$ up to about 0.6–0.7.",
 r"Statements 1, 2 and 3 are mutually exclusive, so at most one of them can be right. Use this to eliminate options quickly."]),

"5.64": ("D!", r"GM is measured at the phase-crossover frequency ($\angle GH=-180^\circ$). If the phase never reaches $-180^\circ$ at a finite frequency, GM is infinite.",
r"""**Step 1 – Phase.**
$$\angle G(j\omega)=-90^\circ-\tan^{-1}\omega$$
This goes from $-90^\circ$ to $-180^\circ$, reaching $-180^\circ$ only as $\omega\to\infty$.

**Step 2 – Magnitude at phase crossover.** $\omega_{pc}=\infty$, where $|G|=\dfrac{1}{\omega\sqrt{1+\omega^2}}\to0$.

**Step 3 – Gain margin.**
$$GM=\dfrac{1}{|G(j\omega_{pc})|}=\dfrac10=\infty\quad\Rightarrow\quad GM=\infty\ \text{dB}$$

This agrees with Routh: $s^2+s+K=0$ is stable for every $K>0$, so the gain can be raised indefinitely. A second-order system's polar plot never crosses the negative real axis.

The source book's key gives (c) $-1$, but a negative GM would mean an unstable closed loop, which contradicts $s^2+s+1=0$ having both roots in the LHP. The correct answer is $\infty$.

Answer: **(d)**""",
[r"Any first- or second-order minimum-phase system has $GM=\infty$, since its phase cannot reach $-180^\circ$ at a finite frequency.",
 r"Do not confuse GM with PM. This system's PM is finite (about $52^\circ$).",
 r"Cross-check margins with Routh: infinite GM ⇔ stable for all $K>0$."]),

"5.65": ("C", r"Resonant frequency (peak of $|M(j\omega)|$): $\omega_r=\omega_n\sqrt{1-2\xi^2}$, for $\xi<0.707$.",
r"""$$|M(j\omega)|=\dfrac{1}{\sqrt{(1-u^2)^2+(2\xi u)^2}},\quad u=\dfrac{\omega}{\omega_n}$$
Minimising the denominator: $\dfrac{d}{du}\left[(1-u^2)^2+4\xi^2u^2\right]=0\Rightarrow u^2=1-2\xi^2$
$$\omega_r=\omega_n\sqrt{1-2\xi^2}$$

Answer: **(c)**""",
[r"Three frequencies to keep apart: $\omega_n$ (natural), $\omega_d=\omega_n\sqrt{1-\xi^2}$ (damped, time domain), $\omega_r=\omega_n\sqrt{1-2\xi^2}$ (resonant, frequency domain).",
 r"For $\xi\ge0.707$ the maximum is at $\omega=0$, option (d). The question intends the underdamped case."]),

"5.66": ("C", r"Write in time-constant form: $\dfrac{K}{1+sT}$. Below the corner $1/T$, the asymptote is flat at $20\log K$.",
r"""**Step 1 – Time-constant form.**
$$\dfrac{10}{10+s}=\dfrac{1}{1+0.1s}$$
DC gain $K=1$ (0 dB). Corner frequency $\omega_c=\dfrac{1}{0.1}=10$ rad/s.

**Step 2 – At $\omega=0.1$ rad/s.** This is two decades below the corner, on the flat part of the asymptote:
$$|G|_{dB}=20\log1=0\ \text{dB}$$

Answer: **(c)**""",
[r"Do not read the 10 in the numerator as a gain of 20 dB. The DC gain is $10/10=1$.",
 r"Always normalise to $(1+sT)$ form before drawing Bode asymptotes."]),

"5.67": ("A", r"Noise power passed by a system is proportional to its bandwidth (for white noise), so excessive bandwidth admits excessive noise.",
r"""A larger bandwidth gives a faster response, which is good. But the system then also passes more high-frequency noise. For white noise, the noise power at the output is proportional to the bandwidth.

So bandwidth is kept only as large as the speed requirement needs.

- (b) Bandwidth itself does not reduce relative stability.
- (c) Larger bandwidth gives a *faster* response, not a slower one.
- (d) Noise power is proportional to bandwidth, not to its square.

Answer: **(a)**""",
[r"Thermal noise power $=kTB$, which is linear in bandwidth $B$."]),

"5.68": ("B", r"Phase crossover: $\angle G(j\omega)=-180^\circ$, i.e. $G(j\omega)$ is real and negative, so the imaginary part of the denominator is zero.",
r"""**Step 1 – Substitute $s=j\omega$.**
$$D(j\omega)=-j\omega^3-6\omega^2+11j\omega+6=(6-6\omega^2)+j(11\omega-\omega^3)$$

**Step 2 – Make $G$ real.** Set the imaginary part to zero:
$$11\omega-\omega^3=0\ \Rightarrow\ \omega=\sqrt{11}$$

**Step 3 – Check the sign.** At $\omega=\sqrt{11}$, the real part is $6-66=-60<0$, so $G=\dfrac{K}{-60}$ is negative real: phase $-180^\circ$ ✓

$\omega_{pc}=\sqrt{11}$ rad/s (frequency is taken as positive).

Answer: **(b)**""",
[r"Check that the real part is *negative* at the found frequency. A positive real value would mean $0^\circ$, not $-180^\circ$.",
 r"Bonus: GM $=60/K$, so the system is stable for $K<60$ (agrees with Routh: $6\times11-6=60$)."]),

"5.69": ("D", r"$G(j\omega)=j\omega$: magnitude $20\log\omega$ (+20 dB/decade through 0 dB at $\omega=1$), phase constant $+90^\circ$.",
r"""- Magnitude: $|j\omega|=\omega$, so $|G|_{dB}=20\log\omega$, a straight line of slope **+20 dB/decade** through 0 dB at $\omega=1$. Statement 2 ✓ (statement 1, constant magnitude, ✗)
- Phase: $\angle j\omega=+90^\circ=\dfrac{\pi}{2}$ at all frequencies. Statement 4 ✓

Statement 3 ('constant phase shift angle') is also true in itself, but (d) is the option that gives the complete and specific description: 2 and 4.

Answer: **(d)**""",
[r"When two options both contain true statements, pick the one that is fully correct and most specific. Option (c) pairs 2 with the vaguer 3.",
 r"Integrator $1/s$: $-20$ dB/dec and $-90^\circ$. Differentiator $s$: $+20$ dB/dec and $+90^\circ$."]),

"5.70": ("C", r"Bode plots give GM and PM directly. Bode-based stability judgments are valid for minimum-phase systems. Stability needs the magnitude at phase crossover to be *negative* in dB.",
r"""**1.** GM and PM can be read straight off the magnitude and phase plots. True.

**2.** Using Bode plots alone (margins), absolute and relative stability can be judged reliably only for minimum-phase systems. Non-minimum-phase systems need Nyquist. True.

**3.** GM is positive only if $|L(j\omega_{pc})|_{dB}$ is *negative* (below 0 dB). The statement says 'positive', which is wrong. False.

Correct: 1 and 2. Answer: **(c)**""",
[r"$GM_{dB}=-|L(j\omega_{pc})|_{dB}$. The two quantities have opposite signs.",
 r"Repeat theme of 5.28 (gain at phase crossover must be below 0 dB)."]),
}
