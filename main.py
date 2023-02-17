from PIL import Image, ImageDraw, ImageFont
from read_file import get_verse, get_translation, latin_to_indian

#load in image back.jpeg
img = Image.open('back.jpeg')
#img = Image.new('RGB', (100, 30), color = (73, 109, 137))

def draw_verse(verse_dict):
    title = 'श्रीमद्भगवद्गीता' + ' ' + latin_to_indian(verse_dict['chapter'] + '.' + verse_dict['verse'])
    text = get_verse()
    txt2 = get_translation(verse_dict['book'], verse_dict['chapter'], verse_dict['verse']'])
    fnt = ImageFont.truetype('NotoSansDevanagari-Regular.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((300, 100), title, font=fnt, fill=(255, 255, 0))
    d.text((300,200), text, font=fnt, fill=(255, 255, 0))
    d.text((300, 300), txt2, font=fnt, fill=(255, 255, 0))
    img.save('pil_text_font.png')

draw_verse(1)
print('done')