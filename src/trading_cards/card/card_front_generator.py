import os
from typing import Tuple

from PIL import Image

from trading_cards.staff_member import StaffMember
from trading_cards.utils.constants import constants
from trading_cards.utils.helpers import Helpers
from trading_cards.utils.types import TextType


class CardFrontGenerator:
    def __init__(self, staff_member: StaffMember, image_dir: str) -> None:
        self.staff_member: StaffMember = staff_member
        self.image_dir: str = image_dir
        size: Tuple[int, int] = (constants.CARD_WIDTH, constants.CARD_HEIGHT)
        self.canvas = Image.new("RGB", size, color=(255, 255, 255))

    def get_card_face(self) -> Image.Image:
        # Add main image to card
        Helpers.add_image_to_canvas(
            self.canvas,
            os.path.join(self.image_dir, self.staff_member.image_path),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        # Add border to card
        Helpers.add_mask_to_canvas(
            self.canvas,
            os.path.join(
                constants.MATERIAL_PATH,
                f"{self.staff_member.department.value}_front.png",
            ),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        # Add text to card
        Helpers.add_text_to_canvas(
            text="Kitchen Lead",
            canvas=self.canvas,
            font_size=12,
            type=TextType.heading,
            position=(constants.FRONT_MARGIN_HORIZONTAL, 885),
            max_width=425,
            max_lines=1,
            vertical_align="center",
        )

        Helpers.add_rect_to_canvas(
            self.canvas,
            (
                constants.FRONT_MARGIN_HORIZONTAL + 425,
                885,
            ),
            (5, 100),
        )

        return self.canvas
