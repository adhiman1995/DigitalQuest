"""Digitized ESE-Prelims questions 5.1-5.102 (Control Systems ch.5 'Frequency Domain Analysis').
Splits into the Frequency Response and Nyquist Stability chapter folders.
Run:  python3 chapter_5_freq_nyquist.py <out.json>   then   node scripts/ingest.js <out.json>
Verified `answer` only where the book's printed answer key / explanation heading was photographed (5.1,5.2,5.3,5.10,5.19,5.28,5.37,5.46,5.55,5.64,5.73,5.82,5.91,5.100).
"""
import sys, json
sys.path.insert(0, '/Users/alok/Desktop/ESE/ese-tracker/scripts/authoring')
from figs import *
from figs_freq import *

AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"]
SR = ["Both Statement (I) and Statement (II) are individually true and Statement (II) is the correct explanation of Statement (I)", "Both Statement (I) and Statement (II) are individually true but Statement (II) is not the correct explanation of Statement (I)", "Statement (I) is true but Statement (II) is false", "Statement (I) is false but Statement (II) is true"]

FR = "paper-2-ece/08-control-systems/04-frequency-response"
NY = "paper-2-ece/08-control-systems/05-nyquist-stability"
F = {
 "p6": "WhatsApp Image 2026-10-14 at 17.34.43 (1).jpeg",   # opener, 5.1-5.6
 "p7": "WhatsApp Image 2026-10-14 at 17.34.43.jpeg",       # pp 58-59, 5.7-5.21
 "p4": "WhatsApp Image 2026-10-14 at 17.34.41.jpeg",       # pp 60-61, 5.22-5.39
 "p2": "WhatsApp Image 2026-10-14 at 17.34.40 (1).jpeg",   # pp 62-63, 5.40-5.57
 "p5": "WhatsApp Image 2026-10-14 at 17.34.42.jpeg",       # pp 64-65, 5.58-5.80
 "p1": "WhatsApp Image 2026-10-14 at 17.34.39.jpeg",       # pp 66-67, 5.81-5.96
 "p3": "WhatsApp Image 2026-10-14 at 17.34.40.jpeg",       # p 68,     5.97-5.102
}
QS = []
def Q(img, n, year, page, topic, text, opts, key=None, mark=None, fig=None, lists=None, table=None, after=None, ny=False):
    d = {"number": f"5.{n}", "year": year, "page": page, "topic": topic, "text": text, "options": opts, "folder": NY if ny else FR}
    if key: d["answer"] = key
    if mark: d["marked"] = mark
    if fig: d["figure"] = fig
    if lists: d["lists"] = lists
    if table: d["table"] = table
    if after: d["after"] = after
    QS.append((img, d))

BODE, POL, NYQ, MARG, RES, MP, BASIC, COMP = "Bode Plot", "Polar Plot", "Nyquist Plot & Criterion", "Gain & Phase Margin", "Resonant Peak & Bandwidth", "Minimum / Non-minimum Phase", "Frequency Response Basics", "Frequency-Domain Compensation"

# ================================================================= p6  (chapter opener)
Q("p6", 1, 2000, 57, BASIC, "Match List-I (Scientist) with List-II (Contribution in the area of) and select the correct answer:",
  ["A–1, B–4, C–2", "A–2, B–3, C–4", "A–3, B–1, C–4", "A–1, B–3, C–2"], "D", "A",
  lists=[{"title": "List-I", "items": [["A", "Bode"], ["B", "Evans"], ["C", "Nyquist"]]}, {"title": "List-II", "items": [["1", "Asymptotic plots"], ["2", "Polar plots"], ["3", "Root-locus technique"], ["4", "Constant M and N plots"]]}])
Q("p6", 2, 2000, 57, MARG, "The polar plot (for positive frequencies) for the open-loop transfer function of a unity feedback control system is shown in the given figure. The phase margin and the gain margin of the system are respectively",
  [r"$150^\circ$ and $4$", r"$150^\circ$ and $3/4$", r"$30^\circ$ and $4$", r"$30^\circ$ and $3/4$"], "A", "A", fig=q52())
Q("p6", 3, 2001, 57, MARG, r"The open loop transfer function of a system is $$G(s)H(s)=\dfrac{K}{(1+s)(1+2s)(1+3s)}$$ The phase crossover frequency $\omega_{pc}$ is",
  [r"$\sqrt{2}$", "$1$", "zero", r"$\sqrt{3}$"], "B")
Q("p6", 4, 2001, 57, NYQ, "Nyquist plot shown in the given figure is for a type", ["zero system", "one system", "two system", "three system"], mark="B", fig=q54(), ny=True)
Q("p6", 5, 2001, 57, MARG, r"The open-loop transfer function of a unity feedback control system is given as $$G(s)=\dfrac{1}{s(1+sT_1)(1+sT_2)}$$ The phase crossover frequency and the gain margin are, respectively",
  [r"$\dfrac{1}{\sqrt{T_1T_2}}$ and $\dfrac{T_1+T_2}{T_1T_2}$", r"$\sqrt{T_1T_2}$ and $\dfrac{T_1+T_2}{T_1T_2}$", r"$\dfrac{1}{\sqrt{T_1T_2}}$ and $\dfrac{T_1T_2}{T_1+T_2}$", r"$\sqrt{T_1T_2}$ and $\dfrac{T_1T_2}{T_1+T_2}$"], mark="A")
