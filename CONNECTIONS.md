# Verified Exhaustive Connection List (10,000x Gain)

## 1. Power & Virtual Ground (MANDATORY)
- **TL074 Pin 4 (VCC+)** -> Breadboard **Red Rail (+9V)**
- **TL074 Pin 11 (VCC-)** -> Breadboard **Blue Rail (0V)**
- **Rvg1 (10k)**: Red Rail to VGND Rail
- **Rvg2 (10k)**: VGND Rail to Blue Rail
- **Cvg (100uF)**: VGND Rail (+) to Blue Rail (-)

## 2. Stage 1: Buffered IA (U1A, U1B)
- **Electrode A** -> **Pin 12** (In+)
- **Electrode B** -> **Pin 5** (In+)
- **Rg (200 Ohm)**: **Pin 13** to **Pin 6**
- **R1 (10k)**: **Pin 14** to **Pin 13**
- **R2 (10k)**: **Pin 7** to **Pin 6**

## 3. Stage 2: Balanced Difference Amp (U1D)
- **Rsub1 (10k)**: **Pin 14** to **Pin 9**
- **Rsub2 (10k)**: **Pin 7** to **Pin 10**
- **Rref (1M)**: **Pin 10** to **VGND Rail** (Matches Rf for balance)
- **Rf (1M)**: **Pin 9** to **Pin 8** (Feedback)
- **Cf (4.7nF)**: **Pin 9** to **Pin 8** (Low-pass filter, fc ~34Hz)

## 4. Stage 3: Active DRL (U1C)
- **Rcm1 (100k)**: **Pin 14** to **Pin 2**
- **Rcm2 (100k)**: **Pin 7** to **Pin 2**
- **Rdrl (1M)**: **Pin 2** to **Pin 1**
- **Pin 3 (In+)** -> **VGND Rail**
- **Pin 1 (DRL Out)** -> **Driven Reference Electrode (Ear)**

## 5. Scope Output
- **Pin 8 (Final signal)** -> **Scope Probe** (Use AC Coupling)
- **Blue Rail (0V)** -> **Scope Ground**
