# Detailed solutions, chapter 5 (frequency response), 5.71-5.101 (Nyquist questions are in d05n.py).
# number -> (answer, concept, solution, [points to take care of])
D = {
"5.71": ("A", r"Closed-loop transfer function $T=\dfrac{G}{1+GH}$. Its denominator is $1+GH$, so the roots of $1+GH=0$ are the closed-loop poles.",
r"""$$T(s)=\dfrac{G(s)}{1+G(s)H(s)}$$
The poles of $T(s)$ are the values of $s$ that make the denominator zero:
$$1+G(s)H(s)=0$$
So the roots of the characteristic equation are the **closed-loop poles**.

Answer: **(a)**""",
[r"Roots of $1+GH=0$ = zeros of $1+GH$ = closed-loop poles. Poles of $1+GH$ = open-loop poles.",
 r"Closed-loop zeros are the zeros of $G$ and the poles of $H$. They do not come from the characteristic equation."]),

"5.72": ("C", r"Non-minimum phase: a pole or zero in the RHP. Stability depends only on the poles.",
r"""$$G(s)=\dfrac{10(s-1)}{s+10}$$
- Zero at $s=+1$ (RHP), so it is **non-minimum phase**.
- Pole at $s=-10$ (LHP), so it is stable. Option (a) is wrong.
- A PID controller has the form $K_p+K_i/s+K_ds$, which is different. Option (d) is wrong.

Answer: **(c)**""",
[r"RHP *zeros* do not make a system unstable. Only RHP *poles* do.",
 r"A non-minimum-phase step response starts in the wrong direction: here $G(\infty)=10>0$ but $G(0)=-1<0$."]),

"5.73": ("B", r"Close the loop first. Then $M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}$ and $\omega_r=\omega_n\sqrt{1-2\xi^2}$.",
r"""**Step 1 – Closed loop.**
$$T(s)=\dfrac{25}{s^2+6s+25}\ \Rightarrow\ \omega_n=5,\quad\xi=\dfrac{6}{10}=0.6$$

**Step 2 – Resonant peak.**
$$M_r=\dfrac{1}{2(0.6)\sqrt{1-0.36}}=\dfrac{1}{1.2\times0.8}=1.04$$

**Step 3 – Resonant frequency.**
$$\omega_r=5\sqrt{1-2(0.36)}=5\sqrt{0.28}=2.65\approx2.67\ \text{rad/s}$$

Answer: **(b)**""",
[r"$\xi=0.6<0.707$, so a (small) resonant peak exists.",
 r"4.8 rad/s (options (c) and (d)) is close to $\omega_d=4$ or $\omega_n=5$. Do not mix up the frequencies."]),

"5.74": ("C", r"For a quadratic factor $s^2+2\xi\omega_ns+\omega_n^2$, the corner frequency is $\omega_n$. Poles at the origin have no corner.",
r"""- Numerator $s^2+10s+100$: $\omega_n^2=100$, so the corner is at **10 rad/s** ($\xi=0.5$, complex zeros).
- Denominator $s^2+15s+1$: $\omega_n^2=1$, so the corner is at **1 rad/s** ($\xi=7.5$; really two real poles at about $0.067$ and $14.9$, but treated as one quadratic factor its corner is $\omega_n=1$).
- $s^2$: poles at the origin, which set the initial slope but have no corner.

Answer: **(c)**""",
[r"Corner frequency of a quadratic is $\sqrt{\text{constant term}}$ (when the $s^2$ coefficient is 1), not the $s$ coefficient.",
 r"For a strict asymptotic plot, an overdamped quadratic should be split into its two real poles. Exam options here use $\omega_n$."]),

"5.75": ("B", r"PD controller $K_p(1+T_ds)$: flat at $20\log K_p$ up to $\omega=1/T_d$, then rising at $+20$ dB/decade.",
r"""**Step 1 – Time-constant form.**
$$0.1+0.01s=0.1(1+0.1s)$$
Low-frequency level $20\log0.1=-20$ dB. Corner at $\omega=1/0.1=10$ rad/s.

**Step 2 – Asymptote above the corner.**
$$|G|_{dB}=-20+20\log\dfrac{\omega}{10}$$

**Step 3 – Set to 20 dB.**
$$20\log\dfrac{\omega}{10}=40\ \Rightarrow\ \dfrac{\omega}{10}=100\ \Rightarrow\ \omega=1000\ \text{rad/s}$$

Answer: **(b)**""",
[r"Rising 40 dB at 20 dB/decade takes two decades: $10\to1000$.",
 r"Start from the correct DC level ($-20$ dB). Starting from 0 dB gives 100 rad/s, option (d)."]),

"5.76": ("A", r"For a desired PM, find $\omega_{gc}$ from the phase condition, then choose $K$ so that $|G(j\omega_{gc})|=1$.",
r"""**Step 1 – Phase condition.**
$$PM=180^\circ-90^\circ-\tan^{-1}\dfrac{\omega_{gc}}{5}=45^\circ\ \Rightarrow\ \tan^{-1}\dfrac{\omega_{gc}}{5}=45^\circ\ \Rightarrow\ \omega_{gc}=5\ \text{rad/s}$$

**Step 2 – Magnitude condition.**
$$|G(j5)|=\dfrac{K}{5\sqrt{25+25}}=\dfrac{K}{5\times7.07}=1\ \Rightarrow\ K=35.4\approx35$$

Answer: **(a)**""",
[r"Use the exact magnitude here, not the asymptotic one. At the corner the asymptote is 3 dB off.",
 r"Order of work for 'find $K$ for a given PM': phase first (gives $\omega_{gc}$), then magnitude (gives $K$)."]),

"5.77": ("D", r"For an unstable system, the margins are usually both negative, but with multiple crossovers (conditionally stable or non-minimum-phase loops) either margin alone can appear positive.",
r"""- **3 (both negative):** the common case for an unstable minimum-phase system. ✓
- **1 (GM positive, PM negative)** and **2 (GM negative, PM positive):** possible when the plot has more than one gain or phase crossover, e.g. conditionally stable systems or systems with RHP poles or zeros. The single-crossover margin read-off can then give one positive and one negative value even though the loop is unstable. ✓

Since all three combinations can occur, all are correct.

Answer: **(d)**""",
[r"The rule 'both margins positive ⇔ stable' holds only for simple minimum-phase systems with single crossovers.",
 r"When margins disagree in sign, use the Nyquist criterion to decide stability."]),

"5.78": ("D", r"A ratio of a first-order zero and a first-order pole: the phase starts at $0^\circ$ and returns to $0^\circ$, since each factor contributes $90^\circ$ at high frequency.",
r"""$$\angle G(j\omega)=\tan^{-1}0.2\omega-\tan^{-1}0.5\omega$$
- $\omega=0$: $0^\circ-0^\circ=0^\circ$
- $\omega=\infty$: $90^\circ-90^\circ=0^\circ$

In between the phase is negative (a lag, since the pole corner at 2 rad/s comes before the zero corner at 5 rad/s). This is a lag network.

Answer: **(d)**""",
[r"Equal numbers of poles and zeros (and no integrators) means the phase returns to $0^\circ$ at $\omega=\infty$.",
 r"The gain 10 does not affect phase."]),

"5.79": ("B", r"Initial slope $=-20N$ (poles at the origin). Each slope change of $+20$ dB/dec is a zero; each change of $-20$ is a pole.",
r"""**Step 1 – Initial slope.** $-40$ dB/dec for $\omega<0.1$: two poles at the origin.

**Step 2 – At $\omega=0.1$.** The slope changes from $-40$ to $-20$, a change of $+20$: a zero with corner 0.1 rad/s.

**Step 3 – At $\omega=10$.** The slope changes from $-20$ to $0$, a change of $+20$: a second zero with corner 10 rad/s.

$$G(s)=\dfrac{K(1+10s)(1+0.1s)}{s^2}$$
Two poles and two zeros.

Answer: **(b)**""",
[r"Final slope $0=-20(P-Z)$ gives $P=Z$. A quick consistency check.",
 r"Poles at the origin count as poles, even though they have no corner frequency."]),

"5.80": ("B", r"All-pass: $|G(j\omega)|=1$ at every frequency. Each pole at $-a$ has a matching zero at $+a$, mirror-symmetric about the $j\omega$ axis.",
r"""Example: $G(s)=\dfrac{s-a}{s+a}$. Then
$$|G(j\omega)|=\dfrac{\sqrt{\omega^2+a^2}}{\sqrt{\omega^2+a^2}}=1\ \text{for all }\omega$$
while the phase changes from $180^\circ$ to $0^\circ$ (or $0^\circ$ to $-180^\circ$, depending on the sign convention).

The zeros are mirror images of the poles about the $j\omega$ axis. This is a **symmetric** pole-zero pattern, with unit magnitude at all frequencies.

Answer: **(b)**""",
[r"An all-pass network only changes phase. It is always non-minimum phase, because its zeros are in the RHP.",
 r"Any non-minimum-phase TF = minimum-phase TF × all-pass TF."]),

"5.81": ("C", r"Relative stability describes *how* stable a system is. It is expressed through GM, PM and pole locations (damping), and it is a comparison with other systems.",
r"""**1.** 'Gain margin *only*' is too narrow. False.

**2.** 'Phase margin and certain other parameters' is vague and incomplete in the standard definition. Taken as false.

**3.** Gain margin, phase margin and pole locations (distance from the $j\omega$ axis, damping) together quantify relative stability. True.

**4.** Relative stability is inherently comparative: system A is 'more stable' than system B. True.

Correct: 3 and 4. Answer: **(c)**""",
[r"Absolute stability is a yes/no question. Relative stability measures the degree, e.g. a settling time $\propto1/\sigma$ or the margins."]),

"5.82": ("C", r"Bode magnitude: a flat level of $20\log K$ dB until the corner, then $-20$ dB/dec means a single pole $\dfrac{K}{1+s/\omega_c}$.",
r"""**Step 1 – Low-frequency level.** 20 dB means $K=10^{20/20}=10$.

**Step 2 – Corner.** The slope changes from 0 to $-20$ dB/dec at $\omega=1$ rad/s, which means a pole at $s=-1$.

**Step 3 – Transfer function.**
$$G(s)H(s)=\dfrac{10}{1+s}=\dfrac{10}{s+1}$$
Check: $|G(j0)|=10=20$ dB ✓, and above 1 rad/s it falls at $-20$ dB/dec ✓.

Answer: **(c)**""",
[r"Convert dB to a ratio: $20\text{ dB}\to10$, not 20. Option (d) has 20.",
 r"A falling slope means a pole. Options (a) and (d) have zeros, which would rise."]),

"5.83": ("A", r"Non-minimum-phase elements (RHP zeros, transport lag) add extra phase lag at high frequency. A transport lag $e^{-sT}$ adds lag $\omega T$ without limit.",
r"""**(I)** Non-minimum-phase elements contribute more phase lag than a minimum-phase element with the same magnitude, and this lag grows with frequency. It reduces the phase margin and makes compensation hard. True.

**(II)** A transportation lag $e^{-sT}$ (common in process control: conveyors, pipes) has $|e^{-j\omega T}|=1$ and phase $-\omega T$, which grows without bound. It is a non-minimum-phase element. True.

**Link.** Transportation lag is the standard example of an element that introduces large, frequency-increasing phase lag. (II) illustrates and explains (I).

Answer: **(a)**""",
[r"Padé approximation $e^{-sT}\approx\dfrac{1-sT/2}{1+sT/2}$ shows the RHP zero explicitly.",
 r"Delay lag in degrees: $\omega T\times\dfrac{180}{\pi}$."]),

"5.84": ("C", r"Low-frequency slope $=-20N$ dB/decade, $N$ = number of poles at the origin.",
r"""$$G(s)=\dfrac{6(s^2+10s+100)}{s^2(50s^2+15s+1)}$$
As $\omega\to0$: $G\approx\dfrac{6\times100}{s^2\times1}=\dfrac{600}{s^2}$.

Two poles at the origin give $-40$ dB/decade.

Answer: **(c)**""",
[r"At low frequency, every non-origin factor is just its constant term. Only the $s^N$ factor shapes the slope.",
 r"Low-frequency asymptote: $20\log600-40\log\omega$, crossing 0 dB at $\omega=\sqrt{600}=24.5$ rad/s."]),

"5.85": ("B", r"Read the Bode magnitude from left to right: the initial slope gives the integrators; each $-20$ change is a pole and each $+20$ change is a zero.",
r"""**Step 1 – Initial slope.** $-20$ dB/dec: one pole at the origin, factor $\dfrac1s$.

**Step 2 – At 2 rad/s.** The slope changes from $-20$ to $-40$ (change $-20$): a pole at $s=-2$.

**Step 3 – At 20 rad/s.** The slope changes from $-40$ to $-20$ (change $+20$): a zero at $s=-20$.

$$G(s)H(s)=\dfrac{K(s+20)}{s(s+2)}$$

Answer: **(b)**""",
[r"A slope going *more negative* means a pole. A slope going *less negative* means a zero.",
 r"Check the final slope: $-20(P-Z)=-20(2-1)=-20$ dB/dec ✓"]),

"5.86": ("C", r"Initial slope $+40$ dB/dec means $s^2$ in the numerator. A slope change of $-20n$ at one corner means $n$ repeated poles there.",
r"""**Step 1 – Initial slope.** The plot rises at $+40$ dB/decade before the corner, so the numerator has $s^2$.

**Step 2 – At 10 rad/s.** The slope changes from $+40$ to $-60$ dB/decade, a change of $-100$ dB/decade:
$$\dfrac{-100}{-20}=5\ \text{poles at }\omega=10$$

**Step 3 – Transfer function.**
$$G(s)H(s)=\dfrac{Ks^2}{\left(1+\frac{s}{10}\right)^5}$$
Final slope check: $+40-100=-60$ ✓

Answer: **(c)**""",
[r"Measure both slopes carefully from the figure. The ratio of fall to rise here is 1.5, i.e. $-60$ vs $+40$.",
 r"Total slope change $\div(-20)$ = number of poles at that corner."]),

"5.88": ("A", r"$e^{-sT}$ has unit magnitude and phase $-\omega T$. On a Bode plot, only the phase curve needs a correction.",
r"""**(II)** $|e^{-j\omega T}|=1$, so it adds 0 dB and the magnitude plot is unchanged. $\angle e^{-j\omega T}=-\omega T$ rad, so the phase plot shifts down by $\omega T$ at each frequency. True.

**(I)** Because of (II), handling a delay on a Bode plot is easy: keep the magnitude and subtract $\omega T$ from the phase. (The characteristic equation becomes transcendental, which root locus and Routh cannot handle easily.) True.

**Link.** (II) is exactly why (I) holds.

Answer: **(a)**""",
[r"Routh–Hurwitz cannot handle $e^{-sT}$ directly. Bode and Nyquist can, which is a key advantage of frequency methods.",
 r"On a log-frequency axis the delay's phase $-\omega T$ is not a straight line. It curves down increasingly steeply."]),

"5.89": ("D", r"A high-pass transfer function needs zero gain at DC (zeros at the origin) and a constant gain at high frequency (number of poles = number of zeros).",
r"""**1. One pole, one zero:** $\dfrac{s}{s+a}$. DC gain 0, HF gain 1. High-pass ✓

**2. Two poles, two zeros:** $\dfrac{s^2}{s^2+bs+c}$. DC gain 0, HF gain 1. A second-order high-pass ✓

**3. Two poles, one zero:** $\dfrac{s}{s^2+bs+c}$. DC gain 0, but HF gain $\to0$ (slope $-20$ dB/dec). This is **band-pass**, not high-pass ✗

Correct: 1 and 2. Answer: **(d)**""",
[r"Final slope $=-20(P-Z)$. A high-pass needs 0 dB/dec at high frequency, so $P=Z$.",
 r"Zeros at the origin give the 'blocking' of low frequencies."]),

"5.90": ("D", r"Frequency response = the steady-state magnitude ratio and phase shift of the output relative to a sinusoidal input, as functions of frequency.",
r"""For an input $A\sin\omega t$, a stable LTI system's steady-state output is
$$A|G(j\omega)|\sin(\omega t+\angle G(j\omega))$$
The pair $\{|G(j\omega)|,\ \angle G(j\omega)\}$ as functions of $\omega$ is called the **frequency response**.

'Magnitude response' covers only half of it, and 'transient' or 'steady-state response' describe time-domain outputs.

Answer: **(d)**""",
[r"Frequency response is defined only for stable systems, where a sinusoidal steady state exists."]),

"5.91": ("A", r"Minimum-phase: all poles and zeros in the LHP.",
r"""A transfer function with every pole and zero in the left half-plane has the smallest possible phase lag for its magnitude response, so it is called **minimum phase**.

- All-pass: zeros are mirror images of the poles (in the RHP).
- 'Maximum phase' would have all zeros in the RHP.

Answer: **(a)**""",
[r"Repeat of 1.16 and 1.22. Minimum phase means a unique gain-phase relationship (Bode)."]),

"5.92": ("B", r"The frequency at which the closed-loop magnitude $M(\omega)$ is maximum is the resonant frequency $\omega_r$; the peak value is $M_r$.",
r"""The peak of the frequency-response magnitude occurs at the **resonant frequency**
$$\omega_r=\omega_n\sqrt{1-2\xi^2}$$
and the peak value is the resonant peak $M_r$.

Answer: **(b)**""",
[r"'Peak frequency' and 'tuned frequency' are not standard control-system terms."]),

"5.93": ("D", r"Unstable: GM negative **or** PM negative. Stable (minimum phase): GM positive **and** PM positive.",
r"""**(I)** For an unstable system, the gain margin is negative or the phase margin is *negative*. A positive PM alone does not indicate instability. As written ('or the phase margin is positive'), the statement is false.

**(II)** For a stable (minimum-phase) feedback system, both GM and PM must be positive. True.

Answer: **(d)**""",
[r"Look for a single altered word, here 'positive' instead of 'negative'. That is the usual trick in these statements."]),

"5.94": ("B", r"Constant-$M$ circles: loci of constant closed-loop *magnitude*. Constant-$N$ circles: loci of constant closed-loop *phase* ($N=\tan\phi$), for unity feedback.",
r"""On the $G(j\omega)$ plane of a unity-feedback system:
- **$M$ circles:** points where $\left|\dfrac{G}{1+G}\right|=M$ is constant (closed-loop magnitude).
- **$N$ circles:** points where $\tan\angle\dfrac{G}{1+G}=N$ is constant (closed-loop phase).

So constant-$N$ circles are loci of constant closed-loop phase.

- Option (a) describes $M$ circles.
- Option (c) describes a compensator.
- Option (d) describes a closed-loop (feedback) system.

Answer: **(b)**""",
[r"Memory aid: M for magnitude, N for phase. Both are drawn on the open-loop polar plane and read closed-loop properties from it.",
 r"The Nichols chart is the same idea on gain-phase axes."]),

"5.95": ("A", r"Asymptotic phase: each pole contributes about $-90^\circ$ well above its corner and $0^\circ$ well below; each zero contributes $+90^\circ$ or $0^\circ$ in the same way.",
r"""At $f=20$ Hz:

**Poles**
- 0.01 Hz (far below): $\approx-90^\circ$
- 1 Hz (well below): $\approx-90^\circ$ (exact $-87^\circ$)
- 80 Hz (above 20 Hz): $\approx0^\circ$ (exact $-14^\circ$)

**Zeros**
- 5 Hz (below): $\approx+90^\circ$ (exact $+76^\circ$)
- 100 Hz, 200 Hz (above): $\approx0^\circ$ (exact $+11^\circ,+6^\circ$)

**Total:** $-90-90+0+90+0+0=-90^\circ$ (exact $\approx-98^\circ$).

Answer: **(a)**""",
[r"Rule: a corner more than a decade away is fully 'on' ($\pm90^\circ$) or fully 'off' ($0^\circ$). Corners within a decade are partial, but the approximate answer is still clear here.",
 r"Hz or rad/s does not matter as long as all frequencies use the same unit."]),

"5.96": (None, r"Second-order magnitude peak: $M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}$ (relative to DC), at $\omega_r=\omega_n\sqrt{1-2\xi^2}$.",
r"""**Step 1 – DC gain.** $|G(0)|=5$.

**Step 2 – Relative peak.** $M_r=\dfrac{10/\sqrt3}{5}=\dfrac{2}{\sqrt3}$
$$2\xi\sqrt{1-\xi^2}=\dfrac{\sqrt3}{2}\ \Rightarrow\ 4\xi^2(1-\xi^2)=\dfrac34\ \Rightarrow\ \xi^2=\dfrac14\ \Rightarrow\ \xi=0.5$$
(taking the root with $\xi<0.707$).

**Step 3 – $\omega_n$.** $\omega_r=\omega_n\sqrt{1-2(0.25)}=\dfrac{\omega_n}{\sqrt2}=5\sqrt2\ \Rightarrow\ \omega_n=10$ rad/s

**Step 4 – Transfer function.**
$$G(s)=\dfrac{5\times100}{s^2+2(0.5)(10)s+100}=\dfrac{500}{s^2+10s+100}$$

**Step 5 – Compare with the options.**
- (a) DC gain 1 ✗
- (b) $\omega_n=8.66$, $\xi=0.29$ ✗
- (c) DC gain 5 and $\omega_n=10$ ✓, but $12s$ gives $\xi=0.6$ ✗
- (d) $\xi=0.83$, no peak ✗

None matches exactly. Option (c) is evidently the intended answer with a misprint ($12s$ for $10s$), but as transcribed no option is correct, so the answer key is left unset.""",
[r"Normalise the peak by the DC gain before using the $M_r$ formula. Using $10/\sqrt3$ directly gives the wrong $\xi$.",
 r"From the quadratic $4\xi^2(1-\xi^2)=0.75$ there are two roots ($\xi^2=0.25$ or $0.75$). Only $\xi<0.707$ is valid for a peak."]),

"5.97": ("C", r"Resonant peak of the standard second-order system: $M_r=\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$ for $0<\zeta<0.707$.",
r"""$$|M(j\omega)|=\dfrac{1}{\sqrt{(1-u^2)^2+(2\zeta u)^2}},\quad u=\omega/\omega_n$$
At the peak, $u^2=1-2\zeta^2$:
$$(1-u^2)^2+4\zeta^2u^2=4\zeta^4+4\zeta^2(1-2\zeta^2)=4\zeta^2(1-\zeta^2)$$
$$M_r=\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$$

Answer: **(c)**""",
[r"Check: $\zeta=0.707\Rightarrow M_r=1$ (no peak). Only option (c) gives this.",
 r"Compare $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$. Both depend only on $\zeta$."]),

"5.98": ("C", r"Gain crossover from $|G(j\omega)|=1$; $PM=180^\circ+\angle G(j\omega_{gc})$.",
r"""**Step 1 – Gain crossover.**
$$\dfrac{2\sqrt3}{\omega\sqrt{1+\omega^2}}=1\ \Rightarrow\ \omega^2(1+\omega^2)=12\ \Rightarrow\ \omega^4+\omega^2-12=0$$
$$(\omega^2+4)(\omega^2-3)=0\ \Rightarrow\ \omega_{gc}=\sqrt3\ \text{rad/s}$$

**Step 2 – Phase.**
$$\angle G(j\sqrt3)=-90^\circ-\tan^{-1}\sqrt3=-90^\circ-60^\circ=-150^\circ$$

**Step 3 – Phase margin.** $PM=180^\circ-150^\circ=30^\circ$

Answer: **(c)**""",
[r"Treat $\omega^4+\omega^2-12=0$ as a quadratic in $\omega^2$.",
 r"The numbers are chosen to give standard angles ($\tan^{-1}\sqrt3=60^\circ$). If you get an awkward angle, recheck."]),

"5.99": ("D", r"If $|G(j\omega)|<1$ at all frequencies, there is no gain crossover, so the phase margin is undefined (taken as infinite).",
r"""**Step 1 – Magnitude.** $|1-j\omega|=\sqrt{1+\omega^2}=|1+j\omega|$, so it cancels:
$$|G(j\omega)|=\dfrac{\sqrt{1+\omega^2}}{\sqrt{1+\omega^2}\sqrt{4+\omega^2}}=\dfrac{1}{\sqrt{4+\omega^2}}\le\dfrac12$$

**Step 2 – Gain crossover.** $|G|\le0.5<1$ for all $\omega$, so it never equals 1 and there is no gain crossover frequency.

**Step 3 – Phase margin.** With no gain crossover, the gain can never reach 1 at $-180^\circ$, so the phase margin is infinite (the plot stays inside the unit circle).

Answer: **(d)**""",
[r"An RHP zero $(1-s)$ has the *same magnitude* as $(1+s)$ but more phase lag. Magnitudes cancel; phases do not.",
 r"Closed-loop check: $s^2+3s+2+1-s=s^2+2s+3$, stable ✓"]),

"5.101": (None, r"Type-2 Bode plot: low-frequency asymptote $|G|\approx K/\omega^2$, slope $-40$ dB/dec, value $20\log K$ at $\omega=1$, crossing 0 dB at $\omega=\sqrt K$. $K=K_a$, the acceleration (parabolic) error constant.",
r"""Low-frequency asymptote: $|G|_{dB}=20\log K-40\log\omega$.

**Statement 1.** 0 dB crossing: $20\log K=40\log\omega_x\Rightarrow\omega_x=\sqrt K$, not $K$. **Not correct.**

**Statement 2.** At $\omega=1$: $|G|_{dB}=20\log K$, not $40\log K$. **Not correct.**

**Statement 3.** $K_a=\lim_{s\to0}s^2G(s)=K$, so $K$ is the static **acceleration** (parabolic) error coefficient, not the ramp (velocity) one. For type 2, $K_v=\infty$. **Not correct.**

As transcribed, all three statements are not correct, but no option offers '1, 2 and 3'. The question (or its transcription) has an error, so the answer key is left unset.""",
[r"Type 1: the $-20$ line crosses 0 dB at $\omega=K_v$. Type 2: the $-40$ line crosses 0 dB at $\omega=\sqrt{K_a}$.",
 r"The value of any low-frequency asymptote at $\omega=1$ is always $20\log K$, whatever the type.",
 r"Ramp ↔ $K_v$ (type 1), parabola/acceleration ↔ $K_a$ (type 2)."]),
}
