from enum import Enum
from typing import List, TypedDict

from trading_cards.utils.constants import constants


# This should be used for different font types, not sizes.
class TextType(Enum):
    h1 = ("h1", 60, constants.HEADING_FONT)
    h2 = ("h2", 30, constants.HEADING_FONT)
    h3 = ("h3", 20, constants.HEADING_FONT)
    body = ("body", 16, constants.BODY_FONT)

    def __init__(
        self,
        label: str,
        base_size: int,
        font_path: str,
    ):
        # `label` isn’t strictly needed beyond repr, but you could use it for debugging.
        self._label = label
        self.base_size = base_size
        self.font_path = font_path


class ProseItem(TypedDict):
    text: str
    type: TextType


ProseData = List[ProseItem]


class Department(str, Enum):
    leadership = "leadership"
    extreme = "extreme"
    laundry = "laundry"
    office = "office"
    waterfront = "waterfront"
    activities = "activities"
    art = "art"
    challenge = "challenge"
    communications = "communications"
    dt = "dt"
    equestrian = "equestrian"
    kitchen = "kitchen"
    maintenance = "maintenance"
    survival = "survival"
    ultimate = "ultimate"
    programming = "programming"
    lifeguard = "lifeguard"
    null = "null"
