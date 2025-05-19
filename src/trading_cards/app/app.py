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
        print("Running the app...")
