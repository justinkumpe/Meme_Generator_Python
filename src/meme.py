"""Meme."""

import os
import random
import argparse
from models.quote import QuoteModel

from meme_engine import MemeEngine
from QuoteEngine.ingestor import Ingestor


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def make_parser():
    """Make Parser."""
    parser = argparse.ArgumentParser(description="Meme Generator!!!")
    parser.add_argument("--body", type=str, help="Quote Body", default='')
    parser.add_argument("--author", type=str, help="Quote Author", default='')
    parser.add_argument("--path", type=str, help="Image Path")
    return parser


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = make_parser()
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
