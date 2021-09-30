# Certificate modules
from PIL import Image, ImageDraw, ImageFont


class CertProcessor:
    def __init__(self, template_path, font_path, font_size):
        self.set_tt_font(font_path, font_size)
        self.image = Image.open(template_path)

    def set_tt_font(self, font_path, font_size):
        self.font = ImageFont.truetype(font_path, font_size)

    def add_text(self, text, pos):
        img = self.image
        draw = ImageDraw.Draw(img)
        # Anchor alignment works only for otf & ttf fonts
        draw.text(xy=pos, text=text, fill='black', font=self.font, anchor="mm")
        self.image = img

    def save_pdf(self, path):
        img = self.image.convert('RGB')
        img.save('{}.pdf'.format(path))

    def save_png(self, path):
        self.image.save('{}.png'.format(path))
