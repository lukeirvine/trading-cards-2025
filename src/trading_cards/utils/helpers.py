import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from trading_cards.utils.constants import constants
from trading_cards.utils.types import TextType


class Helpers:
    @staticmethod
    def save_canvas(canvas: Image.Image, file_name: str, save_dir: str) -> None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        canvas.save(os.path.join(save_dir, file_name))

    @staticmethod
    def add_image_to_canvas(
        canvas: Image.Image,
        image_path: str,
        size: tuple[int, int],
        position: tuple[int, int],
    ) -> None:
        image = Image.open(image_path)
        image_canvas: Image.Image = Helpers.resize_and_crop_image(image, size)
        canvas.paste(image_canvas, position)

    @staticmethod
    def add_mask_to_canvas(
        canvas: Image.Image,
        mask_path: str,
        size: tuple[int, int],
        position: tuple[int, int],
    ) -> None:
        # Open the mask image with an alpha channel
        image = Image.open(mask_path).convert("RGBA")
        # Resize/crop to the desired size
        image = Helpers.resize_and_crop_image(image, size)
        # Use the image’s own alpha channel as the mask
        alpha = image.split()[-1]
        # Paste the RGBA image onto the canvas, preserving transparency
        canvas.paste(image, position, alpha)

    @staticmethod
    def resize_and_crop_image(image: Image.Image, size: tuple[int, int]) -> Image.Image:
        # Sizes
        current_width, current_height = image.size
        target_width, target_height = size

        # Calculate the aspect ratios
        current_aspect_ratio = current_width / current_height
        new_aspect_ratio = target_width / target_height

        # Calculate the scale factor to resize the image
        if new_aspect_ratio > current_aspect_ratio:
            scale_factor = target_height / current_height
        else:
            scale_factor = target_width / current_width

        # Calculate the new size with the preserved aspect ratio
        resized_width = int(current_width * scale_factor)
        resized_height = int(current_height * scale_factor)

        # Resize the image while maintaining the aspect ratio
        new_size: tuple[int, int] = (resized_width, resized_height)
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

        # Calculate the cropping box
        left = (resized_width - target_width) / 2
        top = (resized_height - target_height) / 2
        right = (resized_width + target_width) / 2
        bottom = (resized_height + target_height) / 2

        # Crop the image to the target size
        crop_box = (int(left), int(top), int(right), int(bottom))
        cropped_image = resized_image.crop(crop_box)

        return cropped_image

    @staticmethod
    def add_text_to_canvas(
        text: str,
        canvas: Image.Image,
        font_size: int,
        type: TextType,
        max_lines: int = 0,
        max_width: int = 0,
        max_height: int = 0,
        position: tuple[int, int] = (0, 0),
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> Image.Image:
        if type == TextType.heading:
            font = Helpers.get_title_font(font_size)
        elif type == TextType.body:
            font = Helpers.get_body_font(font_size)
        else:
            raise ValueError(f"Invalid text type: {type}")
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(canvas)

        def get_text_size(text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]

        def calculate_wrap_width(font: ImageFont.FreeTypeFont) -> int:
            avg_char_width = get_text_size("W" * 10, font)[0] / 10
            return int(max_width // avg_char_width) - 1

        # Calculate wrap width
        # If no max_width provided, default to remaining canvas width
        if max_width <= 0:
            max_width = canvas.width - position[0]
        wrap_width = calculate_wrap_width(font)
        # Ensure wrap_width is at least 1 to prevent invalid widths
        if wrap_width < 1:
            wrap_width = 1

        # Respect max_lines by shrinking the font if needed
        if max_lines > 0:
            current_size = font_size
            while True:
                # pick the right font for this size
                font = (
                    Helpers.get_title_font(current_size)
                    if type == TextType.heading
                    else Helpers.get_body_font(current_size)
                )
                # recalc avg char width → wrap_width
                avg_char_width = get_text_size("W" * 10, font)[0] / 10
                wrap_w = int(max_width // avg_char_width) - 1
                wrap_w = max(wrap_w, 1)

                lines = textwrap.wrap(text, width=wrap_w * 2)
                # stop if it fits or font is already minimal
                if len(lines) <= max_lines or current_size <= 1:
                    wrapped_lines = lines
                    break
                current_size -= 1

            # finally, re‐load the font at the reduced size
            font = (
                Helpers.get_title_font(current_size)
                if type == TextType.heading
                else Helpers.get_body_font(current_size)
            )
        else:
            wrapped_lines = textwrap.wrap(text, width=wrap_width * 2)

        # Calculate height of the text block
        # text_height = sum(get_text_size(line, font)[1] for line in wrapped_lines)

        # Draw each line with the calculated position
        pos = list(position)
        for line in wrapped_lines:
            draw.text(tuple(pos), line, font=font, fill=color)  # type: ignore[reportUnknownArgumentType]
            pos[1] += get_text_size(line, font)[1]  # Move down for the next line

        return canvas

    @staticmethod
    def get_title_font(font_size: int) -> ImageFont.FreeTypeFont:
        return Helpers.get_font(constants.HEADING_FONT, font_size)

    @staticmethod
    def get_body_font(font_size: int) -> ImageFont.FreeTypeFont:
        return Helpers.get_font(constants.BODY_FONT, font_size)

    @staticmethod
    def get_font(font_path: str, font_size: int) -> ImageFont.FreeTypeFont:
        font = ImageFont.truetype(font_path, font_size)
        # default font size
        size = 36

        # Measure the text height
        dummy_text = "A"
        bbox = font.getbbox(dummy_text)  # type: ignore
        text_height = bbox[3] - bbox[1]

        # Adjust the font size to match the desired height
        adjusted_size = int(size * font_size / text_height)
        return ImageFont.truetype(font_path, adjusted_size)

    @staticmethod
    def add_rect_to_canvas(
        canvas: Image.Image,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (100, 100),
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        draw = ImageDraw.Draw(canvas)
        draw.rectangle(
            (position[0], position[1], position[0] + size[0], position[1] + size[1]),
            fill=color,
        )
