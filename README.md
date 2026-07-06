> [!WARNING]
> **Battery Power Only!** To ensure user safety and proper electrical isolation (Galvanic Isolation), this EEG circuit must only be powered by a 9V battery. Never connect this circuit to a mains-powered power supply or any device connected to the AC power grid while electrodes are attached to a human subject.

# Machine Learning

This repository contains documentation and designs for a DIY Electroencephalography (EEG) circuit. The design is optimized for simplicity and safety, utilizing a single TL074CN quad operational amplifier and a single 9V battery.

## Key Features
- **3-Op-Amp Instrumentation Amplifier**: High gain and high Common-Mode Rejection Ratio (CMRR) for capturing microvolt-level brain signals.
- **Active Driven-Right-Leg (DRL)**: The 4th op-amp is configured for active noise cancellation, significantly reducing 50/60Hz interference.
- **Single Supply Design**: Operates on a single 9V battery with a virtual ground (VGND) divider at 4.5V.
- **Minimalist Hardware**: Designed to be built on a standard breadboard with discrete components.
