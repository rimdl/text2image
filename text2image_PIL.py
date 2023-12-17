from PIL import Image, ImageDraw, ImageFont


def text_to_image(text, font_path, font_size, image_format):
    font = ImageFont.truetype(font_path, font_size)
    (image_width, image_height) = ImageDraw.Draw(Image.new("RGB", (1, 1))).textsize(text, font=font)
    image = Image.new("RGB", (image_width, image_height + 10), "white")
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill="black")
    image.save(f"./static/output.{image_format}", image_format)


if __name__ == "__main__":
    text = "Hello World!"
    font_path = "static/font/SmileySans-Oblique.ttf"
    font_size = 32
    image_format = "png"
    text_to_image(text, font_path, font_size, image_format)
