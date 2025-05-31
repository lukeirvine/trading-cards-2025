import os
from typing import Tuple

from PIL import Image

from trading_cards.builder.image import ImageBuilder
from trading_cards.staff_member import StaffMember
from trading_cards.utils.constants import constants


class CardBackGenerator:
    def __init__(self, staff_member: StaffMember) -> None:
        self.staff_member: StaffMember = staff_member
        size: Tuple[int, int] = (constants.CARD_WIDTH, constants.CARD_HEIGHT)
        self.canvas = Image.new("RGB", size, color=(255, 255, 255))

    def get_card_back(self) -> Image.Image:
        # Add design to back
        ImageBuilder.add_image_to_canvas(
            self.canvas,
            os.path.join(
                constants.MATERIAL_PATH,
                f"{self.staff_member.department.value}_back.png",
            ),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        return self.canvas
