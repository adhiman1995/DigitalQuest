import sys, json
sys.path.insert(0, '/Users/alok/Desktop/ESE/ese-tracker/scripts/authoring')
from figs import *

AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"]
SR = ["Both Statement (I) and Statement (II) are individually true and Statement (II) is the correct explanation of Statement (I)", "Both Statement (I) and Statement (II) are individually true but Statement (II) is not the correct explanation of Statement (I)", "Statement (I) is true but Statement (II) is false", "Statement (I) is false but Statement (II) is true"]
S4 = ["1, 2 and 3", "1 and 2 only", "1 and 3 only", "2 and 3 only"]

QS = []   # (image_key, question dict)
def Q(img, n, year, page, topic, text, opts, key=None, mark=None, fig=None, lists=None, table=None, after=None):
    d = {"number": n, "year": year, "page": page, "topic": topic, "text": text, "options": opts}
    if key: d["answer"] = key
    if mark: d["marked"] = mark
    if fig: d["figure"] = fig
    if lists: d["lists"] = lists
    if table: d["table"] = table
    if after: d["after"] = after
    QS.append((img, d))

# ======================================================================= CHAPTER 1  (images n1: 1.1-1.18, n0: 1.19-1.32)
FB, TFL, BD, SFG, PZ, MC = "Feedback Basics", "Transfer Functions & Laplace", "Block Diagram Algebra", "Signal Flow Graphs", "Poles, Zeros & Minimum Phase", "Motors & Components"
n1, n0 = "n1", "n0"
Q(n1, "1.1", 2000, 2, FB, r"**Assertion (A):** Feedback control systems offer more accurate control over open-loop systems." "\n" r"**Reason (R):** The feedback path establishes a link for input and output comparison and subsequent error correction.", AR, "A", "A")
Q(n1, "1.2", 2000, 2, FB, "Consider the following statements:\n1. The effect of feedback is to reduce the system error\n2. Feedback increases the gain of the system in one frequency range but decreases in another\n3. Feedback can cause a system that is originally stable to become unstable\nWhich of these statements are correct?", ["1, 2 and 3", "1 and 2", "2 and 3", "1 and 3"], "A", "B")
Q(n1, "1.3", 2001, 2, SFG, r"For the signal flow diagram shown in the given figure, the transmittance between $x_2$ and $x_1$ is",
  [r"$\dfrac{rsu}{1-st}+\dfrac{efh}{1-fg}$", r"$\dfrac{rsu}{1-fg}+\dfrac{efh}{1-st}$", r"$\dfrac{efh}{1-ru}+\dfrac{rsu}{1-eh}$", r"$\dfrac{rst}{1-eh}+\dfrac{rsu}{1-st}$"], "A", "A", fig=q13_sfg())
Q(n1, "1.4", 2006, 2, FB, "Consider the following statements with respect to feedback control systems:\n1. Accuracy cannot be obtained by adjusting loop gain.\n2. Feedback decreases overall gain.\n3. Introduction of noise due to sensor reduces overall accuracy.\n4. Introduction of feedback may lead to the possibility of instability of closed loop system.\nWhich of the statements given above are correct?",
  ["1, 2, 3 and 4", "Only 1, 2 and 4", "Only 1 and 3", "Only 2, 3 and 4"], "D", "D")
Q(n1, "1.5", 2007, 2, TFL, r"A control system whose step response is $-0.5\,(1+e^{-2t})$ is cascaded to another control block whose impulse response is $e^{-t}$. What is the transfer function of the cascaded combination?",
  [r"$\dfrac{1}{(s+1)(s+2)}$", r"$\dfrac{1}{s(s+1)}$", r"$\dfrac{-1}{s(s+2)}$", r"$\dfrac{0.5}{(s+1)(s+2)}$"])
Q(n1, "1.6", 2007, 2, TFL, "If the initial conditions for a system are inherently zero, what does it physically mean?",
  ["The system is at rest but stores energy", "The system is working but does not store energy", "The system is at rest or no energy is stored in any of its parts", "The system is working with zero reference input"], "C", "D")
Q(n1, "1.7", 2008, 2, TFL, r"The impulse response of a linear time invariant system is given as $g(t)=e^{-t},\ t>0$. The transfer function of the system is equal to",
  [r"$1/s$", r"$1/[s(s+1)]$", r"$1/(s+1)$", r"$s/(s+1)$"], "C", "C")
Q(n1, "1.8", 2008, 3, MC, r"In case of DC servo-motor the back-emf is equivalent to an ``electric friction'' which tends to".replace("``", "“").replace("''", "”"),
  ["improve stability of the motor", "slowly decrease stability of the motor", "very rapidly decrease stability of the motor", "have no effect on stability"], "A", "A")
