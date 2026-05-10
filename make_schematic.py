from PIL import Image, ImageDraw, ImageFont

def draw_real_schematic():
    width, height = 2400, 1600
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except:
        font = ImageFont.load_default(); label_font = ImageFont.load_default()

    def opamp(x, y, label, pins):
        draw.polygon([(x, y-80), (x, y+80), (x+140, y)], outline=(0,0,0), width=5)
        draw.text((x+30, y-20), label, fill=(0,0,0), font=font)
        draw.line([x-60, y-45, x, y-45], fill=(0,0,0), width=4)
        draw.line([x-60, y+45, x, y+45], fill=(0,0,0), width=4)
        draw.line([x+140, y, x+220, y], fill=(0,0,0), width=4)
        draw.text((x-90, y-65), pins[0], fill=(0,0,0), font=label_font)
        draw.text((x-90, y+25), pins[1], fill=(0,0,0), font=label_font)
        draw.text((x+230, y-20), pins[2], fill=(0,0,0), font=label_font)

    def res(x1, y1, x2, y2, label):
        draw.line([x1, y1, x2, y2], fill=(0,0,0), width=4)
        mx, my = (x1+x2)//2, (y1+y2)//2
        draw.rectangle([mx-30, my-15, mx+30, my+15], fill=(255,255,255), outline=(0,0,0), width=3)
        draw.text((mx-20, my-50), label, fill=(0,0,0), font=label_font)

    draw.text((width//2, 70), "Professional EEG Schematic (10,000x Gain + Active DRL)", fill=(0,0,0), font=font, anchor="mm")
    opamp(300, 400, "U1A", ["13", "12", "14"])
    opamp(300, 1200, "U1B", ["6", "5", "7"])

    # Connections and Passives
    res(620, 400, 1140, 755, "100k")
    res(620, 1200, 1140, 755, "100k")
    opamp(1200, 800, "U1C", ["2", "3", "1"])

    res(1000, 400, 1940, 755, "10k")
    res(1000, 1200, 1940, 845, "10k")
    opamp(2000, 800, "U1D", ["9", "10", "8"])

    img.save('EEG_Schematic.png')

if __name__ == "__main__": draw_real_schematic()
