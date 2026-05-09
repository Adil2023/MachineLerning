# EEG Circuit Design (Single TL074, Single 9V Battery)

## Architecture
1. **Virtual Ground (VGND):**
   - Created using a resistor divider ($2 \times 10k\Omega$) and a $100\mu F$ capacitor.
   - VGND is $\approx 4.5V$. This acts as the "zero" for the analog signals.
2. **Stage 1: Instrumentation Amplifier (InAmp)**
   - Uses 3 op-amps.
   - Refers to VGND instead of Battery (-).
   - Gain $\approx 21$.
3. **Stage 2: Passive Twin-T Notch Filter (50Hz)**
   - Shunts to VGND.
4. **Stage 3: Non-Inverting Active Bandpass Filter**
   - Uses the 4th op-amp.
   - High Input Impedance (1MΩ) referred to VGND.
   - Stage Gain $\approx 471$.
   - Total Gain $\approx 9,890$.

## Power Supply
- Single 9V Battery.
- **Battery (+):** Connects to Pin 4 (VCC+).
- **Battery (-):** Connects to Pin 11 (VCC-) AND acts as the circuit's 0V return.
- **Virtual Ground (VGND):** 4.5V potential used as the reference for electrodes and filters.

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
11. VCC- (0V / Battery Negative)
12. In+ 4 (InAmp Input 1)
13. In- 4 (InAmp Input 1 - Internal)
14. Out 4 (InAmp First Stage Out 1)

### Virtual Ground Setup
- 10kΩ from +9V to VGND rail.
- 10kΩ from Battery (-) to VGND rail.
- 100µF Capacitor from VGND rail to Battery (-) [Observe Polarity: + to VGND].

### Stage 1: Instrumentation Amplifier
- **Inputs:** Electrode A to Pin 12, Electrode B to Pin 5.
- **First Stage:** 1kΩ between Pin 13 and Pin 6. 10kΩ from Pin 14 to 13. 10kΩ from Pin 7 to 6.
- **Diff Stage:** 10kΩ from Pin 14 to 2. 10kΩ from Pin 7 to 3. 10kΩ from Pin 3 to **VGND**. 10kΩ from Pin 2 to Pin 1.

### Stage 2: 50Hz Notch Filter
- Shunt components (Branch 1 capacitors and Branch 2 resistors) now connect to **VGND**.

### Stage 3: Gain + Filter
- Pull-down resistor $R_{pd}$ (1MΩ) connects Pin 10 to **VGND**.
- Feedback shunt (1kΩ + 47µF) connects to **VGND**.

## Component List (Single Battery Version)
- **1x TL074CN** Quad Op-Amp
- **1x 9V Battery**
- **Resistors (1%):**
  - 2x 1kΩ ($R_g$, $R_{feedback\_shunt}$)
  - 8x 10kΩ (InAmp, VGND Divider)
  - 4x 47kΩ ($R_n1, R_n2$ in upper branch, and $2x$ in parallel for 23.5kΩ shunt)
  - 1x 470kΩ (Final Gain)
  - 1x 1MΩ (Input Pull-down)
- **Capacitors:**
  - 4x 68nF (Notch: 2x in series for branch, 2x in parallel for shunt)
  - 1x 10nF (Low Pass)
  - 1x 100nF (Coupling)
  - 1x 47µF (High Pass)
  - 1x 100µF (VGND Stability)
  - 2x 100nF (Decoupling)
