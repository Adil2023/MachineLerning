# EEG Circuit Design (Single TL074) - Revised

## Architecture
1. **Stage 1: Instrumentation Amplifier (InAmp)**
   - Uses 3 op-amps from the TL074.
   - Purpose: Differential amplification and high common-mode rejection.
   - Gain $\approx 21$.
2. **Stage 2: Passive Twin-T Notch Filter (50Hz)**
   - Purpose: Attenuate power line noise.
   - Design: 50Hz center frequency.
   - **Correction:** Using proper resistor ratios for high attenuation.
3. **Stage 3: Non-Inverting Active Bandpass Filter**
   - Uses the 4th op-amp.
   - Purpose: Final amplification and frequency limiting (approx. 1.6Hz to 34Hz).
   - High Input Impedance (1MΩ) to prevent loading the passive notch filter.
   - Stage Gain $\approx 471$.
   - **Total Gain $\approx 9,890$.**

## Power Supply
- Two 9V batteries in series to create $+9V$, $GND$, and $-9V$.
- GND is the junction between the two batteries.

## Schematic Description

### TL074 Pinout (Top View)
1. Out 1 (InAmp Output)
2. In- 1 (InAmp Diff Stage)
3. In+ 1 (InAmp Diff Stage)
4. VCC+ (+9V)
5. In+ 2 (InAmp Input 2)
6. In- 2 (InAmp Input 2 - Internal)
7. Out 2 (InAmp First Stage Out 2)
8. Out 3 (Final Output)
9. In- 3 (Filter Stage)
10. In+ 3 (Filter Stage)
11. VCC- (-9V)
12. In+ 4 (InAmp Input 1)
13. In- 4 (InAmp Input 1 - Internal)
14. Out 4 (InAmp First Stage Out 1)

### Stage 1: Instrumentation Amplifier (Op-amps 1, 2, 4)
- **Inputs:**
  - Electrode A to Pin 12 (In+ 4)
  - Electrode B to Pin 5 (In+ 2)
- **First Gain Stage:**
  - Resistor $R_g$ (1kΩ) between Pin 13 and Pin 6.
  - Resistor $R_1$ (10kΩ) between Pin 14 and Pin 13.
  - Resistor $R_2$ (10kΩ) between Pin 7 and Pin 6.
- **Differential Stage:**
  - Resistor $R_3$ (10kΩ) from Pin 14 to Pin 2.
  - Resistor $R_4$ (10kΩ) from Pin 7 to Pin 3.
  - Resistor $R_5$ (10kΩ) from Pin 3 to GND.
  - Resistor $R_6$ (10kΩ) from Pin 2 to Pin 1.

### Stage 2: Passive Twin-T Notch (50Hz)
- Input from Pin 1 (Out 1).
- **Upper Branch:** Resistor $R_n1$ (47kΩ) and $R_n2$ (47kΩ) in series. Junction to GND via two 68nF capacitors in parallel ($C_{shunt}$, total 136nF).
- **Lower Branch:** Capacitor $C_n1$ (68nF) and $C_n2$ (68nF) in series. Junction to GND via two 47kΩ resistors in parallel ($R_{shunt}$, total 23.5kΩ).
- **Output:** Junction of the two branches.

### Stage 3: High-Impedance Gain + Filter (Op-amp 3)
- **Input:** From Notch Filter output.
- **High Pass / Coupling:** Notch output connects to $C_c$ (100nF). The other side of $C_c$ connects to Pin 10 (In+ 3).
- **Input Impedance:** Resistor $R_{pd}$ (1MΩ) from Pin 10 to GND.
- **Feedback Loop (Gain + Low Pass):**
  - Resistor $R_f$ (470kΩ) between Pin 9 and Pin 8.
  - Capacitor $C_f$ (10nF) between Pin 9 and Pin 8.
  - Resistor $R_1$ (1kΩ) in series with Capacitor $C_1$ (47µF) from Pin 9 to GND.
- **Output:** Final signal at Pin 8.

## Component List

### Electronics
- **1x TL074CN** Quad Op-Amp
- **2x 9V Batteries**
- **Resistors (1%):**
  - 2x 1kΩ ($R_g$, $R_1$)
  - 6x 10kΩ ($R_1, R_2, R_3, R_4, R_5, R_6$)
  - 4x 47kΩ ($R_n1, R_n2$, $R_{shunt}$)
  - 1x 470kΩ ($R_f$)
  - 1x 1MΩ ($R_{pd}$)
- **Capacitors:**
  - 4x 68nF ($C_n1, C_n2$, $C_{shunt}$)
  - 1x 10nF ($C_f$)
  - 1x 100nF ($C_c$)
  - 1x 47µF ($C_1$)
  - 2x 100nF (Decoupling)
