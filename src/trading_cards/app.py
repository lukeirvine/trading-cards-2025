from typing import List, TypedDict

from trading_cards.card.card_generator import CardGenerator
from trading_cards.csv_reader import CSVReader
from trading_cards.staff_member import Department, StaffMember
from trading_cards.utils.helpers import Helpers


class GeneratedImageMetadata(TypedDict):
    front_file_name: str
    back_file_name: str
    department: Department
    years: int


class App:
    def __init__(
        self,
        csv_file_path: str,
        image_dir: str,
        output_dir: str,
        generate_pdfs: bool = False,
        use_print_layout: bool = False,
    ) -> None:
        self.csv_file_path: str = csv_file_path
        self.image_dir: str = image_dir
        self.output_dir: str = output_dir
        self.generate_pdfs: bool = generate_pdfs
        self.use_print_layout: bool = use_print_layout

    def run(self) -> None:
        reader = CSVReader(self.csv_file_path, self.image_dir)
        staff_members: list[StaffMember] = reader.read_csv()

        print("=========================================")
        print("Generating cards...")
        print("=========================================")

        generator = CardGenerator(self.output_dir, self.image_dir)
        generated_image_metadata: List[GeneratedImageMetadata] = []

        for staff_member in staff_members:
            front_image, back_image = generator.generate_card(staff_member)

            front_file_name = f"{staff_member.name}_front.png"
            back_file_name = f"{staff_member.name}_back.png"
            Helpers.save_canvas(
                canvas=front_image,
                sub_dir=staff_member.department.value,
                file_name=front_file_name,
                output_dir=self.output_dir,
            )
            Helpers.save_canvas(
                canvas=back_image,
                sub_dir=staff_member.department.value,
                file_name=back_file_name,
                output_dir=self.output_dir,
            )

            generated_image_metadata.append(
                {
                    "front_file_name": front_file_name,
                    "back_file_name": back_file_name,
                    "department": staff_member.department,
                    "years": staff_member.years_worked,
                }
            )
            print(f"Generated card for {staff_member.name}")

        print("=========================================")
