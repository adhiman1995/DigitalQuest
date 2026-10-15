# Detailed solutions, chapter 1 (modeling and block diagrams).
# number -> (answer, concept, solution, [points to take care of])
D = {
"1.1": ("A", r"Closed-loop (feedback) control measures the output, compares it with the reference and acts on the error.",
r"""**Step 1 – Check the Assertion.** An open-loop system has no way of knowing what the output actually is, so any disturbance, parameter drift or calibration error appears directly in the output. A closed-loop system measures the output and corrects it, so it is more accurate. (A) is true.

**Step 2 – Check the Reason.** The feedback path brings the output back to the summing point, where the error $e=r-b$ is formed and drives the controller until the error is minimised. (R) is true.

**Step 3 – Does R explain A?** The higher accuracy exists *because* of this comparison and error correction, so (R) is the correct explanation of (A).

Answer: **(a)**""",
[r"In Assertion–Reason questions, decide the truth of A and R separately first, then ask whether R is the *cause* of A.",
 r"Accuracy of a closed-loop system comes from comparison and error correction, not from higher gain. Feedback actually *reduces* overall gain.",
 r"Do not confuse accuracy with stability: feedback improves accuracy but can make a system less stable."]),

"1.2": ("A", r"Effects of negative feedback: reduced error and sensitivity, frequency-dependent gain (bandwidth change), possible instability.",
r"""**Statement 1.** With negative feedback the error is $E=\dfrac{R}{1+GH}$, which is smaller than $R$ when the loop gain is large. True.

**Statement 2.** The closed-loop gain is $\dfrac{G(j\omega)}{1+G(j\omega)H(j\omega)}$. Where $|1+GH|>1$ the gain is reduced; where $|1+GH|<1$ (near the gain crossover in some systems) it is increased, which shows up as a resonant peak. So feedback raises gain in one frequency range and lowers it in another. True.

**Statement 3.** Feedback can move closed-loop poles into the right half-plane at high gain (for example a third-order type-1 system), so an open-loop stable system can become unstable. True.

All three are correct. Answer: **(a)**""",
[r"Feedback lowers overall gain on average, but the resonant peak $M_r$ shows that the gain can rise near some frequencies.",
 r"Feedback increases bandwidth and reduces sensitivity to parameter variations. The price is lost gain and a possible loss of stability.",
 r"A stable open-loop plant does not guarantee a stable closed loop. Always check the characteristic equation $1+GH=0$."]),

"1.3": ("A", r"Mason's gain formula: $T=\dfrac{1}{\Delta}\sum_k P_k\Delta_k$, with $\Delta=1-\sum L_i+\sum L_iL_j-\dots$ over non-touching loops.",
r"""**Step 1 – Forward paths from $x_1$ to $x_2$.**
$P_1=r\cdot s\cdot u=rsu$ (upper path) and $P_2=e\cdot f\cdot h=efh$ (lower path).

**Step 2 – Individual loops.**
Upper loop between the middle nodes: $L_1=st$. Lower loop: $L_2=fg$.

**Step 3 – Non-touching loops.** $L_1$ and $L_2$ share no node, so the pair contributes $L_1L_2=stfg$.
$$\Delta=1-(st+fg)+stfg=(1-st)(1-fg)$$

**Step 4 – Cofactors.** Remove the loops touched by each path.
$P_1$ touches $L_1$ but not $L_2$, so $\Delta_1=1-fg$.
$P_2$ touches $L_2$ but not $L_1$, so $\Delta_2=1-st$.

**Step 5 – Apply Mason's formula.**
$$T=\dfrac{rsu(1-fg)+efh(1-st)}{(1-st)(1-fg)}=\dfrac{rsu}{1-st}+\dfrac{efh}{1-fg}$$

Answer: **(a)**""",
[r"Count non-touching loop pairs in $\Delta$. Forgetting $+L_1L_2$ is the most common Mason's-formula mistake.",
 r"$\Delta_k$ is $\Delta$ with every loop that touches path $k$ removed. A loop touches a path if they share even one node.",
 r"Sanity check: two independent parallel branches, each with its own loop, simply add as $\frac{P_1}{1-L_1}+\frac{P_2}{1-L_2}$.",
 r"Loop gains in a signal flow graph carry their own sign. Here the loop is $+st$, so the factor is $1-st$, not $1+st$."]),

"1.4": ("D", r"Properties of feedback: gain is reduced by $1+GH$, sensor noise enters directly, and the loop can become unstable.",
r"""**Statement 1.** Accuracy *can* be improved by adjusting the loop gain. Raising $K$ lowers the steady-state error, for example $e_{ss}=\dfrac{1}{1+K_p}$. The statement says it cannot, so it is false.

**Statement 2.** Overall gain $M=\dfrac{G}{1+GH}<G$ for $|1+GH|>1$. Feedback decreases the overall gain. True.

**Statement 3.** The sensor is in the feedback path, so sensor noise $N$ is treated like the reference and passes to the output almost unattenuated, since $C/N\approx-1$ for large loop gain. This reduces accuracy. True.

**Statement 4.** Feedback can make the closed-loop system unstable. True.

Correct statements: 2, 3 and 4. Answer: **(d)**""",
[r"Read negative wording such as 'cannot' carefully. Statement 1 is the trap.",
 r"Feedback cannot correct errors from the sensor itself. The output can only be as accurate as the measurement.",
 r"Disturbances in the forward path are attenuated by $1+GH$, but noise in the feedback path is not."]),

"1.5": (None, r"Transfer function from a step response: $G(s)=s\,C(s)$. Transfer function from an impulse response: $G(s)=\mathcal L\{g(t)\}$. Blocks in cascade multiply.",
r"""**Step 1 – First block, from its step response.**
$c(t)=-0.5(1+e^{-2t})\Rightarrow C(s)=-0.5\left(\dfrac1s+\dfrac1{s+2}\right)=-0.5\cdot\dfrac{2s+2}{s(s+2)}=-\dfrac{s+1}{s(s+2)}$
$$G_1(s)=sC(s)=-\dfrac{s+1}{s+2}$$

**Step 2 – Second block, from its impulse response.** $G_2(s)=\mathcal L\{e^{-t}\}=\dfrac1{s+1}$.

**Step 3 – Cascade.** $G_1G_2=-\dfrac{s+1}{s+2}\cdot\dfrac1{s+1}=-\dfrac{1}{s+2}$

**This is not among the options**, so the question as printed contains an error.
If the step response were $0.5(1-e^{-2t})$, then $G_1=s\cdot\dfrac{1}{s(s+2)}=\dfrac1{s+2}$ and the cascade would give $\dfrac{1}{(s+1)(s+2)}$, which is option (a). That is most likely the intended question. The answer key is left unset.""",
[r"A step response gives $G(s)=s\cdot C(s)$. Do not forget to multiply by $s$, because the input is $\frac1s$.",
 r"An impulse response is already the transfer function in the time domain: $G(s)=\mathcal L\{g(t)\}$.",
 r"Quick check: a physical step response with $c(0^+)\ne0$, as here with $c(0^+)=-1$, means a proper but not strictly proper $G$ (equal numerator and denominator order). None of the options is like that, which exposes the misprint."]),

"1.6": ("C", r"Initial conditions represent the energy stored in the system's elements at $t=0$.",
r"""Initial conditions are the values of the state variables at $t=0$: capacitor voltages, inductor currents, spring deflections, mass velocities. Each represents stored energy ($\tfrac12Cv^2$, $\tfrac12Li^2$, $\tfrac12kx^2$, $\tfrac12mv^2$).

Zero initial conditions therefore mean the system is at rest, with no energy stored in any of its parts.

Answer: **(c)**""",
[r"The transfer function is defined only under zero initial conditions. That is why it gives the forced (zero-state) response only.",
 r"'At rest' and 'no stored energy' mean the same thing here. Option (a), at rest but storing energy, contradicts itself."]),

"1.7": ("C", r"The transfer function is the Laplace transform of the impulse response: $G(s)=\mathcal L\{g(t)\}$.",
r"""For an impulse input $r(t)=\delta(t)$, $R(s)=1$, so $C(s)=G(s)$. The output is the impulse response $g(t)$.

$$G(s)=\mathcal L\{e^{-t}\}=\dfrac{1}{s+1}$$

Answer: **(c)**""",
[r"Remember the standard pair $\mathcal L\{e^{-at}\}=\dfrac{1}{s+a}$.",
 r"Do not confuse this with a step response. If $e^{-t}$ were the step response, $G$ would be $\dfrac{s}{s+1}$, which is option (d)."]),

"1.8": ("A", r"In an armature-controlled DC motor, the back-emf $e_b=K_b\omega$ opposes the applied voltage and acts like viscous friction (damping).",
r"""**Step 1 – Motor equations.** $V=R_ai_a+K_b\omega$ and $T=K_ti_a=J\dot\omega+B\omega$.

**Step 2 – Remove $i_a$.**
$$J\dot\omega+\left(B+\dfrac{K_tK_b}{R_a}\right)\omega=\dfrac{K_t}{R_a}V$$

The back-emf adds an extra term $\dfrac{K_tK_b}{R_a}$ to the friction coefficient $B$. This is why it is called 'electric friction'.

**Step 3 – Effect.** More effective damping means the response is less oscillatory, so the motor's stability improves.

Answer: **(a)**""",
[r"The effective damping of an armature-controlled DC motor is $B_{eff}=B+\dfrac{K_tK_b}{R_a}$. This is a standard result.",
 r"In SI units $K_t=K_b$ numerically (N·m/A = V·s/rad).",
 r"The back-emf is an internal feedback loop. It is velocity feedback built into the motor."]),

"1.9": ("A", r"Steady state of a stable system's impulse response is zero. Final value theorem: $f(\infty)=\lim_{s\to0}sF(s)$.",
r"""**Method 1 – Time domain.** Impulse response $g(t)=\mathcal L^{-1}\left\{\dfrac1{s+1}\right\}=e^{-t}$, which tends to $0$ as $t\to\infty$.

**Method 2 – Final value theorem.** $C(s)=G(s)\cdot1$.
$$c(\infty)=\lim_{s\to0}s\cdot\dfrac1{s+1}=0$$
The FVT is valid because the only pole, at $s=-1$, is in the LHP.

Answer: **(a)**""",
[r"For an impulse input $R(s)=1$, so there is no extra $\frac1s$. Do not mix this up with the step response, whose final value is $G(0)=1$.",
 r"Apply the FVT only when all poles of $sC(s)$ are in the LHP.",
 r"The impulse response of every stable system decays to zero, because it is a sum of decaying exponentials."]),

"1.10": ("A", r"Sensitivity: $S_G^M=\dfrac{\partial M/M}{\partial G/G}=\dfrac{G}{M}\dfrac{\partial M}{\partial G}$.",
r"""**Step 1.** $M=\dfrac{G}{1+GH}$

**Step 2 – Differentiate with respect to $G$.**
$$\dfrac{\partial M}{\partial G}=\dfrac{(1+GH)-GH}{(1+GH)^2}=\dfrac{1}{(1+GH)^2}$$

**Step 3 – Normalise.**
$$S_G^M=\dfrac{G}{M}\cdot\dfrac{1}{(1+GH)^2}=(1+GH)\cdot\dfrac{1}{(1+GH)^2}=\dfrac{1}{1+GH}$$

Answer: **(a)**""",
[r"Know all three sensitivities: $S_G^M=\dfrac1{1+GH}$, $S_H^M=\dfrac{-GH}{1+GH}$ ($\approx-1$ for large $GH$), and $S_G^{\text{open loop}}=1$.",
 r"Feedback reduces sensitivity to forward-path changes by $1+GH$, but the output is almost fully sensitive to the feedback element $H$. That is why sensors must be accurate.",
 r"Option (b) is the special case $H=1$. Choose the general expression unless the question says unity feedback."]),

"1.11": ("C", r"For a unit-step input $R(s)=\frac1s$, so $H(s)=\dfrac{Y(s)}{R(s)}=sY(s)$.",
r"""**Step 1 – Transform the output.** $\mathcal L\{te^{-t}\}=\dfrac{1}{(s+1)^2}$, from $\mathcal L\{t\}=\frac1{s^2}$ with $s\to s+1$.

**Step 2 – Divide by the input.**
$$H(s)=\dfrac{Y(s)}{1/s}=\dfrac{s}{(s+1)^2}$$

**Check:** $y(\infty)=H(0)=0$, which matches $te^{-t}\to0$. $y(0^+)=\lim_{s\to\infty}sY(s)=0$ also matches.

Answer: **(c)**""",
[r"Multiplying by $s$ (dividing by $\frac1s$) is the key step. Option (a) is the trap for anyone who stops at $Y(s)$.",
 r"A step response that returns to zero means $H(0)=0$, i.e. a zero at the origin. That alone picks option (c).",
 r"$\mathcal L\{t^ne^{-at}\}=\dfrac{n!}{(s+a)^{n+1}}$."]),

"1.12": ("D", r"Initial value theorem: $f(0^+)=\lim_{s\to\infty}sF(s)$.",
r"""$$sF(s)=\dfrac{5s}{s(s^2+3s+2)}=\dfrac{5}{s^2+3s+2}$$
As $s\to\infty$, $sF(s)\to0$. So $f(0^+)=0$.

**Check:** $F(s)$ has denominator order 3 and numerator order 0, a relative degree of 3. The function starts at zero, and so do its first derivative, since $s^2F\to0$.

Answer: **(d)**""",
[r"Do not confuse the IVT ($s\to\infty$) with the FVT ($s\to0$). The FVT here gives $\dfrac{5}{2}$, which is option (b), the trap.",
 r"Shortcut: if the denominator degree exceeds the numerator degree by 2 or more, $f(0^+)=0$.",
 r"The IVT needs $F(s)$ to be strictly proper. If it is not, take out the impulse part first."]),

"1.13": ("A", r"Superposition: to find $Y/d$, set $R=0$ and reduce the loop as seen from $d$.",
r"""**Step 1 – Set $R=0$.** The first summing junction outputs $0-Y=-Y$, and the gain $3$ makes it $-3Y$.

**Step 2 – Second summing junction.** Its output is $d-3Y$, which feeds the plant $\dfrac2{3s+1}$:
$$Y=\dfrac{2}{3s+1}(d-3Y)$$

**Step 3 – Solve.**
$$Y(3s+1)+6Y=2d\ \Rightarrow\ \dfrac{Y}{d}=\dfrac{2}{3s+7}$$

**Shortcut:** $\dfrac{Y}{d}=\dfrac{\text{forward gain from }d\text{ to }Y}{1+\text{loop gain}}=\dfrac{\frac{2}{3s+1}}{1+\frac{6}{3s+1}}=\dfrac{2}{3s+7}$.

Answer: **(a)**""",
[r"The denominator $1+GH$ is the same for every input of a loop. Only the numerator, the direct path from that input to the output, changes.",
 r"Here the controller gain $3$ is in the loop but not in the path from $d$ to $Y$, so the numerator is $2$, not $6$. Option (c) is the trap.",
 r"A larger controller gain lowers the DC disturbance gain: $Y/d$ at $s=0$ is $2/7$ instead of $2$ open loop."]),

"1.14": ("B", r"Impulse response is $\mathcal L^{-1}\{G(s)\}$. Cascaded blocks multiply.",
r"""**Step 1 – Overall transfer function.** $G(s)=\dfrac1{s+1}\cdot\dfrac1s=\dfrac{1}{s(s+1)}$

**Step 2 – Partial fractions.** $\dfrac{1}{s(s+1)}=\dfrac{A}{s}+\dfrac{B}{s+1}$
with $A=\left.\dfrac1{s+1}\right|_{s=0}=1$ and $B=\left.\dfrac1s\right|_{s=-1}=-1$.

**Step 3 – Inverse transform.** $c(t)=1-e^{-t},\ t\ge0$.

Answer: **(b)**""",
[r"An integrator $\frac1s$ in cascade means the impulse response of the total is the step response of $\frac1{s+1}$.",
 r"Check: $c(0)=0$ (relative degree 2) and $c(\infty)=1$. Only $1-e^{-t}$ satisfies both."]),

"1.15": ("A", r"Mechanical power $P=T\omega$ with $\omega$ in rad/s: $\omega=\dfrac{2\pi N}{60}$.",
r"""**Step 1 – Speed in rad/s.** $\omega=\dfrac{2\pi\times900}{60}=30\pi=94.25$ rad/s

**Step 2 – Torque.**
$$T=\dfrac{P}{\omega}=\dfrac{10\,000}{94.25}=106.1\ \text{N-m}$$

Answer: **(a)**""",
[r"Always convert rpm to rad/s before using $P=T\omega$. Using rpm directly gives $11.1$ N·m, which is wrong.",
 r"Useful shortcut: $T\,(\text{N-m})=\dfrac{9.55\,P\,(\text{W})}{N\,(\text{rpm})}$."]),

"1.16": ("A", r"A minimum-phase transfer function has all its poles and zeros in the left half of the $s$-plane.",
r"""**Statement (I).** Most physical control-system transfer functions, such as motors, RC networks and mechanical systems, have no RHP poles or zeros. True.

**Statement (II).** Transfer functions with no RHP poles or zeros are called *minimum-phase*. True.

**Link.** (I) describes the property and (II) gives the name and definition of exactly that property. By the standard key, (II) is taken as the correct explanation of (I).

Answer: **(a)**""",
[r"A minimum-phase system has the least phase lag possible for a given magnitude response, and its phase is uniquely fixed by $|G(j\omega)|$ (Bode's gain-phase relation).",
 r"Transport delay $e^{-sT}$ and RHP zeros make a system non-minimum phase.",
 r"Some texts define minimum phase using zeros only. ESE questions usually use the poles-and-zeros definition."]),

"1.17": ("B", r"A tachometer constant must be expressed in V/(rad/s). Convert rpm using $1\text{ rpm}=\dfrac{2\pi}{60}$ rad/s.",
r"""**Step 1 – Convert 1000 rpm.** $\omega=\dfrac{2\pi\times1000}{60}=104.72$ rad/s

**Step 2 – Gain constant.**
$$K_t=\dfrac{5\ \text{V}}{104.72\ \text{rad/s}}=0.0477\approx0.048\ \text{V/(rad/s)}$$

Answer: **(b)**""",
[r"Multiplying by $\frac{60}{2\pi}$ instead of $\frac{2\pi}{60}$ gives a value about 100 times too large. Check the direction of the conversion.",
 r"$1$ rad/s $=9.55$ rpm, so $K_t=\dfrac{5}{1000}\times9.55=0.048$ V/(rad/s) is a quick way."]),

"1.18": ("D", r"For unity negative feedback, $T=\dfrac{G}{1+G}\iff G=\dfrac{T}{1-T}$. Equivalently, $G=\dfrac{N}{D-N}$ where $T=\dfrac ND$.",
r"""Write $T=\dfrac{N}{D}$ with $N=100$ and $D=s^2+8s+100$.
$$G=\dfrac{T}{1-T}=\dfrac{N}{D-N}=\dfrac{100}{s^2+8s+100-100}=\dfrac{100}{s^2+8s}=\dfrac{100}{s(s+8)}$$

**Check:** $\dfrac{G}{1+G}=\dfrac{100}{s^2+8s+100}$ ✓

Answer: **(d)**""",
[r"Shortcut for unity feedback: open-loop denominator = closed-loop denominator − closed-loop numerator.",
 r"The result is type 1 (pole at the origin). This matches $T(0)=1$, i.e. zero step error.",
 r"Watch the sign in (c). With negative feedback, $D-N$ keeps the $+8s$ term."]),

"1.19": ("C", r"Laplace pair $\mathcal L\{\sin at\}=\dfrac{a}{s^2+a^2}$ and the frequency-shift property $\mathcal L\{e^{-bt}f(t)\}=F(s+b)$.",
r"""**Step 1 – Without the exponential.** With $a=2\omega$: $\mathcal L\{\sin2\omega t\}=\dfrac{2\omega}{s^2+4\omega^2}$

**Step 2 – Multiply by $e^{-2t}$.** Replace $s$ by $s+2$:
$$\mathcal L\{e^{-2t}\sin2\omega t\}=\dfrac{2\omega}{(s+2)^2+4\omega^2}$$

Answer: **(c)**""",
[r"$e^{-at}$ shifts $s\to s+a$ (plus sign). $e^{+at}$ shifts $s\to s-a$. Options (b) and (d) use the wrong sign.",
 r"Square the whole frequency: $(2\omega)^2=4\omega^2$, not $2\omega^2$.",
 r"The numerator of a sine transform is the frequency $a$. A cosine transform has $s$ (or $s+b$) in the numerator."]),

"1.20": ("A", r"Output-rate (velocity) feedback from a tachogenerator acts on the speed of the output shaft.",
r"""**Step 1 – What 'output rate control' means.** A signal proportional to the rate of change of the output is fed back. A tachogenerator on the motor shaft provides it.

**Step 2 – Effect.** This rate feedback opposes the drive signal more strongly as the motor speeds up. It adds damping and holds back, i.e. limits, the speed the motor can reach for a given error signal.

By the standard key, rate control is used to limit the speed of the motor.

Answer: **(a)**""",
[r"Rate (tacho) feedback adds damping. It increases $\xi$, which reduces overshoot without changing $\omega_n$, and it reduces the speed.",
 r"Rate feedback reduces damping-related problems; it does not reduce damping, so option (c) is the opposite effect.",
 r"Rate feedback increases the steady-state error for a ramp input. Keep this in mind for related questions."]),

"1.21": ("D", r"A tachogenerator produces a voltage proportional to shaft speed, which is the derivative of shaft position.",
r"""In a position servo, the controlled variable is the angle $\theta$. Derivative feedback means feeding back $\dfrac{d\theta}{dt}=\omega$.

A tachogenerator is a small generator whose output voltage is $e=K_t\omega$. That is exactly the derivative of position, so it provides derivative (velocity) feedback.

- Synchro: an error detector for angular position.
- Servomotor: the actuator.
- Potentiometer: a position sensor or error detector.

Answer: **(d)**""",
[r"Match each device to its signal: potentiometer or synchro → position, tachogenerator → velocity, accelerometer → acceleration.",
 r"Tacho feedback is mathematically equivalent to adding a zero (PD-like) in the feedback path."]),

"1.22": ("A", r"Minimum-phase transfer function: no poles or zeros in the right half of the $s$-plane.",
r"""A stable system already has all its poles in the LHP. If, in addition, it has no zeros in the RHP, its transfer function is called **minimum-phase**. For a given magnitude response, it has the smallest possible phase shift.

A system with RHP zeros, or with a transport delay $e^{-sT}$, is non-minimum phase.

Answer: **(a)**""",
[r"'Minimum frequency response function' and 'minimum gain transfer function' are not standard terms. Treat them as distractors.",
 r"For minimum phase, the phase at $\omega\to\infty$ is $-90^\circ\times(n-m)$. A non-minimum-phase system has more lag than this."]),

"1.23": ("C", r"The dominant pole is the one closest to the $j\omega$ axis, i.e. the lowest-frequency pole. Its mode decays slowest and governs the response.",
r"""A pole at $s=-p$ gives a term $e^{-pt}$. The smaller $p$ is, the slower that term decays and the longer it remains in the response.

The pole nearest the imaginary axis, the lowest-frequency pole, therefore dominates the transient. Other poles further left decay quickly and can often be neglected.

By the given key, the dominant pole is the lowest-frequency pole among all poles.

Answer: **(c)**""",
[r"Rule of thumb: other poles can be ignored if they are at least 5–10 times further from the $j\omega$ axis than the dominant pole.",
 r"Option (b) adds a separation condition, which is a condition for the dominant-pole *approximation* to be valid. The definition of the dominant pole is simply the lowest-frequency pole.",
 r"When neglecting a far pole, keep the DC gain unchanged: $\dfrac{1}{s+a}\to\dfrac1a$."]),

"1.24": ("B", r"Signal flow graphs represent sets of linear algebraic equations, and many different graphs can describe the same system.",
r"""**Statement 1.** A signal flow graph is built from linear algebraic equations (node value = sum of branch gain × source node). Mason's rule relies on linearity, so non-linear systems cannot be represented. False.

**Statement 2.** The same system can be described by different sets of equations or different choices of node variables, each giving a different graph. The graph is not unique. True.

Only 2. Answer: **(b)**""",
[r"Both block diagrams and signal flow graphs are for linear time-invariant systems only.",
 r"The graph is not unique, but the transfer function between any two given nodes is unique."]),

"1.25": ("A", r"Unity feedback around a first-order plant $\dfrac{K_0}{1+\tau s}$ gives a closed-loop time constant $\dfrac{\tau}{1+K_0}$.",
r"""**Step 1 – Close the loop.**
$$\dfrac CR=\dfrac{\frac{10K}{1+10s}}{1+\frac{10K}{1+10s}}=\dfrac{10K}{1+10K+10s}$$

**Step 2 – Put it in time-constant form.**
$$\dfrac CR=\dfrac{\frac{10K}{1+10K}}{1+\frac{10}{1+10K}s}\ \Rightarrow\ \tau_{cl}=\dfrac{10}{1+10K}$$

**Step 3 – Apply the condition.** $\tau_{ol}=10$ s, reduced 20 times to $\tau_{cl}=0.5$ s:
$$\dfrac{10}{1+10K}=0.5\ \Rightarrow\ 1+10K=20\ \Rightarrow\ K=1.9$$

Answer: **(a)**""",
[r"The time constant is the coefficient of $s$ only after the constant term is made $1$. Do not read $10$ off $1+10K+10s$ directly.",
 r"Feedback makes the response faster by a factor $1+K_{dc}$, where $K_{dc}=10K$ is the open-loop DC gain.",
 r"Faster response costs DC gain, which falls from $10K$ to $\dfrac{10K}{1+10K}$."]),

"1.26": ("B", r"Reduce the block diagram by writing the signal at each summing junction. A feedback signal that cancels to zero leaves the system effectively open loop.",
r"""**Step 1 – Name the signals.** Let $e=R-F$ be the output of the first summing junction. It feeds both blocks.

**Step 2 – Upper block.** $C=\dfrac{e}{s+1}$

**Step 3 – Lower path and second junction.** The lower block also produces $\dfrac{e}{s+1}$. The second summing junction takes $+C$ from above and subtracts the lower block output:
$$F=C-\dfrac{e}{s+1}=\dfrac{e}{s+1}-\dfrac{e}{s+1}=0$$

**Step 4 – Result.** The fed-back signal is zero, so $e=R$:
$$\dfrac{C}{R}=\dfrac{1}{s+1}$$

Answer: **(b)**""",
[r"Check signs at every summing junction from the figure before reducing. Here the cancellation depends on the $-$ sign on the lower block.",
 r"Equivalently: feedback element $H=1-1=0$ when expressed relative to $C$, so $\dfrac CR=G$.",
 r"Writing equations at each summer is often faster and safer than moving blocks around."]),

"1.27": ("A", r"Feedback divides the gain by $1+GH$ in exchange for reducing sensitivity by the same factor.",
r"""Closed-loop gain: $M=\dfrac{G}{1+GH}$, which is smaller than the open-loop gain $G$ by the factor $1+GH$.
Sensitivity: $S_G^M=\dfrac{1}{1+GH}$, which is improved (reduced) by the same factor $1+GH$.

So the improvement in sensitivity is paid for by a loss of overall system gain. The lost gain is usually recovered with an amplifier.

Answer: **(a)**""",
[r"Gain × sensitivity trade-off: both change by the same factor $1+GH$.",
 r"Feedback usually *improves* the transient response (faster, wider bandwidth), so (c) and (d) are not the price paid. The other real cost is possible instability."]),

"1.28": ("A", r"Characteristic equation of a negative-feedback loop: $1+G(s)H(s)=0$.",
r"""With unity feedback ($H=1$):
$$1+\dfrac{K(s+2)}{(s+1)(s+4)}=0$$
Multiply through by $(s+1)(s+4)$:
$$(s+1)(s+4)+K(s+2)=0$$

Answer: **(a)**""",
[r"Characteristic polynomial = denominator of $GH$ + numerator of $GH$, i.e. $D(s)+N(s)$.",
 r"The open-loop zeros stay in the $K$ term and the open-loop poles go in the first term. Option (b) swaps them.",
 r"For positive feedback it would be $D(s)-N(s)=0$."]),

"1.29": ("C", r"A signal flow graph is a graphical form of a set of linear algebraic equations, each written as cause → effect.",
r"""To draw a signal flow graph:
1. Write the system's differential equations and take Laplace transforms. They become **algebraic** equations in $s$.
2. Arrange each equation as an effect (output node) equal to the sum of causes (input nodes × branch gains).
3. Draw one node per variable and one branch per cause–effect term.

So the graph is constructed from algebraic equations through cause-and-effect relations.

Answer: **(c)**""",
[r"Signal flow graphs work with Laplace-domain algebraic equations, never directly with differential equations.",
 r"Each equation must be written in cause-and-effect form, $x_j=\sum_i a_{ij}x_i$. This is what distinguishes (c) from (b)."]),

"1.30": ("D", r"Feedback is used to reduce parameter sensitivity, reject internal disturbances, and reduce non-linear distortion.",
r"""**1. Sensitivity.** Feedback reduces it by $1+GH$. ✓

**2. Internal disturbances.** A disturbance entering the forward path is attenuated by $1+GH$. ✓

**3. Distortion in non-linear systems.** Non-linear distortion arising inside the loop (e.g. amplifier non-linearity) is suppressed by the loop gain, which is why negative-feedback amplifiers have low distortion. ✓

All three. Answer: **(d)**""",
[r"Anything generated *inside* the forward path (disturbance, distortion, parameter change) is reduced by $1+GH$.",
 r"Anything entering at the sensor (noise, sensor error) is *not* reduced."]),

"1.31": ("A", r"Basic terminology: the controller computes the plant input (manipulated variable) from the error.",
r"""In a feedback loop: reference → comparator → **controller** → (actuator) → plant → output.

The block that produces the input applied to the plant or process is the **controller**.
- The controlled variable is the plant *output*.
- Controllability is a system property, not a subsystem.
- A compensator is a subsystem added to *modify* the dynamics. It is a kind of controller, but the general name for the block generating the plant input is 'controller'.

Answer: **(a)**""",
[r"Manipulated variable = controller output = plant input. Controlled variable = plant output.",
 r"Distinguish system *properties* (controllability, observability) from system *blocks* (controller, plant, sensor)."]),

"1.32": ("D", r"For unity feedback, $G=\dfrac{T}{1-T}=\dfrac{N}{D-N}$. Open-loop DC gain is $G(0)$.",
r"""**Step 1 – Recover $G(s)$.** $N=s+4$ and $D=s^2+7s+13$.
$$G=\dfrac{N}{D-N}=\dfrac{s+4}{s^2+7s+13-(s+4)}=\dfrac{s+4}{s^2+6s+9}=\dfrac{s+4}{(s+3)^2}$$

**Step 2 – DC gain.** $G(0)=\dfrac{4}{9}$

**Check:** $T(0)=\dfrac{4}{13}$ and $\dfrac{G(0)}{1+G(0)}=\dfrac{4/9}{13/9}=\dfrac{4}{13}$ ✓

Answer: **(d)**""",
[r"Do not give the closed-loop DC gain $T(0)=\dfrac4{13}$, which is option (a), the trap. The question asks for the *open-loop* DC gain.",
 r"Shortcut at DC only: $G(0)=\dfrac{T(0)}{1-T(0)}=\dfrac{4/13}{9/13}=\dfrac49$. There is no need to find the full $G(s)$."]),
}