Q(n1, "1.9", 2009, 3, TFL, r"The transfer function of a linear-time-invariant system is given as $\dfrac{1}{s+1}$. What is the steady-state value of the unit-impulse response?", ["Zero", "One", "Two", "Infinite"], "A", "A")
Q(n1, "1.10", 2009, 3, FB, "In closed loop control system, what is the sensitivity of the gain of the overall system, $M$ to the variation in $G$?",
  [r"$\dfrac{1}{1+G(s)H(s)}$", r"$\dfrac{1}{1+G(s)}$", r"$\dfrac{G(s)}{1+G(s)H(s)}$", r"$\dfrac{G(s)}{1+G(s)}$"], "A", "A")
Q(n1, "1.11", 2010, 3, TFL, r"A linear time-invariant system initially at rest, when subjected to a unit-step input, gives a response $y(t)=te^{-t},\ t>0$. The transfer function of the system is:",
  [r"$\dfrac{1}{(s+1)^2}$", r"$\dfrac{1}{s(s+1)^2}$", r"$\dfrac{s}{(s+1)^2}$", r"$\dfrac{1}{s+1}$"], "C", "C")
Q(n1, "1.12", 2010, 3, TFL, r"Consider the function $$F(s)=\dfrac{5}{s(s^2+3s+2)}$$ where $F(s)$ is Laplace transform of function $f(t)$. The initial value of $f(t)$ is:", ["$5$", r"$\dfrac{5}{2}$", r"$\dfrac{5}{3}$", "$0$"], "D", "A")
Q(n1, "1.13", 2010, 3, BD, r"The transfer function from $d(s)$ to $y(s)$ is", [r"$\dfrac{2}{3s+7}$", r"$\dfrac{2}{3s+1}$", r"$\dfrac{6}{3s+7}$", r"$\dfrac{2}{3s+6}$"], "A", "A",
  fig=dist_loop("3", r"\dfrac{2}{3s+1}", g1w=50, g2w=96, dlabel="d(s)", rin="R(s)", cout="Y(s)"))
Q(n1, "1.14", 2011, 3, BD, r"What is the unit impulse response of the system shown in figure for $t\ge 0$?", [r"$1+e^{-t}$", r"$1-e^{-t}$", r"$e^{-t}$", r"$-e^{-t}$"], "B", "B",
  fig=series([(r"\dfrac{1}{s+1}", 80), (r"\dfrac{1}{s}", 56)]))
Q(n1, "1.15", 2013, 3, MC, "An electric motor is developing 10 kW at a speed of 900 rpm. The torque available at the shaft is", ["106 N-m", "66 N-m", "1600 N-m", "90 N-m"], "A")
Q(n1, "1.16", 2013, 3, PZ, "**Statement (I):** Many of the linear control system transfer functions do not have poles or zeros in the right half of s-plane.\n**Statement (II):** These are called minimum-phase transfer functions.", SR, "A", "A")
Q(n1, "1.17", 2014, 3, MC, "A tachometer has a sensitivity of 5 V/1000 rpm. The gain constant of the tachometer is", ["0.48 V/rad/sec", "0.048 V/rad/sec", "4.8 V/rad/sec", "48 V/rad/sec"], "B")
Q(n1, "1.18", 2015, 3, TFL, r"The closed loop transfer function of a unity negative feedback system is $\dfrac{100}{s^2+8s+100}$. Its open loop transfer function is",
  [r"$\dfrac{100}{s+8}$", r"$\dfrac{1}{s^2+8s}$", r"$\dfrac{100}{s^2-8s}$", r"$\dfrac{100}{s^2+8s}$"], "D", "D")
Q(n0, "1.19", 2015, 4, TFL, r"The Laplace transform of $e^{-2t}\sin(2\omega t)$ is",
  [r"$\dfrac{2s}{(s+2)^2+2\omega^2}$", r"$\dfrac{2\omega}{(s-2)^2+4\omega^2}$", r"$\dfrac{2\omega}{(s+2)^2+4\omega^2}$", r"$\dfrac{2s}{(s-2)^2+2\omega^2}$"], "C", "C")
