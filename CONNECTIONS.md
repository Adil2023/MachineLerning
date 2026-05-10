# Detailed Connection List (Point-to-Point)

## Power Supply & Virtual Ground
- **Battery (+9V)** -> Breadboard **Red Rail (+)**
- **Battery (0V)** -> Breadboard **Blue Rail (-)**
- **Resistor Rvg1 (10k)** -> Terminal 1: **Red Rail (+)**, Terminal 2: **VGND Rail**
- **Resistor Rvg2 (10k)** -> Terminal 1: **VGND Rail**, Terminal 2: **Blue Rail (-)**
- **Capacitor Cvg (100uF)** -> Terminal (+): **VGND Rail**, Terminal (-): **Blue Rail (-)**

## TL074 IC Connections
- **Pin 4 (VCC+)** -> **Red Rail (+)**
- **Pin 11 (VCC-)** -> **Blue Rail (-)**
- **Pin 10 (Stage 3 Input+)** -> **VGND Rail** (via 1M Rpd resistor)

## Stage 1: Instrumentation Amplifier
- **Rg (1k)** -> Terminal 1: **Pin 13**, Terminal 2: **Pin 6**
- **R1 (10k)** -> Terminal 1: **Pin 14**, Terminal 2: **Pin 13**
- **R2 (10k)** -> Terminal 1: **Pin 7**, Terminal 2: **Pin 6**
- **R3 (10k)** -> Terminal 1: **Pin 14**, Terminal 2: **Pin 2**
- **R4 (10k)** -> Terminal 1: **Pin 7**, Terminal 2: **Pin 3**
- **R5 (10k)** -> Terminal 1: **Pin 3**, Terminal 2: **VGND Rail**
- **R6 (10k)** -> Terminal 1: **Pin 2**, Terminal 2: **Pin 1**

## Stage 2: 50Hz Notch Filter
- **Rn1 (47k)** -> Terminal 1: **Pin 1**, Terminal 2: **Node X**
- **Rn2 (47k)** -> Terminal 1: **Node X**, Terminal 2: **Node Y (Notch Out)**
- **Cn1/Cn2 (2x 68n in parallel)** -> From **Node X** to **VGND Rail**
- **Cn3 (68n)** -> Terminal 1: **Pin 1**, Terminal 2: **Node Z**
- **Cn4 (68n)** -> Terminal 1: **Node Z**, Terminal 2: **Node Y (Notch Out)**
- **Rn3/Rn4 (2x 47k in parallel)** -> From **Node Z** to **VGND Rail**

## Stage 3: Gain & Filter
- **Cc (100n)** -> Terminal 1: **Node Y (Notch Out)**, Terminal 2: **Pin 10**
- **Rpd (1M)** -> Terminal 1: **Pin 10**, Terminal 2: **VGND Rail**
- **Rf (470k)** -> Terminal 1: **Pin 8**, Terminal 2: **Pin 9**
- **Cf (10n)** -> Terminal 1: **Pin 8**, Terminal 2: **Pin 9**
- **Rs (1k)** -> Terminal 1: **Pin 9**, Terminal 2: **Node W**
- **Cs (47uF)** -> Terminal (+): **Node W**, Terminal (-): **VGND Rail**

## External Interfaces
- **Electrode A** -> **Pin 12**
- **Electrode B** -> **Pin 5**
- **Reference Electrode** -> **VGND Rail**
- **Oscilloscope Probe** -> **Pin 8**
- **Oscilloscope Ground** -> **Blue Rail (-)** (Battery Negative)
