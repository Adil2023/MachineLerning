# EEG Circuit Design: Professional DRL Redesign (10,000x Gain)

## Technical Architecture
1. **Precision Input buffers:** High-impedance buffering for Electrode A and B.
2. **AC Inter-stage Coupling:** 100nF and 1M bias resistors block DC offsets.
3. **Difference & Gain Stage:** 10,000x total gain (100x Stage 1, 100x Stage 2).
4. **Active Noise Cancellation:** Driven-Right-Leg (DRL) circuit cancels hum.
5. **Power:** Single 9V battery with 4.5V Virtual Ground.
