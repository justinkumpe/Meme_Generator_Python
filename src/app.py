"""Meme Generator App"""

import os
import random
import requests
from flask import Flask, render_template, request

from meme_engine import MemeEngine
from QuoteEngine.ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []
    try:
        for path in quote_files:
            quotes.extend(Ingestor.parse(path))
    except Exception as error:
        print(error)

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""

    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    res = requests.get(request.form["image_url"], timeout=10)
    try:
        temp_img_path = f"meme-custom-{random.randint(0,100000000)}.jpg"
        with open(temp_img_path, "wb") as f:
            f.write(res.content)
    except Exception as error:
        print(error)
        return render_template("meme_form.html")

    path = meme.make_meme(temp_img_path, request.form["body"], request.form["author"])

    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