Q("p6", 6, 2001, 57, BODE, "An open loop transfer function of a unity feedback control system has two finite zeros, two poles at origin and two pairs of complex conjugate poles. The slope of high frequency asymptote in Bode magnitude plot will be",
  ["$+40$ dB/decade", "$0$ dB/decade", "$-40$ dB/decade", "$-80$ dB/decade"], mark="D")

# ================================================================= p7  (pp. 58-59)
Q("p7", 7, 2001, 58, MP, "Open loop transfer function of a system having one zero with a positive real value is called", ["zero phase function", "negative phase function", "positive phase function", "non-minimum phase function"], mark="D")
Q("p7", 8, 2002, 58, NYQ, r"The Nyquist plot of $$G(s)H(s)=\dfrac{10}{s^2(1+0.5s)(1+s)}$$",
  [r"will start ($\omega=\infty$) in the first quadrant and will terminate ($\omega=0$) in the second quadrant", r"will start ($\omega=\infty$) in the fourth quadrant and will terminate ($\omega=0$) in the second quadrant",
   r"will start ($\omega=\infty$) in the second quadrant and will terminate ($\omega=0$) in the third quadrant", r"will start ($\omega=\infty$) in the first quadrant and will terminate ($\omega=0$) in the fourth quadrant"], mark="A", ny=True)
Q("p7", 9, 2002, 58, NYQ, r"Which of the following is the Nyquist diagram for the open loop function $$G(s)\cdot H(s)=\dfrac{5}{s(1+0.1s)(1+0.01s)}\ ?$$", ["Plot (a)", "Plot (b)", "Plot (c)", "Plot (d)"], mark="C", fig=q59(), ny=True)
Q("p7", 10, 2002, 58, MARG, "Consider the following statements associated with phase and gain margins:\n1. They are a measure of closeness of the polar plot to the $-1+j0$ point\n2. For a non-minimum phase to be stable it must have positive phase and gain margins\n3. For a minimum phase system to be stable, both the margins must be positive\nWhich of the above statements is/are correct?",
  ["2 and 3", "1 and 3", "1 and 2", "1 alone"], "B", "B")
Q("p7", 11, 2002, 58, MP, r"**Assertion (A):** $G(s)=\dfrac{10(s-25)}{s(s+1)(s+5)}$ represents a non-minimum phase transfer function." "\n" r"**Reason (R):** A minimum phase transfer function has the property that its magnitude and phase are uniquely related.", AR, mark="B")
Q("p7", 12, 2002, 58, RES, "**Assertion (A):** The bandwidth of a control system indicates the noise filtering characteristic of the system.\n**Reason (R):** The bandwidth is a measure of ability of a control system to reproduce the input signal.", AR)
Q("p7", 13, 2002, 58, RES, "**Assertion (A):** Addition of a pole to the open loop transfer function of a system increases the rise time of the closed-loop step-response.\n**Reason (R):** Additional pole has the effect of reducing the bandwidth of the system.", AR)
Q("p7", 14, 2002, 58, COMP, "Consider the following performance characteristics:\n1. Reduced velocity constant for a given relative stability.\n2. Reduced gain cross-over frequency\n3. Reduced bandwidth\n4. Reduced resonance peak of the system\nWhich of these performance characteristics are achieved with the phase-lag compensation?",
  ["1 and 2", "1 and 3", "2, 3 and 4", "1, 2, 3 and 4"])
Q("p7", 15, 2003, 58, MARG, "Consider the following open loop frequency response of a unity feedback system:",
  ["$0.00$ dB, $-180^\\circ$", "$3.86$ dB, $-180^\\circ$", "$0.00$ dB, $-10^\\circ$", "$3.86$ dB, $10^\\circ$"], mark="D",
  table={"head": [r"$\omega$ (rad/s)", "2", "3", "4", "5", "6", "8", "10"],
         "rows": [[r"$|G(j\omega)|$", "7.5", "4.8", "3.15", "2.25", "1.70", "1.00", "0.64"], [r"$\angle G(j\omega)$", r"$-118^\circ$", r"$-130^\circ$", r"$-140^\circ$", r"$-150^\circ$", r"$-157^\circ$", r"$-170^\circ$", r"$-180^\circ$"]]},
  after="The gain and phase margin of the system are respectively")
Q("p7", 16, 2003, 59, NYQ, "The Nyquist plot shown below matches with the transfer function", [r"$\dfrac{1}{(s+1)^3}$", r"$\dfrac{1}{(s+1)^2}$", r"$\dfrac{1}{s^2+2s+2}$", r"$\dfrac{1}{s+1}$"], mark="B", fig=q516(), ny=True)
Q("p7", 17, 2003, 59, MARG, r"The phase margin (PM) and the damping ratio ($\xi$) are related by",
  [r"$PM=90^\circ-\tan^{-1}\left\{\dfrac{\sqrt{-2\xi^2+\sqrt{1+4\xi^4}}}{2}\right\}$", r"$PM=\tan^{-1}\left\{\dfrac{2\xi}{\sqrt{-2\xi^2+\sqrt{1+4\xi^4}}}\right\}$",
   r"$PM=90^\circ+\tan^{-1}\left\{\dfrac{\sqrt{2\xi^2+\sqrt{1+4\xi^4}}}{2\xi}\right\}$", r"$PM=180^\circ-\tan^{-1}\left\{\dfrac{\sqrt{2\xi^2-\sqrt{1+4\xi^4}}}{2}\right\}$"])
