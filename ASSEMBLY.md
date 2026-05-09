# Breadboard Assembly - Single 9V Battery Version

## Step 1: Virtual Ground (VGND) Setup
1. Battery (+) to Red Rail (+9V).
2. Battery (-) to Blue Rail (0V).
3. Place two 10kΩ resistors in series from +9V rail to 0V rail.
4. The junction between the two resistors is your **VGND**. Wire this to a middle row or extra rail.
5. Place a 100µF capacitor between **VGND** and **0V** rail (+ to VGND).

## Step 2: IC Power
1. TL074 Pin 4 to +9V rail.
2. TL074 Pin 11 to 0V rail.

## Step 3: Instrumentation Amplifier (Stage 1)
1. **First Gain Stage:** 1kΩ ($R_g$) between Pin 13 and Pin 6.
2. 10kΩ between Pin 14 and Pin 13.
3. 10kΩ between Pin 7 and Pin 6.
4. **Differential Stage:** 10kΩ from Pin 14 to Pin 2.
5. 10kΩ from Pin 7 to Pin 3.
6. 10kΩ from Pin 3 to **VGND**.
7. 10kΩ from Pin 2 to Pin 1.

## Step 4: 50Hz Notch Filter (Stage 2)
1. **Upper Branch:**
   - Connect Pin 1 to a 47kΩ resistor.
   - Other end of resistor to a new row (Row X).
   - From Row X, connect another 47kΩ resistor to a new row (Row Y - Notch Output).
   - From Row X, connect two 68nF capacitors in parallel to **VGND**.
2. **Lower Branch:**
   - Connect Pin 1 to a 68nF capacitor.
   - Other end of capacitor to a new row (Row Z).
   - From Row Z, connect another 68nF capacitor to Row Y.
   - From Row Z, connect two 47kΩ resistors in parallel to **VGND**.

## Step 5: High-Impedance Stage (Stage 3)
1. Place 100nF capacitor from Row Y (Notch Output) to Pin 10.
2. Place 1MΩ resistor from Pin 10 to **VGND**.
3. Place 470kΩ resistor and 10nF capacitor in parallel between Pin 8 and Pin 9.
4. Connect Pin 9 to a 1kΩ resistor in series with a 47µF capacitor (+ side to resistor). The other side of the capacitor goes to **VGND**.

## Step 6: Electrodes & Scope
1. **Electrode A (Temple):** Pin 12
2. **Electrode B (Temple):** Pin 5
3. **Reference Electrode (Ear):** **VGND** (Middle rail).
4. **Oscilloscope:**
   - Ground Clip to **0V** rail (Battery negative).
   - Probe to Pin 8.
   - **Settings:** Set Oscilloscope to **AC Coupling**. Timebase: 200ms/div.
