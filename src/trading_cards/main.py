from trading_cards.app.app import App


def main() -> None:
    app = App(
        csv_file_path="staff-2025-final.csv",
        output_dir="output",
        generate_pdfs=True,
        use_print_layout=True,
    )
    app.run()


if __name__ == "__main__":
    main()