Q("p7", 18, 2003, 59, BODE, "Consider the following statements regarding the frequency response of a system as shown below:\n1. The type of the system is one\n2. $\\omega_3=$ static error coefficient (numerically)\n3. $\\omega_2=\\dfrac{\\omega_1+\\omega_3}{2}$\nSelect the correct answer using the code given below:",
  ["1, 2 and 3", "1 and 2", "2 and 3", "1 and 3"], mark="B", fig=q518())
Q("p7", 19, 2003, 59, COMP, r"A closed loop system, employing lag-lead compensator $G_c(s)$ is shown in the figure given below: $$G_c(s)=\left[\dfrac{1+\tau_1 s}{1+\tau_1 s/\beta}\right]\left[\dfrac{1+\tau_2 s}{1+\beta\tau_2 s}\right],\quad \beta<1$$ If $G(s)$ has 3 poles in the left half of a s-plane, then the shape of the Bode plot for $|G(s)G_c(s)|$ in the highest frequency range will be",
  ["$-20$ dB/decade", "$-40$ dB/decade", "$-60$ dB/decade", "$-80$ dB/decade"], "C", "C", fig=chain_loop([("G_c(s)", 90), ("G(s)", 90)], rin=r"\text{Input}", cout=r"\text{Output}"))
Q("p7", 20, 2004, 59, RES, r"The forward path transfer function of a unity feedback system is given by $$G(s)=\dfrac{100}{s^2+10s+100}$$ The frequency response of this system will exhibit the resonance peak at",
  ["$10$ rad/s", "$8.66$ rad/s", "$7.07$ rad/s", "$5$ rad/s"], mark="C")
Q("p7", 21, 2004, 59, NYQ, "Consider the following Nyquist plot. With which one of the following transfer functions does the above Nyquist plot match?", [r"$\dfrac{1}{(s+1)^3}$", r"$\dfrac{1}{(s+1)^2}$", r"$\dfrac{1}{s^2+2s+2}$", r"$\dfrac{1}{s+1}$"], mark="B", fig=q516(), ny=True)

# ================================================================= p4  (pp. 60-61)
Q("p4", 22, 2004, 60, MARG, r"The forward path transfer function of a unity feedback system is given by $G(s)=\dfrac{1}{(1+s)^2}$. What is the phase margin for this system?", [r"$-\pi$ rad", "$0$ rad", r"$\pi/2$ rad", r"$\pi$ rad"], mark="D")
Q("p4", 23, 2004, 60, RES, "**Assertion (A):** The bandwidth of a control system indicates the noise filtering characteristic of the system.\n**Reason (R):** The bandwidth is a measure of ability of a control system to reproduce the input signal.", AR)
Q("p4", 24, 2004, 60, MARG, "Which one of the following statements is correct in respect of the theory of stability?",
  ["Phase margin is the phase angle lagging, in short of $180^\\circ$, at the frequency corresponding to a gain of 10.", "Gain margin is the value by which the gain falls short of unity, at a frequency corresponding to $90^\\circ$ phase lag.", "Routh-Hurwitz criterion can determine the degree of stability", "Gain margin and phase margin are the measure of the degree of stability"], mark="D")
Q("p4", 25, 2004, 60, BODE, r"If $X(s)=1/(1+s)$ is the given network function, which one of the following describes the correct Bode plot?",
  ["A straight line with a slope of $-20$ dB/decade", "A straight line with a slope of $20$ dB/decade passing through the point 0 dB and 1 rad/s", r"Constant at 0 dB for $\omega<1$ and a slope of $+20$ dB/decade for $\omega>1$", r"Constant at 0 dB for $\omega<1$ and a slope of $-20$ dB/decade for $\omega>1$"], mark="D")
Q("p4", 26, 2005, 60, RES, "Consider the following statements: The frequency response of a control system has very sharp cut off characteristics. This implies that:\n1. It has large peak resonance.\n2. It has large bandwidth.\n3. It is a less stable system.\nWhich of the statements given above is/are correct?", ["1 only", "2 and 3", "1 and 3", "1, 2 and 3"])
Q("p4", 27, 2005, 60, MARG, "For the minimum phase system to be stable:", ["Phase margin should be negative and gain margin should be positive", "Phase margin should be positive and gain margin should be negative", "Both phase margin and gain margin should be positive", "Both phase margin and gain margin should be negative"], mark="C")
Q("p4", 28, 2005, 60, MARG, "For a stable closed loop system, the gain at phase cross-over frequency should always be:", ["$>20$ dB", "$>6$ dB", "$<6$ dB", "$<0$ dB"], "D")
Q("p4", 29, 2005, 60, MARG, "If the gain of the open loop system is doubled, the gain margin of the system is", ["not affected", "doubled", "halved", "one fourth of original value"], mark="C")
Q("p4", 30, 2005, 60, BASIC, "Match List-I (Frequency Response) with List-II (Time Response) and select the correct answer using the code given below the Lists:",
  ["A–3, B–2, C–1, D–4", "A–1, B–4, C–3, D–2", "A–3, B–4, C–1, D–2", "A–1, B–2, C–3, D–4"], mark="A",
  lists=[{"title": "List-I", "items": [["A", "Bandwidth"], ["B", "Phase margin"], ["C", "Response peak"], ["D", "Gain margin"]]}, {"title": "List-II", "items": [["1", "Overshoot"], ["2", "Stability"], ["3", "Speed of time response"], ["4", "Damping ratio"]]}])
