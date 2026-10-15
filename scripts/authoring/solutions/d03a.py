# Detailed solutions, chapter 3 (stability: Routh-Hurwitz), 3.21-3.46.
# number -> (answer, concept, solution, [points to take care of])
D = {
"3.21": ("D", r"Routh array: marginal stability occurs when a full row (here the $s^1$ row) becomes zero. The auxiliary equation from the row above then gives the $j\omega$-axis roots.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 4 & K\\ s^3 & 4 & 3 & \\ s^2 & \frac{13}{4} & K & \\ s^1 & \frac{\frac{39}{4}-4K}{13/4} & & \\ s^0 & K & & \end{array}$$
where $s^2$: $\dfrac{4\cdot4-1\cdot3}{4}=\dfrac{13}{4}$, and $s^1$: $\dfrac{\frac{13}{4}\cdot3-4K}{13/4}$.

**Step 2 – Stability conditions.** $K>0$ and $\dfrac{39}{4}-4K>0\Rightarrow K<\dfrac{39}{16}$.

**Step 3 – Marginal stability.** The $s^1$ row is zero when
$$K=\dfrac{39}{16}$$
Then the auxiliary equation $\frac{13}{4}s^2+\frac{39}{16}=0$ gives $s=\pm j\dfrac{\sqrt3}{2}$, a sustained oscillation at $\omega\approx0.866$ rad/s.

Answer: **(d)**""",
[r"Marginal stability = the upper limit of the stable range of $K$, where the $s^1$ row vanishes.",
 r"Compute $s^2$ carefully: $\dfrac{(4)(4)-(1)(3)}{4}$. A slip here changes the answer completely, since all the options have denominator 16.",
 r"The frequency of oscillation comes from the auxiliary equation formed from the row *above* the zero row."]),

"3.22": ("B", r"Characteristic equation $1+G(s)H(s)=0$, with $G$ the full forward path and $H$ the feedback element.",
r"""**Step 1 – Loop transfer function.**
$$G(s)=4\cdot\dfrac{3}{s+1}=\dfrac{12}{s+1},\qquad H(s)=\dfrac{10}{s+10}$$
$$G(s)H(s)=\dfrac{120}{(s+1)(s+10)}$$

**Step 2 – Characteristic equation.**
$$(s+1)(s+10)+120=0\ \Rightarrow\ s^2+11s+10+120=0$$
$$s^2+11s+130=0$$

Answer: **(b)**""",
[r"Include the feedback gain: $H(0)=1$, but the $10$ in its numerator multiplies the loop gain to 120.",
 r"Option (a) is the open-loop denominator alone, i.e. with the '+120' forgotten."]),

"3.23": ("D", r"Routh array: the system is stable only if all first-column entries are positive. Find the range of $K$ and test each option.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 24 & K\\ s^3 & 8 & 32 & \\ s^2 & 20 & K & \\ s^1 & 32-0.4K & & \\ s^0 & K & & \end{array}$$
($s^2$: $\frac{8\cdot24-32}{8}=20$; $s^1$: $\frac{20\cdot32-8K}{20}=32-0.4K$.)

**Step 2 – Stability range.** $K>0$ and $32-0.4K>0\Rightarrow K<80$, so it is stable for $0<K<80$.

**Step 3 – Check the options.** $10, 20, 60$ are all inside the range (stable). $K=100>80$ makes the $s^1$ entry $-8$: two sign changes, unstable.

Answer: **(d)**""",
[r"Find the full stable range once, then test the options. This is faster than checking each option separately.",
 r"$s^4+8s^3+24s^2+32s+16=(s+2)^4$, which is why the coefficients look 'binomial'. At $K=80$ the roots touch the $j\omega$ axis at $\omega=\sqrt{80/20}=2$ rad/s."]),

"3.24": ("A", r"A zero row in the Routh array means roots symmetric about the origin. Here they are a purely imaginary pair, i.e. zero damping.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 6\\ s^2 & 2 & 12\\ s^1 & 0 & \end{array}$$
($s^1$: $\frac{2\cdot6-1\cdot12}{2}=0$, a complete zero row.)

**Step 2 – Auxiliary equation** (from the $s^2$ row):
$$2s^2+12=0\ \Rightarrow\ s=\pm j\sqrt6$$

**Step 3 – Factorise.** $s^3+2s^2+6s+12=(s+2)(s^2+6)$

The oscillatory pair $s^2+6$ has no $s$ term, so $\delta=0$ (undamped, sustained oscillation at $\sqrt6$ rad/s).

Answer: **(a)**""",
[r"Try grouping first: $s^2(s+2)+6(s+2)$ factorises immediately when coefficient pairs are in the same ratio (1:2 and 6:12).",
 r"Zero damping means a marginally stable system: sustained oscillation, not instability."]),

"3.25": ("B", r"For $s^3+a_2s^2+a_1s+a_0$, the Routh conditions are all coefficients $>0$ and $a_2a_1>a_0$.",
r"""**Step 1 – Characteristic equation.**
$$s(s+1)(s+2)+K=0\ \Rightarrow\ s^3+3s^2+2s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 2\\ s^2 & 3 & K\\ s^1 & \frac{6-K}{3} & \\ s^0 & K & \end{array}$$

**Step 3 – Conditions.** $K>0$ and $6-K>0$, so $0<K<6$.

At $K=6$: $3s^2+6=0\Rightarrow\omega=\sqrt2$ rad/s.

Answer: **(b)**""",
[r"Third-order shortcut: stable if and only if $a_2a_1>a_3a_0$ (here $3\times2>1\times K$).",
 r"Expand $s(s+1)(s+2)=s^3+3s^2+2s$ carefully. A wrong middle coefficient gives the distractor $K<3$."]),

"3.26": ("C", r"Gain margin = factor by which the gain can be raised before instability: $GM=\dfrac{K_{crit}}{K}$, or in dB $20\log_{10}\dfrac{K_{crit}}{K}$.",
r"""$$GM=\dfrac{K_{crit}}{K_{op}}=\dfrac{40}{20}=2$$
$$GM_{dB}=20\log_{10}2=20\times0.301=6.02\ \text{dB}\approx6\ \text{dB}$$

Answer: **(c)**""",
[r"Use $20\log$ for gain ratios, not $10\log$ (which would give 3 dB, option (b)).",
 r"Remember: a factor of 2 is 6 dB and a factor of 10 is 20 dB."]),

"3.27": ("D", r"Routh array with a parameter: write each first-column entry as a function of $K$ and check whether they can all be positive at once.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 5 & 15\\ s^3 & 20K & 10 & \\ s^2 & b & 15 & \\ s^1 & 10-\frac{300K}{b} & & \\ s^0 & 15 & & \end{array}\qquad b=\dfrac{100K-10}{20K}=5-\dfrac{0.5}{K}$$

**Step 2 – Conditions.**
- $20K>0\Rightarrow K>0$
- $b>0\Rightarrow K>0.1$
- $s^1>0\Rightarrow10b>300K\Rightarrow50-\dfrac5K>300K\Rightarrow300K^2-50K+5<0$

**Step 3 – Test the quadratic.** Discriminant $=2500-4(300)(5)=2500-6000<0$, so $300K^2-50K+5$ is *always positive*. The $s^1$ condition can never be met.

For $K<0$ the $s^3$ entry is negative anyway. So the system is unstable for every $K$.

Answer: **(d)**""",
[r"When a condition reduces to a quadratic inequality, check the discriminant. A negative discriminant means the quadratic never changes sign.",
 r"All coefficients being positive is necessary but not sufficient. This question is the classic example.",
 r"Multiply inequalities by $K$ only after establishing $K>0$, or the inequality direction may flip."]),

"3.28": ("C", r"Third-order Routh conditions for $s^3+a_2s^2+a_1s+a_0$: all $a_i>0$ and $a_2a_1>a_0$.",
r"""**Step 1 – Write the coefficients.** $s^3+4s^2+1\cdot s+(K-6)=0$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 1\\ s^2 & 4 & K-6\\ s^1 & \frac{4-(K-6)}{4} & \\ s^0 & K-6 & \end{array}$$

**Step 3 – Conditions.**
- $s^0$: $K-6>0\Rightarrow K>6$
- $s^1$: $4-(K-6)>0\Rightarrow K<10$

Stable for $6<K<10$.

Answer: **(c)**""",
[r"The constant term is $K-6$, not $K$. Forgetting the $-6$ gives $0<K<4$-type answers.",
 r"At $K=10$, $4s^2+4=0$ gives oscillation at 1 rad/s. At $K=6$, there is a root at the origin."]),

"3.29": ("C", r"Sustained oscillation = marginal stability. Find the $K$ that makes the $s^1$ row zero, and the frequency from the auxiliary equation.",
r"""**Step 1 – Characteristic equation.**
$$s(s+1)(s+5)+K=s^3+6s^2+5s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 5\\ s^2 & 6 & K\\ s^1 & \frac{30-K}{6} & \\ s^0 & K & \end{array}$$

**Step 3 – Marginal value.** The $s^1$ row is zero when $K=30$.

**Step 4 – Frequency.** $6s^2+30=0\Rightarrow s=\pm j\sqrt5$, so the oscillation is at $\sqrt5=2.24$ rad/s.

Answer: **(c)**""",
[r"$K_{mar}=a_2a_1$ for $s^3+a_2s^2+a_1s+K$: here $6\times5=30$.",
 r"Questions often ask for the frequency of oscillation as well: $\omega=\sqrt{a_1}=\sqrt5$ rad/s here."]),

"3.30": ("C", r"Routh criterion: the number of sign changes in the first column equals the number of RHP roots.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 2 & 3 & 7\\ s^3 & 1 & 5 & \\ s^2 & -7 & 7 & \\ s^1 & 6 & & \\ s^0 & 7 & & \end{array}$$
- $s^2$: $\frac{1\cdot3-2\cdot5}{1}=-7$ and $\frac{1\cdot7-2\cdot0}{1}=7$
- $s^1$: $\frac{(-7)(5)-(1)(7)}{-7}=\frac{-42}{-7}=6$

**Step 2 – Count sign changes.** First column: $2,\ 1,\ -7,\ 6,\ 7$. That is $+\to-$ (1) and $-\to+$ (2): two sign changes.

Two roots in the RHP.

Answer: **(c)**""",
[r"All coefficients positive does *not* guarantee stability for order $\ge3$. Always build the array.",
 r"Divide by the pivot carefully, keeping its sign. The $s^1$ entry here has a negative divisor."]),

"3.31": ("A", r"For a stable minimum-phase feedback system, both gain margin and phase margin are positive.",
r"""The phase margin is $PM=180^\circ+\angle G(j\omega_{gc})H(j\omega_{gc})$.
- Positive PM: the Nyquist plot passes to the right of $-1$, so the closed loop is stable.
- Negative PM: the Nyquist plot encircles $-1$, so it is unstable.

For the usual (minimum-phase, open-loop stable) systems, a stable feedback system always has a positive phase margin.

Answer: **(a)**""",
[r"The rule 'positive margins ⇔ stable' holds for minimum-phase, open-loop-stable systems. For open-loop unstable or conditionally stable systems, use the full Nyquist criterion.",
 r"A PM of 30° to 60° is the usual design target."]),

"3.32": ("A", r"Negative feedback reduces sensitivity to parameter variations and disturbances by $1+GH$, and when properly designed it can stabilise and improve the response.",
r"""- **Stability:** feedback moves the closed-loop poles. With a suitable gain, negative feedback can stabilise an unstable plant or improve damping. (Too much gain can also destabilise; 'improves' refers to proper design.)
- **Sensitivity:** $S=\dfrac{1}{1+GH}$, so the response is less sensitive to parameter variations and external disturbances.

Option (a) states both effects correctly. (b) and (c) wrongly say feedback does not affect stability, and (d) says it increases sensitivity.

Answer: **(a)**""",
[r"Feedback always *affects* stability, for better or worse. Any option claiming 'does not affect stability' is wrong.",
 r"Disturbances in the forward path are reduced by $1+GH$. Sensor noise is not reduced."]),

"3.33": ("C", r"Type = number of poles at the origin. Order = degree of the denominator (total number of poles).",
r"""$$G(s)=\dfrac{K}{s^2(1+sT)}$$
- Poles at the origin: $s^2$, so **type 2**.
- Denominator degree: $s^2\times s=s^3$, so **order 3**.

Type 2, order 3. Answer: **(c)**""",
[r"Type ≤ order always. Option (a) (type 5, order 2) is impossible.",
 r"Order counts all poles, type counts only those at $s=0$."]),

"3.34": ("A", r"A zero row in the Routh array gives an auxiliary equation whose roots are the $j\omega$-axis roots. The oscillation frequency is the (positive) magnitude $\omega$.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|cccc} s^6 & 1 & 3 & 3 & 1\\ s^5 & 2 & 4 & 2 & \\ s^4 & 1 & 2 & 1 & \\ s^3 & 0 & 0 & & \end{array}$$
($s^4$: $\frac{2\cdot3-4}{2}=1$, $\frac{2\cdot3-2}{2}=2$, $\frac{2\cdot1}{2}=1$; $s^3$: $\frac{1\cdot4-2\cdot2}{1}=0$, $\frac{1\cdot2-2\cdot1}{1}=0$, a zero row.)

**Step 2 – Auxiliary equation** (from the $s^4$ row):
$$s^4+2s^2+1=(s^2+1)^2=0\ \Rightarrow\ s=\pm j1\ (\text{each twice})$$

**Step 3 – Frequency.** The roots on the $j\omega$ axis are at $\omega=1$, so the oscillation frequency is **1 rad/s**.

Answer: **(a)** (derived; the source has no printed key for this question)""",
[r"A frequency is a real positive number. $\pm j1$ are the *roots*, not the frequency. That is why (c) and (d) are traps and (b) is meaningless.",
 r"Here the $j\omega$-axis roots are *repeated*, so the system is actually unstable (response grows like $t\sin t$), even though the oscillation frequency is 1 rad/s.",
 r"Continue the array by differentiating the auxiliary equation ($4s^3+4s$) to check the remaining roots."]),

"3.35": ("D", r"Routh array with a parameter: check whether all first-column entries can be positive simultaneously.",
r"""This is the same characteristic equation as question 3.27.

**Step 1 – First column.**
$$20K,\quad b=5-\dfrac{0.5}{K},\quad 10-\dfrac{300K}{b},\quad 15$$

**Step 2 – Conditions.** $K>0.1$ is needed for $b>0$. Then the $s^1$ entry $>0$ requires
$$300K^2-50K+5<0$$
Discriminant $2500-6000<0$, so this quadratic is always positive and the condition is never satisfied.

Unstable for every value of $K$.

Answer: **(d)**""",
[r"A repeated question with different option wording. Option (c) here says $7<K<\infty$, which is different from 3.27's (c). Always read the options again.",
 r"Large $K$ makes the $s^1$ entry about $10-60K<0$. Small $K$ makes $b<0$. Neither end works."]),

"3.36": ("C", r"Routh conditions for a fourth-order polynomial with a parameter in the constant term.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 13 & K\\ s^3 & 4 & 36 & \\ s^2 & 4 & K & \\ s^1 & 36-K & & \\ s^0 & K & & \end{array}$$
($s^2$: $\frac{4\cdot13-36}{4}=4$; $s^1$: $\frac{4\cdot36-4K}{4}=36-K$.)

**Step 2 – Conditions.** $K>0$ and $36-K>0$, so $0<K<36$.

At $K=36$: $4s^2+36=0$ gives oscillation at 3 rad/s.

Answer: **(c)**""",
[r"The $s^0$ entry is always the constant term. It gives the lower bound $K>0$.",
 r"Do not confuse the coefficient $13$ with a bound. Option (d) is a distractor built from the coefficients."]),

"3.37": ("B", r"Build the characteristic equation from the open-loop poles and zeros. For a quadratic, the signs of the coefficients decide the root locations.",
r"""**Step 1 – Open-loop function.**
$$G(s)=\dfrac{K(s+1)(s+2)}{(s+0.1)(s-1)}$$

**Step 2 – Characteristic equation.**
$$(s^2-0.9s-0.1)+K(s^2+3s+2)=0$$
$$(1+K)s^2+(3K-0.9)s+(2K-0.1)=0$$

**Step 3 – Sign analysis** (for $K>0$, so $1+K>0$):
- $K<0.05$: constant $<0$, so the product of the roots is negative. One positive and one negative real root: **one RHP pole**.
- $0.05<K<0.3$: constant $>0$ but middle $<0$. Both roots have positive real parts: two RHP poles.
- $K>0.3$: all coefficients $>0$, both roots in the LHP: stable.

One RHP pole for $K<0.05$.

Answer: **(b)**""",
[r"For a quadratic, Routh reduces to the signs of the coefficients. The number of sign changes in $(1+K),(3K-0.9),(2K-0.1)$ gives the number of RHP roots.",
 r"The open-loop pole at $s=+1$ makes the plant unstable. A sufficiently large gain stabilises it ($K>0.3$).",
 r"Question asks for *exactly one* RHP pole. Do not choose the range with two RHP poles."]),

"3.38": ("D", r"Third-order Routh test: all coefficients positive and $a_2a_1>a_3a_0$.",
r"""**Step 1 – Characteristic equation.**
$$s(s+2)(s+K)+10=s^3+(2+K)s^2+2Ks+10=0$$

**Step 2 – Conditions.**
- $2+K>0$ and $2K>0\Rightarrow K>0$
- $(2+K)(2K)>10\Rightarrow2K^2+4K-10>0\Rightarrow K^2+2K-5>0$

**Step 3 – Solve the quadratic.** Roots $K=-1\pm\sqrt6$. With $K>0$:
$$K>-1+\sqrt6=1.449$$

Stable for $K>1.45$.

Answer: **(d)**""",
[r"Expand $(s+2)(s+K)=s^2+(2+K)s+2K$ before multiplying by $s$.",
 r"Take only the positive root of the quadratic, since $K>0$ is already required."]),

"3.39": ("C", r"Open-loop stability depends on the open-loop poles. Closed-loop stability depends on the roots of $1+G=0$.",
r"""**1. Open loop.** $G(s)=\dfrac{K(s+1)}{s^2(s+2)}$ has a **double pole at the origin**. Its impulse response contains a term proportional to $t$, which grows without bound. Unstable.

**2. Closed loop.**
$$s^2(s+2)+K(s+1)=s^3+2s^2+Ks+K=0$$
$$\begin{array}{c|cc} s^3 & 1 & K\\ s^2 & 2 & K\\ s^1 & \frac{2K-K}{2}=\frac K2 & \\ s^0 & K & \end{array}$$
For $K>0$ all entries are positive, so it is stable.

1 is unstable and 2 is stable. Answer: **(c)**""",
[r"Repeated poles on the $j\omega$ axis (including the origin) mean instability, not marginal stability.",
 r"Feedback can stabilise an unstable open-loop system. Here the zero at $-1$ pulls the locus into the LHP."]),

"3.40": ("B", r"Routh conditions for a fourth-order polynomial with $K$ in the constant term.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|ccc} s^4 & 1 & 15 & K\\ s^3 & 20 & 2 & \\ s^2 & 14.9 & K & \\ s^1 & 2-\frac{20K}{14.9} & & \\ s^0 & K & & \end{array}$$
($s^2$: $\frac{20\cdot15-1\cdot2}{20}=\frac{298}{20}=14.9$.)

**Step 2 – Conditions.**
- $K>0$
- $2-\dfrac{20K}{14.9}>0\Rightarrow K<\dfrac{29.8}{20}=1.49$

Stable for $0<K<1.49$.

Answer: **(b)**""",
[r"The $s^2$ entry is $14.9$, not $15$. Using $15$ gives $K<1.5$, close enough here, but in other questions it matters.",
 r"The lower limit is always $K>0$ from the $s^0$ row, unless the constant term contains other terms."]),

"3.41": ("A", r"Stability (asymptotic and BIBO for LTI systems): all characteristic roots have negative real parts.",
r"""If every root of the characteristic equation is in the left half-plane, every natural-response term $e^{p_it}$ decays to zero. The system is **stable**.

- Marginally stable: simple (non-repeated) roots on the $j\omega$ axis, all others in the LHP.
- Unstable: any RHP root, or repeated $j\omega$-axis roots.
- Conditionally stable: stable only for a range of gain.

Answer: **(a)**""",
[r"Strictly negative real parts are needed. Zero real part means marginally stable at best."]),

"3.42": ("D", r"Instability: any RHP root, or repeated roots on the $j\omega$ axis.",
r"""- A root with positive real part gives a growing term $e^{\sigma t}$, $\sigma>0$.
- A repeated root on the $j\omega$ axis gives terms like $t\sin\omega t$ (or $t$ for a double root at the origin), which grow without bound.

In both cases the response is unbounded, so the system is **unstable**.

Answer: **(d)**""",
[r"*Simple* $j\omega$-axis roots mean marginally (limitedly) stable. *Repeated* ones mean unstable. The difference is the key point.",
 r"'Conditionally stable' describes systems that are stable only for a range of gain. It is not related to root multiplicity."]),

"3.43": ("C", r"Form the characteristic equation carefully when the loop has an RHP zero $(1-s)$, then apply Routh.",
r"""**Step 1 – Characteristic equation.**
$$s(s^2+5s+9)+K(1-s)=0\ \Rightarrow\ s^3+5s^2+(9-K)s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 9-K\\ s^2 & 5 & K\\ s^1 & \frac{5(9-K)-K}{5} & \\ s^0 & K & \end{array}$$

**Step 3 – Conditions.**
- $K>0$
- $45-5K-K>0\Rightarrow6K<45\Rightarrow K<7.5$

The maximum $K$ for stability is $7.5$.

Answer: **(c)**""",
[r"The RHP zero gives $-Ks$, which *reduces* the $s$ coefficient to $9-K$. Getting this sign wrong ($9+K$) gives the wrong limit.",
 r"Non-minimum-phase zeros limit the achievable gain. That is why the limit is fairly low."]),

"3.44": ("D", r"Form the characteristic equation carefully when the loop has an RHP zero $(1-s)$, then apply Routh.",
r"""This is the same system as question 3.43.

**Step 1 – Characteristic equation.**
$$s^3+5s^2+(9-K)s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 9-K\\ s^2 & 5 & K\\ s^1 & \frac{45-6K}{5} & \\ s^0 & K & \end{array}$$

**Step 3 – Conditions.** $K>0$ and $45-6K>0\Rightarrow K<7.5$

The maximum $K$ is $7.5$.

Answer: **(d)**""",
[r"Repeated question (ESE 2021 and 2024) with the answer in a different option position. Match the value, not the letter.",
 r"At $K=7.5$: $5s^2+7.5=0$ gives oscillation at $\sqrt{1.5}=1.22$ rad/s."]),

"3.45": ("D", r"Routh array for a sixth-order polynomial. The number of sign changes in the first column = number of RHP poles.",
r"""**Step 1 – Routh array.**
$$\begin{array}{c|cccc} s^6 & 5 & 12 & 100 & 200\\ s^5 & 8 & 20 & 150 & \\ s^4 & -0.5 & 6.25 & 200 & \\ s^3 & 120 & 3350 & & \\ s^2 & 20.2 & 200 & & \\ s^1 & 2162 & & & \\ s^0 & 200 & & & \end{array}$$
Working:
- $s^4$: $\frac{8\cdot12-5\cdot20}{8}=-0.5$, $\frac{8\cdot100-5\cdot150}{8}=6.25$, $\frac{8\cdot200}{8}=200$
- $s^3$: $\frac{(-0.5)(20)-8(6.25)}{-0.5}=120$, $\frac{(-0.5)(150)-8(200)}{-0.5}=3350$
- $s^2$: $\frac{120(6.25)-(-0.5)(3350)}{120}=20.2$, $200$
- $s^1$: $\frac{20.2(3350)-120(200)}{20.2}\approx2162$

**Step 2 – Sign changes.** $5,\ 8,\ -0.5,\ 120,\ 20.2,\ 2162,\ 200$ gives $+\to-$ and $-\to+$: two changes.

Two poles in the RHP, so the system is unstable.

Answer: **(d)**""",
[r"You only need the *signs*. Once you see $-0.5$ followed by positive entries, you already have two sign changes, provided no further negatives appear.",
 r"'A stable system having a pole in the RHP' (options (a) and (c)) is self-contradictory. Eliminate those first.",
 r"RHP poles come in pairs here (complex conjugates), which is consistent with an even count of 2."]),

"3.46": ("C", r"For $s^3+a_2s^2+a_1s+K$: stable when $0<K<a_2a_1$.",
r"""**Step 1 – Characteristic equation.**
$$s(s+1)(s+2)+K=s^3+3s^2+2s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 2\\ s^2 & 3 & K\\ s^1 & \frac{6-K}{3} & \\ s^0 & K & \end{array}$$

**Step 3 – Range.** $K>0$ and $K<6$, so $0<K<6$.

Answer: **(c)**""",
[r"Same system as 3.25 (ESE 2012 and 2024). It is a very frequently repeated question.",
 r"At $K=6$ the system oscillates at $\omega=\sqrt2$ rad/s."]),
}
