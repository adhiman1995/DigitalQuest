# Detailed solutions, chapter 4 (root locus), 4.1-4.24.
# number -> (answer, concept, solution, [points to take care of])
D = {
"4.1": ("D", r"Centroid of the asymptotes: $\sigma_A=\dfrac{\sum\text{(finite poles)}-\sum\text{(finite zeros)}}{P-Z}$.",
r"""**Step 1 – Poles and zeros.** Poles at $0,\,-1,\,-3$ ($P=3$). No finite zeros ($Z=0$).

**Step 2 – Centroid.**
$$\sigma_A=\dfrac{(0-1-3)-0}{3-0}=\dfrac{-4}{3}=-1.33$$

(The asymptote angles are $60^\circ$, $180^\circ$, $300^\circ$.)

Answer: **(d)**""",
[r"Use the pole *locations* (with sign), e.g. $-1$ and $-3$, not the factor constants $+1$ and $+3$. That sign error gives $+1.33$, option (b).",
 r"The centroid is always real, since poles and zeros come in conjugate pairs."]),

"4.2": ("B", r"Breakaway/break-in points are the roots of $\dfrac{dK}{ds}=0$ that give a real positive $K$ on the locus.",
r"""**Step 1 – Write $K$ as a function of $s$.**
$$K=-s(s+4)(s^2+4s+5)$$
Let $u=s^2+4s$. Then $s(s+4)=u$ and $s^2+4s+5=u+5$, so $K=-u(u+5)$.

**Step 2 – Differentiate.**
$$\dfrac{dK}{ds}=-(2u+5)\dfrac{du}{ds}=-(2u+5)(2s+4)=0$$

**Step 3 – Candidate points.**
- $2s+4=0\Rightarrow s=-2$, with $K=-(-4)(1)=4>0$ ✓
- $2u+5=0\Rightarrow s^2+4s+2.5=0\Rightarrow s=-2\pm1.225=-0.775,\,-3.225$, with $K=-(-2.5)(2.5)=6.25>0$ ✓

**Step 4 – Check they are on the locus.** All three lie on the real-axis segment between $0$ and $-4$, which is part of the locus (one pole to the right). So there are three real breakaway points.

(At $K=4$ the complex branches from $-2\pm j1$ meet on the axis at $-2$. At $K=6.25$ branches meet at $-0.775$ and $-3.225$ and break away again.)

Answer: **(b)**""",
[r"A root of $dK/ds=0$ is a valid breakaway point only if it lies on the locus and gives a real positive $K$.",
 r"Symmetric pole patterns (here symmetric about $s=-2$) are much easier with a substitution like $u=s^2+4s$.",
 r"Breakaway points need not be only between two real poles. Here one comes from complex poles meeting on the axis."]),

"4.3": ("C", r"The number of zeros at infinity equals $P-Z$, the number of branches that go to infinity.",
r"""**Step 1 – Count.**
- Poles: $s=0,\ -2,\ -1\pm j1$ (from $s^2+2s+2$), so $P=4$.
- Finite zeros: $s=-1$, so $Z=1$.

**Step 2 – Zeros at infinity.** $P-Z=4-1=3$.

As $s\to\infty$, $G(s)H(s)\approx\dfrac{K}{s^3}\to0$, a zero of order 3 at infinity.

Answer: **(c)**""",
[r"Total poles = total zeros (finite + at infinity). This is always true for a rational function.",
 r"Remember to count both complex poles from the quadratic."]),

"4.4": ("D", r"Read the open-loop poles from where the branches start ($K=0$) and check the asymptotes against $P-Z$.",
r"""**Step 1 – Starting points.** Three branches ($r_1,r_2,r_3$) start from only two points: the origin (two branches, $r_1$ and $r_2$) and a real point on the negative axis ($r_3$). So there is a **double pole at the origin** and a single pole at $s=-1/T_1$.

**Step 2 – Asymptotes.** No finite zeros, so $P-Z=3$ and the asymptotes are at $\pm60^\circ$ and $180^\circ$. Branch $r_3$ runs left to $-\infty$, and $r_1,r_2$ curve into the RHP along $\pm60^\circ$. ✓

**Step 3 – Transfer function.**
$$G(s)H(s)=\dfrac{K}{s^2(sT_1+1)}$$

(This system is unstable for every $K>0$, since the branches from the origin go straight into the RHP.)

Answer: **(d)**""",
[r"Two branches leaving the same point means a double pole there.",
 r"A double pole at the origin with a pole to its left gives a locus that is unstable for all $K$. A zero is needed to pull it back."]),

"4.5": ("B", r"The Spirule is a mechanical aid (protractor plus arm) for adding angles and multiplying lengths when sketching a root locus by hand.",
r"""Before computers, root loci were sketched by hand using a **Spirule**, invented by W. R. Evans, who also developed the root locus method. It lets you add up the angles from the poles and zeros to a test point (to check the $\pm180^\circ$ angle condition) and multiply the vector lengths (to find $K$).

- A slide rule is a general calculation aid.
- Synchro and Selsyn are electromechanical position-sensing devices.

Answer: **(b)**""",
[r"Evans → root locus → Spirule. These three facts are linked.",
 r"Synchro and Selsyn are the same device (a synchro transmitter/receiver) and are not plotting tools."]),

"4.6": ("C", r"Real-axis rule: a point on the real axis is on the locus if the total number of real poles and zeros to its right is odd.",
r"""Poles at $0,\ -3,\ -4$ and a zero at $-1$. Count the poles and zeros to the right of each segment:

- $(-1,\,0)$: 1 (pole at 0), odd → **on the locus**
- $(-3,\,-1)$: 2, even → not on the locus
- $(-4,\,-3)$: 3, odd → **on the locus**
- $(-\infty,\,-4)$: 4, even → not on the locus

Of the options, only 'between $-3$ and $-4$' is a locus segment.

Answer: **(c)**""",
[r"Count only the *real* poles and zeros. Complex pairs contribute equal and opposite angles and do not affect the real-axis rule.",
 r"Option (b), 0 to $-4$, is only *partly* on the locus. The question needs a whole segment."]),

"4.7": ("D", r"For two poles and one zero (all real), the complex part of the locus is a circle centred on the zero with radius $\sqrt{|z-p_1||z-p_2|}$.",
r"""**Step 1 – Read the figure.** Branches start at $0$ and $-1$ (open-loop poles), move towards each other, and leave the real axis. They follow a circle centred at $-2$ of radius $\sqrt2$, and return to the axis to the left of $-2$.

**Step 2 – Identify the zero.** A circular locus centred at $-2$ means a zero at $s=-2$.

**Step 3 – Check the radius.**
$$r=\sqrt{|{-2}-0|\cdot|{-2}-(-1)|}=\sqrt{2\times1}=\sqrt2\ \checkmark$$

**Step 4 – Transfer function.**
$$G(s)=\dfrac{K(s+2)}{s(s+1)}$$

Answer: **(d)**""",
[r"Breakaway and break-in points are at $z\pm r$: here $-2+\sqrt2=-0.586$ (breakaway) and $-2-\sqrt2=-3.414$ (break-in).",
 r"Option (c) puts the zero between the poles. The locus would then stay on the real axis and no circle would form."]),

"4.8": ("B", r"MATLAB's Control System Toolbox (`rlocus`) computes and plots root loci accurately.",
r"""MATLAB is numerical-computation software. Its `rlocus(sys)` command computes the closed-loop roots for many values of $K$ and plots the exact root locus.

- LISP is a programming language used mainly in AI.
- dBase and Oracle are database systems.

Answer: **(b)**""",
[r"Related MATLAB commands: `bode`, `nyquist`, `step`, `rlocus`, `margin`."]),

"4.9": ("B", r"The $j\omega$-axis crossing is found from the Routh array: the marginal $K$ makes the $s^1$ row zero, and the auxiliary equation gives $\omega$.",
r"""Where the root locus crosses the imaginary axis, the closed loop is marginally stable. Using the **Routh–Hurwitz criterion**:
1. Find the $K$ that makes a row (usually $s^1$) of the Routh array zero. That is the crossing gain $K_{mar}$.
2. Form the auxiliary equation from the row above with $K=K_{mar}$. Its roots $\pm j\omega$ give the crossing point.

Alternatively, substitute $s=j\omega$ into the characteristic equation and set the real and imaginary parts to zero.

Answer: **(b)**""",
[r"Routh gives the exact crossing gain and frequency. Bode and Nyquist give the same information, but from frequency plots.",
 r"The crossing frequency from Routh equals the phase-crossover frequency $\omega_{pc}$ in the Bode plot."]),

"4.10": ("B", r"Asymptote angles: $\theta_k=\dfrac{(2k+1)\,180^\circ}{P-Z}$, $k=0,1,\dots,P-Z-1$.",
r"""For large $|s|$, $G(s)H(s)\approx\dfrac{K}{s^{P-Z}}$. The angle condition $\angle GH=(2k+1)\pi$ becomes
$$-(P-Z)\theta=(2k+1)\pi\ \Rightarrow\ \theta=\dfrac{(2k+1)\pi}{p-z}$$
(The sign is absorbed because the angles are symmetric.)

Answer: **(b)**""",
[r"Examples: $P-Z=1\to180^\circ$; $2\to\pm90^\circ$; $3\to\pm60^\circ,180^\circ$; $4\to\pm45^\circ,\pm135^\circ$.",
 r"For positive feedback (or $K<0$), the angles are $\dfrac{2k\pi}{P-Z}$."]),

"4.11": ("B", r"Two separate root-locus rules: $P-Z$ branches end at infinity, and the real-axis rule (odd count to the right).",
r"""**(A)** Each branch starts at a pole. $Z$ branches end at the finite zeros, so the remaining $P-Z$ end at infinity. True.

**(R)** A real-axis segment is on the locus if the number of real poles and zeros to its right is odd. True.

**Link.** (R) is about *which parts of the real axis* belong to the locus. It says nothing about how many branches go to infinity. The two rules are independent.

Answer: **(b)**""",
[r"Both statements are standard rules, but one does not follow from the other. This is the typical structure of a (b) answer.",
 r"Read (R) carefully: 'odd' and 'to the right'. Changing either word would make it false."]),

"4.12": ("A", r"The root locus is symmetrical about the **real** axis, because complex roots occur in conjugate pairs.",
r"""Check each statement.

- (a) 'Symmetrical about the $j\omega$ axis.' **False.** The symmetry is about the real axis. A locus symmetric about the $j\omega$ axis would put LHP and RHP roots in mirror pairs, which is not generally true.
- (b) Branches start at open-loop poles ($K=0$) and end at open-loop zeros ($K\to\infty$). True.
- (c) Breakaway points come from $dK/ds=0$. True.
- (d) The real-axis rule with an odd total count to the right. True.

The statement that is *not* a property is (a).

Answer: **(a)**""",
[r"The question asks for the statement that is **not** a property.",
 r"Symmetry about the real axis comes from real coefficients in the characteristic equation."]),

"4.13": ("B", r"Number of branches = number of open-loop poles $P$ (when $P\ge Z$), i.e. the order of the characteristic equation.",
r"""The characteristic equation $D(s)+KN(s)=0$ has degree $P$ (when $P\ge Z$), so it has $P$ roots for every $K$. Each root traces one branch as $K$ varies.

Number of separate loci = number of poles of $G(s)H(s)$.

Answer: **(b)**""",
[r"In general, the number of branches is $\max(P,Z)$. For physical (proper) systems, $P\ge Z$, so it equals $P$.",
 r"Options (c) and (d) count closed-loop roots by location. Those counts change with $K$, while the number of branches is fixed."]),

"4.14": ("C", r"Centroid $\sigma_A=\dfrac{\sum p_i-\sum z_j}{P-Z}$, using the actual locations (with sign).",
r"""**Step 1 – Poles and zeros.**
- Poles: $0,\ -1,\ -2,\ -5$, sum $=-8$, $P=4$
- Zero: $-3$, sum $=-3$, $Z=1$

**Step 2 – Centroid.**
$$\sigma_A=\dfrac{-8-(-3)}{4-1}=\dfrac{-5}{3}$$

(Asymptote angles: $60^\circ,180^\circ,300^\circ$.)

Answer: **(c)**""",
[r"Subtract the *sum of zeros*: $-8-(-3)=-5$. Adding it instead gives $-11/3$.",
 r"Divide by $P-Z=3$, not by $P=4$. Dividing by 4 leads towards option (b)-type values."]),

"4.15": ("C", r"With $P-Z=2$, the asymptotes are vertical ($\pm90^\circ$) through the centroid. A double pole with no zeros gives a locus exactly on that vertical line.",
r"""**Step 1 – Check each option.**
- (a) $\dfrac{K}{s+1}$: one branch along the negative real axis. Not vertical.
- (b) $\dfrac{K(s+1)}{(s+2)^2}$: $P-Z=1$. The locus stays on the real axis or goes around a circle centred on the zero.
- (c) $\dfrac{K}{(s+2)^2}$: closed loop $(s+2)^2+K=0\Rightarrow s=-2\pm j\sqrt K$. Both branches move **vertically** along $\sigma=-2$, parallel to the $j\omega$ axis. ✓
- (d) $\dfrac{K(s+2)}{(s+1)^2}$: $P-Z=1$, a circle centred at $-2$.

Answer: **(c)**""",
[r"$\dfrac{K}{(s+a)(s+b)}$ gives a vertical line at $\sigma=-\dfrac{a+b}{2}$ after breakaway. With $a=b$, the whole complex part is that line.",
 r"For this type of plant, increasing $K$ changes only $\omega_d$. The settling time stays fixed."]),

"4.16": ("C", r"Each finite zero absorbs one branch. The remaining $P-Z$ branches go to infinity along the asymptotes.",
r"""There are $P$ branches. As $K\to\infty$:
- $Z$ branches end on the $Z$ finite zeros.
- The remaining $P-Z$ branches do **not** end on finite zeros; they go to infinity (the 'zeros at infinity').

Answer: **(c)**""",
[r"Same idea as question 4.11's assertion. 'Not terminating on zeros' means terminating at infinity."]),

"4.17": ("B", r"Check each sketch against the construction rules: real-axis segments, asymptotes, departure angles, and the circle theorem (two real poles and one zero give a circle *centred on the zero*).",
r"""**Plot 1.** Complex poles at $-0.45\pm j0.4$ and a zero at $-1.1$. The branches arc round to the left and meet on the axis at about $-1.85$. Then one branch goes to the zero and one to $-\infty$ ($P-Z=1$, $180^\circ$ asymptote). The arc is centred on the zero with radius $\sqrt{0.65^2+0.4^2}\approx0.76$, giving break-in at $\approx-1.86$ ✓. The departure angle ($\approx122^\circ$) also matches. Correct.

**Plot 2.** Real poles at $-0.2$ and $-1.05$, zero at $-1.63$. For two real poles and one zero, the complex part must be a circle **centred on the zero**, with radius
$$r=\sqrt{(1.63-0.2)(1.63-1.05)}=\sqrt{1.43\times0.58}\approx0.91$$
So the breakaway should be at $\approx-0.72$ and the break-in at $\approx-2.54$. The drawn circle is centred at about $-1.2$, not on the zero, with breakaway near $-0.45$ and break-in near $-1.95$. This violates the circle property. **Not correct.**

**Plot 3.** One real pole, a complex pair and one zero: $P-Z=2$, so asymptotes at $\pm90^\circ$ through $\sigma_A\approx-0.53$. The real branch runs from $-0.45$ to the zero. The complex branches depart at about $+12^\circ$ and bend upwards. Consistent.

**Plot 4.** Four poles and one zero: $P-Z=3$, asymptotes at $\pm60^\circ$ and $180^\circ$. The real-axis segments $(-0.75,-0.02)$ and $(-\infty,-1.45)$ are used, and $(-1.45,-0.75)$ is avoided, as the rule requires. The circle theorem does not apply with four poles, so the loop shape is acceptable for a sketch.

The plot that is not correct is 2.

Answer: **(b)** (derived; the source has no printed key for this question)""",
[r"Circle theorem: for $\dfrac{K(s+z)}{(s+p_1)(s+p_2)}$ with all three real, the complex part is a circle centred at $-z$ with radius $\sqrt{(z-p_1)(z-p_2)}$. It is a quick check on sketches.",
 r"When judging sketches, first check the real-axis segments and the number of asymptotes, then the finer geometric properties.",
 r"This answer comes from analysing the redrawn figure. If the original print differs slightly, re-check plot 4's departure angles as well."]),

"4.18": ("B", r"The root locus is symmetrical about the real axis. Real-axis segments have an **odd** number of poles plus zeros to their **right**.",
r"""- (a) Asymmetrical about the real axis: false. Complex roots come in conjugate pairs.
- (b) Symmetrical about the real axis: **true**.
- (c) 'Even number to the left': wrong rule, which uses an odd count to the right.
- (d) 'Even number to the right': wrong. It must be odd.

Answer: **(b)**""",
[r"Trap words to look for: 'even' instead of 'odd', 'left' instead of 'right', '$j\omega$ axis' instead of 'real axis'."]),

"4.19": ("C", r"The root locus is the set of closed-loop pole locations as one parameter, usually the gain $K$, varies from $0$ to $\infty$.",
r"""The characteristic equation $1+KG_0(s)H_0(s)=0$ has roots that depend on $K$ (or any other single parameter). Plotting these roots as the parameter varies gives the **root locus**.

It does not depend on the input or output signals, since the poles are a property of the system.

Answer: **(c)**""",
[r"A root locus is drawn with respect to any *one* parameter, not only the gain. That case is called a root contour.",
 r"'Sensitivity' is sometimes used loosely for $K$, but the correct general description is 'a system parameter'."]),

"4.20": ("A", r"Write the equation as $1+K\dfrac{N(s)}{D(s)}=0$, solve $\dfrac{dK}{ds}=0$, and keep only the roots that lie on the real-axis locus.",
r"""**Step 1 – Identify poles and zero.** $1+\dfrac{K(s+2)}{s^2+2s+2}=0$ has poles $-1\pm j1$ and a zero at $-2$.

**Step 2 – $K$ as a function of $s$.**
$$K=-\dfrac{s^2+2s+2}{s+2}$$

**Step 3 – Differentiate and set to zero.**
$$(2s+2)(s+2)-(s^2+2s+2)=0\ \Rightarrow\ s^2+4s+2=0\ \Rightarrow\ s=-2\pm\sqrt2$$
$$s=-0.586\quad\text{or}\quad s=-3.414$$

**Step 4 – Check which point is on the locus.** The real-axis locus is only to the left of the zero, $s<-2$ (one zero to the right). So $-0.586$ is not on the locus, while $-3.414$ is ($K=-\frac{11.66-6.83+2}{-1.414}\approx4.83>0$ ✓).

The complex branches from $-1\pm j$ arc round a circle centred at $-2$ (radius $\sqrt2$) and break in at $-3.414$.

Answer: **(a)**""",
[r"Always discard the $dK/ds=0$ roots that are not on the real-axis locus (or that give negative $K$). Option (d), $-0.414$, is a distractor, and $-0.586$ is the invalid root.",
 r"Circle check: centre $-2$, radius $\sqrt{|{-2}-(-1+j)|^2}=\sqrt2$, so the break-in is at $-2-\sqrt2$."]),

"4.21": ("D", r"Number of branches = number of closed-loop roots = $\max(P,Z)$ = degree of the characteristic equation.",
r"""$$s(s+2)(s+3)+K(s+1)=0$$
This is a cubic in $s$ (degree 3), so there are 3 roots for each $K$, giving 3 branches.

Equivalently, $P=3$ (poles $0,-2,-3$) and $Z=1$ (zero $-1$), so $\max(P,Z)=3$.

Answer: **(d)**""",
[r"The degree of the characteristic polynomial gives the number of branches immediately.",
 r"Of the 3 branches, one ends at the zero $-1$ and two go to infinity at $\pm90^\circ$."]),

"4.22": ("D", r"At $K=0$, the characteristic equation $D(s)+KN(s)=0$ reduces to $D(s)=0$, so the closed-loop roots are the open-loop poles.",
r"""$$1+KG_0(s)H_0(s)=0\ \Rightarrow\ D(s)+K\,N(s)=0$$
With $K=0$: $D(s)=0$. The roots are exactly the open-loop poles. That is why every root-locus branch *starts* at an open-loop pole.

Answer: **(d)**""",
[r"$K=0$ → open-loop poles (start). $K\to\infty$ → open-loop zeros or infinity (end).",
 r"'Coincide with zeros', option (a), is the $K\to\infty$ case."]),

"4.23": ("A", r"Adding an open-loop zero (in the LHP) shifts the centroid left, reduces the number of asymptotes, and bends the locus towards the left, which improves relative stability.",
r"""Effects of adding a LHP zero:
1. $P-Z$ decreases, so there are fewer branches going to infinity and the asymptote angles become larger.
2. The centroid $\dfrac{\sum p-\sum z}{P-Z}$ moves left.
3. The branches are attracted towards the zero and bend into the LHP.

So the locus is pulled to the left and the system becomes more stable, with better damping and faster settling.

Answer: **(a)**""",
[r"Adding a *pole* does the opposite: it pushes the locus to the right, reducing stability.",
 r"This is the root-locus view of derivative (PD) or lead compensation: adding a zero improves the transient response."]),

"4.24": ("B", r"As $|K|\to\infty$, the roots of $D(s)+KN(s)=0$ approach the roots of $N(s)=0$, the open-loop zeros (including those at infinity).",
r"""Divide the characteristic equation by $K$:
$$\dfrac{D(s)}{K}+N(s)=0$$
As $K\to\pm\infty$, the first term vanishes and the roots approach $N(s)=0$: the **zeros of $G(s)H(s)$** (finite zeros, plus $P-Z$ zeros at infinity).

Answer: **(b)**""",
[r"$K=0$ points are at the poles and $K=\pm\infty$ points are at the zeros. This holds for both the normal ($K>0$) and complementary ($K<0$) root loci."]),
}