Q("p4", 31, 2006, 61, RES, "For a unity feedback control system the damping ratio is 0.421. What is the resonance magnitude?", ["$M_r=1$", "$M_r=0.707$", "$M_r=1.30$", "$M_r=1.95$"], mark="C")
Q("p4", 32, 2006, 61, MP, "Consider the following statements for a minimum phase system:\n1. All the poles of the transfer function should lie in the left of s-plane.\n2. The zeros of the transfer function can lie anywhere in the s-plane\n3. Given the magnitude characteristic over the entire frequency range, the phase angle characteristic can be uniquely determined.\nWhich of the statements given above are correct?",
  ["1, 2 and 3", "Only 1 and 2", "Only 2 and 3", "Only 1 and 3"])
Q("p4", 33, 2006, 61, BODE, "Consider the following statements regarding the asymptotic Bode plots used for frequency response analysis:\n1. The deviation of the actual magnitude response for a zero on real axis is 3 dB at the corner frequency.\n2. The phase angle for a pair of complex conjugate poles at undamped frequency depends upon the value of damping ratio.\nWhat of the statements given above is/are correct?",
  ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 and 2"], mark="A")
Q("p4", 34, 2006, 61, MARG, r"Consider the unity feedback system with $$G(s)=\dfrac{2}{s(s+1)(2s+1)}$$ What is the gain margin of the system?", ["$3/4$", "$4/3$", "$1/2$", "$3/5$"], mark="B", fig=ufb("G(s)"))
Q("p4", 35, 2006, 61, MARG, r"The system having characteristic equation $s^4+2s^3+3s^2+2s+K=0$ is to be used as an oscillator. What are the values of $K$ and the frequency of oscillation $\omega$?",
  [r"$K=1$ and $\omega=1$ r/s", r"$K=1$ and $\omega=2$ r/s", r"$K=2$ and $\omega=1$ r/s", r"$K=2$ and $\omega=2$ r/s"], mark="C")
Q("p4", 36, 2006, 61, MARG, "For a stable system, what are the restrictions on the gain margin and phase margin?", ["Both gain margin and phase margin are negative", "Gain margin is negative and phase margin is positive", "Gain margin is positive and phase margin is negative", "Both gain margin and phase margin are positive"], mark="D")
Q("p4", 37, 2006, 61, NYQ, "**Assertion (A):** The closed loop stability can be determined from the poles of an open loop system and the polar plot of frequency response.\n**Reason (R):** Unstable system has right half-poles.", AR, "B", "A", ny=True)
Q("p4", 38, 2007, 61, MARG, r"Which one of the following statements is correct for gain margin and phase margin of two closed-loop systems having loop functions $G(s)H(s)$ and $\exp(-s)\,G(s)H(s)$?",
  ["Both gain and phase margins of the two systems will be identical.", r"Both gain and phase margins of $G(s)H(s)$ will be more.", r"Gain margins of the two systems are the same but phase margin of $G(s)H(s)$ will be more.", r"Phase margins of the two systems are the same but gain margin of $G(s)H(s)$ will be less."], mark="C")
Q("p4", 39, 2007, 61, MARG, "Consider the following statements with reference to relative stability of a system:\n1. Phase margin is related to effective damping of the system.\n2. Gain margin gives better estimate of damping ratio than phase margin.\n3. When expressed in dB, gain margin is negative for a stable system.\nWhich of the statements given above are correct?",
  ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], mark="A")

# ================================================================= p2  (pp. 62-63)
Q("p2", 40, 2007, 62, POL, r"Which one of the following polar plots corresponds to $$G(j\omega)=\dfrac{1}{(j\omega)^2(1+j\omega T)}\ ?$$", ["Plot (a)", "Plot (b)", "Plot (c)", "Plot (d)"], mark="C", fig=q540())
Q("p2", 41, 2008, 62, MARG, "A system with gain margin close to unity or a phase margin close to zero is", ["relatively stable", "oscillatory", "stable", "highly stable"], mark="B")
Q("p2", 42, 2008, 62, NYQ, r"The open-loop transfer function of a unity feedback control system is given by $G(s)=Ke^{-Ts}$ where $K$ and $T$ are variables and are greater than zero. The stability of the closed-loop system depends on", [r"$K$ only", r"Both $K$ and $T$", r"$T$ only", r"Neither $K$ nor $T$"], mark="B", ny=True)
Q("p2", 43, 2008, 62, NYQ, "Match List-I (Shape of Nyquist Plot) with List-II (Gain Margin) and select the correct answer using the codes given below the lists:",
  ["A–3, B–4, C–1, D–2", "A–4, B–3, C–2, D–1", "A–3, B–4, C–2, D–1", "A–4, B–3, C–1, D–2"], mark="B", ny=True,
  lists=[{"title": "List-I", "items": [["A", r"The plot does not intersect negative real axis"], ["B", r"The plot intersects negative real axis between $0$ and $(-1, j0)$"], ["C", r"The plot passes through the point $(-1, j0)$"], ["D", r"The plot encloses the point $(-1, j0)$"]]},
         {"title": "List-II", "items": [["1", "$<0$ dB"], ["2", "$0$ dB"], ["3", "$>0$ dB"], ["4", r"$\infty$ dB"]]}])
Q("p2", 44, 2008, 62, MARG, "The gain-phase plot of a linear control system is shown in the below figure. What are the gain-margin (GM) and the phase-margin (PM) of the system?",
  ["GM $>0$ dB and PM $>0$ degree", "GM $>0$ dB and PM $<0$ degree", "GM $<0$ dB and PM $>0$ degree", "GM $<0$ dB and PM $<0$ degree"], mark="B", fig=q544())
