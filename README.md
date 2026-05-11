# Machine Learning - DIY EEG Circuit Design

A repository dedicated to accessible, single-supply EEG circuit designs optimized for DIY enthusiasts and researchers.

## 📋 Table of Contents
- [⚠️ Safety Warning](#️-safety-warning)
- [🛠️ Technical Specifications](#️-technical-specifications)
- [🏗️ Architectural Overview](#️-architectural-overview)
- [🚀 Getting Started](#-getting-started)

---

## ⚠️ Safety Warning

> **IMPORTANT: ELECTRICAL SAFETY IS PARAMOUNT.**

- **Battery Power Only:** This circuit must **ONLY** be powered by a single 9V battery. Never connect this device to a mains-powered DC adapter or any AC source while connected to a human subject.
- **Isolation:** Battery operation provides essential galvanic isolation from the power grid, preventing potentially lethal electric shocks.
- **Electrodes:** Use only high-quality electrodes and conductive paste (e.g., Ten20) for consistent and safe signal acquisition.
- **Disclaimer:** This project is for educational and research purposes. It is not a medical device.

---

## 🛠️ Technical Specifications

| Feature | Specification |
| :--- | :--- |
| **Operational Amplifier** | 1x TL074CN (Quad Op-Amp) |
| **Power Supply** | 1x 9V Battery |
| **Virtual Ground (VGND)** | 4.5V (Voltage Divider) |
| **Notch Filter** | 50Hz (Tuned for local power grid frequency) |
| **Connectivity** | Ten20 Conductive Paste |

## 🏗️ Architectural Overview

The design utilizes a single TL074CN integrated circuit to implement a high-performance EEG front-end:

1.  **Instrumentation Amplifier (IA):** Three of the four op-amps are configured as a classic 3-op-amp IA, providing high input impedance, high gain, and excellent Common-Mode Rejection Ratio (CMRR).
2.  **Driven-Right-Leg (DRL):** The fourth op-amp is configured as an active DRL circuit to actively cancel common-mode noise, significantly improving signal quality.
3.  **Biasing:** A 4.5V virtual ground allows for bipolar signal processing using a single-ended 9V supply.

## 🚀 Getting Started

To begin building your EEG circuit:
1. Review the [Architectural Overview](#️-architectural-overview).
2. Gather the components listed in [Technical Specifications](#️-technical-specifications).
3. **Always** adhere to the [Safety Warning](#️-safety-warning).

---

*Part of the Palette UX Improvement Initiative - Enhancing documentation accessibility and safety.*
