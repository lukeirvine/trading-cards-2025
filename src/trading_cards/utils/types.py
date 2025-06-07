from enum import Enum
from typing import List, TypedDict

from trading_cards.utils.constants import constants


# This should be used for different font types, not sizes.
class TextType(Enum):
    h1 = ("h1", 60, constants.HEADING_FONT, 20, 1.2)
    h2 = ("h2", 28, constants.HEADING_FONT, 12, 1.2)
    h3 = ("h3", 24, constants.HEADING_FONT, 12, 1.2)
    body = ("body", 18, constants.BODY_FONT, 40, 1.2)

    def __init__(
        self,
        label: str,
        base_size: int,
        font_path: str,
        margin_after: int,
        leading: float = 1,
    ):
        self._label = label
        self.base_size = base_size
        self.leading = leading
        self.font_path = font_path
        self.margin_after = margin_after


class ProseItem(TypedDict):
    text: str
    type: TextType


ProseData = List[ProseItem]


class TextColor(tuple[int, int, int], Enum):
    white = (255, 255, 255)
    black = (0, 0, 0)


class Department(Enum):
    leadership = ("leadership", (191, 214, 250), TextColor.black)
    extreme = ("extreme", (232, 163, 109))
    laundry = ("laundry", (182, 154, 205))
    office = ("office", (238, 125, 121))
    waterfront = ("waterfront", (81, 122, 144))
    activities = ("activities", (221, 236, 157), TextColor.black)
    art = ("art", (235, 203, 224), TextColor.black)
    challenge = ("challenge", (195, 199, 171), TextColor.black)
    communications = ("communications", (98, 104, 148))
    equestrian = ("equestrian", (86, 53, 29))
    kitchen = ("kitchen", (15, 45, 44))
    maintenance = ("maintenance", (128, 61, 62))
    programming = ("programming", (250, 234, 184), TextColor.black)
    lifeguard = ("lifeguard", (210, 45, 31))
    null = ("null", (0, 0, 0))

    def __init__(
        self,
        label: str,
        bg_color: tuple[int, int, int],
        text_color: TextColor = TextColor.white,
    ):
        self.label = label
        self.bg_color = bg_color
        self.text_color = text_color

    def __getitem__(self, item: str):
        if item == "label":
            return self.label
        elif item == "bg_color":
            return self.bg_color
        elif item == "text_color":
            return self.text_color
        else:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{item}'")

    @staticmethod
    def is_valid(label: str) -> bool:
        return any(dept.label == label for dept in Department)

    @staticmethod
    def get_enum_by_label(label: str) -> "Department":
        for dept in Department:
            if dept.label == label:
                return dept
        raise ValueError(f"Invalid department label: {label}")
