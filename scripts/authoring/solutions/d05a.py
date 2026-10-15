# Detailed solutions, chapter 5 (frequency response), 5.1-5.35 (Nyquist questions are in d05n.py).
# number -> (answer, concept, solution, [points to take care of])
D = {
"5.1": ("D", r"Classical control pioneers: Bode (asymptotic log plots), Evans (root locus), Nyquist (polar plot and stability criterion).",
r"""- **A. Bode:** Bode plots, i.e. asymptotic (straight-line) log-magnitude and phase plots → **1**
- **B. Evans:** root-locus technique (1948) → **3**
- **C. Nyquist:** polar (Nyquist) plots and the Nyquist stability criterion (1932) → **2**

Constant M and N circles (List-II item 4) are associated with Hall and Nichols, not with anyone in List-I.

A–1, B–3, C–2. Answer: **(d)**""",
[r"Also worth knowing: Routh and Hurwitz (algebraic criterion), Nichols (Nichols chart: gain vs phase), Hall (M and N circles).",
 r"Only three items in List-I, so one List-II item is unused. That is normal in match questions."]),

"5.2": ("A", r"$PM=180^\circ+\angle G(j\omega_{gc})$, where the plot crosses the unit circle. $GM=\dfrac{1}{|G(j\omega_{pc})|}$, where the plot crosses the negative real axis.",
r"""**Step 1 – Phase margin.** The plot meets the unit circle (gain crossover) at a point $30^\circ$ *below* the positive real axis, so $\angle G(j\omega_{gc})=-30^\circ$.
$$PM=180^\circ+(-30^\circ)=150^\circ$$

**Step 2 – Gain margin.** The plot crosses the negative real axis at $-0.25$, so $|G(j\omega_{pc})|=0.25$.
$$GM=\dfrac{1}{0.25}=4\quad(=12\ \text{dB})$$

Answer: **(a)**""",
[r"PM is measured from the *negative* real axis to the crossing point. A crossing at $-30^\circ$ is $150^\circ$ away from $-180^\circ$, not $30^\circ$.",
 r"$GM=1/0.25$, not $0.25$ and not $1-0.25=3/4$. Option (b) has that trap."]),

"5.3": ("B", r"Phase crossover frequency: $\angle G(j\omega_{pc})=-180^\circ$.",
r"""**Step 1 – Phase.**
$$\phi(\omega)=-\left[\tan^{-1}\omega+\tan^{-1}2\omega+\tan^{-1}3\omega\right]$$

**Step 2 – Solve $\phi=-180^\circ$.** Use $\tan^{-1}2\omega+\tan^{-1}3\omega=180^\circ-\tan^{-1}\omega$. Taking tangents:
$$\dfrac{5\omega}{1-6\omega^2}=-\omega\ \Rightarrow\ 5=-(1-6\omega^2)\ \Rightarrow\ 6\omega^2=6\ \Rightarrow\ \omega=1$$

**Step 3 – Check.** At $\omega=1$: $45^\circ+63.43^\circ+71.57^\circ=180^\circ$ ✓

$\omega_{pc}=1$ rad/s. Answer: **(b)**""",
[r"With answer options, simply test each one. $\omega=1$ gives exactly $180^\circ$.",
 r"$\tan^{-1}2+\tan^{-1}3=135^\circ$ is a useful identity to remember."]),

"5.5": ("A", r"For $\dfrac{K}{s(1+sT_1)(1+sT_2)}$: $\omega_{pc}=\dfrac{1}{\sqrt{T_1T_2}}$ and $|G(j\omega_{pc})|=\dfrac{KT_1T_2}{T_1+T_2}$.",
r"""**Step 1 – Phase crossover.**
$$-90^\circ-\tan^{-1}\omega T_1-\tan^{-1}\omega T_2=-180^\circ\ \Rightarrow\ \tan^{-1}\omega T_1+\tan^{-1}\omega T_2=90^\circ$$
Two angles summing to $90^\circ$ have tangents with product 1: $\omega^2T_1T_2=1$, so
$$\omega_{pc}=\dfrac{1}{\sqrt{T_1T_2}}$$

**Step 2 – Magnitude there.** With $\omega^2T_1^2=T_1/T_2$ and $\omega^2T_2^2=T_2/T_1$:
$$|G|=\dfrac{1}{\omega\sqrt{\left(1+\frac{T_1}{T_2}\right)\left(1+\frac{T_2}{T_1}\right)}}=\dfrac{\sqrt{T_1T_2}}{\frac{T_1+T_2}{\sqrt{T_1T_2}}}=\dfrac{T_1T_2}{T_1+T_2}$$

**Step 3 – Gain margin.**
$$GM=\dfrac{1}{|G|}=\dfrac{T_1+T_2}{T_1T_2}$$

Answer: **(a)**""",
[r"Option (c) gives $|G(j\omega_{pc})|$, not the GM. Remember to take the reciprocal.",
 r"Equivalent result: the closed loop is stable for $K<\dfrac{T_1+T_2}{T_1T_2}=\dfrac1{T_1}+\dfrac1{T_2}$ (matches the Routh test)."]),

"5.6": ("D", r"High-frequency slope of the Bode magnitude plot $=-20(P-Z)$ dB/decade.",
r"""**Count.**
- Poles: 2 at the origin + 2 complex pairs (4 poles) $=6$
- Zeros: 2

**Slope.**
$$-20(6-2)=-80\ \text{dB/decade}$$

Answer: **(d)**""",
[r"Each complex *pair* counts as two poles ($-40$ dB/decade).",
 r"Poles at the origin set the *initial* slope too, but at high frequency all poles and zeros count equally."]),

"5.7": ("D", r"A transfer function with any pole or zero in the right-half $s$-plane is non-minimum phase.",
r"""A zero with positive real part ($s=+a$) lies in the RHP. Compared with its LHP mirror image ($s=-a$), it has the same magnitude response but *more* phase lag. So the transfer function does not have the minimum possible phase for its magnitude, and it is called **non-minimum phase**.

Answer: **(d)**""",
[r"An RHP zero causes an initial undershoot in the step response (the response first moves the wrong way).",
 r"'Zero phase', 'negative phase' and 'positive phase' function are not standard terms."]),

"5.10": ("B", r"Gain and phase margins measure the distance of the polar plot from $-1+j0$. For *minimum-phase* systems, positive margins ⇔ stability.",
r"""**1.** GM is the distance along the real axis from the crossing to $-1$, and PM is the angular distance on the unit circle. Both measure how close the polar plot is to $-1+j0$. True.

**2.** For non-minimum-phase (or open-loop unstable) systems, the margin rule fails. A stable system can have a negative margin and vice versa, so the full Nyquist criterion is needed. False.

**3.** For a minimum-phase system, stability requires both GM > 0 dB and PM > 0°. True.

Correct: 1 and 3. Answer: **(b)**""",
[r"The 'both margins positive' rule is valid only for minimum-phase, open-loop-stable systems.",
 r"Conditionally stable systems can also confuse the margin rule. Use Nyquist when in doubt."]),

"5.11": ("B", r"Non-minimum phase: RHP poles or zeros. Bode's gain-phase relation holds only for minimum-phase systems.",
r"""**(A)** $G(s)=\dfrac{10(s-25)}{s(s+1)(s+5)}$ has a zero at $s=+25$, in the RHP, so it is non-minimum phase. True.

**(R)** For a minimum-phase transfer function, the phase is uniquely determined by the magnitude (Bode's gain-phase relation). True.

**Link.** (A) is true because of the RHP zero. (R) describes a property of *minimum-phase* systems and does not explain why this $G$ is non-minimum phase.

Answer: **(b)**""",
[r"$(s-25)$ means a zero at $+25$. Read the sign of the factor carefully.",
 r"The pole at the origin is on the $j\omega$ axis, not in the RHP, so it does not affect the minimum-phase test."]),

"5.12": ("B", r"Bandwidth sets both the speed and accuracy of following the input, and the amount of high-frequency noise passed.",
r"""**(A)** A system passes frequencies up to its bandwidth. A smaller bandwidth rejects more high-frequency noise, so the bandwidth indicates the noise-filtering characteristic. True.

**(R)** Bandwidth also indicates how faithfully (and how fast) the system reproduces the input. A wider bandwidth means a faster response and better tracking of fast inputs. True.

**Link.** These are two separate consequences of the same parameter. Reproducing the input does not *explain* noise filtering.

Answer: **(b)**""",
[r"Bandwidth trade-off: wide BW gives a fast response but more noise; narrow BW gives less noise but a slow response."]),

"5.13": ("A", r"An extra open-loop pole reduces the closed-loop bandwidth, and rise time is inversely proportional to bandwidth.",
r"""**(A)** Adding a pole adds lag. The closed-loop response becomes slower, so the rise time increases. True.

**(R)** The additional pole adds attenuation at high frequency, so the closed-loop bandwidth decreases. True.

**Link.** Since $t_r\propto\dfrac{1}{\omega_{BW}}$, the reduced bandwidth is exactly why the rise time increases. (R) explains (A).

Answer: **(a)**""",
[r"Compare question 2.53: rise time and bandwidth are inversely related.",
 r"Adding a pole (or lag compensation) reduces BW and slows the response. Adding a zero (or lead compensation) does the opposite."]),

"5.14": ("C", r"A phase-lag compensator attenuates high frequencies. This lowers the gain crossover frequency, bandwidth and resonance peak, while allowing a *higher* low-frequency gain.",
r"""A lag compensator $\dfrac{1+Ts}{1+\beta Ts}$ ($\beta>1$) gives high-frequency attenuation of $1/\beta$:

1. **Reduced velocity constant?** No. Lag compensation is used to *increase* $K_v$ (better steady-state accuracy) for a given relative stability. ✗
2. **Reduced gain crossover frequency:** the attenuation moves $\omega_{gc}$ lower. ✓
3. **Reduced bandwidth:** follows from the lower $\omega_{gc}$. ✓
4. **Reduced resonance peak:** at the lower $\omega_{gc}$ the phase margin is larger, so $M_r$ falls. ✓

Achieved: 2, 3 and 4. Answer: **(c)**""",
[r"Lag compensation improves steady-state error and relative stability but makes the response slower (lower BW).",
 r"Lead compensation increases BW, speeds up the response and improves PM, but does not help steady-state error much."]),

"5.15": ("D", r"Gain crossover: $|G|=1$, giving $PM=180^\circ+\angle G$. Phase crossover: $\angle G=-180^\circ$, giving $GM=20\log\dfrac{1}{|G|}$.",
r"""**Step 1 – Gain crossover.** From the table, $|G|=1.00$ at $\omega=8$ rad/s, where $\angle G=-170^\circ$.
$$PM=180^\circ-170^\circ=10^\circ$$

**Step 2 – Phase crossover.** $\angle G=-180^\circ$ at $\omega=10$ rad/s, where $|G|=0.64$.
$$GM=20\log_{10}\dfrac{1}{0.64}=20\times0.194=3.88\ \text{dB}\approx3.86\ \text{dB}$$

Both margins are positive but small: stable, with poor relative stability.

Answer: **(d)**""",
[r"PM is $180^\circ+\angle G$, not the angle itself. Option (b) quotes $-180^\circ$, which is the phase, not a margin.",
 r"$20\log(1/0.64)$: $\log0.64=-0.194$. Keep the sign right, since GM is positive here."]),

"5.17": ("B", r"For the standard loop $G=\dfrac{\omega_n^2}{s(s+2\xi\omega_n)}$: $\omega_{gc}=\omega_n\sqrt{\sqrt{1+4\xi^4}-2\xi^2}$ and $PM=\tan^{-1}\dfrac{2\xi}{\sqrt{\sqrt{1+4\xi^4}-2\xi^2}}$.",
r"""**Step 1 – Gain crossover.** $|G(j\omega)|=\dfrac{\omega_n^2}{\omega\sqrt{\omega^2+4\xi^2\omega_n^2}}=1$. Let $u=(\omega/\omega_n)^2$:
$$u^2+4\xi^2u-1=0\ \Rightarrow\ u=\sqrt{4\xi^4+1}-2\xi^2$$

**Step 2 – Phase there.** $\angle G=-90^\circ-\tan^{-1}\dfrac{\omega_{gc}}{2\xi\omega_n}$
$$PM=180^\circ+\angle G=90^\circ-\tan^{-1}\dfrac{\sqrt u}{2\xi}=\tan^{-1}\dfrac{2\xi}{\sqrt u}$$

**Result.**
$$PM=\tan^{-1}\left\{\dfrac{2\xi}{\sqrt{-2\xi^2+\sqrt{1+4\xi^4}}}\right\}$$

Answer: **(b)**""",
[r"Handy approximation for $\xi<0.7$: $PM\,(\text{deg})\approx100\,\xi$, e.g. $\xi=0.5\Rightarrow PM\approx52^\circ$.",
 r"Check with $\xi\to0$: PM $\to0$. Only option (b) gives this."]),

"5.18": ("B", r"Bode magnitude of a type-1 system: the initial $-20$ dB/dec line (extended) cuts 0 dB at $\omega=K_v$. On log scales, slopes relate the corner and crossing frequencies *geometrically*.",
r"""**Statement 1.** The initial slope is $-20$ dB/decade, so there is one integrator: type 1. True.

**Statement 2.** For type 1, the low-frequency asymptote is $20\log\dfrac{K_v}{\omega}$. Its extension (dashed in the figure) crosses 0 dB at $\omega=K_v$. That point is marked $\omega_3$, so $\omega_3$ equals the static (velocity) error coefficient numerically. True.

**Statement 3.** At $\omega_1$ the level is $20\log\dfrac{\omega_3}{\omega_1}$ (from the $-20$ line). The actual plot then falls at $-40$ dB/dec and reaches 0 dB at $\omega_2$:
$$40\log\dfrac{\omega_2}{\omega_1}=20\log\dfrac{\omega_3}{\omega_1}\ \Rightarrow\ \omega_2^2=\omega_1\omega_3\ \Rightarrow\ \omega_2=\sqrt{\omega_1\omega_3}$$
This is the *geometric* mean, not the arithmetic mean. False.

Correct: 1 and 2. Answer: **(b)**""",
[r"On a log-frequency axis, 'midpoints' are geometric means. Arithmetic means are almost always a trap.",
 r"Type 0: the initial level is $20\log K_p$. Type 2: the $-40$ line cuts 0 dB at $\sqrt{K_a}$."]),

"5.19": ("C", r"High-frequency slope $=-20\times(\text{poles}-\text{zeros})$. A lag-lead compensator has equal numbers of poles and zeros, so it adds no net slope at high frequency.",
r"""**Compensator.** Two zeros ($1+\tau_1s$, $1+\tau_2s$) and two poles ($1+\tau_1s/\beta$, $1+\beta\tau_2s$). At very high frequency it tends to a constant:
$$G_c(j\omega)\to\dfrac{\tau_1\tau_2}{(\tau_1/\beta)(\beta\tau_2)}=1$$
So its net slope is 0 dB/decade.

**Plant.** $G(s)$ has 3 poles (and, as implied, no zeros), so its slope is $-60$ dB/decade.

**Total.** $-60+0=-60$ dB/decade.

Answer: **(c)**""",
[r"Lead, lag and lag-lead compensators are all biproper (equal numbers of poles and zeros). They do not change the final slope.",
 r"'3 poles in the LHP' fixes the count. Stability of $G$ is irrelevant to the slope."]),

"5.20": ("C", r"Resonant frequency $\omega_r=\omega_n\sqrt{1-2\xi^2}$ (exists only for $\xi<0.707$).",
r"""**Step 1 – Parameters** (taking the given second-order function as the frequency response being examined): $\omega_n=\sqrt{100}=10$ rad/s and $2\xi\omega_n=10\Rightarrow\xi=0.5$.

**Step 2 – Resonant frequency.**
$$\omega_r=10\sqrt{1-2(0.25)}=10\sqrt{0.5}=7.07\ \text{rad/s}$$

(The resonant peak is $M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}=1.155$.)

Answer: **(c)**""",
[r"Strictly, closing the unity loop around this $G$ gives $\dfrac{100}{s^2+10s+200}$ ($\omega_n=14.1$, $\xi=0.354$), with $\omega_r=12.2$ rad/s, which is not an option. The examiners intended the given standard form to be used directly.",
 r"Do not confuse $\omega_r=\omega_n\sqrt{1-2\xi^2}$ (7.07) with $\omega_d=\omega_n\sqrt{1-\xi^2}$ (8.66, option (b)).",
 r"For $\xi\ge0.707$ there is no resonant peak."]),

"5.22": ("D", r"Phase margin $=180^\circ+\angle G(j\omega_{gc})$, where $|G(j\omega_{gc})|=1$.",
r"""**Step 1 – Magnitude.**
$$|G(j\omega)|=\dfrac{1}{1+\omega^2}\le1$$
This equals 1 only at $\omega=0$, so $\omega_{gc}=0$.

**Step 2 – Phase there.** $\angle G(j0)=-2\tan^{-1}0=0^\circ$

**Step 3 – Phase margin.**
$$PM=180^\circ+0^\circ=180^\circ=\pi\ \text{rad}$$

Answer: **(d)**""",
[r"When the magnitude never exceeds 1 (DC gain $\le1$), the gain crossover is at $\omega=0$ or does not exist. Check that edge case.",
 r"This system also has infinite GM, since the phase reaches $-180^\circ$ only as $\omega\to\infty$."]),

"5.23": ("B", r"Bandwidth governs both noise filtering and the ability to reproduce the input. These are two separate consequences.",
r"""This is the same as question 5.12.

**(A)** A narrower bandwidth means more high-frequency noise is filtered out, so bandwidth indicates noise filtering. True.

**(R)** Bandwidth also measures how well (and how fast) the system reproduces the input. True.

**Link.** Both follow from the bandwidth, but (R) does not explain (A).

Answer: **(b)**""",
[r"Repeated question (ESE 2002 and 2004)."]),

"5.24": ("D", r"Gain margin and phase margin are measures of relative stability (degree of stability). Routh–Hurwitz gives only absolute stability.",
r"""- (a) Wrong definition. PM is measured at the gain-crossover frequency, where the gain is **1** (0 dB), not 10.
- (b) Wrong definition. GM is measured at the frequency of **$180^\circ$** phase lag, not $90^\circ$.
- (c) The basic Routh–Hurwitz criterion tells only whether the system is stable or not (absolute stability). It does not give the degree of stability without modification (e.g. shifting the axis).
- (d) GM and PM measure how close the system is to instability, i.e. the degree (relative) stability. ✓

Answer: **(d)**""",
[r"Absolute stability: Routh, Hurwitz. Relative stability: GM, PM, $M_r$, $\xi$.",
 r"Watch for altered numbers in definitions: 'gain of 10' and '90° lag' are deliberate traps."]),

"5.25": ("D", r"Bode plot of $\dfrac{1}{1+s}$: 0 dB below the corner $\omega=1$, then $-20$ dB/decade above it.",
r"""$$|X(j\omega)|_{dB}=-20\log\sqrt{1+\omega^2}$$
- $\omega\ll1$: $\approx0$ dB (flat)
- $\omega\gg1$: $\approx-20\log\omega$, a slope of $-20$ dB/decade
- Corner frequency: $\omega=1$ rad/s, where the true value is $-3$ dB

So the asymptotic plot is constant at 0 dB for $\omega<1$ and falls at $-20$ dB/decade for $\omega>1$.

Answer: **(d)**""",
[r"A pole gives $-20$ dB/dec after its corner; a zero gives $+20$ dB/dec. Option (c) describes the zero $1+s$.",
 r"A single straight line through all frequencies (options (a) and (b)) is the plot of a pure integrator or differentiator, $1/s$ or $s$."]),

"5.26": ("C", r"A sharp cut-off in the frequency response means a high resonance peak $M_r$, which corresponds to low $\xi$, large overshoot and poor relative stability.",
r"""**1.** A sharp cut-off (a steep drop after the peak) goes together with a large resonant peak $M_r$. True.

**2.** Sharpness of cut-off is about the *shape* of the response near the edge, not the *width*. A sharp cut-off does not imply a large bandwidth. False.

**3.** Large $M_r$ means small $\xi$, which means large overshoot and lower relative stability. True.

Correct: 1 and 3. Answer: **(c)**""",
[r"Large $M_r$ ⇔ small $\xi$ ⇔ large $M_p$ ⇔ small PM. All of these indicate poorer relative stability.",
 r"$M_r$ between 1.1 and 1.5 (i.e. $\xi$ between about 0.4 and 0.7) is the usual design target."]),

"5.27": ("C", r"Minimum-phase systems are stable if and only if both GM and PM are positive.",
r"""For a minimum-phase (open-loop-stable) system:
- GM $>0$ dB: the gain at the phase crossover is below 1.
- PM $>0^\circ$: the phase at the gain crossover is above $-180^\circ$.

Both must be positive, which means the Nyquist plot passes to the right of $-1$ without encircling it.

Answer: **(c)**""",
[r"One positive and one negative margin indicates a problem. Check carefully with Nyquist (usually unstable or conditionally stable).",
 r"Practical targets: GM ≥ 6 dB and PM ≥ 30° to 45°."]),

"5.28": ("D", r"Gain margin $=-|G(j\omega_{pc})|_{dB}$. For stability the gain at phase crossover must be below 1 (below 0 dB).",
r"""At the phase crossover ($\angle GH=-180^\circ$):
- $|GH|<1$, i.e. $<0$ dB: the plot crosses between $0$ and $-1$. Stable (positive GM).
- $|GH|=1$, i.e. $0$ dB: marginal.
- $|GH|>1$, i.e. $>0$ dB: unstable.

So the gain at the phase crossover must always be less than 0 dB.

Answer: **(d)**""",
[r"Do not confuse 'gain at phase crossover' (must be $<0$ dB) with 'gain margin' (must be $>0$ dB). They are negatives of each other in dB."]),

"5.29": ("C", r"$GM=\dfrac{1}{|G(j\omega_{pc})|}$. Changing the gain does not move $\omega_{pc}$, since phase is independent of gain.",
r"""**Step 1.** Doubling $K$ leaves the phase unchanged, so $\omega_{pc}$ stays the same.

**Step 2.** $|G(j\omega_{pc})|$ doubles, so
$$GM_{new}=\dfrac{1}{2|G(j\omega_{pc})|}=\dfrac{GM}{2}$$

In dB, the GM drops by $20\log2=6$ dB.

Answer: **(c)**""",
[r"Gain changes shift the Bode magnitude plot up or down and leave the phase plot alone.",
 r"PM *does* change with gain, because $\omega_{gc}$ moves."]),

"5.30": ("C", r"Frequency-domain ↔ time-domain: BW ↔ speed; PM ↔ $\xi$ (damping); $M_r$ ↔ overshoot; GM ↔ stability.",
r"""- **A. Bandwidth** → speed of the time response, since $t_r\propto1/BW$ (3)
- **B. Phase margin** → damping ratio, since $PM\approx100\xi$ (4)
- **C. Response (resonance) peak** → overshoot, since both increase as $\xi$ falls (1)
- **D. Gain margin** → stability, i.e. how much gain increase is tolerated (2)

A–3, B–4, C–1, D–2. Answer: **(c)**""",
[r"PM relates to damping and GM relates to stability. Options swapping these two are the main trap.",
 r"Both PM and $M_r$ are linked to $\xi$. Pick the closest pairing: $M_r$ ↔ overshoot, PM ↔ damping."]),

"5.31": ("C", r"Resonance peak $M_r=\dfrac{1}{2\xi\sqrt{1-\xi^2}}$ for $\xi<0.707$.",
r"""**Step 1.** $\xi=0.421$, $\xi^2=0.177$, $\sqrt{1-0.177}=\sqrt{0.823}=0.907$.

**Step 2.**
$$M_r=\dfrac{1}{2\times0.421\times0.907}=\dfrac{1}{0.764}=1.31\approx1.30$$

Answer: **(c)**""",
[r"$M_r\ge1$ always. Options below 1, (a) and (b), can be rejected immediately for $\xi<0.707$.",
 r"$M_r=1.3$ is a typical design value (corresponds to about 25% overshoot)."]),

"5.32": ("D", r"Minimum phase: all poles **and zeros** in the LHP. Then the magnitude response uniquely determines the phase (Bode gain-phase relation).",
r"""**1.** All poles must be in the LHP. True.

**2.** For a minimum-phase system the zeros must *also* be in the LHP. An RHP zero makes the system non-minimum phase. False.

**3.** For a minimum-phase system, the phase is uniquely determined by the magnitude characteristic over all frequencies. True.

Correct: 1 and 3. Answer: **(d)**""",
[r"Non-minimum-phase systems with the same magnitude response can have different phase responses. That is why statement 3 needs minimum phase."]),

"5.33": ("A", r"Asymptotic Bode errors: a real pole or zero is off by 3 dB at its corner. For a complex pair, the phase at $\omega_n$ is exactly $\mp90^\circ$ for every $\xi$.",
r"""**1.** For a real zero $(1+s/\omega_c)$, the exact magnitude at $\omega=\omega_c$ is $20\log\sqrt2=+3$ dB, while the asymptote gives 0 dB. The deviation is 3 dB. True.

**2.** For a complex pole pair, $\angle=-\tan^{-1}\dfrac{2\xi u}{1-u^2}$ with $u=\omega/\omega_n$. At $u=1$ the denominator is 0, so the angle is $-90^\circ$ **whatever $\xi$ is**. Only the steepness of the phase transition depends on $\xi$. False.

Only 1. Answer: **(a)**""",
[r"For a complex pair, the *magnitude* error at $\omega_n$ depends on $\xi$ (it equals $-20\log2\xi$). The *phase* at $\omega_n$ does not.",
 r"Corner deviation: 3 dB for first order, $20\log(1/2\xi)$ for second order."]),

"5.34": ("A", r"$GM=\dfrac{1}{|G(j\omega_{pc})|}$, with $\omega_{pc}$ from $\angle G=-180^\circ$.",
r"""**Step 1 – Phase crossover.** Write $G=\dfrac{2}{s(1+s)(1+2s)}$.
$$-90^\circ-\tan^{-1}\omega-\tan^{-1}2\omega=-180^\circ\ \Rightarrow\ \omega\cdot2\omega=1\ \Rightarrow\ \omega_{pc}=\dfrac{1}{\sqrt2}$$

**Step 2 – Magnitude there.**
$$|G|=\dfrac{2}{\omega\sqrt{1+\omega^2}\sqrt{1+4\omega^2}}=\dfrac{2}{0.707\times1.225\times1.732}=\dfrac{2}{1.5}=\dfrac43$$
(Formula check: $\dfrac{KT_1T_2}{T_1+T_2}=\dfrac{2\times1\times2}{3}=\dfrac43$ ✓)

**Step 3 – Gain margin.**
$$GM=\dfrac{1}{4/3}=\dfrac34\quad(\approx-2.5\ \text{dB})$$
GM $<1$ means the closed loop is **unstable**. Routh on $2s^3+3s^2+s+2$: $3\times1<2\times2$ confirms it.

Answer: **(a)**""",
[r"Option (b), 4/3, is $|G(j\omega_{pc})|$ itself. Take the reciprocal for the GM.",
 r"Rewrite in time-constant form first: $(s+1)(2s+1)$ means $T_1=1$, $T_2=2$."]),

"5.35": ("C", r"An oscillator is a marginally stable system: find $K$ that makes a Routh row zero, and $\omega$ from the auxiliary equation.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 3 & K\\ s^3 & 2 & 2 & \\ s^2 & 2 & K & \\ s^1 & 2-K & & \\ s^0 & K & & \end{array}$$
($s^2$: $\frac{2\cdot3-1\cdot2}{2}=2$; $s^1$: $\frac{2\cdot2-2K}{2}=2-K$.)

**Step 2 – Sustained oscillation.** $s^1$ row zero: $K=2$.

**Step 3 – Frequency.** Auxiliary equation from the $s^2$ row:
$$2s^2+2=0\ \Rightarrow\ s=\pm j1\ \Rightarrow\ \omega=1\ \text{rad/s}$$

Answer: **(c)**""",
[r"Find $K$ first, then substitute it into the auxiliary equation. Using the wrong row gives the wrong $\omega$.",
 r"At $K=2$: $s^4+2s^3+3s^2+2s+2=(s^2+1)(s^2+2s+2)$, which confirms $\pm j1$."]),
}
