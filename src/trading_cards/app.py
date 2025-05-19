from trading_cards.csv_reader import CSVReader


class App:
    def __init__(
        self,
        csv_file_path: str,
        output_dir: str,
        generate_pdfs: bool = False,
        use_print_layout: bool = False,
    ) -> None:
        self.csv_file_path: str = csv_file_path
        self.output_dir: str = output_dir
        self.generate_pdfs: bool = generate_pdfs
        self.use_print_layout: bool = use_print_layout

    def run(self) -> None:
        reader = CSVReader(self.csv_file_path)
        staff_members = reader.read_csv()

        print("=========================================")
        print("Generating cards...")
        print("=========================================")
        for staff_member in staff_members:
            print(f"Generating card for {staff_member.name}...")
            # Here you would call the card generator to create the card
            # For example:
            # card_generator = CardGenerator(self.output_dir, self.use_print_layout)
            # card_generator.generate_card(staff_member)
