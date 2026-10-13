// ESE (IES) Stage 1 syllabus for ECE, written from the UPSC pattern.
// Verify against the latest UPSC notification before relying on it.
// Format: [paperId, subjectName, [[chapterName, [topics...]], ...]]

const RAW = [
  // ---------------- PAPER I : General Studies & Engineering Aptitude (200 marks) ----------------
  ['p1', 'Engineering Mathematics & Numerical Analysis', [
    ['Linear Algebra', ['Matrices, rank, inverse', 'Systems of linear equations', 'Eigenvalues and eigenvectors', 'Cayley-Hamilton theorem']],
    ['Calculus', ['Limits, continuity, differentiability', 'Mean value theorems, Taylor series', 'Maxima and minima', 'Definite and improper integrals', 'Partial derivatives, Jacobian']],
    ['Vector Calculus', ['Gradient, divergence, curl', 'Line, surface and volume integrals', 'Green, Gauss and Stokes theorems']],
    ['Differential Equations', ['First-order ODEs', 'Higher-order linear ODEs', 'Cauchy-Euler equation', 'Partial differential equations (basics)']],
    ['Complex Variables', ['Analytic functions, Cauchy-Riemann', 'Cauchy integral theorem and formula', 'Taylor and Laurent series, residues']],
    ['Probability & Statistics', ['Conditional probability, Bayes theorem', 'Random variables and distributions', 'Mean, variance, correlation, regression']],
    ['Numerical Methods', ['Roots of equations (bisection, Newton-Raphson)', 'Interpolation', 'Numerical integration (trapezoidal, Simpson)', 'Numerical solution of ODEs (Euler, Runge-Kutta)', 'Solving linear systems (Gauss, LU)']],
  ]],
  ['p1', 'Engineering Aptitude: Reasoning & Analytical Ability', [
    ['Logical Reasoning', ['Syllogisms and deductions', 'Statements and conclusions', 'Series, analogy, classification', 'Coding-decoding, blood relations', 'Directions, seating arrangements']],
    ['Analytical & Quantitative Ability', ['Percentages, ratio and proportion', 'Time, speed, distance, work', 'Profit and loss, interest', 'Permutation and combination', 'Data interpretation and sufficiency']],
    ['Basic English', ['Comprehension and vocabulary', 'Grammar and usage']],
  ]],
  ['p1', 'Current Issues & Engineering Awareness', [
    ['Current Issues', ['Social, economic and industrial development', 'National and international importance']],
    ['Design, Drawing & Safety', ['General principles of design', 'Engineering drawing basics', 'Importance of safety']],
    ['Standards & Quality Practices', ['Standards in production and construction', 'Quality in maintenance and services', 'TQM, ISO standards']],
  ]],
  ['p1', 'Energy, Environment & Climate', [
    ['Energy', ['Conventional energy sources', 'Renewable energy (solar, wind, hydro, biomass)', 'Energy conservation and audit']],
    ['Environment & Ecology', ['Ecology and ecosystems', 'Pollution (air, water, soil, noise)', 'Environmental impact assessment', 'Climate change, global warming, mitigation']],
  ]],
  ['p1', 'Project Management', [
    ['Project Management Basics', ['Project planning and scheduling', 'CPM and PERT', 'Cost estimation and control', 'Risk management']],
  ]],
  ['p1', 'Basics of Material Science & Engineering', [
    ['Material Science', ['Crystal structure and defects', 'Mechanical properties of materials', 'Metals, alloys, ceramics, polymers, composites', 'Phase diagrams (basics)']],
  ]],
  ['p1', 'ICT in Engineering', [
    ['Information & Communication Technologies', ['Networking basics', 'E-governance', 'Technology based education', 'Cyber security awareness', 'AI, IoT and emerging tech']],
  ]],
  ['p1', 'Ethics & Values in Engineering', [
    ['Engineering Ethics', ['Professional ethics and codes', 'Values in engineering profession', 'Responsibility, whistle-blowing']],
  ]],

  // ---------------- PAPER II : Electronics & Telecommunication Engineering (300 marks) ----------------
  ['p2', 'Basic Electrical Engineering', [
    ['DC Circuits & Theorems', ['Ohm and Kirchhoff laws', 'Thevenin, Norton, superposition', 'Maximum power transfer']],
    ['AC Circuits', ['Phasors, impedance, power factor', 'Resonance', 'Three-phase systems and power measurement']],
    ['Transformers', ['Equivalent circuit, regulation, efficiency', 'Auto and three-phase transformers']],
    ['DC Machines', ['Construction, EMF and torque', 'Characteristics, speed control']],
    ['Induction & Synchronous Machines', ['Rotating magnetic field, slip, torque-slip', 'Starting and speed control', 'Alternator and synchronous motor basics']],
    ['Power Systems & Protection (Basics)', ['Transmission line basics', 'Circuit breakers, relays, fuses']],
  ]],
  ['p2', 'Materials Science & Electronic Components', [
    ['Electrical & Electronic Materials', ['Conductors and resistive materials', 'Dielectrics, polarization, breakdown', 'Insulating materials']],
    ['Semiconductor & Magnetic Materials', ['Elemental and compound semiconductors', 'Dia-, para-, ferro- and ferri-magnetism', 'Hysteresis, soft and hard magnets, ferrites']],
    ['Special Materials', ['Ferroelectric, piezoelectric, pyroelectric', 'Superconductivity', 'Nanomaterials and thin films']],
    ['Passive & Electromechanical Components', ['Resistors, capacitors, inductors', 'Relays, switches, connectors', 'Printed circuit boards']],
  ]],
  ['p2', 'Network Theory', [
    ['Network Elements & Graph Theory', ['Network graphs, tie-set, cut-set', 'Nodal and mesh analysis', 'Dependent sources']],
    ['Network Theorems', ['Superposition, Thevenin, Norton', 'Reciprocity, Millman, Tellegen', 'Maximum power transfer']],
    ['Transient Analysis', ['First-order RL, RC circuits', 'Second-order RLC circuits', 'Initial and final conditions']],
    ['Laplace Transform in Circuits', ['Circuit analysis in s-domain', 'Transfer function, poles and zeros', 'Impulse and step response']],
    ['Sinusoidal Steady State & Resonance', ['Phasor analysis', 'Series and parallel resonance, Q-factor', 'Coupled circuits']],
    ['Two-Port Networks', ['Z, Y, h, ABCD parameters', 'Interconnection of two-ports']],
    ['Network Synthesis & Filters', ['Positive real functions', 'Foster and Cauer forms', 'Passive filters, image parameters']],
    ['Transmission Lines (Circuit View)', ['Characteristic impedance, propagation constant', 'Reflection coefficient, VSWR']],
  ]],
  ['p2', 'Signals & Systems', [
    ['Signal Classification & Operations', ['Continuous and discrete signals', 'Energy and power signals', 'Time scaling, shifting, folding']],
    ['LTI Systems', ['Impulse response and convolution', 'Causality, stability, memory', 'Differential and difference equations']],
    ['Fourier Series & Transform (CT)', ['Trigonometric and exponential series', 'Fourier transform and properties', 'Parseval theorem, energy spectral density']],
    ['Laplace Transform', ['ROC and properties', 'Inverse Laplace', 'System analysis using Laplace']],
    ['Sampling', ['Sampling theorem, aliasing', 'Reconstruction']],
    ['DTFT, DFT & Z-Transform', ['DTFT properties', 'DFT and FFT basics', 'Z-transform, ROC, inverse Z', 'System analysis using Z-transform']],
    ['Random Signals', ['Random processes, stationarity', 'Autocorrelation and power spectral density', 'White noise through LTI systems']],
  ]],
  ['p2', 'Electronic Measurements & Instrumentation', [
    ['Measurement Fundamentals', ['Accuracy, precision, errors', 'Standards and calibration', 'Statistical analysis of errors']],
    ['Analog Meters & Bridges', ['PMMC, moving iron, dynamometer', 'Wheatstone, Kelvin, Maxwell, Hay, Schering bridges', 'Q-meter']],
    ['Electronic Instruments', ['Digital voltmeters and multimeters', 'Frequency counters', 'Signal generators, wave analyzers, spectrum analyzers']],
    ['Oscilloscopes', ['CRO working and deflection', 'Dual trace, sampling, DSO', 'Lissajous patterns']],
    ['Transducers & Sensors', ['Resistive, capacitive, inductive', 'Strain gauge, LVDT, thermocouple, RTD', 'Piezoelectric, Hall effect, optical sensors']],
    ['Data Acquisition & Signal Conditioning', ['Instrumentation amplifier', 'ADC/DAC in measurement', 'Telemetry basics']],
  ]],
  ['p2', 'Analog Electronics', [
    ['Semiconductor Physics & Diodes', ['Carrier concentration, drift and diffusion', 'PN junction, Zener, special diodes', 'Rectifiers, clippers, clampers, voltage multipliers']],
    ['BJT', ['Operation, characteristics', 'Biasing and stability', 'Small-signal models (re, hybrid-pi, h-parameters)']],
    ['FET & MOSFET', ['JFET and MOSFET characteristics', 'Biasing', 'Small-signal models']],
    ['Amplifiers', ['CE, CB, CC and CS, CG, CD stages', 'Multistage, cascode, differential amplifier', 'Frequency response']],
    ['Feedback Amplifiers', ['Four feedback topologies', 'Effect on gain, impedance, bandwidth', 'Stability criteria']],
    ['Oscillators', ['Barkhausen criterion', 'RC phase shift, Wien bridge', 'LC (Colpitts, Hartley) and crystal']],
    ['Power Amplifiers', ['Class A, B, AB, C', 'Efficiency and distortion', 'Heat sinks']],
    ['Operational Amplifiers', ['Ideal and practical op-amp parameters', 'Inverting, non-inverting, summing, integrator, differentiator', 'Comparators, Schmitt trigger', 'Active filters, instrumentation amplifier']],
    ['Waveform Generators & Timers', ['555 timer (astable, monostable)', 'Multivibrators', 'Function generators']],
    ['Voltage Regulators & Power Supplies', ['Zener and series regulators', 'IC regulators (78xx, 79xx, LM317)', 'SMPS basics']],
  ]],
  ['p2', 'Digital Electronics', [
    ['Number Systems & Boolean Algebra', ['Binary, octal, hex, codes', 'Boolean theorems', 'Complements and arithmetic']],
    ['Logic Gates & Minimization', ['K-map, Quine-McCluskey', 'NAND/NOR universality', 'Logic families (TTL, CMOS, ECL) characteristics']],
    ['Combinational Circuits', ['Adders, subtractors, comparators', 'Mux, demux, encoders, decoders', 'Hazards', 'Implementation using MUX and PLA']],
    ['Sequential Circuits', ['Latches and flip-flops (SR, JK, D, T)', 'Excitation tables, conversions', 'Counters (sync and async)', 'Shift registers']],
    ['FSM Design', ['Mealy and Moore machines', 'State reduction and assignment', 'Sequence detectors']],
    ['Memories & Programmable Logic', ['ROM, RAM, DRAM, SRAM', 'PLA, PAL, CPLD, FPGA', 'Memory expansion']],
    ['Data Converters', ['DAC types (R-2R, weighted)', 'ADC types (flash, SAR, dual slope)', 'Resolution, errors']],
  ]],
  ['p2', 'Control Systems', [
    ['Modeling & Block Diagrams', ['Transfer function', 'Block diagram reduction', 'Signal flow graph and Mason gain formula']],
    ['Time Response Analysis', ['Standard test signals', 'First and second-order systems', 'Steady state error and error constants']],
    ['Stability & Root Locus', ['Routh-Hurwitz criterion', 'Root locus construction', 'Effect of adding poles and zeros']],
    ['Frequency Response', ['Bode plot', 'Polar plot', 'Gain and phase margin']],
    ['Nyquist Stability', ['Nyquist criterion', 'Relative stability']],
    ['Compensators & Controllers', ['Lead, lag, lead-lag', 'P, PI, PD, PID controllers']],
    ['State Variable Analysis', ['State space models', 'Controllability and observability', 'State transition matrix', 'State feedback']],
    ['Sampled Data & Nonlinear Systems', ['Discrete-time systems and z-domain stability', 'Describing function', 'Phase plane analysis']],
    ['Control Components', ['Synchros, servomotors', 'Tachogenerators, stepper motors', 'AC/DC position control']],
  ]],
  ['p2', 'Electromagnetic Theory', [
    ['Vector Analysis & Static Fields', ['Coordinate systems', 'Coulomb law, Gauss law, potential', 'Biot-Savart, Ampere law']],
    ['Boundary Value Problems', ['Poisson and Laplace equations', 'Method of images', 'Capacitance and inductance']],
    ['Maxwell Equations', ['Differential and integral forms', 'Boundary conditions', 'Poynting theorem']],
    ['Wave Propagation', ['Plane waves in free space, dielectrics, conductors', 'Polarization', 'Skin depth', 'Reflection and refraction, Brewster angle']],
    ['Transmission Lines', ['Line parameters, telegrapher equations', 'Smith chart', 'Impedance matching (stub, quarter wave)']],
    ['Waveguides', ['Rectangular waveguide TE/TM modes', 'Cutoff, guide wavelength', 'Cavity resonators']],
    ['Antennas', ['Radiation fundamentals, dipole, loop', 'Antenna parameters', 'Arrays, Friis equation', 'Aperture, horn, parabolic']],
    ['Radio Wave Propagation', ['Ground, sky and space waves', 'Ionosphere, MUF, skip distance']],
  ]],
  ['p2', 'Analog Communication', [
    ['Noise', ['Thermal and shot noise', 'Noise figure and temperature', 'Friis formula for cascade']],
    ['Amplitude Modulation', ['AM, DSB-SC, SSB, VSB', 'Generation and detection', 'Power and bandwidth']],
    ['Angle Modulation', ['FM and PM', 'Carson rule, NBFM, WBFM', 'FM generation and demodulation', 'Pre-emphasis and de-emphasis']],
    ['Receivers & Transmitters', ['TRF and superheterodyne', 'AGC, image rejection', 'Performance parameters']],
    ['Noise in Analog Systems', ['SNR in AM, DSB, SSB', 'SNR in FM, threshold effect']],
    ['Television & Radar Basics', ['TV scanning and standards', 'Colour TV basics', 'Radar range equation']],
  ]],
  ['p2', 'Digital Communication', [
    ['Probability & Random Processes', ['Random variables, Gaussian distribution', 'Stationary processes and PSD', 'Matched filter']],
    ['Information Theory', ['Entropy, mutual information', 'Source coding (Huffman, Shannon-Fano)', 'Channel capacity, Shannon theorem']],
    ['Pulse Modulation', ['PAM, PWM, PPM', 'PCM, quantization noise', 'Companding, DM, ADM, DPCM']],
    ['Baseband Transmission', ['Line codes', 'ISI and Nyquist criterion', 'Eye diagram, equalization']],
    ['Digital Modulation', ['ASK, FSK, PSK, QPSK, MSK, QAM', 'Coherent and non-coherent detection', 'Probability of error, BER']],
    ['Error Control Coding', ['Linear block codes, cyclic codes', 'Convolutional codes, Viterbi', 'Hamming distance, syndrome']],
    ['Multiplexing & Spread Spectrum', ['TDM, FDM, T1 carrier', 'DSSS, FHSS', 'CDMA basics']],
  ]],
  ['p2', 'Microwave, Optical & Satellite Communication', [
    ['Microwave Components & Tubes', ['Waveguide components (tees, couplers, circulators)', 'Klystron, magnetron, TWT', 'S-parameters']],
    ['Microwave Solid-State Devices', ['Gunn, IMPATT, TRAPATT', 'Tunnel and varactor diodes', 'Microwave transistors, MMIC']],
    ['Microstrip & Planar Lines', ['Microstrip, stripline', 'Filters, couplers, resonators']],
    ['Radar Systems', ['Radar equation', 'CW, FM-CW, MTI, pulse Doppler', 'Tracking radar']],
    ['Optical Fibre Communication', ['Fibre types, modes, NA', 'Attenuation and dispersion', 'LED, laser, PIN, APD', 'Optical link budget, WDM']],
    ['Satellite Communication', ['Orbits, Kepler laws', 'Link budget', 'Multiple access (FDMA, TDMA, CDMA)', 'Transponders, VSAT, GPS']],
    ['Mobile & Wireless Communication', ['Cellular concept, frequency reuse', 'Handoff, GSM, CDMA, LTE basics', 'Fading and multipath', 'Wi-Fi, Bluetooth basics']],
    ['Networks & Data Communication', ['OSI and TCP/IP models', 'MAC protocols, Ethernet', 'Routing, IP addressing', 'ISDN, ATM basics']],
  ]],
  ['p2', 'Computer Organization & Architecture', [
    ['Basic Structure & Instruction Sets', ['Von Neumann architecture', 'Instruction formats, addressing modes', 'RISC vs CISC']],
    ['Arithmetic & ALU', ['Fixed and floating point', 'Booth multiplication, division', 'IEEE 754']],
    ['Control Unit', ['Hardwired vs microprogrammed', 'Instruction cycle']],
    ['Pipelining', ['Pipeline hazards and speedup', 'Superscalar basics']],
    ['Memory Hierarchy', ['Cache mapping and replacement', 'Virtual memory, paging', 'Memory interleaving']],
    ['I/O Organization', ['Programmed I/O, interrupts, DMA', 'Buses and standards']],
    ['Operating System Basics', ['Process scheduling', 'Memory management', 'Deadlocks']],
  ]],
  ['p2', 'Microprocessors & Microcontrollers', [
    ['8085 Microprocessor', ['Architecture and pin diagram', 'Instruction set and addressing modes', 'Timing diagrams', 'Assembly programming', 'Interrupts']],
    ['8086 Microprocessor', ['Architecture, segmentation', 'Min and max mode', 'Instruction set', 'Interrupts']],
    ['Peripheral Interfacing', ['8255 PPI, 8253/54 timer', '8259 PIC, 8257 DMA', '8251 USART', 'ADC/DAC interfacing']],
    ['8051 Microcontroller', ['Architecture and memory', 'Timers, serial port, interrupts', 'Programming and interfacing']],
    ['ARM & Embedded Systems', ['ARM architecture basics', 'Embedded system design', 'RTOS basics']],
  ]],
  ['p2', 'Power Electronics', [
    ['Power Semiconductor Devices', ['Power diode, SCR, TRIAC, GTO', 'Power BJT, MOSFET, IGBT', 'Turn-on/off, snubbers, protection']],
    ['Phase Controlled Rectifiers', ['Single phase half and full controlled', 'Three phase converters', 'Effect of source inductance']],
    ['DC-DC Converters', ['Buck, boost, buck-boost', 'Chopper classes', 'Commutation circuits']],
    ['Inverters', ['Single and three phase VSI', 'PWM techniques', 'Harmonic reduction']],
    ['AC Voltage Controllers & Cycloconverters', ['Phase control, on-off control', 'Cycloconverter basics']],
    ['Motor Drives', ['DC drives', 'Induction motor drives (V/f)']],
  ]],
  ['p2', 'Advanced Electronics: VLSI, DSP & Others', [
    ['VLSI Design', ['CMOS inverter, VTC, noise margin', 'Static and dynamic CMOS logic', 'Fabrication process, scaling', 'Layout, design rules', 'Delay and power']],
    ['Digital Signal Processing', ['DFT, FFT (radix-2)', 'FIR design (window, frequency sampling)', 'IIR design (Butterworth, Chebyshev, bilinear, impulse invariance)', 'Filter structures', 'DSP processor architecture']],
    ['Image & Speech Processing (Basics)', ['Image enhancement and transforms', 'Speech coding basics']],
    ['Sensors & Opto-electronics', ['LED, photodiode, solar cell', 'Optocouplers, LCD, displays']],
    ['Biomedical & Industrial Electronics', ['ECG, EEG basics', 'PLC and SCADA basics']],
    ['Emerging Topics', ['IoT, WSN', 'MEMS', 'Machine learning basics']],
  ]],
];

const slug = (s) =>
  s.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

const PAPERS = [
  { id: 'p1', name: 'Paper I', title: 'General Studies & Engineering Aptitude', marks: 200 },
  { id: 'p2', name: 'Paper II', title: 'Electronics & Telecommunication Engineering', marks: 300 },
];

const subjects = RAW.map(([paper, name, chapters]) => {
  const sid = `${paper}-${slug(name)}`;
  return {
    id: sid,
    paper,
    name,
    chapters: chapters.map(([cname, topics]) => {
      const cid = `${sid}--${slug(cname)}`;
      return {
        id: cid,
        name: cname,
        topics: topics.map((t) => ({ id: `${cid}--${slug(t)}`, name: t })),
      };
    }),
  };
});

module.exports = { PAPERS, subjects };
