from PIL import Image, ImageDraw, ImageFont

def create_diagram():
    # Create a blank image with a light background
    width, height = 1200, 800
    img = Image.new('RGB', (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    # Draw Title
    draw.text((width//2, 40), "EEG Breadboard Layout Guide (TL074 + 9V)", fill=(0,0,0), font=title_font, anchor="mm")

    # Draw Breadboard outline
    bb_x1, bb_y1, bb_x2, bb_y2 = 100, 100, 1100, 700
    draw.rectangle([bb_x1, bb_y1, bb_x2, bb_y2], fill=(255, 255, 255), outline=(200, 200, 200), width=3)

    # Draw Power Rails
    # Top (+9V)
    draw.line([120, 130, 1080, 130], fill=(255, 0, 0), width=5)
    draw.text((120, 110), "+9V Rail", fill=(255, 0, 0), font=font)

    # VGND (Virtual Ground 4.5V)
    draw.line([120, 160, 1080, 160], fill=(0, 200, 0), width=5)
    draw.text((120, 140), "VGND Rail (4.5V Reference)", fill=(0, 150, 0), font=font)

    # Bottom (0V / GND)
    draw.line([120, 670, 1080, 670], fill=(0, 0, 255), width=5)
    draw.text((120, 680), "0V Rail (Battery Negative)", fill=(0, 0, 255), font=font)

    # Draw TL074 IC
    ic_w, ic_h = 400, 150
    ic_x = (width - ic_w) // 2
    ic_y = (height - ic_h) // 2
    draw.rectangle([ic_x, ic_y, ic_x + ic_w, ic_y + ic_h], fill=(50, 50, 50))
    draw.text((ic_x + ic_w//2, ic_y + ic_h//2), "TL074 IC", fill=(255, 255, 255), font=font, anchor="mm")

    # IC Pins (simplified)
    for i in range(7):
        # Bottom pins (1-7)
        px = ic_x + 30 + i * 55
        draw.rectangle([px, ic_y + ic_h, px + 20, ic_y + ic_h + 20], fill=(150, 150, 150))
        draw.text((px + 5, ic_y + ic_h + 25), str(i+1), fill=(0,0,0), font=font)

        # Top pins (14-8)
        px = ic_x + 30 + i * 55
        draw.rectangle([px, ic_y - 20, px + 20, ic_y], fill=(150, 150, 150))
        draw.text((px + 5, ic_y - 45), str(14-i), fill=(0,0,0), font=font)

    # Labels for Sections
    sections = [
        ("Virtual Ground Divider", 150, 250, (0, 150, 0)),
        ("Stage 1: InAmp\n(Pins 1-7, 12-14)", 350, 500, (0, 0, 0)),
        ("Stage 2: 50Hz Notch\n(Passive between 1 & 10)", 750, 500, (150, 0, 150)),
        ("Stage 3: Gain + Filter\n(Pins 8-10)", 900, 250, (200, 0, 0))
    ]

    for text, x, y, color in sections:
        draw.text((x, y), text, fill=color, font=font, align="center")

    # Input/Output Markers
    draw.ellipse([ic_x + 330, ic_y - 80, ic_x + 350, ic_y - 60], fill=(0,0,0)) # Pin 12
    draw.text((ic_x + 360, ic_y - 85), "Electrode A (Pin 12)", fill=(0,0,0), font=font)

    draw.ellipse([ic_x + 220, ic_y + 170, ic_x + 240, ic_y + 190], fill=(0,0,0)) # Pin 5
    draw.text((ic_x + 250, ic_y + 165), "Electrode B (Pin 5)", fill=(0,0,0), font=font)

    draw.ellipse([ic_x + 380, ic_y + 170, ic_x + 400, ic_y + 190], fill=(200, 0, 0)) # Pin 8
    draw.text((ic_x + 410, ic_y + 165), "Oscilloscope Output (Pin 8)", fill=(200,0,0), font=font)

    img.save('EEG_Breadboard_Layout.png')

if __name__ == "__main__":
    create_diagram()
