from trading_cards.app import App


def main() -> None:
    app = App(
        csv_file_path="input/staff-test.csv",
        image_dir="images",
        output_dir="output",
        generate_pdfs=True,
        use_print_layout=True,
    )
    app.run()


if __name__ == "__main__":
    main()