Q("p2", 45, 2008, 62, MARG, "What is the gain margin of a system when the magnitude of the polar plot at phase cross over is 'a'?", ["$1/a$", "$-a$", "zero", "$a$"], mark="A")
Q("p2", 46, 2008, 62, RES, "What is the value of the damping ratio of a second order system when the value of the resonant peak is unity?", [r"$\sqrt{2}$", "Unity", r"$1/\sqrt{2}$", "Zero"], "C", "C")
Q("p2", 47, 2008, 63, MARG, r"The closed loop transfer function of a control system is $$\dfrac{K}{s(s+1)(s+5)+K}$$ What is the frequency of the sustained oscillations for marginally stable condition?", [r"$\sqrt{5}$ rad/s", r"$\sqrt{6}$ rad/s", "$5$ rad/s", "$6$ rad/s"], mark="A")
Q("p2", 48, 2010, 63, MARG, r"In the Bode plot of a unity feedback control system, the value of phase angle of $G(j\omega)$ is $-90^\circ$ at the gain cross over frequency of the Bode plot, the phase margin of the system is", [r"$-180^\circ$", r"$+180^\circ$", r"$-90^\circ$", r"$+90^\circ$"], mark="D")
Q("p2", 49, 2010, 63, NYQ, r"The Nyquist plot of loop transfer function $G(s)H(s)$ of a closed loop control system passes through the point $(-1, j0)$ in the $G(s)H(s)$ plane. The phase margin of the system is", [r"$0^\circ$", r"$45^\circ$", r"$90^\circ$", r"$180^\circ$"], mark="A", ny=True)
Q("p2", 50, 2010, 63, BODE, r"The magnitude and phase of the transfer function $G(s)=\dfrac{1}{s+1}$ at $\omega=1$ is", [r"$0.707$ and $45^\circ$", "$-3$ dB and $0.78$ rad", r"$0.707$ and $-45^\circ$", r"$3$ dB and $-90^\circ$"], mark="C")
Q("p2", 51, 2010, 63, BODE, r"The transfer function $G(s)=\dfrac{1}{3s+1}$ has a corner frequency", ["$3$ rad/s", "$0.33$ rad/s", "$1$ rad/s", "$30$ rad/s"], mark="B")
Q("p2", 52, 2011, 63, BODE, r"What are the gain and phase angle of a system having the transfer function $G(s)=(s+1)$ at a frequency of 1 rad/sec?", [r"$0.41$ and $0^\circ$", r"$1.41$ and $45^\circ$", r"$1.41$ and $-45^\circ$", r"$2.41$ and $90^\circ$"], mark="B")
Q("p2", 53, 2011, 63, BODE, r"For the Bode plot of the system $$G(s)=\dfrac{10}{0.66s^2+2.33s+1}$$ the corner frequencies are", ["$0.66$ and $0.33$", "$0.22$ and $2.00$", "$0.30$ and $2.33$", "$0.50$ and $3.00$"])
Q("p2", 54, 2011, 63, MARG, "If the gain margin of a system in decibels is negative, the system is", ["Stable", "Marginally stable", "Unstable", "Could be stable or unstable or marginally stable"], mark="C")
Q("p2", 55, 2011, 63, MARG, "System is said to be marginally stable, if", ["Gain crossover frequency $>$ Phase crossover frequency", "Gain crossover frequency $=$ Phase crossover frequency", "Gain crossover frequency $<$ Phase crossover frequency", r"Gain crossover frequency $\neq$ Phase crossover frequency"], "B", "B")
Q("p2", 56, 2012, 63, NYQ, "**Statement (I):** Nyquist criterion is a powerful tool to determine stability of a closed loop system using open loop transfer function.\n**Statement (II):** Nyquist criterion relates the locations of poles and zeros of the closed loop transfer function.", SR, mark="C", ny=True)
Q("p2", 57, 2012, 63, RES, "**Statement (I):** All the systems which exhibit overshoot in transient response will also exhibit resonance peak in frequency response.\n**Statement (II):** A large resonance peak in frequency response corresponds to a large overshoot in transient response.", SR, mark="A")

