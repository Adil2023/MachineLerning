# Machine Learning

## Table of Contents
- [Safety Instructions](#safety-instructions)
- [Project Overview](#project-overview)
- [Technical Specifications](#technical-specifications)
- [Bill of Materials](#bill-of-materials)

## Safety Instructions

> [!WARNING]
> **WARNING: BATTERY POWER ONLY!**
> This project involves connecting electrodes directly to the human body. To ensure safety and galvanic isolation, **ONLY use a 9V battery** as the power source. NEVER use a wall adapter, USB power, or any other mains-connected power supply.

## Project Overview

This repository contains DIY EEG circuit designs specifically constrained to use a single TL074CN op-amp and a single 9V battery. The goal is to provide a low-cost, accessible way to explore brain-computer interfacing.

## Technical Specifications

- **Amplifier Architecture:** 3-op-amp Instrumentation Amplifier (IA) for high gain and Common-Mode Rejection Ratio (CMRR).
- **Active Noise Cancellation:** 4th op-amp configured as an Active Driven-Right-Leg (DRL) circuit.
- **Power Supply:** Single 9V Battery.
- **Virtual Ground:** 4.5V divider to accommodate bipolar signals with a unipolar supply.
- **Filter Tuning:** Notch filters are tuned to 50Hz by default (optimized for local power line frequency).
- **Electrode Connectivity:** Designed for use with Ten20 conductive paste.

## Bill of Materials

- 1x TL074CN Quad Op-Amp
- 1x 9V Battery
- 1x Breadboard
- 16x Resistors
- 8x Capacitors
- EEG Electrodes
- Ten20 Conductive Paste
