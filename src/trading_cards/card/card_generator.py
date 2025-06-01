import os
from enum import Enum
from typing import Tuple

from PIL import Image

from trading_cards.card.card_back_generator import CardBackGenerator
from trading_cards.card.card_front_generator import CardFrontGenerator
from trading_cards.staff_member import StaffMember
from trading_cards.utils.constants import constants


class Side(str, Enum):
    FRONT = "front"
    BACK = "back"


class CardGenerator:
    def __init__(self, output_dir: str, image_dir: str, use_print_layout: bool = False) -> None:
        self.output_dir: str = output_dir
        self.image_dir: str = image_dir
        self.use_print_layout: bool = use_print_layout

    def generate_card(self, staff_member: StaffMember) -> Tuple[Image.Image, Image.Image]:
        print("Generating card for:", staff_member.name)

        front_canvas: Image.Image = CardFrontGenerator(staff_member, self.image_dir).get_card_face()
        back_canvas: Image.Image = CardBackGenerator(staff_member).get_card_back()

        return (front_canvas, back_canvas)

    def add_print_layout(
        self, image: Image.Image, staff_member: StaffMember, side: Side = Side.BACK
    ) -> Image.Image:
        canvas = Image.new(
            "RGB",
            (constants.PRINT_WIDTH, constants.PRINT_HEIGHT),
            color=staff_member.department.bg_color,
        )

        # add the print border
        border = Image.open("materials/print-border-5.png")
        border = border.resize((constants.PRINT_WIDTH, constants.PRINT_HEIGHT))
        paste_alpha = border.split()[-1]
        canvas.paste(border, (0, 0), mask=paste_alpha)

        # paste the image onto the canvas
        canvas.paste(
            image,
            (
                (constants.PRINT_WIDTH - constants.CARD_WIDTH) // 2,
                (constants.PRINT_HEIGHT - constants.CARD_HEIGHT) // 2,
            ),
        )

        return canvas

    def save_card(self, image: Image.Image, sub_dir: str, file_name: str) -> None:
        save_dir = os.path.join(self.output_dir, sub_dir)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image.save(os.path.join(save_dir, file_name))
