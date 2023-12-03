from PIL import Image, ImageDraw, ImageFont

from flask import Flask, send_from_directory, request

app = Flask(__name__)

def read_string_with_linebreak(s: str, limit: int) -> str:
    lines = []
    for i in range(0, len(s), limit):
        lines.append(s[i:i+limit] + "\n")
    return "".join(lines)

def t2i(args):
    text = args
    text = read_string_with_linebreak(text,30)
    font = ImageFont.truetype('SmileySans-Oblique.ttf', size=36)
    if len(text) > 30:
        width = 33 * 30
    else:
        width = 33 * len(text)
    height = (text.count('\n') + 1) * 50
    size = (width, height)

    image = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((50, 20), text, font=font, fill=(0, 0, 0))
    image.save('./static/output.png')

@app.route('/t2i',methods=['POST'])
def t2i_page():
    text = request.form['text']
    t2i(text)
    return "success"

@app.route('/static/<path:filename>')
def static_from_directory(filename):
    return send_from_directory('static', filename)

app.run(host='0.0.0.0', port=5000, debug=True)

