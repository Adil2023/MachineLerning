# Testing & Safety Procedures

## ⚠️ MANDATORY SAFETY RULES
**FAILURE TO FOLLOW THESE RULES CAN RESULT IN ELECTRIC SHOCK.**

1. **SINGLE 9V BATTERY POWER ONLY:** Never use a wall-plug power supply or more than one 9V battery in a way that bypasses the single-battery design.
2. **OSCILLOSCOPE ISOLATION:**
   - If using a mains-powered oscilloscope, ensure the circuit is **only** connected to the oscilloscope via the probe and ground clip.
   - Do not connect any other mains-powered devices (like a PC via USB) to the circuit while it is attached to a human.
   - **Note:** The oscilloscope ground is connected to Battery (-), while your body is connected to VGND (4.5V). This is safe as long as the battery is isolated from the mains.
3. **NO LIQUID SPILLS:** Keep Ten20 paste away from the breadboard. Keep all liquids away from the experimental setup.
4. **DISCONNECT BEFORE MODIFYING:** Always remove the electrodes from your body before making any changes to the circuit.

## Step 1: Pre-Human Verification (Dry Run)
Before attaching electrodes to yourself, perform these tests:

1. **Power Check:**
   - Measure voltage between Pin 4 and Pin 11 (should be ~9V).
   - Measure voltage between VGND and Pin 11 (should be ~4.5V).
2. **Noise Floor Check:**
   - Short Pin 12 and Pin 5 to GND using jumper wires.
   - Observe Pin 8 on the oscilloscope. You should see a very flat line with minimal noise (less than 100mV peak-to-peak).
3. **Notch Filter Test (If possible):**
   - If you have a signal generator, inject a 50Hz, 100mV sine wave into Pin 12 (with Pin 5 at GND).
   - The output at Pin 8 should be significantly attenuated at 50Hz compared to 40Hz or 60Hz.

## Step 2: Human Testing (Alpha Wave Capture)
Alpha waves (8-13 Hz) are the easiest to see.

1. **Electrode Placement:**
   - Reference: Earlobe or Mastoid (bone behind the ear).
   - A & B: On the occipital lobe (back of the head) or the forehead.
2. **Protocol:**
   - Sit in a comfortable chair and relax.
   - **Eyes Open:** You should see chaotic, low-amplitude signals.
   - **Eyes Closed:** After a few seconds of relaxation with eyes closed, Alpha waves (rhythmic oscillations) should appear on the oscilloscope.
   - **Eyes Open again:** The Alpha waves should immediately disappear (Alpha blocking).

## Troubleshooting
- **Flat line at +9V or -9V:** One of the op-amp stages is "saturated." Check for short circuits or missing resistors in the feedback loops.
- **Heavy 50Hz Sine Wave:** Your notch filter is not tuned or your grounding is poor. Check the Reference electrode connection and the capacitor values in the Twin-T filter.
- **Random Spikes:** Usually caused by moving your eyes, swallowing, or clenching your jaw (muscle artifacts). Stay as still as possible.
