> [!WARNING]
> **CRITICAL SAFETY: BATTERY POWER ONLY**
> This EEG circuit must ONLY be powered by a single 9V battery. NEVER connect this device to a mains-powered supply or any equipment connected to the grid. This is essential for maintaining **Galvanic Isolation** and ensuring user safety during human electrode connection.

# Machine Learning

DIY EEG circuit designs specifically constrained to use a single TL074CN op-amp and a single 9V battery.

## Table of Contents
- [Technical Architecture](#technical-architecture)
- [Usage Instructions](#usage-instructions)
- [Safety and Isolation](#safety-and-isolation)

## Technical Architecture

The optimal technical architecture for this single-TL074 EEG circuit utilizes a 3-op-amp **Instrumentation Amplifier (IA)** configuration to achieve high gain and high Common-Mode Rejection Ratio (CMRR).

- **Amplification:** 3 op-amps are configured as an IA.
- **Noise Cancellation:** The 4th op-amp is configured as an **Active Driven-Right-Leg (DRL)** circuit for active noise cancellation.
- **Power:** A **Virtual Ground (VGND)** divider at 4.5V is used to accommodate bipolar signals with a unipolar 9V supply.
- **Filtering:** Includes notch filters tuned to 50Hz (local power line frequency) for interference reduction.

## Usage Instructions

1. **Electrode Connection:** Use **Ten20 conductive paste** for reliable electrode connectivity to the scalp.
2. **Powering:** Connect a single 9V battery to the designated terminals.
3. **Safety:** Ensure all connections are secure and only use battery power.

## Safety and Isolation

For human electrode connection, the circuit prioritizes battery power for maximum safety and electrical isolation. Always double-check connections before use.
