from PIL import Image, ImageDraw, ImageFont
import math

def draw_realistic_breadboard():
    width, height = 2400, 1800
    hole_pitch = 30
    img = Image.new('RGB', (width, height), color=(220, 220, 220))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        pin_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        pin_font = ImageFont.load_default()

    # Breadboard constants
    bb_x1, bb_y1 = 100, 150
    bb_w, bb_h = 63 * hole_pitch + 200, 35 * hole_pitch

    # Draw Breadboard Body
    draw.rectangle([bb_x1, bb_y1, bb_x1 + bb_w, bb_y1 + bb_h], fill=(240, 240, 240), outline=(180, 180, 180), width=3)

    def get_hole_pos(col, row_name):
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
        draw.line([p1, p2], fill=(160, 160, 160), width=4)
        mid_x, mid_y = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
        dist = 60
        bx1, by1 = mid_x - math.cos(angle)*dist/2, mid_y - math.sin(angle)*dist/2
        bx2, by2 = mid_x + math.cos(angle)*dist/2, mid_y + math.sin(angle)*dist/2
        draw.line([bx1, by1, bx2, by2], fill=(222, 184, 135), width=20)
        band_colors = {
            'brown': (139, 69, 19), 'black': (0, 0, 0), 'red': (255, 0, 0),
            'orange': (255, 165, 0), 'yellow': (255, 255, 0), 'green': (0, 128, 0),
            'violet': (238, 130, 238), 'gold': (218, 165, 32)
        }
        for i, b in enumerate(bands):
            f = (i + 1) / (len(bands) + 1)
            b_x = bx1 + (bx2-bx1)*f
            b_y = by1 + (by2-by1)*f
            perp_dx, perp_dy = math.sin(angle) * 10, -math.cos(angle) * 10
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
        else:
            draw.rectangle([mid_x-12, mid_y-20, mid_x+12, mid_y+20], fill=(40, 40, 40))
            draw.line([mid_x-12, mid_y-10, mid_x+12, mid_y-10], fill=(200, 200, 200), width=5)
        draw.text((mid_x + 25, mid_y), value, fill=(0,0,0), font=small_font, anchor="lm")

    # 1. 9V Battery Realistic Drawing
    bat_x, bat_y = 100, 1300
    draw.rectangle([bat_x, bat_y, bat_x+250, bat_y+400], fill=(30,30,30), outline=(0,0,0), width=2)
    draw.text((bat_x+125, bat_y+200), "9V BATTERY", fill=(255,255,0), font=font, anchor="mm")
    # Terminals
    draw.ellipse([bat_x+50, bat_y-30, bat_x+100, bat_y+20], fill=(200,200,200), outline=(0,0,0)) # Neg
    draw.ellipse([bat_x+150, bat_y-30, bat_x+200, bat_y+20], fill=(200,200,200), outline=(0,0,0)) # Pos
    # Battery Wires
    draw.line([bat_x+175, bat_y-15, 200, 1300, 200, 210], fill=(255,0,0), width=6) # Battery + to V+ Rail
    draw.line([bat_x+75, bat_y-15, 150, 1300, 150, 750], fill=(0,0,255), width=6) # Battery - to 0V Rail

    # 2. Virtual Ground Setup
    draw_res_realistic(5, 'V+', 5, 'VG', "10k", ['brown', 'black', 'orange', 'gold'])
    draw_res_realistic(7, 'VG', 7, '0V', "10k", ['brown', 'black', 'orange', 'gold'])
    draw_cap_realistic(9, 'VG', '0V', "100uF", type='elec')

    # 3. TL074 IC with VISIBLE PINS
    ic_col = 25
    ic_x1, ic_y1 = get_hole_pos(ic_col, 'E')
    ic_x2, ic_y2 = get_hole_pos(ic_col+6, 'F')
    # IC Body
    draw.rectangle([ic_x1-15, ic_y1-5, ic_x2+15, ic_y2+5], fill=(30, 30, 30))
    # Notch and Dot
    draw.arc([ic_x1-25, (ic_y1+ic_y2)//2-15, ic_x1-5, (ic_y1+ic_y2)//2+15], start=270, end=90, fill=(100,100,100), width=3)
    draw.ellipse([ic_x1-5, ic_y1+5, ic_x1+5, ic_y1+15], fill=(100,100,100)) # Pin 1 Dot
    draw.text(((ic_x1+ic_x2)//2, (ic_y1+ic_y2)//2), "TL074CN", fill=(200,200,200), font=small_font, anchor="mm")

    # Visible Pin Labels
    # Side 1 (Bottom in layout A-E rows): Pins 1-7
    for i in range(7):
        p_pos = get_hole_pos(ic_col + i, 'E')
        draw.text((p_pos[0], p_pos[1]-40), str(i+1), fill=(255,0,0), font=pin_font, anchor="mm")

    # Side 2 (Top in layout F-J rows): Pins 14-8
    for i in range(7):
        p_pos = get_hole_pos(ic_col + i, 'F')
        draw.text((p_pos[0], p_pos[1]+40), str(14-i), fill=(255,0,0), font=pin_font, anchor="mm")

    # 4. Wiring
    draw.line([get_hole_pos(ic_col+3, 'E'), get_hole_pos(ic_col+3, 'V+')], fill=(255,0,0), width=4) # Pin 4
    draw.line([get_hole_pos(ic_col+3, 'F'), get_hole_pos(ic_col+3, '0V')], fill=(0,0,255), width=4) # Pin 11

    # Stage 1 InAmp
    draw_res_realistic(ic_col+1, 'F', ic_col+5, 'E', "1k Rg", ['brown', 'black', 'red', 'gold']) # 13 to 6
    draw_res_realistic(ic_col, 'F', ic_col+1, 'F', "10k R1", ['brown', 'black', 'orange', 'gold']) # 14 to 13
    draw_res_realistic(ic_col+6, 'E', ic_col+5, 'E', "10k R2", ['brown', 'black', 'orange', 'gold']) # 7 to 6

    # Titles
    draw.text((width//2, 70), "Realistic EEG Breadboard Layout with 9V Battery", fill=(0,0,0), font=font, anchor="mm")
    img.save('EEG_Fritzing_Layout.png')

if __name__ == "__main__":
    draw_realistic_breadboard()
