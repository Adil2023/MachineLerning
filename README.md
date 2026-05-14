# Machine Learning

DIY EEG circuit designs specifically constrained to use a single TL074CN op-amp and a single 9V battery.

## ⚠️ Safety Warning

**BATTERY POWER ONLY.** This device must never be connected to a mains-powered power supply or any device connected to the mains (like a computer via USB) unless proper galvanic isolation is used. Failure to follow this warning can result in serious injury or death from electrical shock.

## Table of Contents

- [Safety Warning](#-safety-warning)
- [Technical Overview](#technical-overview)
- [Circuit Constraints](#circuit-constraints)
- [Usage](#usage)

## Technical Overview

This project provides a minimalist yet effective EEG acquisition circuit design. The architecture leverages a single TL074 quad op-amp to implement a full instrumentation stage and active noise cancellation.

- **Instrumentation Amplifier (IA):** A 3-op-amp configuration providing high gain and high Common-Mode Rejection Ratio (CMRR).
- **Driven-Right-Leg (DRL):** The 4th op-amp is configured as an active DRL circuit for active noise cancellation, significantly reducing power line interference.
- **Virtual Ground:** A voltage divider creates a 4.5V virtual ground (VGND) from the 9V supply to allow for bipolar signal processing.
- **Notch Filter:** Tuned to 50Hz to suppress local power line noise.

## Circuit Constraints

- **Power:** Single 9V Battery.
- **Amplifier:** Single TL074CN Quad Op-Amp.
- **Electrodes:** Compatible with Ten20 conductive paste.

## Usage

*Documentation for assembly and connection lists coming soon.*
