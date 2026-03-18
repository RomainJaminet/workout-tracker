from PIL import Image, ImageDraw, ImageFont
import os

for size in [192, 512]:
    img = Image.new('RGB', (size, size), '#0a0a0f')
    draw = ImageDraw.Draw(img)
    # Gradient-ish circle
    cx, cy = size//2, size//2
    r = int(size * 0.38)
    for i in range(r, 0, -1):
        ratio = i / r
        red = int(99 * (1 - ratio) + 59 * ratio)
        green = int(102 * (1 - ratio) + 130 * ratio)
        blue = int(241 * (1 - ratio) + 246 * ratio)
        draw.ellipse([cx-i, cy-i, cx+i, cy+i], fill=(red, green, blue))
    # W letter
    fs = int(size * 0.4)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", fs)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), "W", font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2 - int(size*0.04)), "W", fill='#ffffff', font=font)
    img.save(f'/home/claude/pwa/icons/icon-{size}.png')
    print(f'icon-{size}.png OK')