Q(n0, "1.20", 2015, 4, MC, "In a closed loop system for which the output is the speed of a motor, the output rate control can be used to", ["Limit the speed of the motor", "Limit the torque output of the motor", "Reduce the damping of the system", "Limit the acceleration of the motor"], "A")
Q(n0, "1.21", 2015, 4, MC, "In a servo-system, the device used for providing derivative feedback is known as", ["Synchro", "Servomotor", "Potentiometer", "Techogenerator"], "D")
Q(n0, "1.22", 2015, 4, PZ, r"The transfer function of any stable system which has no zeros or poles in the right half of the s-plane is said to be", ["Minimum phase transfer function", "Non-minimum phase transfer function", "Minimum frequency response function", "Minimum gain transfer function"], "A", "A")
Q(n0, "1.23", 2017, 4, PZ, "A dominant pole is determined as", ["the highest frequency pole among all poles.", "the lowest frequency pole at least two octaves lower than other poles.", "the lowest frequency pole among all poles.", "the highest frequency pole at least two octaves higher than other poles."], "C", "D")
Q(n0, "1.24", 2018, 4, SFG, "Consider the following statements for signal flow graph:\n1. It represents linear as well as non-linear systems.\n2. It is not unique for a given system.\nWhich of the above statements is /are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "B", "B")
Q(n0, "1.25", 2018, 4, BD, r"The open-loop transfer function of a system is $$\dfrac{10K}{1+10s}$$ When the system is converted into a closed-loop with unity feedback, the time constant of the system is reduced by a factor of 20. The value of $K$ is", ["$1.9$", "$1.6$", "$1.3$", "$1.0$"], "A", "A")
Q(n0, "1.26", 2018, 4, BD, r"The closed-loop transfer function $\dfrac{C(s)}{R(s)}$ of the system represented by the block diagram in the figure is", [r"$\dfrac{1}{(s+1)^2}$", r"$\dfrac{1}{s+1}$", r"$s+1$", "$1$"], "B", "B", fig=q126())
Q(n0, "1.27", 2019, 4, FB, "The price for improvement in sensitivity by the use of feedback is paid in terms of", ["loss of system gain", "rise of system gain", "improvement in transient response, delayed response", "poor transient response"], "A", "B")
Q(n0, "1.28", 2019, 4, BD, r"Consider the following open-loop transfer function: $$G=\dfrac{K(s+2)}{(s+1)(s+4)}$$ The characteristic equation of the unity negative feedback will be",
  [r"$(s+1)(s+4)+K(s+2)=0$", r"$(s+2)(s+1)+K(s+4)=0$", r"$(s+1)(s-2)+K(s+4)=0$", r"$(s+2)(s+4)+K(s+1)=0$"], "A", "A")
Q(n0, "1.29", 2020, 4, SFG, "The signal flow graph of a system is constructed from its", ["Differential equations", "Algebraic equations", "Algebraic equations through the cause-and-effect relations", "Differential equations through the cause-and-effect relations"], "C")
Q(n0, "1.30", 2020, 5, FB, "The important aspects in the study of feedback systems are to control\n1. Sensitivity\n2. Effect of an internal disturbance\n3. Distortion in a nonlinear system", ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "D", "D")
Q(n0, "1.31", 2022, 5, FB, "The subsystem that generates the input to the plant or process is known as", ["controller", "controlled variable", "controllability", "compensator"], "A", "A")
Q(n0, "1.32", 2023, 5, TFL, r"The open-loop DC gain of a unity negative feedback system with closed-loop transfer function $\dfrac{s+4}{s^2+7s+13}$ is", [r"$\dfrac{4}{13}$", r"$\dfrac{2}{3}$", r"$\dfrac{1}{3}$", r"$\dfrac{4}{9}$"], "D", "D")

# ======================================================================= CHAPTER 3  (n3: 3.21-3.44, n2: 3.45-3.46)
RH, SC = "Routh-Hurwitz Criterion", "Stability Concepts"
n3, n2 = "n3", "n2"
Q(n3, "3.21", 2009, 38, RH, r"The characteristic equation of a control system is given as $$s^4+4s^3+4s^2+3s+K=0$$ What is the value of $K$ for which this system is marginally stable?", [r"$\dfrac{9}{16}$", r"$\dfrac{19}{16}$", r"$\dfrac{29}{16}$", r"$\dfrac{39}{16}$"], "D", "D")
Q(n3, "3.22", 2010, 38, RH, "The characteristic equation of the below closed-loop system is", [r"$s^2+11s+10=0$", r"$s^2+11s+130=0$", r"$s^2+10s+120=0$", r"$s^2+10s+12=0$"], "B", "B",
  fig=chain_loop([("4", 50), (r"\dfrac{3}{s+1}", 90)], fb=r"\dfrac{10}{s+10}", rin="R(s)", cout="Y(s)"))
Q(n3, "3.23", 2011, 38, RH, r"The characteristic equation of a control system is given as $$s^4+8s^3+24s^2+32s+K=0$$ What is the value of $K$ for which the system is unstable?", ["$10$", "$20$", "$60$", "$100$"], "D", "D")
Q(n3, "3.24", 2012, 38, SC, r"The characteristic equation of a particular system is given by $s^3+2s^2+6s+12=0$. The damping ratio $\delta$ will be", [r"$\delta=0$", r"$0<\delta<1$", r"$\delta=1$", r"$\delta>1$"], "A", "B")
Q(n3, "3.25", 2012, 38, RH, r"The range of $K$ for stability of a feedback system whose open-loop transfer function is $$G(s)=\dfrac{K}{s(s+1)(s+2)}$$", [r"$0<K<3$", r"$0<K<6$", r"$K>6$", r"$0>K>3$"], "B", "B")
Q(n3, "3.26", 2013, 38, SC, "The critical value of gain for a system is 40. The system is operating at a gain of 20. The gain margin of the system is", ["2 dB", "3 dB", "6 dB", "4 dB"], "C", "C")
Q(n3, "3.27", 2013, 38, RH, r"A feedback system with characteristic equation $s^4+20Ks^3+5s^2+10s+15=0$ is", [r"stable for all values of $K$", r"stable only for $K\ge 0$", r"stable for $\infty>K>70$", r"Unstable for all values of $K$"], "D", "B")
Q(n3, "3.28", 2013, 38, RH, r"The system having the characteristic equation $s^3+4s^2+s-6+K=0$ will be stable for", [r"$K>6$", r"$0<K<6$", r"$6<K<10$", r"$0<K<10$"], mark="C")
Q(n3, "3.29", 2014, 38, RH, r"The loop transfer function of a system is $\dfrac{K}{s(s+1)(s+5)}$. The loop gain $K$ is adjusted for inducing sustained oscillations. What is the value of $K$ for this objective?", ["$15$", "$25$", "$30$", "$45$"], mark="C")
Q(n3, "3.30", 2014, 38, RH, r"The number of roots of the equation $2s^4+s^3+3s^2+5s+7=0$ which lie in the right half of s-plane is", ["$0$", "$1$", "$2$", "$3$"], mark="C")
Q(n3, "3.31", 2014, 38, SC, "Which one of the following statements is correct?", ["Phase margin is always positive for stable feedback system.", "Phase margin is always negative for stable feedback system.", "Phase margin can be negative or positive for stable feedback system.", "None of the above"], mark="A")
Q(n3, "3.32", 2015, 38, SC, "The effects of feedback on stability and sensitivity are",
  ["Negative feedback improves stability and system response is less sensitive to external inputs and parameter variations", "Feedback does not affect stability but system response is insensitive to disturbances and parameter variations",
   "Feedback does not affect stability and system response is sensitive to disturbances and parameter variations", "Negative feedback affects stability and system response is more sensitive to disturbances and parameter variations"], mark="A")
Q(n3, "3.33", 2015, 39, SC, r"Given that the transfer function $G(s)=\dfrac{K}{s^2(1+sT)}$, the type and order of this system are respectively", ["5 and 2", "2 and 2", "2 and 3", "3 and 3"], mark="C")
Q(n3, "3.34", 2015, 39, RH, r"The oscillation frequency of the system with the characteristic equation $$s^6+2s^5+3s^4+4s^3+3s^2+2s+1=0$$ is", [r"$+1$ radian/sec", r"$-1$ radian/sec", r"$j1$ radian/sec", r"$-j1$ radian/sec"], mark="C")
Q(n3, "3.35", 2015, 39, RH, r"The feedback system with characteristic equation $$s^4+20Ks^3+5s^2+10s+15=0$$ is", [r"Stable for all values of $K$", r"Stable for positive values of $K$", r"Stable for $7.0<K<\infty$", r"Unstable for any value of $K$"])
Q(n3, "3.36", 2016, 39, RH, r"The characteristic equation of a certain feedback control system is given by $s^4+4s^3+13s^2+36s+K=0$. The range of values of $K$ for which the feedback system is stable, is given by", [r"$0<K<4$", r"$4<K<36$", r"$0<K<36$", r"$13<K<36$"])
Q(n3, "3.37", 2017, 39, RH, r"A unity feedback system has open-loop transfer function with two of its poles located at $-0.1$, $1$; and two zeros located at $-2$ and $-1$ with a variable gain $K$. For what value(s) of $K$ would the closed-loop system have one pole in the right half of the s-plane.", [r"$K>0.3$", r"$K<0.05$", r"$0.05<K<0.3$", r"$K>0$"], mark="B")
Q(n3, "3.38", 2017, 39, RH, r"The open-loop transfer function of a unity feedback control system is $$G(s)H(s)=\dfrac{10}{s(s+2)(s+K)}$$ Here $K$ is a variable parameter. The system will be stable for all values of", [r"$K>-2$", r"$K>0$", r"$K>1$", r"$K>1.45$"], mark="D")
Q(n3, "3.39", 2018, 39, RH, "Consider the stability of the system shown in the figure when analyzed with a positive real value of gain $K$ in\n1. open-loop configuration\n2. closed-loop configuration",
  ["Both 1 and 2 are stable", "1 is stable and 2 is unstable", "1 is unstable and 2 is stable", "Both 1 and 2 are unstable"], mark="C", fig=ufb(r"\dfrac{K(s+1)}{s^2(s+2)}"), after="Which of the following statements is correct?")
Q(n3, "3.40", 2019, 39, RH, r"If the characteristic equation of a feedback control system is given by, $$s^4+20s^3+15s^2+2s+K=0$$ then the range of values of $K$ for the system to be stable will be", [r"$1<K<2.49$", r"$0<K<1.49$", r"$1<K<4.49$", r"$0<K<3.49$"], mark="B")
Q(n3, "3.41", 2020, 39, SC, "If all the roots of the characteristic equation have negative real parts, the system is", ["Stable", "Unstable", "Marginally stable", "Conditionally stable"], mark="A")
Q(n3, "3.42", 2020, 39, SC, r"If any root of the characteristic equation has a positive real part or if there is a repeated root on the $j\omega$-axis, then the system is", ["Limitedly stable", "Conditionally stable", "Stable", "Unstable"], mark="D")
Q(n3, "3.43", 2021, 39, RH, r"A feedback system has an open-loop transfer function of $$G(s)H(s)=\dfrac{K(1-s)}{s(s^2+5s+9)}$$ By using the Routh criterion, the maximum value of $K$ for the closed-loop system to be stable is", ["$2.5$", "$5$", "$7.5$", "$9$"], "C")
Q(n3, "3.44", 2024, 39, RH, r"A feedback system has an open loop transfer function of $$G(s)H(s)=\dfrac{K(1-s)}{s(s^2+5s+9)}$$ The maximum value of $K$ for the closed loop system to be stable is", ["$3.5$", "$4.8$", "$6.5$", "$7.5$"], "D", "D")
Q(n2, "3.45", 2024, 40, RH, r"The system represented by $$5s^6+8s^5+12s^4+20s^3+100s^2+150s+200=0$$ is", ["a stable system having all poles in the right half of the s-plane.", "an unstable system having one pole in the right half of the s-plane.", "a stable system having one pole in the right half of the s-plane.", "an unstable system having two poles in the right half of the s-plane."], "D")
Q(n2, "3.46", 2024, 40, RH, r"For the unity feedback system given by $$G(s)=\dfrac{K}{s(s+1)(s+2)}$$ the range of $K$ for stability is", [r"$0<K<2$", r"$0<K<3$", r"$0<K<6$", r"$1<K<6$"], "C")

# ======================================================================= CHAPTER 4 (n7: 4.1-4.7, n5: 4.8-4.26, n6: 4.27-4.46)
RP, AC, BA, PG = "Root Locus Properties", "Asymptotes & Centroid", "Breakaway Points", "Root Locus Plots & Gain"
n7, n5, n6 = "n7", "n5", "n6"
Q(n7, "4.1", 2000, 47, AC, r"The intersection of asymptotes of root-loci of a system with open-loop transfer function $$G(s)H(s)=\dfrac{K}{s(s+1)(s+3)}$$ is", ["$1.44$", "$1.33$", "$-1.44$", "$-1.33$"], mark="D")
Q(n7, "4.2", 2001, 47, BA, r"The root locus plot of the system having the loop transfer function $$G(s)H(s)=\dfrac{K}{s(s+4)(s^2+4s+5)}$$ has", ["no breakaway point", "three real breakaway points", "only one breakaway point", "one real and two complex breakaway points"])
Q(n7, "4.3", 2001, 47, AC, r"An open loop transfer function is given by $$G(s)H(s)=\dfrac{K(s+1)}{s(s+2)(s^2+2s+2)}$$ It has", ["one zero at infinity", "two zeros at infinity", "three zeros at infinity", "four zeros at infinity"], mark="C")
Q(n7, "4.4", 2002, 47, PG, "Which of the following is the open loop transfer function of the root loci shown in figure?", [r"$\dfrac{K}{s(s+T_1)^2}$", r"$\dfrac{K}{(s+T_1)(s+T_2)^2}$", r"$\dfrac{K}{(s+T_1)^3}$", r"$\dfrac{K}{s^2(sT_1+1)}$"], mark="D", fig=q44())
Q(n7, "4.5", 2002, 47, RP, "The instrument used for plotting the root locus is called", ["Slide rule", "Spirule", "Synchro", "Selsyn"])
Q(n7, "4.6", 2002, 47, RP, r"A control system has $$G(s)H(s)=\dfrac{K(s+1)}{s(s+3)(s+4)}$$ Root locus of the system can lie on the real axis", [r"between $s=-1$ and $s=-3$", r"between $s=0$ and $s=-4$", r"between $s=-3$ and $s=-4$", r"towards left of $s=-4$"], mark="C")
Q(n7, "4.7", 2003, 47, PG, "The below figure shows the root locus of a unity feedback system. The open loop transfer function of the system is", [r"$\dfrac{K}{s(s+1)(s+2)}$", r"$\dfrac{Ks}{(s+1)(s+2)}$", r"$\dfrac{K(s+1)}{s(s+2)}$", r"$\dfrac{K(s+2)}{s(s+1)}$"], mark="D", fig=q47())
Q(n5, "4.8", 2003, 48, RP, "Which one of the following application softwares is used to obtain an accurate root locus plot?", ["LISP", "MATLAB", "dBase", "Oracle"])
Q(n5, "4.9", 2003, 48, RP, "Which one of the following techniques is utilized to determine the actual point at which the root locus crosses the imaginary axis?", ["Nyquist technique", "Routh-Hurwitz criterion", "Nichol's criterion", "Bode technique"], mark="B")
Q(n5, "4.10", 2004, 48, AC, r"The root loci of a feedback control system for large values of $s$ are asymptotic to the straight lines with angles $\theta$ to the real axis given by which one of the following?", [r"$\dfrac{(p-z)\pi}{2k+1}$", r"$\dfrac{(2k+1)\pi}{p-z}$", r"$2k(p-z)$", r"$\dfrac{2k}{p}\,z$"],
  mark="B", after=r"where $p=$ Number of finite poles of $G(s)H(s)$, $z=$ Number of finite zeros of $G(s)H(s)$ and $k=0,1,2,\ldots$")
Q(n5, "4.11", 2004, 48, RP, "**Assertion (A):** The number of branches of root locus terminating on infinity is equal to the number of open loop poles minus the number of zeros.\n**Reason (R):** Segment of the real axis having an odd number of real axis open loop poles plus zeros to their right are parts of the root locus.", AR, mark="B")
Q(n5, "4.12", 2005, 48, RP, "Which one of the following is not a property of root loci?", [r"The root locus is symmetrical about $j\omega$ axis.", "They start from the open loop poles and terminate at the open loop zeros.", r"The breakaway points are determined from $dK/ds=0$.", "Segments of the real axis are part of the root locus, if and only if, the total number of real poles and zeros to their right is odd."], mark="A")
Q(n5, "4.13", 2006, 48, RP, "In root locus, what is the number of separate loci?", [r"The number of zeros of the open loop transfer function", r"The number of poles of $G(s)H(s)$", "The number of roots of the characteristic equation with positive real part", "The number of zeros of the characteristic equation with the negative real parts"])
Q(n5, "4.14", 2006, 48, AC, r"For a given unity feedback system with $$G(s)=\dfrac{K(s+3)}{s(s+1)(s+2)(s+5)}$$ what is the real axis intercept for root locus asymptotes?", [r"$2/3$", r"$1/4$", r"$-5/3$", r"$-3/2$"], mark="C")
Q(n5, "4.15", 2007, 48, PG, "Which one of the following open-loop transfer functions has root locus parallel to imaginary axis?", [r"$K/(s+1)$", r"$K(s+1)/(s+2)^2$", r"$K/(s+2)^2$", r"$K(s+2)/(s+1)^2$"], mark="C")
Q(n5, "4.16", 2007, 48, RP, "What is the number of root-locus segments which do not terminate on zeros?", ["The number of poles", "The number of zeros", "The difference between the number of poles and the number of zeros", "The sum of the number of poles and the number of zeros"], mark="C")
Q(n5, "4.17", 2008, 48, PG, "Consider the root loci plots:", ["1", "2", "3", "4"], mark="B", fig=q417(), after="Which one of the above plots is not correct?")
Q(n5, "4.18", 2008, 49, RP, "Which one of the following statements is correct for root loci?", ["The root loci are asymmetrical with respect to the real axis", "The root loci are symmetrical with respect to the real axis", "The root locus lies in a section of the real axis to the left of which an even number of poles and zeros of open loop system are present", "The root locus lies in a section of the real axis to the right of which an even number of poles and zeros of open loop system are present"], mark="B")
Q(n5, "4.19", 2008, 49, RP, "Which one of the following is correct? The root locus is the path of the roots of the characteristic equation traced out in the s-plane", ["as the input of the system is changed", "as the output of the system is changed", "as a system parameter is changed", "as the sensitivity is changed"], mark="C")
Q(n5, "4.20", 2009, 49, BA, r"Consider the equation $$s^2+2s+2+K(s+2)=0.$$ Where do the roots of this equation break on the root loci plot?", [r"$-3.414$", r"$-2.414$", r"$-1.414$", r"$-0.414$"], mark="A")
Q(n5, "4.21", 2009, 49, RP, r"How many number of branches the root loci of the equation $s(s+2)(s+3)+K(s+1)=0$ have?", ["Zero", "One", "Two", "Three"], mark="C")
Q(n5, "4.22", 2010, 49, RP, "If the gain of the system is reduced to zero value, the roots of the system in the s-plane", ["Coincide with zeros", "Move away from the zeros", "Move away from the poles", "Coincide with the poles"], mark="D")
Q(n5, "4.23", 2010, 49, RP, "The addition of open loop zero pulls the root-loci towards", ["The left and therefore system becomes more stable", "The right and therefore system becomes unstable", "Imaginary axis and therefore system becomes marginally stable", "The left and therefore system becomes unstable"], mark="A")
Q(n5, "4.24", 2011, 49, RP, r"Where are the $K=\pm\infty$ points on the root loci of the characteristic equation of the closed loop control system located at?", [r"Poles of $G(s)H(s)$", r"Zeros of $G(s)H(s)$", r"Both Zeros and Poles of $G(s)H(s)$", r"Neither at Zeros nor at Poles of $G(s)H(s)$"], mark="B")
Q(n5, "4.25", 2011, 49, AC, r"The characteristic equation of a control system is given as $$1+\dfrac{K(s+1)}{s(s+4)(s^2+2s+2)}=0$$ For large values of $s$, the root loci for $K\ge0$ are asymptotic to asymptotes, where do the asymptotes intersect on the real axis?", [r"$\dfrac{5}{3}$", r"$-\dfrac{2}{3}$", r"$-\dfrac{5}{3}$", r"$\dfrac{4}{3}$"], mark="C")
Q(n5, "4.26", 2011, 49, RP, r"Where are the $K=0$ points on the root loci of the characteristic equation of the closed loop control system located at?", [r"Zeros of $G(s)H(s)$", r"Poles of $G(s)H(s)$", r"Both Zeros and Poles of $G(s)H(s)$", r"Neither at Zeros nor at Poles of $G(s)H(s)$"], mark="B")
Q(n6, "4.27", 2011, 50, PG, r"Given the root locus of a system $$G(s)=\dfrac{4K}{(s+1)(s+3)}$$ What will be the gain for obtaining the damping ratio 0.707?", [r"$1/4$", r"$5/4$", r"$-3/4$", r"$11/4$"], fig=q427())
Q(n6, "4.28", 2011, 50, RP, "The number of individual loci in a root locus plot is equal to", ["The number of open loop poles", "The number of open loop zeros", "The difference of the number of open loop poles and the number of open loop zeros", "The number of open loop poles or zeros whichever is greater"])
Q(n6, "4.29", 2012, 50, RP, "**Statement (I):** Root loci are symmetrical with respect to real axis of the s-plane.\n**Statement (II):** Root loci are normally symmetrical with respect to the perpendicular axis of symmetry of the pole-zero combination of the loop transfer function.", SR)
Q(n6, "4.30", 2012, 50, AC, r"If a feedback control system has its open-loop transfer function $$G(s)H(s)=\dfrac{K}{[s(s+2)(s^2+2s+5)]}$$ the coordinates of the centroid of the asymptotes of its root-locus are", [r"$-1$ and $0$", r"$1$ and $0$", r"$0$ and $-1$", r"$0$ and $1$"])
Q(n6, "4.31", 2012, 50, RP, "If root loci plots of a particular control system do not intersect the imaginary axis at any point, then the gain margin of the system will be", ["zero", "0.707", "1.0", "infinite"])
Q(n6, "4.32", 2013, 50, PG, r"Consider the transfer function $$KG(s)H(s)=\dfrac{K}{s^3+4s^2+s-6}$$ The root-locus plot of the system passes through $s=0$. The value of $K$ at this point will be", ["$10$", "$0$", "$6$", "$8$"])
Q(n6, "4.33", 2013, 50, PG, r"A system has its open-loop transfer function of $\dfrac{K}{s(s^2+6s+10)}$. The break-points are at $s=-1.18$ and $s=-2.82$, the centroid is at $s=-2$, while the asymptotic angles are $\pm60^\circ$ and $\pm180^\circ$. The value of $K$ for the closed loop system to be oscillatory and the frequency of oscillations are respectively:", ["600 and 10 rad/sec", "120 and 5 rad/sec", "60 and 3.16 rad/sec", "30 and 3.16 rad/sec"])
Q(n6, "4.34", 2014, 50, RP, "When the number of poles is equal to the number of zeros, how many branches of root locus tend towards infinity?", ["1", "2", "0", "equal to number of zeros"])
Q(n6, "4.35", 2014, 50, PG, r"The open-loop transfer function of a unity feedback control system is $G(s)=\dfrac{1}{(s+2)^2}$. The closed-loop transfer function will have poles at", [r"$-2,\ -2$", r"$-2,\ -1$", r"$-2\pm j$", r"$-2,\ 2$"])
Q(n6, "4.36", 2015, 50, RP, r"The number of branches of the root loci of the equation $s(s+4)(s+5)+K(s+2)=0$ is (when $K$ varies from $-\infty$ to $+\infty$)", ["$2$", "$3$", "$4$", "$5$"])
Q(n6, "4.37", 2016, 51, BA, r"Consider the system with $G(s)=\dfrac{K(s+2)}{s^2+2s+3}$ and $H(s)=1$. The breakaway point(s) of the root loci is/are at", [r"$-0.265$ only", r"$-3.735$ only", r"$-3.735$ and $-0.265$", "There is no breakaway point"])
Q(n6, "4.38", 2016, 51, PG, "The main objectives of drawing the root-locus plot are\n1. To obtain a clear picture of the open-loop poles and zeros of the system.\n2. To obtain a clear picture of the transient response of the system for varying gain, $K$.\n3. To find the range of $K$ to make the system stable.\nWhich of the above statements are correct?", ["1, 2 and 3", "1 and 2 only", "1 and 3 only", "2 and 3 only"])
Q(n6, "4.39", 2016, 51, AC, r"A unity feedback system has open-loop poles at $s=-2\pm j2$, $s=-1$ and $s=0$ and a zero at $s=-3$. What are the angles made by the root-loci asymptotes with the real axis?", [r"$60^\circ,\ 180^\circ$ and $-60^\circ$", r"$30^\circ,\ 90^\circ$ and $60^\circ$", r"$60^\circ,\ 120^\circ$ and $-30^\circ$", r"$30^\circ,\ 60^\circ$ and $180^\circ$"])
Q(n6, "4.40", 2016, 51, RP, "**Statement (I):** The complex conjugate poles and zeros of the open-loop transfer function have no effect on the root-loci on the real axis.\n" r"**Statement (II):** Angle contribution of such a pair of conjugate poles or zeros is $2\pi$ radians on the real axis.", SR)
Q(n6, "4.41", 2017, 51, PG, "Consider that in a system loop transfer function, addition of a pole results in the following:\n1. Root locus gets pulled to the right-hand side.\n2. Steady-state error is increased.\n3. System response gets slower.\nWhich of the above are correct?", S4, mark="A")
Q(n6, "4.42", 2018, 51, BA, r"For the open-loop system $$G(s)H(s)=\dfrac{K}{s(s+1)(s+2)}$$ the breakaway point is", [r"$-0.23$", r"$-0.42$", r"$-1.47$", r"$-3.47$"], mark="C")
Q(n6, "4.43", 2019, 51, AC, r"Consider a feedback system with the characteristic equation $$1+K\dfrac{1}{s(s+1)(s+2)}=0$$ The asymptotes of the three branches of root locus plot of this system will form the following angles with the real axis", [r"$60^\circ,\ 120^\circ$ and $300^\circ$", r"$60^\circ,\ 120^\circ$ and $180^\circ$", r"$60^\circ,\ 180^\circ$ and $300^\circ$", r"$40^\circ,\ 120^\circ$ and $200^\circ$"])
Q(n6, "4.44", 2020, 51, RP, "The angle of departure from a real open-loop pole and the angle of arrival at a real open-loop zero is always equal to", [r"$0^\circ$ only", r"$90^\circ$ only", r"$180^\circ$ only", r"$0^\circ$ or $180^\circ$"], mark="D")
Q(n6, "4.45", 2022, 51, RP, "Which one of the following techniques can be used to analyze and design the effect of loop gain upon the system's transient response and stability?", ["Open-loop transfer function technique.", "Closed-loop transfer function technique.", "Root locus technique", "Compensation technique"], mark="C")
Q(n6, "4.46", 2024, 51, BA, r"What are the breakaway points of the root locus of a unity feedback system with open loop transfer function $G(s)=\dfrac{K(s+2)}{(s+1)^2}$?", [r"$-1,\ 2$", r"$-1,\ 3$", r"$-1,\ -2$", r"$-1,\ -3$"], mark="D")

# ---------------------------------------------------------------------------------- batches
import os
from collections import OrderedDict
FILES = {
 "n0": "01-modeling-and-block-diagrams/WhatsApp Image 2026-10-14 at 01.57.23 (1).jpeg",
 "n1": "01-modeling-and-block-diagrams/WhatsApp Image 2026-10-14 at 01.57.23.jpeg",
 "n2": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 01.59.56 (1).jpeg",
 "n3": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 01.59.56 (2).jpeg",
 "n4": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 01.59.56.jpeg",   # same page as n2 (duplicate photo)
 "n5": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 02.01.54 (1).jpeg",
 "n6": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 02.01.54.jpeg",
 "n7": "03-stability-and-root-locus/WhatsApp Image 2026-10-14 at 02.01.55.jpeg",
}
BANK = "paper-2-ece/08-control-systems/"
by = OrderedDict((k, []) for k in FILES)
for k, d in QS:
    by[k].append(d)
batch = [{"image": BANK + FILES[k], "questions": v} for k, v in by.items()]
json.dump(batch, open('/private/tmp/claude-501/-Users-alok-Desktop-ESE/351e66c8-e2cb-4170-8386-ec0e7f9de92d/scratchpad/batch_new.json', 'w'), ensure_ascii=False, indent=1)
nums = [d["number"] for _, d in QS]
print(len(QS), "questions;", len(set(nums)), "unique;", sum(1 for _, d in QS if d.get("answer")), "with verified key;", sum(1 for _, d in QS if d.get("figure")), "figures")
exp = [f"1.{i}" for i in range(1, 33)] + [f"3.{i}" for i in range(21, 47)] + [f"4.{i}" for i in range(1, 47)]
print("missing:", sorted(set(exp) - set(nums)), "extra:", sorted(set(nums) - set(exp)))
