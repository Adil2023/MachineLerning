from PIL import Image, ImageDraw, ImageFont
import math

def draw_definitive_breadboard():
    width, height = 3600, 3600
    hp = 50
    img = Image.new('RGB', (width, height), color=(220, 220, 220))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 45)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        pin_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    except:
        font = ImageFont.load_default(); small_font = ImageFont.load_default(); pin_font = ImageFont.load_default()

    bx, by = 200, 800
    bw, bh = 63 * hp + 200, 35 * hp
    draw.rectangle([bx, by, bx+bw, by+bh], fill=(240, 240, 240), outline=(180, 180, 180), width=3)

    def get_pos(col, row):
        row_map = {'V+': 2, 'VG': 3, 'A': 8, 'B': 9, 'C': 10, 'D': 11, 'E': 12, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, '0V': 25}
        return bx + 100 + (col-1) * hp, by + row_map[row] * hp

    for c in range(1, 64):
        for r in ['V+', 'VG', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '0V']:
            x, y = get_pos(c, r); draw.ellipse([x-10, y-10, x+10, y+10], fill=(180, 180, 180))

    def wire(p1, p2, color=(0,0,0), w=8):
        draw.line([p1, p2], fill=color, width=w)

    def component_wire(c, r, target_p, color=(100,100,100)):
        wire(get_pos(c, r), target_p, color, 6)

    def res(c1, r1, c2, r2, val, label):
        p1, p2 = get_pos(c1, r1), get_pos(c2, r2)
        draw.line([p1, p2], fill=(150, 150, 150), width=6)
        mx, my = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        draw.rectangle([mx-40, my-15, mx+40, my+15], fill=(222, 184, 135), outline=(0,0,0))
        draw.text((mx, my-45), f"{label}: {val}", fill=(0,0,0), font=small_font, anchor="mm")

    def cap(c1, r1, c2, r2, val, label, elec=False):
        p1, p2 = get_pos(c1, r1), get_pos(c2, r2)
        draw.line([p1, p2], fill=(150, 150, 150), width=6)
        mx, my = (p1[0]+p2[0])//2, (p1[1]+p2[1])//2
        if elec: draw.rectangle([mx-25, my-35, mx+25, my+35], fill=(40,40,40))
        else: draw.ellipse([mx-20, my-20, mx+20, my+20], fill=(255, 140, 0), outline=(0,0,0))
        draw.text((mx+40, my), f"{label}: {val}", fill=(0,0,0), font=small_font, anchor="lm")

    # TL074 IC (center)
    ic_c = 30
    draw.rectangle([get_pos(ic_c, 'E')[0]-30, get_pos(ic_c, 'E')[1]-10, get_pos(ic_c+6, 'F')[0]+30, get_pos(ic_c+6, 'F')[1]+10], fill=(30,30,30))
    for i in range(7):
        p_pos = get_pos(ic_c+i, 'E'); draw.text((p_pos[0], p_pos[1]-70), str(i+1), fill=(255,0,0), font=pin_font, anchor="mm")
        p_pos = get_pos(ic_c+i, 'F'); draw.text((p_pos[0], p_pos[1]+70), str(14-i), fill=(255,0,0), font=pin_font, anchor="mm")

    # 1. VGND Group (Top Left)
    res(2, 'V+', 2, 'VG', "10k", "R1"); res(4, 'VG', 4, '0V', "10k", "R2")
    cap(6, 'VG', 6, '0V', "100uF", "C1", elec=True)
    wire(get_pos(ic_c+3, 'E'), get_pos(1, 'V+'), (255,0,0)) # Pin 4 to V+
    wire(get_pos(ic_c+3, 'F'), get_pos(1, '0V'), (0,0,255)) # Pin 11 to 0V

    # 2. IA Stage 1 (Top Left Corners) - POINT-TO-POINT TO IC
    res(10, 'A', 15, 'A', "10k", "R3")
    component_wire(10, 'A', get_pos(ic_c, 'F'), (100,100,100)) # to Pin 14
    component_wire(15, 'A', get_pos(ic_c+1, 'F'), (100,100,100)) # to Pin 13

    res(20, 'A', 25, 'A', "10k", "R4")
    component_wire(20, 'A', get_pos(ic_c+6, 'E'), (100,100,100)) # to Pin 7
    component_wire(25, 'A', get_pos(ic_c+5, 'E'), (100,100,100)) # to Pin 6

    res(12, 'B', 18, 'B', "200", "Rg")
    component_wire(12, 'B', get_pos(ic_c+1, 'F'), (100,100,100)) # to Pin 13
    component_wire(18, 'B', get_pos(ic_c+5, 'E'), (100,100,100)) # to Pin 6

    # 3. AC Coupling (Top Right)
    cap(40, 'A', 45, 'A', "100n", "C2")
    component_wire(40, 'A', get_pos(ic_c, 'F'), (50,150,50)) # Pin 14 to C2
    res(45, 'B', 45, 'VG', "1M", "Rbias1")

    cap(50, 'A', 55, 'A', "100n", "C3")
    component_wire(50, 'A', get_pos(ic_c+6, 'E'), (50,150,50)) # Pin 7 to C3
    res(55, 'B', 55, 'VG', "1M", "Rbias2")

    # 4. Difference Amp (Bottom Middle)
    res(38, 'I', 44, 'I', "10k", "R6")
    component_wire(38, 'I', get_pos(45, 'A'), (100,100,100)) # Node X to R6
    component_wire(44, 'I', get_pos(ic_c+5, 'F'), (100,100,100)) # to Pin 9

    res(46, 'I', 52, 'I', "10k", "R7")
    component_wire(46, 'I', get_pos(55, 'A'), (100,100,100)) # Node Y to R7
    component_wire(52, 'I', get_pos(ic_c+4, 'F'), (100,100,100)) # to Pin 10

    res(54, 'I', 54, 'VG', "1M", "R8"); res(56, 'I', 62, 'I', "1M", "R9"); cap(56, 'J', 62, 'J', "4.7n", "C4")
    component_wire(54, 'I', get_pos(ic_c+4, 'F'), (100,100,100)) # to Pin 10
    component_wire(56, 'I', get_pos(ic_c+5, 'F'), (100,100,100)) # to Pin 9
    component_wire(62, 'I', get_pos(ic_c+6, 'F'), (100,100,100)) # to Pin 8

    # 5. DRL (Bottom Left)
    res(5, 'I', 15, 'I', "100k", "R10"); res(18, 'I', 26, 'I', "100k", "R11")
    component_wire(5, 'I', get_pos(45, 'A'), (150,50,50)) # Node X to DRL
    component_wire(18, 'I', get_pos(55, 'A'), (150,50,50)) # Node Y to DRL
    component_wire(15, 'I', get_pos(ic_c+1, 'E'), (150,50,50)) # to Pin 2
    component_wire(26, 'I', get_pos(ic_c+1, 'E'), (150,50,50)) # to Pin 2
    res(10, 'J', 20, 'J', "1M", "R12")
    component_wire(10, 'J', get_pos(ic_c+1, 'E'), (150,50,50)) # to Pin 2
    component_wire(20, 'J', get_pos(ic_c, 'E'), (150,50,50)) # to Pin 1

    # 6. EXTERNAL
    # Electrodes FAR LEFT
    el_y = 2000
    draw.text((300, el_y - 120), "ELECTRODE INPUTS (FAR LEFT)", fill=(0,0,0), font=font)
    wire((150, el_y), get_pos(ic_c+2, 'F'), (255, 165, 0), 12) # Pin 12 - A
    wire((450, el_y), get_pos(ic_c+4, 'E'), (255, 165, 0), 12) # Pin 5 - B
    wire((750, el_y), get_pos(ic_c, 'E'), (0, 200, 0), 12) # Pin 1 - Driven Ref
    draw.text((150, el_y + 40), "ELECTRODE A", fill=(255, 165, 0), font=small_font, anchor="mm")
    draw.text((450, el_y + 40), "ELECTRODE B", fill=(255, 165, 0), font=small_font, anchor="mm")
    draw.text((750, el_y + 40), "DRIVEN REF", fill=(0, 200, 0), font=small_font, anchor="mm")

    # Battery UNDER
    bat_y = by + bh + 800
    draw.rectangle([bx+bw//2-250, bat_y, bx+bw//2+250, bat_y+400], fill=(40,40,40))
    draw.text((bx+bw//2, bat_y+200), "9V BATTERY (UNDER BOARD)", fill=(255,255,0), font=font, anchor="mm")
    wire((bx+bw//2+150, bat_y), get_pos(60, 'V+'), (255,0,0), 14)
    wire((bx+bw//2-150, bat_y), get_pos(60, '0V'), (0,0,255), 14)

    # Scope BOTTOM
    wire((bx+bw//2, height-300), get_pos(ic_c+6, 'F'), (255, 255, 255), 12) # Pin 8
    draw.text((bx+bw//2, height-150), "SCOPE OUTPUT (BOTTOM)", fill=(0,0,0), font=font, anchor="mm")

    draw.text((width//2, 150), "DEFINITIVE AUDITED EEG LAYOUT - POINT-TO-POINT WIRES ROUTED AROUND IC", fill=(0,0,0), font=font, anchor="mm")
    img.save('EEG_Fritzing_Layout.png')

if __name__ == "__main__": draw_definitive_breadboard()
