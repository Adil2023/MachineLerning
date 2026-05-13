# Machine Learning

> [!CAUTION]
> ### ⚠️ SAFETY FIRST
> **BATTERY POWER ONLY.** Never connect this circuit to any mains-powered equipment (including wall adapters or PCs) while connected to a human.
> **GALVANIC ISOLATION.** Ensure the user is completely isolated from any electrical ground other than the circuit's floating ground.

## Overview
This repository contains DIY EEG (Electroencephalography) circuit designs specifically optimized for low-cost, high-performance bio-signal acquisition.

### Technical Architecture
- **Single TL074CN Op-Amp:** Optimized for a single-chip solution.
- **Single 9V Battery:** Ensures safety and portability.
- **3-Op-Amp Instrumentation Amplifier:** Provides high gain and superior CMRR.
- **Active Driven-Right-Leg (DRL):** Integrated for active noise cancellation.
- **50Hz Notch Filter:** Tuned for power line interference rejection.

## Usage
- Use **Ten20 conductive paste** for electrode connectivity.
- Follow the `CONNECTIONS.md` guide for precise assembly instructions.
- Refer to `PROMPTS.md` for the AI prompts used to generate these designs.
