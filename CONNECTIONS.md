# Detailed Connection List (Point-to-Point)

## 1. VGND Group
- R1 (10k): V+ to VGND
- R2 (10k): VGND to 0V
- C1 (100uF): VGND (+) to 0V (-)

## 2. IC Power
- Pin 4: V+
- Pin 11: 0V

## 3. InAmp (Stage 1)
- R5 (Rg, 1k): Pin 13 to Pin 6
- R3 (10k): Pin 14 to Pin 13
- R4 (10k): Pin 7 to Pin 6
- R6 (10k): Pin 14 to Pin 2
- R7 (10k): Pin 7 to Pin 3
- R8 (10k): Pin 3 to VGND
- R9 (10k): Pin 2 to Pin 1

## 4. Notch Filter (Stage 2)
- R10 (47k): Pin 1 to Node X
- R11 (47k): Node X to Node Y (Notch Out)
- C2/C3 (2x 68n parallel): Node X to VGND
- C4 (68n): Pin 1 to Node Z
- C5 (68n): Node Z to Node Y
- R12/R13 (2x 47k parallel): Node Z to VGND

## 5. Output Stage (Stage 3)
- C6 (100n): Node Y to Pin 10
- R14 (1M): Pin 10 to VGND
- R15 (470k): Pin 8 to Pin 9
- C7 (10n): Pin 8 to Pin 9
- R16 (1k): Pin 9 to Node W
- C8 (47uF): Node W (+) to VGND
