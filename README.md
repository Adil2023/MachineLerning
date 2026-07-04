> [!WARNING]
> **CRITICAL SAFETY: BATTERY POWER ONLY**
> This DIY EEG circuit must ONLY be powered by a 9V battery. NEVER connect this circuit to any mains-powered device or wall outlet, even through a power adapter. Proper galvanic isolation is mandatory for human electrode connection to prevent electric shock.

# Machine Learning

This project provides a professional-grade DIY EEG circuit design optimized for simplicity and safety. The architecture utilizes a single **TL074CN** quad op-amp and is strictly constrained to run on a single **9V battery**.

The design features a 3-op-amp instrumentation amplifier for high gain and common-mode rejection, with the fourth op-amp configured as an active Driven-Right-Leg (DRL) circuit for noise cancellation.
