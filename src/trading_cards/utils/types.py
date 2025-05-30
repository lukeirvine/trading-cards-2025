from enum import Enum


# This should be used for different font types, not sizes.
class TextType(str, Enum):
    heading = "heading"
    body = "body"


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
