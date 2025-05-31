class Constants:
    # Paths ========================
    MATERIAL_PATH: str = "materials"

    # Limits ========================
    MAX_YEARS: int = 14

    # Layouts ========================
    CARD_WIDTH: int = 750
    CARD_HEIGHT: int = 1050
    # height is 149
    CONT_1_TOP: int = 741
    CONT_1_MIN_WIDTH: int = 482
    CONT_1_MAX_WIDTH: int = 650
    # height is 124
    CONT_2_TOP: int = 888
    CONT_2_MAX_WIDTH: int = 340
    STAR_START_POS_X: int = 340
    STAR_START_POS_Y: int = 935
    STAR_SPACING_X: int = 10
    STAR_SPACING_Y: int = 10
    STAR_ROW_OFFSET: int = -25
    PRINT_WIDTH: int = 825
    PRINT_HEIGHT: int = 1125
    # Margins ========================
    FRONT_MARGIN_HORIZONTAL: int = 20

    BACK_MARGIN: int = 50

    # Styles ========================
    HEADING_FONT: str = "fonts/Cleanow-j9v60.ttf"
    BODY_FONT: str = "fonts/Cleanow-j9v60.ttf"


constants: Constants = Constants()
