from PIL import Image, ImageDraw
import random

def j(v): return v + random.uniform(-1, 1)

def generate():
    # 3 frames of a boiling box
    sheet = Image.new("RGBA", (96, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(sheet)
    for f in range(3):
        cx = f * 32 + 16
        # Draw a simple box with jitter
        pts = [(cx-10, 6), (cx+10, 6), (cx+10, 26), (cx-10, 26)]
        draw.polygon([(j(p[0]), j(p[1])) for p in pts], outline=(0,0,0,255))
    sheet.save("sprite.png")
    print("Generated: example sprite")

if __name__ == "__main__": generate()
