from PIL import Image, ImageDraw, ImageFont

def draw_realistic_breadboard():
    width, height = 2400, 1600
    hole_pitch = 30
    img = Image.new('RGB', (width, height), color=(220, 220, 220))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Breadboard constants
    bb_x1, bb_y1 = 100, 150
    bb_w, bb_h = 63 * hole_pitch + 200, 35 * hole_pitch

    # Draw Breadboard Body (Realistic look)
    draw.rectangle([bb_x1, bb_y1, bb_x1 + bb_w, bb_y1 + bb_h], fill=(240, 240, 240), outline=(180, 180, 180), width=3)

    def get_hole_pos(col, row_name):
        # Rows: P1(+), P2(VG), A-E, <Gap>, F-J, P3(GND)
        row_map = {
            'V+': 2, 'VG': 3,
            'A': 6, 'B': 7, 'C': 8, 'D': 9, 'E': 10,
            'F': 13, 'G': 14, 'H': 15, 'I': 16, 'J': 17,
            '0V': 20
        }
        x = bb_x1 + 100 + (col-1) * hole_pitch
        y = bb_y1 + row_map[row_name] * hole_pitch
        return (x, y)

    # Draw Holes
    for col in range(1, 64):
        for row in ['V+', 'VG', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '0V']:
            x, y = get_hole_pos(col, row)
            draw.ellipse([x-5, y-5, x+5, y+5], fill=(180, 180, 180), outline=(150, 150, 150))

    # Helper for realistic resistor
    def draw_res_realistic(col1, row1, col2, row2, value, bands):
        p1 = get_hole_pos(col1, row1)
        p2 = get_hole_pos(col2, row2)
        # Wire leads
        draw.line([p1, p2], fill=(160, 160, 160), width=4)
        # Body
        mid_x, mid_y = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        import math
        angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
        dist = 60
        bx1, by1 = mid_x - math.cos(angle)*dist/2, mid_y - math.sin(angle)*dist/2
        bx2, by2 = mid_x + math.cos(angle)*dist/2, mid_y + math.sin(angle)*dist/2

        # Draw body rectangle (slightly rounded)
        draw.line([bx1, by1, bx2, by2], fill=(222, 184, 135), width=20)

        # Draw bands
        band_colors = {
            'brown': (139, 69, 19), 'black': (0, 0, 0), 'red': (255, 0, 0),
            'orange': (255, 165, 0), 'yellow': (255, 255, 0), 'green': (0, 128, 0),
            'violet': (238, 130, 238), 'gold': (218, 165, 32)
        }
        for i, b in enumerate(bands):
            f = (i + 1) / (len(bands) + 1)
            b_x = bx1 + (bx2-bx1)*f
            b_y = by1 + (by2-by1)*f
            # Draw a small perpendicular line for the band
            perp_dx = math.sin(angle) * 10
            perp_dy = -math.cos(angle) * 10
            draw.line([b_x-perp_dx, b_y-perp_dy, b_x+perp_dx, b_y+perp_dy], fill=band_colors[b], width=4)

        draw.text((mid_x, mid_y - 30), value, fill=(0,0,0), font=small_font, anchor="mm")

    # Helper for realistic capacitor
    def draw_cap_realistic(col, row1, row2, value, type='disc'):
        p1 = get_hole_pos(col, row1)
        p2 = get_hole_pos(col, row2)
        draw.line([p1, p2], fill=(160, 160, 160), width=3)
        mid_x, mid_y = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        if type == 'disc':
            draw.ellipse([mid_x-15, mid_y-15, mid_x+15, mid_y+15], fill=(255, 140, 0), outline=(0,0,0))
        else: # Electrolytic
            draw.rectangle([mid_x-12, mid_y-20, mid_x+12, mid_y+20], fill=(40, 40, 40))
            draw.line([mid_x-12, mid_y-10, mid_x+12, mid_y-10], fill=(200, 200, 200), width=5)
        draw.text((mid_x + 25, mid_y), value, fill=(0,0,0), font=small_font, anchor="lm")

    # Layout Plan (Spread out)
    # Cols 5-10: Virtual Ground
    draw_res_realistic(5, 'V+', 5, 'VG', "10k", ['brown', 'black', 'orange', 'gold'])
    draw_res_realistic(7, 'VG', 7, '0V', "10k", ['brown', 'black', 'orange', 'gold'])
    draw_cap_realistic(9, 'VG', '0V', "100uF", type='elec')

    # Cols 20-30: TL074 IC and stage 1
    # Pinout: Notch left.
    # Top (Row F-J): 14 13 12 11 10 9 8
    # Bottom (Row A-E): 1 2 3 4 5 6 7
    ic_col_start = 25
    draw.rectangle([get_hole_pos(ic_col_start, 'E')[0]-10, get_hole_pos(ic_col_start, 'E')[1]-10,
                    get_hole_pos(ic_col_start+6, 'F')[0]+10, get_hole_pos(ic_col_start+6, 'F')[1]+10], fill=(30, 30, 30))
    draw.text((get_hole_pos(ic_col_start+3, 'E')[0], get_hole_pos(ic_col_start, 'E')[1]+30), "TL074", fill=(255,255,255), font=font, anchor="mm")

    # Power
    draw.line([get_hole_pos(ic_col_start+3, 'E'), get_hole_pos(ic_col_start+3, 'V+')], fill=(255,0,0), width=4) # Pin 4
    draw.line([get_hole_pos(ic_col_start+3, 'F'), get_hole_pos(ic_col_start+3, '0V')], fill=(0,0,255), width=4) # Pin 11

    # InAmp Resistors
    draw_res_realistic(ic_col_start+1, 'F', ic_col_start+5, 'E', "1k Rg", ['brown', 'black', 'red', 'gold']) # 13 to 6
    draw_res_realistic(ic_col_start, 'F', ic_col_start+1, 'F', "10k R1", ['brown', 'black', 'orange', 'gold']) # 14 to 13
    draw_res_realistic(ic_col_start+6, 'E', ic_col_start+5, 'E', "10k R2", ['brown', 'black', 'orange', 'gold']) # 7 to 6

    # Stage 2: Notch (Cols 40-55)
    # Pin 1 is at ic_col_start (Row E)
    draw.line([get_hole_pos(ic_col_start, 'E'), get_hole_pos(40, 'E')], fill=(100,100,100), width=3) # Jump from Pin 1
    # Upper
    draw_res_realistic(40, 'E', 45, 'E', "47k", ['yellow', 'violet', 'orange', 'gold'])
    draw_res_realistic(45, 'E', 50, 'E', "47k", ['yellow', 'violet', 'orange', 'gold'])
    draw_cap_realistic(45, 'E', 'VG', "136n", type='disc')
    # Lower
    draw_cap_realistic(40, 'D', 'D', "68n", type='disc') # Just visual placeholder
    draw_line_holes = lambda c1, r1, c2, r2, col: draw.line([get_hole_pos(c1, r1), get_hole_pos(c2, r2)], fill=col, width=3)
    draw_line_holes(40, 'E', 40, 'B', (100,100,100))
    draw_cap_realistic(40, 'B', 'B', "68n", type='disc') # Placeholder logic
    draw_res_realistic(42, 'B', 42, 'VG', "23k", ['red', 'orange', 'orange', 'gold'])

    # Stage 3
    draw_cap_realistic(50, 'E', 'I', "100n Cc", type='disc')
    draw_line_holes(50, 'I', ic_col_start+4, 'I', (100,100,100))
    draw_line_holes(ic_col_start+4, 'I', ic_col_start+4, 'F', (100,100,100)) # To Pin 10
    draw_res_realistic(ic_col_start+4, 'G', ic_col_start+4, 'VG', "1M", ['brown', 'black', 'green', 'gold'])

    # Title and Labels
    draw.text((width//2, 50), "Realistic EEG Breadboard Guide", fill=(0,0,0), font=font, anchor="mm")

    img.save('EEG_Fritzing_Layout.png')

if __name__ == "__main__":
    draw_realistic_breadboard()
