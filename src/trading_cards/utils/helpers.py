import os

from PIL import Image


class Helpers:
    @staticmethod
    def save_canvas(canvas: Image.Image, file_name: str, save_dir: str) -> None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        canvas.save(os.path.join(save_dir, file_name))
