from flask import Flask, url_for
import os 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="random_images"> Click </a>'


@app.route("/random_images")
def random_image():
    image_list = os.listdir('M3L1/HW/static/images')
    file_name = random.choice(image_list)
    image_url = url_for('static', filename=f'images/{file_name}')
    return f"<img src='{image_url}' alt='random-image' width='500'>"


app.run(debug=True)