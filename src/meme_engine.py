"""Meme Engine"""

import os
import random
from PIL import Image, ImageFont, ImageDraw


class MemeEngine():
    """Meme Engine class"""

    def __init__(self, path):
        """Initialize meme engine with path

        Args:
            path (str): path of image after generate
        """

        self.folder_dir = path
        if not os.path.exists(path):
            os.makedirs(path)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate meme with img_path, text, and author.

        Args:
            img_path (_type_): img path
            text (_type_): text from qoute
            author (_type_): author from qoute
            width (int, optional): Max width for img. Defaults to 500px.

        Returns:
            str: out_file_path
        """

        out_file_path = os.path.join(
            self.folder_dir, f"meme-{random.randint(0,1000000)}.jpg"
        )

        try:
            with Image.open(img_path) as img:
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height

                new_width = min(img_width, width)
                new_height = int(new_width / aspect_ratio)

                img = img.resize((new_width, new_height))
                draw = ImageDraw.Draw(img)

                font_size = int(img.height / 25)
                font = ImageFont.truetype("./_data/fonts/arial_black.ttf", font_size)

                x_loc = random.randint(0, int(img.width / 8))
                y_loc = random.randint(0, int(img.height - font_size * 5))

                draw.text((x_loc, y_loc), text, font=font, fill=(0, 0, 0))
                draw.text(
                    (int(x_loc * 1.2), y_loc + font_size), " - " + author, font=font
                )

                img.save(out_file_path)
        except Exception as error:
            print(error)
            raise Exception("Error generate meme.") from error
        return out_file_path
