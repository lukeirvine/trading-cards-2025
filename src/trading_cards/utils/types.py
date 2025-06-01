from enum import Enum
from typing import List, TypedDict

from trading_cards.utils.constants import constants


# This should be used for different font types, not sizes.
class TextType(Enum):
    h1 = ("h1", 60, constants.HEADING_FONT, 20)
    h2 = ("h2", 28, constants.HEADING_FONT, 12)
    h3 = ("h3", 22, constants.HEADING_FONT, 20)
    body = ("body", 18, constants.BODY_FONT, 40)

    def __init__(
        self,
        label: str,
        base_size: int,
        font_path: str,
        margin_after: int,
    ):
        # `label` isn’t strictly needed beyond repr, but you could use it for debugging.
        self._label = label
        self.base_size = base_size
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
    extreme = ("extreme", (0, 0, 0))
    laundry = ("laundry", (0, 0, 0))
    office = ("office", (0, 0, 0))
    waterfront = ("waterfront", (0, 0, 0))
    activities = ("activities", (0, 0, 0), TextColor.black)
    art = ("art", (0, 0, 0), TextColor.black)
    challenge = ("challenge", (0, 0, 0), TextColor.black)
    communications = ("communications", (0, 0, 0))
    equestrian = ("equestrian", (0, 0, 0))
    kitchen = ("kitchen", (0, 0, 0))
    maintenance = ("maintenance", (0, 0, 0))
    programming = ("programming", (0, 0, 0), TextColor.black)
    lifeguard = ("lifeguard", (0, 0, 0))
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
