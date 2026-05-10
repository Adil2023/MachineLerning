# Verified Exhaustive Connection List (Active DRL Subtractor)

## 1. Power
- Pin 4: V+ (+9V)
- Pin 11: 0V (Battery Negative)
- R1 (10k): V+ to VGND rail
- R2 (10k): VGND rail to 0V rail
- C1 (100uF): VGND to 0V

## 2. Signal Chain
- Electrode A -> Pin 12 (U1A In+)
- Pin 13 (In-) -> Pin 14 (Out) - Unity Gain Buffer
- Electrode B -> Pin 5 (U1B In+)
- Pin 6 (In-) -> Pin 7 (Out) - Unity Gain Buffer

## 3. Difference stage & Gain
- R3 (10k): Pin 14 to Pin 9 (U1D In-)
- R4 (10k): Pin 7 to Pin 10 (U1D In+)
- R5 (1M): Pin 10 to VGND
- Rf (1M): Pin 9 to Pin 8 (Out)
- Cf (4.7nF): Pin 9 to Pin 8

## 4. Active DRL
- R6 (100k): Pin 14 to Pin 2 (U1C In-)
- R7 (100k): Pin 7 to Pin 2 (U1C In-)
- Rdrl (1M): Pin 2 to Pin 1 (Out)
- Pin 3 (In+): To VGND
- Pin 1 (DRL Out) -> Driven Reference Electrode
