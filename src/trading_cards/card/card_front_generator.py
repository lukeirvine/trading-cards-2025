from typing import Tuple

from PIL import Image

from trading_cards.staff_member import StaffMember
from trading_cards.utils.constants import constants


class CardFrontGenerator:
    def __init__(self, staff_member: StaffMember) -> None:
        self.staff_member: StaffMember = staff_member
        size: Tuple[int, int] = (constants.CARD_WIDTH, constants.CARD_HEIGHT)
        self.canvas = Image.new("RGB", size, color=(255, 255, 255))

    def get_card_face(self) -> Image.Image:
        return self.canvas
