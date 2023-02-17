from PIL import Image, ImageDraw, ImageFont
font = ImageFont.load_default()

#font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 48)
im = Image.new("RGB", (200, 200), "white")
d = ImageDraw.Draw(im)
d.line(((0, 100), (200, 100)), "gray")
d.line(((100, 0), (100, 200)), "gray")
d.text((100, 100), "रलबी", fill="black", anchor="ms", font=font)

im.save("mag.png")