# ================================================================= p5  (pp. 64-65)
Q("p5", 58, 2012, 64, MARG, "**Statement (I):** The phase angle plot in Bode diagram is not affected by the variation in open loop gain of the system.\n**Statement (II):** The variation in gain of the system has no effect on the phase margin.", SR)
Q("p5", 59, 2012, 64, MARG, r"For a unity feedback control system, if its open-loop transfer function is given by $$G(s)H(s)=\dfrac{10}{(s+5)^3}$$ then its gain margin will be", ["$20$ dB", "$40$ dB", "$60$ dB", "$80$ dB"], mark="B")
Q("p5", 60, 2012, 64, MARG, r"The gain cross-over frequency and phase margin of the transfer function $\dfrac{1}{s(s+1)}$ are", [r"$1$ rad/s and $45^\circ$", r"$2$ rad/s and $45^\circ$", r"$2$ rad/s and $135^\circ$", r"$1$ rad/s and $135^\circ$"])
Q("p5", 61, 2012, 64, BODE, "For a type 1 system, the low frequency asymptote of its Bode plot will have a slope of", ["$0$ dB/decade", "$6$ dB/decade", "$20$ dB/decade", "$-20$ dB/decade"], mark="D")
Q("p5", 62, 2012, 64, BASIC, r"The unit step response $y(t)$ of a linear system is $y(t)=(1-3e^{-t}+3e^{-2t})\,u(t)$. For the system function, the frequency at which the forced response becomes zero is", [r"$\dfrac{1}{\sqrt{2}}$ rad/s", r"$\dfrac{1}{2}$ rad/s", r"$\sqrt{2}$ rad/s", "$2$ rad/s"])
Q("p5", 63, 2013, 64, MARG, "In a feedback control system, phase margin (PM) is\n1. Directly proportional to $\\xi$\n2. Inversely proportional to $\\xi$\n3. Independent of $\\xi$\n4. Zero when $\\xi=0$\nWhich of the above statements are correct?", ["1 and 2", "2 and 3", "3 and 4", "1 and 4"], mark="D")
Q("p5", 64, 2013, 64, MARG, r"The gain margin in dBs of a unity feedback control system whose open-loop transfer function $$G(s)H(s)=\dfrac{1}{s(s+1)}$$ is", ["$0$", "$1$", "$-1$", r"$\infty$"], "C", "D")
Q("p5", 65, 2013, 64, RES, r"A second order system has $\dfrac{C(s)}{R(s)}=\dfrac{\omega_n^2}{s^2+2\xi\omega_n s+\omega_n^2}$. Its frequency response will have maximum value at the frequency:", [r"$\omega_n\sqrt{1-\xi^2}$", r"$\omega_n\xi$", r"$\omega_n\sqrt{1-2\xi^2}$", "zero"], mark="C")
Q("p5", 66, 2013, 64, BODE, r"The transfer function of a system is $\dfrac{10}{10+s}$. At a frequency of 0.1 rad/sec, the straight line Bode plot will have a magnitude of", ["$10$ dB", "$20$ dB", "$0$ dB", "$40$ dB"], mark="C")
Q("p5", 67, 2013, 64, RES, "In control systems, excessive bandwidth is NOT employed because", ["noise is proportional to bandwidth", "it leads to low relative stability", "it leads to slower response", "noise is proportional to the square of the bandwidth"])
Q("p5", 68, 2014, 64, MARG, r"For a $3^{rd}$ order system given below, what is the phase crossover frequency? $$G(s)H(s)=\dfrac{K}{s^3+6s^2+11s+6}$$", [r"$\sqrt{6}$", r"$\sqrt{11}$", r"$\pm\sqrt{11}$", r"$\pm\sqrt{6}$"], mark="B")
Q("p5", 69, 2015, 64, BODE, r"The Bode plot of the transfer function $G(s)=s$ is\n1. Constant magnitude\n2. $20$ dB/decade\n3. Constant phase shift angle\n4. Constant phase shift of $\pi/2$\nWhich of these are correct?".replace(r"\n", "\n"), ["1 and 3", "1 and 4", "2 and 3", "2 and 4"], mark="D")
Q("p5", 70, 2015, 65, BODE, "Which of the following statements are correct for Bode plots?\n1. Gain margin and phase margin can be easily determined.\n2. Absolute and relative stability of only minimum-phase systems can be determined.\n3. Gain margin is positive and system is stable, if magnitude of $L(j\\omega)$ at phase crossover is positive.",
  ["1, 2 and 3", "1 and 3 only", "1 and 2 only", "2 and 3 only"], mark="C")
