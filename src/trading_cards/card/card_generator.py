from trading_cards.staff_member import StaffMember


class CardGeenrator:
    def __init__(self, output_dir: str, use_print_layout: bool = False) -> None:
        self.output_dir: str = output_dir
        self.use_print_layout: bool = use_print_layout

    def generate_card(self, staff_member: StaffMember) -> None:
        print("Generating card for:", staff_member.name)
