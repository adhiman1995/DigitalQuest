# Detailed solutions, chapter 4 (root locus), 4.25-4.46.
# number -> (answer, concept, solution, [points to take care of])
D = {
"4.25": ("C", r"Centroid $\sigma_A=\dfrac{\sum p_i-\sum z_j}{P-Z}$. Complex poles contribute only their real parts to the sum.",
r"""**Step 1 – Poles and zeros.**
- Poles: $0,\ -4,\ -1\pm j1$ (from $s^2+2s+2$). Sum $=0-4-1-1=-6$, $P=4$.
- Zero: $-1$. Sum $=-1$, $Z=1$.

**Step 2 – Centroid.**
$$\sigma_A=\dfrac{-6-(-1)}{4-1}=-\dfrac{5}{3}$$

Answer: **(c)**""",
[r"Shortcut for the sum of the roots of $s^2+bs+c$: it is $-b$. Here $s^2+2s+2$ contributes $-2$.",
 r"The imaginary parts of a conjugate pair cancel. Only the real parts enter the centroid."]),

"4.26": ("B", r"At $K=0$, the characteristic equation $D(s)+KN(s)=0$ reduces to $D(s)=0$, so the roots are the open-loop poles.",
r"""$$D(s)+K\,N(s)=0\ \xrightarrow{\ K=0\ }\ D(s)=0$$
The closed-loop roots coincide with the **poles of $G(s)H(s)$**. Every branch starts at an open-loop pole.

Answer: **(b)**""",
[r"Pair this with question 4.24: $K=0$ at the poles, $K=\infty$ at the zeros."]),

"4.27": ("B", r"$\xi=\cos\theta$, where $\theta$ is the angle of the pole from the negative real axis. $\xi=0.707$ means $\theta=45^\circ$, so the real and imaginary parts are equal.",
r"""**Step 1 – Closed-loop characteristic equation.**
$$(s+1)(s+3)+4K=0\ \Rightarrow\ s^2+4s+(3+4K)=0$$
$$s=-2\pm\sqrt{1-4K}$$
After breakaway ($K>\frac14$), the poles move vertically on the line $\sigma=-2$, as shown in the figure.

**Step 2 – Pole location for $\xi=0.707$.** At $45^\circ$, $|\text{Im}|=|\text{Re}|=2$, so the poles are at $-2\pm j2$.

**Step 3 – Solve for $K$.**
$$\sqrt{1-4K}=j2\ \Rightarrow\ 1-4K=-4\ \Rightarrow\ K=\dfrac54$$

**Check (magnitude condition).** $|4K|=|s+1||s+3|$ at $s=-2+j2$: $\sqrt5\cdot\sqrt5=5\Rightarrow K=\dfrac54$ ✓

Answer: **(b)**""",
[r"Note the factor 4 in $4K$. The closed-loop constant term is $3+4K$, not $3+K$. Ignoring it gives $K=5$.",
 r"Alternative: compare with $s^2+2\xi\omega_ns+\omega_n^2$. $2\xi\omega_n=4$ and $\xi=0.707$ give $\omega_n^2=8=3+4K$, so $K=5/4$.",
 r"Gain cannot be negative on the ordinary root locus, so option (c) is out immediately."]),

"4.28": ("D", r"Number of branches = $\max(P,Z)$ = degree of the characteristic equation.",
r"""The characteristic equation $D(s)+KN(s)=0$ has degree $\max(\deg D,\deg N)=\max(P,Z)$, so it has that many roots, and each root traces one locus.

For physical systems $P\ge Z$, so this usually equals $P$. But the general statement is 'the number of open-loop poles or zeros, whichever is greater'.

Answer: **(d)**""",
[r"Compare question 4.13, where option '(b) number of poles' was the best available answer. Here the more general option (d) is offered, so choose it.",
 r"When two options are both acceptable, pick the more general, precise one."]),

"4.29": ("B", r"Symmetry about the real axis comes from complex roots occurring in conjugate pairs (real coefficients). Symmetry about other axes happens only for symmetric pole-zero patterns.",
r"""**Statement (I).** The characteristic polynomial has real coefficients, so complex roots occur in conjugate pairs. The locus is always symmetrical about the real axis. True.

**Statement (II).** If the pole-zero pattern itself has an axis of symmetry perpendicular to the real axis (for example poles at $0$ and $-4$ symmetric about $\sigma=-2$), the locus is normally symmetrical about that axis too. True (as a 'normally' statement).

**Link.** (I) is due to conjugate pairs, not to the pole-zero symmetry described in (II). (II) does not explain (I).

Answer: **(b)**""",
[r"Real-axis symmetry is *always* present. Symmetry about a vertical axis exists only for symmetric pole-zero patterns.",
 r"Assertion–reason pattern: two true but unrelated properties give (b)."]),

"4.30": ("A", r"Centroid $\sigma_A=\dfrac{\sum p_i-\sum z_j}{P-Z}$. It always lies on the real axis, so its coordinates are $(\sigma_A,0)$.",
r"""**Step 1 – Poles.** $0,\ -2,\ -1\pm j2$ (from $s^2+2s+5$). Sum $=0-2-2=-4$. $P=4$, $Z=0$.

**Step 2 – Centroid.**
$$\sigma_A=\dfrac{-4}{4}=-1$$

**Step 3 – Coordinates.** It is on the real axis, so the point is $(-1,\ 0)$.

Answer: **(a)**""",
[r"The order of the coordinates is (real, imaginary). $(0,-1)$, option (c), would be a point on the imaginary axis, which is impossible for a centroid.",
 r"Asymptote angles here are $\pm45^\circ$ and $\pm135^\circ$."]),

"4.31": ("D", r"Gain margin = factor by which $K$ can be raised before the closed loop becomes unstable. In root-locus terms, $GM=K_{crossing}/K_{design}$.",
r"""On a root locus, instability starts where a branch crosses into the RHP through the $j\omega$ axis, at a gain $K_c$. Then $GM=\dfrac{K_c}{K}$.

If no branch ever crosses the $j\omega$ axis, the system stays stable for every $K>0$. No finite critical gain exists, so
$$GM=\infty$$

Answer: **(d)**""",
[r"Example: $\dfrac{K}{s(s+a)}$ never crosses the $j\omega$ axis, so its GM is infinite. Any first- or second-order system without RHP zeros behaves like this.",
 r"In Bode terms, infinite GM means the phase never reaches $-180^\circ$."]),

"4.32": ("C", r"A point lies on the root locus if it satisfies the characteristic equation $D(s)+K=0$ for some real $K$. Substitute the point to find $K$.",
r"""**Step 1 – Characteristic equation.**
$$s^3+4s^2+s-6+K=0$$

**Step 2 – Substitute $s=0$.**
$$0+0+0-6+K=0\ \Rightarrow\ K=6$$

**Check with the magnitude condition.** $K=|D(0)|=|-6|=6$ ✓

Answer: **(c)**""",
[r"$s^3+4s^2+s-6=(s-1)(s+2)(s+3)$, so there is an open-loop pole at $s=+1$. The branch from $+1$ moves left and reaches the origin at $K=6$. For $K>6$ the system can become stable.",
 r"Do not answer $K=0$. At $K=0$ the roots are at the poles $1,-2,-3$, not at the origin."]),

"4.33": ("C", r"Oscillatory (marginally stable) gain from the Routh array, and the frequency from the auxiliary equation.",
r"""**Step 1 – Characteristic equation.**
$$s(s^2+6s+10)+K=s^3+6s^2+10s+K=0$$

**Step 2 – Routh array.**
$$\begin{array}{c|cc} s^3 & 1 & 10\\ s^2 & 6 & K\\ s^1 & \frac{60-K}{6} & \\ s^0 & K & \end{array}$$

**Step 3 – Marginal gain.** $60-K=0\Rightarrow K=60$

**Step 4 – Frequency.** $6s^2+60=0\Rightarrow s=\pm j\sqrt{10}$, so $\omega=3.16$ rad/s.

Answer: **(c)**""",
[r"The breakaway points, centroid and asymptotes in the question are distractions. Only Routh is needed.",
 r"For $s^3+a s^2+b s+K$: $K_{mar}=ab$ and $\omega=\sqrt b$. Here $6\times10=60$ and $\sqrt{10}$."]),

"4.34": ("C", r"Branches tending to infinity $=P-Z$.",
r"""Each branch starts at a pole and ends at a zero. With $P=Z$, every branch finds a finite zero to end on, so
$$P-Z=0$$
No branch goes to infinity, and there are no asymptotes.

Answer: **(c)**""",
[r"No asymptotes when $P=Z$. The centroid formula would divide by zero, which is a reminder that it does not apply."]),

"4.35": ("C", r"Closed-loop poles are the roots of $1+G(s)=0$.",
r"""$$1+\dfrac{1}{(s+2)^2}=0\ \Rightarrow\ (s+2)^2=-1\ \Rightarrow\ s=-2\pm j1$$

Answer: **(c)**""",
[r"Repeat of question 2.64 (with different option letters).",
 r"Option (a), $-2,-2$, gives the *open-loop* poles."]),

"4.36": ("B", r"Number of branches = degree of the characteristic equation = $\max(P,Z)$, for both $K>0$ and $K<0$.",
r"""$$s(s+4)(s+5)+K(s+2)=0$$
This is a cubic, so there are 3 roots for every $K$ and therefore **3 branches**.

When $K$ runs from $-\infty$ to $+\infty$, each branch has a $K>0$ part (root locus) and a $K<0$ part (complementary root locus). The *number* of branches is still 3.

Answer: **(b)**""",
[r"Do not double the count for the negative-$K$ part. The $K<0$ locus continues the same branches.",
 r"$P=3$ and $Z=1$, so $\max=3$."]),

"4.37": ("B", r"Solve $dK/ds=0$, then keep only the roots on the real-axis part of the locus (with $K>0$).",
r"""**Step 1 – Poles and zero.** Poles $-1\pm j\sqrt2$ (from $s^2+2s+3$), zero $-2$.

**Step 2 – $K(s)$ and its derivative.**
$$K=-\dfrac{s^2+2s+3}{s+2}$$
$$\dfrac{dK}{ds}=0\ \Rightarrow\ (2s+2)(s+2)-(s^2+2s+3)=s^2+4s+1=0$$
$$s=-2\pm\sqrt3=-0.268,\ -3.732$$

**Step 3 – Validity.** The real-axis locus is only to the left of the zero, $s<-2$. So $-0.268$ is rejected and $-3.732$ is accepted ($K\approx5.46>0$). It is a break-in point, where the complex branches meet the axis.

(The complex branches follow a circle centred on the zero $-2$ with radius $\sqrt{|{-2}+1|^2+2}=\sqrt3$, so the break-in is at $-2-\sqrt3$.)

Answer: **(b)**""",
[r"Option (c) lists both roots of $dK/ds=0$. Always test each root against the real-axis rule.",
 r"Complex poles with one zero: the locus is a circle centred on the zero, radius $=$ distance from the zero to a pole."]),

"4.38": ("A", r"The root locus shows how the closed-loop poles move with $K$, and therefore the transient response and stability range.",
r"""**1.** The open-loop poles and zeros are the starting and ending points of the plot, so they are clearly displayed. True.

**2.** Each point on the locus is a closed-loop pole for some $K$. Its position gives $\xi$, $\omega_n$ and the settling time, so you can see how the transient response changes with $K$. True.

**3.** The $j\omega$-axis crossings give the gain range for stability. True.

All three. Answer: **(a)**""",
[r"The root locus is a design tool: pick the point with the desired $\xi$ or $\omega_n$ on the locus, then find $K$ from the magnitude condition."]),

"4.39": ("A", r"Asymptote angles $\theta_k=\dfrac{(2k+1)180^\circ}{P-Z}$.",
r"""**Step 1 – Count.** Poles $-2\pm j2,\ -1,\ 0$ give $P=4$. Zero $-3$ gives $Z=1$. So $P-Z=3$.

**Step 2 – Angles.**
$$\theta=\dfrac{180^\circ}{3},\ \dfrac{3\times180^\circ}{3},\ \dfrac{5\times180^\circ}{3}=60^\circ,\ 180^\circ,\ 300^\circ$$
$300^\circ\equiv-60^\circ$.

Answer: **(a)**""",
[r"Three asymptotes are always $\pm60^\circ$ and $180^\circ$, regardless of where the poles are.",
 r"(Centroid here: $\frac{(-2-2-1+0)-(-3)}{3}=-\frac23$.)"]),

"4.40": ("A", r"On the real axis, a complex-conjugate pair of poles or zeros contributes angles $\theta$ and $-\theta$ (equivalently $2\pi$ in total), which leaves the angle condition unchanged.",
r"""**Statement (I).** Whether a real-axis point is on the locus depends only on real poles and zeros to its right. Complex pairs do not affect it. True.

**Statement (II).** For a test point on the real axis, the angles from a conjugate pair are $\theta$ and $2\pi-\theta$, summing to $2\pi$, which is equivalent to $0$. True.

**Link.** Because the pair adds a multiple of $2\pi$, the condition 'total angle $=$ odd multiple of $\pi$' is unchanged. That is exactly why (I) holds. (II) explains (I).

Answer: **(a)**""",
[r"Similarly, real poles and zeros to the *left* of the test point contribute $0$, and those to the right contribute $\pi$ each. That is the origin of the odd-count rule.",
 r"Complex pairs do affect the locus *off* the real axis (departure angles, etc.)."]),

"4.41": ("C", r"Adding a (LHP) open-loop pole pushes the root locus to the right, reducing relative stability and slowing the response. Its effect on steady-state error depends on how it is added.",
r"""**1. Locus pulled to the right.** An extra pole increases $P-Z$, giving more asymptotes at smaller angles, and moves the centroid right. The branches bend towards the RHP. True.

**3. Slower response.** The extra pole adds lag. The dominant poles move closer to the $j\omega$ axis, giving lower damping and a longer settling time. True.

**2. Steady-state error increased.** Not true in general.
- A pole at the origin raises the type and *reduces* the error.
- A pole added as $\dfrac{1}{1+sT}$ leaves $K_p,K_v,K_a$ unchanged, so the error is unchanged.
- Only a pole added as $\dfrac{1}{s+p}$ with the gain $K$ held fixed lowers the error constant.

So statement 2 is not a general consequence of adding a pole. The correct statements are 1 and 3.

Answer: **(c)** (derived; the source has no printed key for this question)""",
[r"Standard summary: adding a pole → locus moves right, less stable, slower. Adding a zero → locus moves left, more stable, faster.",
 r"Steady-state error is governed by the error constants (type and DC gain), not by the root-locus shape. Check this separately.",
 r"Some coaching keys mark all three as correct by assuming the $\frac1{s+p}$ form. Read the statement critically."]),

"4.42": ("B", r"Breakaway between two adjacent real poles on the locus: the root of $dK/ds=0$ lying in that segment.",
r"""**Step 1 – $K(s)$.**
$$K=-s(s+1)(s+2)=-(s^3+3s^2+2s)$$

**Step 2 – $dK/ds=0$.**
$$3s^2+6s+2=0\ \Rightarrow\ s=\dfrac{-6\pm\sqrt{36-24}}{6}=-1\pm0.577$$
$$s=-0.423\quad\text{or}\quad s=-1.577$$

**Step 3 – Check the locus.** Real-axis segments on the locus are $(-1,0)$ and $(-\infty,-2)$. $-0.423$ is in $(-1,0)$ ✓ ($K=0.385>0$). $-1.577$ is in $(-2,-1)$, which is not on the locus ✗.

Breakaway point: $-0.42$.

Answer: **(b)**""",
[r"A breakaway point must lie between two poles on a real-axis locus segment. $-1.577$ gives $K<0$ (complementary locus).",
 r"Quick check: the breakaway is always closer to the pole that is 'more isolated'. Here it is closer to $0$ than to $-1$."]),

"4.43": ("C", r"Asymptote angles for $P-Z=3$: $60^\circ$, $180^\circ$, $300^\circ$.",
r"""$P=3$ (poles $0,-1,-2$), $Z=0$:
$$\theta_k=\dfrac{(2k+1)180^\circ}{3},\ k=0,1,2\ \Rightarrow\ 60^\circ,\ 180^\circ,\ 300^\circ$$

Answer: **(c)**""",
[r"Asymptotes are spaced equally by $360^\circ/(P-Z)=120^\circ$. Option (b) has $60^\circ$ and $120^\circ$, only $60^\circ$ apart, which is impossible.",
 r"$300^\circ$ and $-60^\circ$ are the same direction."]),

"4.44": ("D", r"Branches leaving a real pole or entering a real zero along a real-axis segment move along the axis, i.e. at $0^\circ$ or $180^\circ$.",
r"""For a real pole (or zero) on a real-axis segment of the locus, the branch must start (or end) **along the real axis**:
- If the locus segment is to the *left* of the pole, the departure angle is $180^\circ$.
- If the locus segment is to the *right* of the pole, the departure angle is $0^\circ$.

The same applies to arrival at a real zero. So the angle is $0^\circ$ or $180^\circ$.

Answer: **(d)**""",
[r"Exception: a *repeated* real pole of multiplicity $m$ has $m$ branches leaving at $\frac{(2k+1)180^\circ}{m}$ (e.g. $\pm90^\circ$ for a double pole). The question assumes simple poles.",
 r"Departure angles need calculating only for *complex* poles and zeros."]),

"4.45": ("C", r"The root locus shows how closed-loop pole positions (hence stability and transient response) vary with loop gain.",
r"""The root locus plots the closed-loop poles for $0\le K<\infty$. From it you can see directly:
- the gain range for stability (from the $j\omega$-axis crossings),
- the damping ratio, natural frequency and settling time for each $K$,
- where to put compensator poles and zeros to reshape the locus.

So it is *the* technique for analysing and designing the effect of loop gain on the transient response and stability.

Answer: **(c)**""",
[r"Bode and Nyquist plots also show the effect of gain on *stability* (through the margins), but the root locus shows the *transient response* directly."]),

"4.46": ("D", r"Breakaway and break-in points from $dK/ds=0$. A double pole is itself a breakaway point.",
r"""**Step 1 – $K(s)$.**
$$K=-\dfrac{(s+1)^2}{s+2}$$

**Step 2 – $dK/ds=0$.**
$$2(s+1)(s+2)-(s+1)^2=(s+1)\left[2(s+2)-(s+1)\right]=(s+1)(s+3)=0$$
$$s=-1,\quad s=-3$$

**Step 3 – Interpretation.**
- $s=-1$ is the double open-loop pole, where the branches break away ($K=0$) into the complex plane.
- $s=-3$ is the break-in point ($K=-\frac{4}{-1}=4>0$). The circle centred at the zero $-2$ with radius 1 returns to the axis here.

Breakaway/break-in points: $-1$ and $-3$.

Answer: **(d)**""",
[r"A repeated pole is always a breakaway point, at $K=0$.",
 r"Circle check: centre at the zero $-2$, radius $|{-2}-(-1)|=1$, so the circle touches the axis at $-1$ and $-3$ ✓.",
 r"Options with positive values are impossible here, since no part of the locus lies on the positive real axis."]),
}
