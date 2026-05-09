# Prompts to Re-create this EEG Circuit Project

If you want an AI to design this exact circuit, use the following sequence of prompts:

## 1. Technical Design Prompt
> "Design a professional EEG circuit that fits on a standard breadboard using exactly one TL074 quad op-amp and powered by a single 9V battery. The target is to visualize Alpha brain waves (8-13Hz) on an oscilloscope in real-time. Use a 3-op-amp Instrumentation Amplifier configuration for the input stage, a passive Twin-T notch filter for 50Hz mains hum rejection, and the final 4th op-amp as a bandpass gain stage (target total gain ~10,000x). Since we only have one 9V battery, implement a virtual ground (VGND) at 4.5V using a resistor divider and a 100uF decoupling capacitor. Provide the Bill of Materials (BOM) and gain/filter calculations."

## 2. Assembly & Safety Prompt
> "Write a step-by-step breadboard assembly guide for the single-TL074 EEG circuit. Include detailed wiring for the virtual ground setup, IC power, and the three signal stages. Add a dedicated section for safety and testing that mandates battery power only and warns about oscilloscope grounding risks. Provide instructions for DIY electrode placement (Forehead/Temples and Ear/Mastoid reference) and using Ten20 conductive paste."

## 3. High-Fidelity Layout Prompt
> "Generate a high-fidelity, 'Fritzing-style' breadboard layout diagram for the EEG circuit. The diagram must show the 9V battery on the bottom-right and the electrode inputs (A, B, and Reference) on the bottom-left to avoid confusion. **CRITICAL:** Implement a strict 'no-fly zone' over the IC body; no wires or components may cross over the TL074. All jumper wires connecting the top and bottom rows must be routed around the ends of the chip. Ensure all 14 pin numbers are clearly labeled and visible on the diagram. Draw realistic resistors with color bands and distinct capacitor types."

## 4. Professional Schematic Prompt
> "Create a professional electrical schematic for the single-TL074 EEG circuit. Use standard symbols for op-amps, resistors, and capacitors. Clearly label all IC pins (1-14) and functional blocks: Instrumentation Amp, 50Hz Notch Filter, and Active Bandpass Filter. Show the Virtual Ground (VGND) reference point clearly."

## 5. Documentation Packaging Prompt
> "Compile the circuit theory, assembly guide, testing protocol, realistic layout diagram, and schematic into a single, professional PDF manual titled 'DIY EEG Circuit Guide'. Ensure all mathematical symbols (like Ohm and micro) are correctly formatted for a portable document."
