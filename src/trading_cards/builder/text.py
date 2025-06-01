import textwrap
from typing import Optional, TypedDict

from PIL import Image, ImageDraw, ImageFont

from trading_cards.utils.types import ProseData, TextType


class TextResults(TypedDict):
    line_count: int
    line_height: int


class TextBuilder:
    @staticmethod
    def add_body_to_canvas(
        text: ProseData,
        canvas: Image.Image,
        max_width: Optional[int] = None,
        max_lines: Optional[int] = None,
        position: tuple[int, int] = (0, 0),
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> Image.Image:
        y_pos: int = position[1]
        for item in text:
            results = TextBuilder.add_text_to_canvas(
                text=item["text"],
                canvas=canvas,
                type=item["type"],
                max_lines=max_lines,
                max_width=max_width,
                position=(position[0], y_pos),
                color=color,
            )

            y_pos += int(results["line_height"] * results["line_count"] + item["type"].margin_after)

        return canvas

    @staticmethod
    def add_text_to_canvas(
        text: str,
        canvas: Image.Image,
        type: TextType,
        vertical_align: str = "top",
        max_lines: Optional[int] = None,
        max_width: Optional[int] = None,
        max_height: int = 0,
        position: tuple[int, int] = (0, 0),
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> TextResults:
        font_size = type.base_size
        font = TextBuilder.get_font(type.font_path, font_size)

        draw: ImageDraw.ImageDraw = ImageDraw.Draw(canvas)

        def get_text_size(text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]

        def calculate_wrap_width(font: ImageFont.FreeTypeFont) -> int:
            local_max_width = max_width
            if local_max_width is None:
                # If no max_width is provided, use the canvas width
                local_max_width = canvas.width - position[0]
            avg_char_width = get_text_size("W" * 10, font)[0] / 10
            return int(local_max_width // avg_char_width) - 1

        # Calculate wrap width
        # If no max_width provided, default to remaining canvas width
        if max_width is not None:
            max_width = canvas.width - position[0]
        wrap_width = calculate_wrap_width(font)
        # Ensure wrap_width is at least 1 to prevent invalid widths
        if wrap_width < 1:
            wrap_width = 1

        # Get original block height
        original_height: int = get_text_size(text, font)[1]

        # Respect max_lines by shrinking the font if needed
        wrap_adjustment = 1.75
        if max_lines is not None:
            current_size = font_size
            while True:
                # pick the right font for this size
                font = (
                    TextBuilder.get_font(type.font_path, current_size)
                    if type == TextType.h1 or type == TextType.h2 or type == TextType.h3
                    else TextBuilder.get_font(type.font_path, current_size)
                )
                # recalc avg char width → wrap_width
                wrap_w = calculate_wrap_width(font)
                wrap_w = max(wrap_w, 1)

                lines = textwrap.wrap(text, width=int(wrap_w * wrap_adjustment))
                # enforce max width: measure longest wrapped line
                max_line_width = max(get_text_size(line, font)[0] for line in lines) if lines else 0
                # stop if it fits or font is already minimal
                if (
                    len(lines) <= max_lines and (max_width is None or max_line_width <= max_width)
                ) or current_size <= 1:
                    wrapped_lines = lines
                    break
                current_size -= 1

            # finally, re‐load the font at the reduced size
            font = (
                TextBuilder.get_font(type.font_path, current_size)
                if type == TextType.h1 or type == TextType.h2 or type == TextType.h3
                else TextBuilder.get_font(type.font_path, current_size)
            )
        else:
            wrapped_lines = textwrap.wrap(text, width=int(wrap_width * wrap_adjustment))

        # Calculate height of the text block
        # text_height = sum(get_text_size(line, font)[1] for line in wrapped_lines)

        # Adjust position based on vertical alignment
        if vertical_align == "center":
            total_height = sum(get_text_size(line, font)[1] for line in wrapped_lines)
            position = (
                position[0],
                (position[1] + (original_height - total_height) // 2 if original_height > 0 else position[1]),
            )
        elif vertical_align == "bottom":
            total_height = sum(get_text_size(line, font)[1] for line in wrapped_lines)
            position = (
                position[0],
                (position[1] + (max_height - total_height) if max_height > 0 else position[1]),
            )

        # Draw each line with the calculated position
        pos = list(position)
        for line in wrapped_lines:
            draw.text(tuple(pos), line, font=font, fill=color)  # type: ignore[reportUnknownArgumentType]
            pos[1] += get_text_size(line, font)[1]  # Move down for the next line

        return {
            "line_count": len(wrapped_lines),
            "line_height": (get_text_size(wrapped_lines[0], font)[1] if wrapped_lines else 0),
        }

    @staticmethod
    def get_font(font_path: str, font_size: int) -> ImageFont.FreeTypeFont:
        font = ImageFont.truetype(font_path, font_size)

        # Measure the text height
        dummy_text = "A"
        bbox = font.getbbox(dummy_text)  # type: ignore
        text_height = bbox[3] - bbox[1]

        # default font size
        size = font_size / text_height

        # Adjust the font size to match the desired height
        adjusted_size = int(size * font_size)
        font = ImageFont.truetype(font_path, adjusted_size)
        return font
