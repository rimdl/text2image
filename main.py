from flask import Flask, send_from_directory, request, render_template
import markdown
from text2image_PIL import text_to_image

app = Flask(__name__)

def read_string_with_linebreak(s: str, limit: int) -> str:
    lines = []
    for i in range(0, len(s), limit):
        lines.append(s[i:i+limit] + "\n")
    return "".join(lines)

@app.route('/')
def index():
    input_file = "./README.md"
    output_file = "./templates/output.html"

    with open(input_file, "r",encoding="utf-8") as f:
        markdown_text = f.read()

    html_text = markdown.markdown(markdown_text)

    with open(output_file, "w",encoding="utf-8") as f:
        f.write(html_text)
    return render_template("output.html")
@app.route('/t2i',methods=['POST'])
def t2i_page():
    text = request.form['text']
    # t2i(text)
    font_path = "./static/font/SanJiDianHeiJianTi-Zhong-2.ttf"
    font_size = 32
    image_format = "png"
    text_to_image(text, font_path, font_size, image_format)
    return "success"

@app.route('/static/<path:filename>')
def static_from_directory(filename):
    return send_from_directory('static', filename)

app.run(host='0.0.0.0', port=5000)

