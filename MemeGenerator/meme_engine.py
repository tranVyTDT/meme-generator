import os
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """ Create a Meme """

    def __init__(self, output_dir):
        self.output_dir = output_dir.replace("\/", "\\") if os.name == "nt" else output_dir

    def make_meme(self, img, body, author, width=500):
        """
        Generate a meme, by add text into image then rescale.
        
        Args:
            img(str): path of an input image
            body(str): a quote
            author(str): name of a author

        Returns:
            meme_path(str): path of new meme
        """
        if not img:
            raise Exception("There is no images to generate!!!")
        
        if os.name == "nt":
            img = img.replace("\/", "\\")

        image = Image.open(img)
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf", 36)
        text_color = (255, 255, 255)
        text_position = (50, 50)
        draw.text(text_position, f"{body} {author}", font=font, fill=text_color)
        
        scaled_image = image.resize((width, width))
        file_name = os.path.basename(img)
        meme_path = os.path.join(self.output_dir, file_name)
        
        scaled_image.save(meme_path)
        return meme_path
