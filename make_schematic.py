from PIL import Image, ImageDraw, ImageFont

def draw_schematic():
    width, height = 1600, 1000
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    # Title
    draw.text((width//2, 50), "EEG Circuit Schematic (Single TL074)", fill=(0,0,0), font=title_font, anchor="mm")

    def draw_opamp(x, y, label, pins):
        # Triangle
        draw.polygon([(x, y-50), (x, y+50), (x+80, y)], outline=(0,0,0), width=3)
        draw.text((x+25, y-10), label, fill=(0,0,0), font=font)
        # Pins
        draw.line([x-30, y-30, x, y-30], fill=(0,0,0), width=2) # In-
        draw.line([x-30, y+30, x, y+30], fill=(0,0,0), width=2) # In+
        draw.line([x+80, y, x+110, y], fill=(0,0,0), width=2)   # Out
        draw.text((x-50, y-40), pins[0], fill=(0,0,0), font=font)
        draw.text((x-50, y+20), pins[1], fill=(0,0,0), font=font)
        draw.text((x+115, y-10), pins[2], fill=(0,0,0), font=font)
        return x+110, y

    # Draw Stage 1 (InAmp)
    draw_opamp(200, 300, "U1A", ["13", "12", "14"])
    draw_opamp(200, 600, "U1B", ["6", "5", "7"])
    draw_opamp(500, 450, "U1C", ["2", "3", "1"])

    # Draw Notch (simplified block)
    draw.rectangle([700, 400, 850, 500], outline=(0,0,0), width=2)
    draw.text((720, 440), "50Hz Notch", fill=(0,0,0), font=font)
    draw.line([610, 450, 700, 450], fill=(0,0,0), width=2) # Conn to U1C Out

    # Draw Stage 3
    draw_opamp(1000, 450, "U1D", ["9", "10", "8"])
    draw.line([850, 450, 1000, 480], fill=(0,0,0), width=2) # Conn Notch to U1D In+ (10)

    # Add Ground and VCC labels
    draw.text((width-200, height-100), "VCC: 9V Battery\nREF: 4.5V VGND", fill=(0,0,0), font=font)

    img.save('EEG_Schematic.png')

if __name__ == "__main__":
    draw_schematic()