Q("p5", 71, 2015, 65, BASIC, r"The roots of the characteristic equation $1+G(s)H(s)=0$ are the same as the", ["Poles of the closed loop transfer function", "Poles of the open loop transfer function", "Zeros of the closed loop transfer function", "Zeros of the open loop transfer function"], mark="B")
Q("p5", 72, 2016, 65, MP, r"The transfer function $G(s)=\dfrac{10(s-1)}{(s+10)}$ represents", ["Unstable system", "Minimum phase system", "Non-minimum phase system", "PID controller system"])
Q("p5", 73, 2016, 65, RES, r"For a unity feedback system with open-loop transfer function $\dfrac{25}{s(s+6)}$, the resonant peak at output $M_m$ and the corresponding resonant frequency $\omega_m$ are respectively", ["$2.6$ and $2.67$ r/s", "$1.04$ and $2.67$ r/s", "$2.6$ and $4.8$ r/s", "$1.04$ and $4.8$ r/s"], "B", "B")
Q("p5", 74, 2016, 65, BODE, r"Consider the transfer function $$G(s)=\dfrac{5(s^2+10s+100)}{s^2(s^2+15s+1)}$$ The corner frequencies in Bode's plot for this transfer function are as", ["$10$ r/s and $10$ r/s", "$100$ r/s and $10$ r/s", "$10$ r/s and $1$ r/s", "$100$ r/s and $1$ r/s"])
Q("p5", 75, 2016, 65, BODE, r"Consider the transfer function $(0.1+0.01s)$ for a PD controller. What is the frequency at which the magnitude is 20 dB (by using asymptotic Bode's plot)?", ["$2000$ r/s", "$1000$ r/s", "$200$ r/s", "$100$ r/s"], mark="B")
Q("p5", 76, 2016, 65, MARG, r"The open-loop transfer function of a unity feedback system is $G(s)=\dfrac{K}{s(s+5)}$. The gain $K$ that results in a phase margin of $45^\circ$ is", ["$35$", "$30$", "$25$", "$20$"], mark="C")
Q("p5", 77, 2016, 65, MARG, "Consider the following statements: The Gain margin and Phase margin of an unstable system may respectively be\n1. Positive, negative\n2. Negative, positive\n3. Negative, negative\nWhich of the above statements is/are correct?", ["3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], mark="B")
Q("p5", 78, 2016, 65, BODE, r"The open-loop transfer function of a unity feedback system is $G(s)=\dfrac{10(1+0.2s)}{(1+0.5s)}$. The phase shift at $\omega=0$ and $\omega=\infty$, will be, respectively", [r"$-90^\circ$ and $180^\circ$", r"$0^\circ$ and $180^\circ$", r"$-90^\circ$ and $90^\circ$", r"$0^\circ$ and $0^\circ$"], mark="D")
Q("p5", 79, 2016, 65, BODE, "The Bode plot of the open-loop transfer function of a system is described as follows:\n- Slope $-40$ dB/decade; $\\omega<0.1$ rad/s\n- Slope $-20$ dB/decade; $0.1<\\omega<10$ rad/s\n- Slope $0$; $\\omega>10$ rad/s\nThe system described will have", ["1 pole and 2 zeros", "2 poles and 2 zeros", "2 poles and 1 zero", "1 pole and 1 zero"], mark="B")
Q("p5", 80, 2016, 65, MP, "The transfer function of a control system is said to be 'All Pass System', if it has",
  ["Unit magnitude at all frequencies with anti-symmetric pole-zero pattern", "Unit magnitude at all frequencies with symmetric pole-zero pattern", "Magnitude varying with frequency and with anti-symmetric pole-zero pattern", "Unit magnitude at some frequencies with symmetric pole-zero pattern"], mark="B")

# ================================================================= p1  (pp. 66-67)
Q("p1", 81, 2017, 66, MARG, "Consider the following statements regarding 'relative stability': It is defined\n1. in terms of gain margin only\n2. in terms of phase margin and certain other parameters\n3. in terms of gain margin, phase margin and location of poles in s-plane\n4. in relation to another identified system\nWhich of the above statements are correct?", ["1 and 2", "2 and 3", "3 and 4", "1 and 4"], mark="C")
Q("p1", 82, 2017, 66, BODE, "The magnitude plot for the open-loop transfer function of a control system is shown in the figure given below. Its open-loop transfer function, $G(s)H(s)$, is", [r"$10(s+1)$", r"$\dfrac{1}{s+1}$", r"$\dfrac{10}{s+1}$", r"$20(s+1)$"], "C", "C", fig=q582())
Q("p1", 83, 2017, 66, MP, "**Statement (I):** Elements with non-minimum phase transfer functions introduce large phase lags with increasing frequency resulting in complex compensation problems.\n**Statement (II):** Transportation lag commonly encountered in process control systems is a non-minimum phase element.", SR, mark="A")
Q("p1", 84, 2018, 66, BODE, r"The low-frequency asymptote in the Bode plot of $$G(s)=\dfrac{6(s^2+10s+100)}{s^2(50s^2+15s+1)}$$ has a slope of", ["$-10$ dB/dec", "$-20$ dB/dec", "$-40$ dB/dec", "$-60$ dB/dec"], mark="C")
Q("p1", 85, 2018, 66, BODE, r"The open-loop transfer function $G(s)H(s)$ of the Bode plot as shown in the figure is", [r"$\dfrac{Ks(s+2)}{s+20}$", r"$\dfrac{K(s+20)}{s(s+2)}$", r"$\dfrac{K(s+2)}{s(s+20)}$", r"$\dfrac{Ks(s+20)}{s+2}$"], mark="B", fig=q585())
Q("p1", 86, 2018, 66, BODE, r"Which one of the following transfer functions represents the Bode plot as shown in the figure (where $K$ is constant)?", [r"$\dfrac{Ks^2}{\left(1+\frac{s}{10}\right)^3}$", r"$\dfrac{Ks^2}{\left(1+\frac{s}{10}\right)^4}$", r"$\dfrac{Ks^2}{\left(1+\frac{s}{10}\right)^5}$", r"$\dfrac{Ks^2}{\left(1+\frac{s}{10}\right)^2}$"], mark="C", fig=q586())
Q("p1", 87, 2018, 67, NYQ, r"The open-loop transfer function of a system has two poles on the imaginary axis, one in the left-half and the other in the right-half, together with a zero at the origin of coordinates and also two zeros in the left-half of the s-plane. The closed-loop response for unity feedback will be stable if the encirclement of the critical point $(-1, j0)$ is", ["$-1$", "$+1$", "$-2$", "$+2$"], mark="C", ny=True)
Q("p1", 88, 2018, 67, BODE, r"**Statement (I):** The transportation lag in a system can be easily handled by using Bode plot." "\n" r"**Statement (II):** The magnitude plot is unaffected, and only the phase plot shifts by $-\omega T$ rad due to the presence of $e^{-sT}$.", SR, mark="A")
Q("p1", 89, 2018, 67, BASIC, "In case of high-pass filter, the transfer function should be with\n1. 1 pole and 1 zero\n2. 2 poles and 2 zeros\n3. 2 poles and 1 zero\nWhich of the above are correct?", ["1, 2 and 3", "1 and 3 only", "2 and 3 only", "1 and 2 only"])
Q("p1", 90, 2019, 67, BASIC, "The magnitude and phase relationship between the sinusoidal input and the steady-state output of a system is called as", ["magnitude response", "transient response", "steady-state response", "frequency response"], mark="C")
Q("p1", 91, 2019, 67, MP, "A transfer function having all its poles and zeros only in the left-half of the s-plane is called", ["a minimum-phase function", "a complex transfer function", "an all-pass transfer function", "a maximum-phase transfer function"], "A", "A")
Q("p1", 92, 2019, 67, RES, "The frequency where magnitude $M$ has a peak value in frequency response is known as", ["normalized frequency", "resonant frequency", "peak frequency", "tuned frequency"], mark="B")
Q("p1", 93, 2020, 67, MARG, "**Statement (I):** For an unstable feedback system, the gain margin is negative or the phase margin is positive.\n**Statement (II):** For a stable feedback system, both gain margin and phase margin must be positive.", SR, mark="A")
Q("p1", 94, 2021, 67, RES, "Which one of the following statements is correct regarding constant N circles?",
  ["The locus of constant, closed-loop magnitude frequency response for unity feedback systems.", "The locus of constant, closed-loop phase frequency response for unity feedback systems.", "A subsystem inserted into the forward or feedback path for the purpose of improving the transient response or steady-state error.", "A system that monitors its output and corrects for disturbances. It is characterized by feedback paths from the output."])
Q("p1", 95, 2023, 67, BODE, r"A system has poles at 0.01 Hz, 1 Hz and 80 Hz; zeros at 5 Hz, 100 Hz and 200 Hz. The approximate phase of the system response at 20 Hz is", [r"$-90^\circ$", r"$0^\circ$", r"$90^\circ$", r"$-180^\circ$"], mark="A")
Q("p1", 96, 2023, 67, RES, r"The magnitude of frequency response of an underdamped second-order system is 5 at 0 rad/sec and peaks at $\dfrac{10}{\sqrt{3}}$ at $5\sqrt{2}$ rad/sec. The transfer function of the system is", [r"$\dfrac{100}{s^2+10s+100}$", r"$\dfrac{375}{s^2+5s+75}$", r"$\dfrac{500}{s^2+12s+100}$", r"$\dfrac{1125}{s^2+25s+225}$"])

# ================================================================= p3  (p. 68)
Q("p3", 97, 2023, 68, RES, "By considering standard notations, the peak value of the magnitude in the resonant peak $M_r$ is", [r"$\dfrac{2}{\zeta\sqrt{1-\zeta^2}}$", r"$\dfrac{1}{\zeta\sqrt{2-\zeta^2}}$", r"$\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$", r"$\dfrac{1}{\zeta\sqrt{1-\zeta^2}}$"])
Q("p3", 98, 2023, 68, MARG, r"The phase margin of a system having the loop transfer function $G(s)H(s)=\dfrac{2\sqrt{3}}{s(s+1)}$ is", [r"$45^\circ$", r"$90^\circ$", r"$30^\circ$", r"$60^\circ$"])
Q("p3", 99, 2023, 68, MARG, r"The phase margin of a system with the open-loop transfer function $G(s)H(s)=\dfrac{1-s}{(s+1)(s+2)}$ is", [r"$0^\circ$", r"$63.4^\circ$", r"$90^\circ$", r"$\infty^\circ$"])
Q("p3", 100, 2023, 68, NYQ, r"The Nyquist criterion for stability states that an amplifier is unstable if the Nyquist curve encloses the $-1+j0$ point, and the amplifier is stable if the curve does not enclose this point. If $A\beta$",
  ["extends outside this circle, the feedback is negative.", r"lies within this circle, then $|1+A\beta|<1$, and the feedback is negative.", r"does not enclose the point $-1+j0$, i.e., $|1+A\beta|>1$, then the amplifier is unstable and the feedback is negative for all frequencies.", "extends inside this circle, the feedback is negative."], "B", ny=True)
Q("p3", 101, 2024, 68, BODE, r"Consider the following statements regarding the Bode plot for the type-2 system having transfer function of the form $$G(j\omega)=\dfrac{K}{(j\omega)^2(1+j\omega T)}$$" "\n" r"1. The intercept of the low frequency slope of $-40$ dB/decade (or its extension) with the 0 dB axis occurs at a frequency $\omega_x$, where $\omega_x=K$" "\n" r"2. The value on the low frequency slope of $-40$ dB/decade (or its extension) at the frequency $\omega=1$, is equal to $40\log(K)$." "\n" r"3. The gain $K$ is the static ramp error coefficient." "\nWhich of the above statements is/are not correct?",
  ["1 only", "1 and 2", "1 and 3", "2 and 3"], mark="D")
Q("p3", 102, 2024, 68, NYQ, "Consider the following statements:\n1. Gain margin is used to indicate the proximity of the intersection of the negative real axis made by the polar plot of $G(j\\omega)H(j\\omega)$ to the $(-1+j)$ point.\n2. Phase crossover point is the point in the $G(j\\omega)H(j\\omega)$ plane at which the polar $G(j\\omega)H(j\\omega)$ plot intersects the positive real axis.\n3. The phase crossover frequency is the frequency at the phase crossover point or where $\\angle\\{G(j\\omega)H(j\\omega)\\}=180^\\circ$.\nWhich of the above statements is/are not correct?",
  ["2 only", "1 and 2 only", "1 and 3 only", "2 and 3 only"], mark="C", ny=True)

# ---------------------------------------------------------------------------------- batches
from collections import OrderedDict
by = OrderedDict((k, []) for k in F)
for k, d in QS:
    by[k].append(d)
batch = [{"image": f"{FR}/{F[k]}", "questions": v} for k, v in by.items()]
json.dump(batch, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
nums = [d["number"] for _, d in QS]
print(len(QS), "questions;", len(set(nums)), "unique;", sum(1 for _, d in QS if d.get("answer")), "with verified key;", sum(1 for _, d in QS if d.get("figure")), "figures;",
      sum(1 for _, d in QS if d["folder"] == NY), "nyquist")
missing = [f"5.{i}" for i in range(1, 103) if f"5.{i}" not in nums]
print("missing:", missing)
