# Breadboard Assembly & Electrode Guide - Revised

## Step 1: Power Supply Setup
1. Place TL074 on breadboard.
2. Battery 1 (+) to Red Rail (+9V).
3. Battery 1 (-) to Battery 2 (+). Connect this junction to Blue Rail (GND).
4. Battery 2 (-) to Bottom Red Rail (-9V).
5. Pin 4 to +9V, Pin 11 to -9V.

## Step 2: Instrumentation Amplifier
1. 1kΩ ($R_g$) between Pin 13 and Pin 6.
2. 10kΩ between Pin 14 and Pin 13.
3. 10kΩ between Pin 7 and Pin 6.
4. 10kΩ from Pin 14 to Pin 2.
5. 10kΩ from Pin 7 to Pin 3.
6. 10kΩ from Pin 3 to GND.
7. 10kΩ from Pin 2 to Pin 1.

## Step 3: 50Hz Notch Filter (Fixing Resistor Error)
1. **Upper Branch:** Pin 1 -> 47kΩ -> Row X. Row X -> 47kΩ -> Row Y (Filter Output). From Row X, place two 68nF capacitors to GND.
2. **Lower Branch:** Pin 1 -> 68nF -> Row Z. Row Z -> 68nF -> Row Y. From Row Z, place two 47kΩ resistors in parallel to GND.

## Step 4: High-Impedance Stage (Non-Inverting)
1. Place 100nF capacitor from Row Y (Filter Output) to Pin 10.
2. Place 1MΩ resistor from Pin 10 to GND.
3. Place 470kΩ resistor and 10nF capacitor in parallel between Pin 8 and Pin 9.
4. Connect Pin 9 to a 1kΩ resistor in series with a 47µF capacitor (+ side to resistor). The other side of the capacitor goes to GND.

## Step 5: Electrodes & Testing
1. **Electrode A:** Pin 12
2. **Electrode B:** Pin 5
3. **Reference:** GND Rail
4. **Oscilloscope:** Probe to Pin 8, Ground to GND Rail.
