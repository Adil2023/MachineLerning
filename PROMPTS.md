# AI Prompts for High-Performance EEG DRL Project

## 1. Technical Design Prompt (Subtractor + DRL)
> "Design a high-performance DIY EEG circuit using one TL074 quad op-amp and a 9V battery. Implement:
> - **Input Buffers (U1A/U1B):** High-impedance unity gain buffers for Electrode A and B.
> - **Active DRL (U1C):** Difference stage to sense common-mode noise, inverted and injected via Pin 1 to the body.
> - **Differential Subtractor & Gain (U1D):** Final stage to perform (V_buffer_A - V_buffer_B) subtraction and ~10,000x total gain with integrated bandpass filtering (3-30Hz).
> - **Power:** 9V battery with VGND rail splitter."

## 2. Exhaustive Connection Prompt
> "Generate a terminal-by-terminal connection list for the 4-op-amp EEG DRL Subtractor circuit. List every connection between the 14 IC pins, resistors, capacitors, battery, electrodes, and scope."

## 3. Spatial Layout Prompt
> "Generate a realistic breadboard diagram with components away from the IC, electrodes far LEFT, battery positioned UNDER, and scope connection at the BOTTOM. Keep IC area completely clear."
