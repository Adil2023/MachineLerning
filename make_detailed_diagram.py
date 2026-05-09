from PIL import Image, ImageDraw, ImageFont

def draw_breadboard():
    # Dimensions and Grid
    width, height = 2400, 1200
    hole_pitch = 30
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Draw Breadboard Body
    bb_x1, bb_y1 = 100, 100
    bb_w, bb_h = 63 * hole_pitch + 200, 20 * hole_pitch
    draw.rectangle([bb_x1, bb_y1, bb_x1 + bb_w, bb_y1 + bb_h], fill=(245, 245, 245), outline=(200, 200, 200), width=2)

    # Function to get pixel coordinates for hole (col, row)
    # Rows: 1-2 (Power Top), 3-7 (A-E), 8-12 (F-J), 13-14 (Power Bottom)
    def get_hole_pos(col, row_name):
        row_map = {
            'V+': 1, 'VG': 2,
            'A': 5, 'B': 6, 'C': 7, 'D': 8, 'E': 9,
            'F': 11, 'G': 12, 'H': 13, 'I': 14, 'J': 15,
            '0V': 18
        }
        x = bb_x1 + 100 + (col-1) * hole_pitch
        y = bb_y1 + row_map[row_name] * hole_pitch
        return (x, y)

    # Draw Holes
    for col in range(1, 64):
        for row in ['V+', 'VG', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '0V']:
            x, y = get_hole_pos(col, row)
            draw.ellipse([x-4, y-4, x+4, y+4], fill=(200, 200, 200))

    # Power Rails Coloring
    # V+ (Red)
    draw.line([bb_x1 + 80, bb_y1 + 1 * hole_pitch, bb_x1 + bb_w - 80, bb_y1 + 1 * hole_pitch], fill=(255, 0, 0), width=3)
    # VG (Green)
    draw.line([bb_x1 + 80, bb_y1 + 2 * hole_pitch, bb_x1 + bb_w - 80, bb_y1 + 2 * hole_pitch], fill=(0, 200, 0), width=3)
    # 0V (Blue)
    draw.line([bb_x1 + 80, bb_y1 + 18 * hole_pitch, bb_x1 + bb_w - 80, bb_y1 + 18 * hole_pitch], fill=(0, 0, 255), width=3)

    # Components Logic
    def draw_resistor(col1, row1, col2, row2, value, color=(200, 150, 100)):
        p1 = get_hole_pos(col1, row1)
        p2 = get_hole_pos(col2, row2)
        draw.line([p1, p2], fill=(100, 100, 100), width=4) # Leads
        # Body
        mid_x, mid_y = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        draw.rectangle([mid_x-20, mid_y-10, mid_x+20, mid_y+10], fill=color, outline=(0,0,0))
        draw.text((mid_x, mid_y-25), value, fill=(0,0,0), font=small_font, anchor="mm")

    def draw_capacitor(col1, row1, col2, row2, value, color=(100, 200, 255), polar=False):
        p1 = get_hole_pos(col1, row1)
        p2 = get_hole_pos(col2, row2)
        draw.line([p1, p2], fill=(120, 120, 120), width=3)
        mid_x, mid_y = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        if polar:
            draw.ellipse([mid_x-15, mid_y-15, mid_x+15, mid_y+15], fill=(50, 50, 50))
            draw.text((mid_x, mid_y), "+", fill=(255,255,255), font=small_font, anchor="mm")
        else:
            draw.rectangle([mid_x-10, mid_y-10, mid_x+10, mid_y+10], fill=color, outline=(0,0,0))
        draw.text((mid_x, mid_y-25), value, fill=(0,0,0), font=small_font, anchor="mm")

    def draw_wire(col1, row1, col2, row2, color=(0,0,0)):
        p1 = get_hole_pos(col1, row1)
        p2 = get_hole_pos(col2, row2)
        draw.line([p1, p2], fill=color, width=5)

    # 1. VGND Divider (Cols 1-5)
    draw_resistor(2, 'V+', 2, 'VG', "10k")
    draw_resistor(4, 'VG', 4, '0V', "10k")
    draw_capacitor(5, 'VG', 5, '0V', "100uF", polar=True)

    # 2. TL074 (Cols 20-26, across center)
    ic_x1, ic_y1 = get_hole_pos(20, 'E')
    ic_x2, ic_y2 = get_hole_pos(26, 'F')
    draw.rectangle([ic_x1-15, ic_y1-15, ic_x2+15, ic_y2+15], fill=(40, 40, 40))
    draw.text(((ic_x1+ic_x2)//2, (ic_y1+ic_y2)//2), "TL074", fill=(255,255,255), font=font, anchor="mm")
    # Pin Labels
    draw.text(get_hole_pos(20, 'D'), "1", fill=(0,0,0), font=small_font)
    draw.text(get_hole_pos(26, 'D'), "7", fill=(0,0,0), font=small_font)
    draw.text(get_hole_pos(26, 'G'), "8", fill=(0,0,0), font=small_font)
    draw.text(get_hole_pos(20, 'G'), "14", fill=(0,0,0), font=small_font)

    # 3. IC Power
    draw_wire(23, 'F', 23, 'V+', (255, 0, 0)) # Pin 4 to +9V (wait, Pin 4 is at Col 23, Row E? No, Pin 4 is on Side 1)
    # Correction: DIP14: 1-7 on bottom (relative to notch left), 8-14 on top.
    # Let's use:
    # Top Row (F-J): 14 13 12 11 10 9 8
    # Bottom Row (A-E): 1 2 3 4 5 6 7
    # Notch is on the left.
    # Col 20: 1 (E) and 14 (F)
    # Col 23: 4 (E) and 11 (F)
    draw_wire(23, 'E', 23, 'V+', (255, 0, 0))   # Pin 4 to +9V
    draw_wire(23, 'F', 23, '0V', (0, 0, 255))   # Pin 11 to 0V

    # 4. Stage 1 (InAmp)
    draw_resistor(21, 'F', 25, 'E', "1k Rg") # Pin 13 to Pin 6 (Diagonal)
    draw_resistor(20, 'F', 21, 'F', "10k R1") # Pin 14 to 13
    draw_resistor(26, 'E', 25, 'E', "10k R2") # Pin 7 to 6
    draw_wire(20, 'F', 30, 'F', (150, 150, 150)) # Pin 14 jump
    draw_resistor(30, 'F', 21, 'E', "10k R3") # Pin 14(jump) to Pin 2
    draw_resistor(26, 'E', 22, 'E', "10k R4") # Pin 7 to 3
    draw_resistor(22, 'E', 22, 'VG', "10k R5") # Pin 3 to VGND
    draw_resistor(21, 'E', 20, 'E', "10k R6") # Pin 2 to 1

    # 5. Stage 2 (Notch)
    # Upper Branch: Pin 1 -> 47k -> Col 35 -> 47k -> Col 40 (Notch Out)
    draw_resistor(20, 'E', 35, 'C', "47k")
    draw_resistor(35, 'C', 40, 'C', "47k")
    draw_capacitor(35, 'C', 35, 'VG', "136nF(2x68n)") # Shunt
    # Lower Branch: Pin 1 -> 68n -> Col 38 -> 68n -> Col 40
    draw_capacitor(20, 'E', 38, 'A', "68n")
    draw_capacitor(38, 'A', 40, 'C', "68n")
    draw_resistor(38, 'A', 38, 'VG', "23.5k(2x47k)") # Shunt

    # 6. Stage 3 (Gain)
    draw_capacitor(40, 'C', 24, 'F', "100n Cc") # Notch Out to Pin 10
    draw_resistor(24, 'F', 24, 'VG', "1M Rpd") # Pin 10 to VGND
    draw_resistor(26, 'F', 25, 'F', "470k Rf") # Pin 8 to 9
    draw_capacitor(26, 'F', 27, 'G', "10n Cf") # Parallel Cf
    draw_wire(27, 'G', 25, 'F', (100, 100, 100))
    draw_resistor(25, 'F', 45, 'F', "1k") # Pin 9 to C1
    draw_capacitor(45, 'F', 45, 'VG', "47uF C1", polar=True)

    # 7. Inputs/Outputs
    draw_wire(32, 'F', 32, 'V+', (255, 0, 0)) # Placeholder
    draw.text(get_hole_pos(24, 'E'), "A", fill=(255,0,0), font=font) # Pin 12 Input
    draw.text(get_hole_pos(21, 'A'), "B", fill=(255,0,0), font=font) # Pin 5 Input
    draw.text(get_hole_pos(26, 'J'), "OUT", fill=(255,0,0), font=font) # Pin 8 Output

    # Save
    img.save('EEG_Breadboard_Detailed_Layout.png')

if __name__ == "__main__":
    draw_breadboard()
