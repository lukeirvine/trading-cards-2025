import os

from PIL import Image


class Helpers:
    @staticmethod
    def save_canvas(
        canvas: Image.Image, sub_dir: str, file_name: str, output_dir: str
    ) -> None:
        save_dir = os.path.join(output_dir, sub_dir)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        canvas.save(os.path.join(save_dir, file_name))
