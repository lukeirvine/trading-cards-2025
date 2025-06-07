# Trading Cards Generator 2025

A Python-based system for generating custom trading cards with staff information from a csv file. The intent is to accumulate a library of helpful methods for adding text and images to a Pillow canvas, so minimal work is needed to design trading cards in future years.

## Features

- Generate trading cards from staff data in CSV format
- Custom styling for different departments
- Automatic image processing and resizing
- Automatic text scaling and resizing based on available space
- PDF compilation
- Turn on/off print bleed margins
- Can handle card rarity in the print PDF based on tenure

## Prerequisites

- Python 3.8 or higher
- Poetry (>=1.2.0) installed globally
- Homebrew (for macOS users)

### Install Poetry

Poetry is required to manage dependencies and virtual environments. Install it globally using one of the following:

```bash
# macOS (Homebrew)
brew install poetry

# All platforms
curl -sSL https://install.python-poetry.org | python3 -
```

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd trading-cards-2025
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install Python dependencies:

```bash
poetry install
```

## Project Structure

```
trading-cards-2025/
├── classes/              # Core application classes
│   ├── card_app.py      # Main application logic
│   ├── card_front_generator.py  # Card front generation
│   └── csv_reader.py    # CSV data processing
├── utils/               # Utility functions
│   └── utils.py        # Helper functions and constants
├── materials/          # Design assets
│   ├── border.svg      # Card border template
│   ├── job_container.svg  # Job title container
│   └── star.svg        # Star template
├── fonts/              # Font files
│   └── PoetsenOne-Regular.ttf
├── images/            # Staff images
└── requirements.txt   # Python dependencies
```

## Usage

1. Prepare your staff data in CSV format with the following columns:

   - `image_path`
     - The file name of the image of the staff member.
   - `name`
   - `position`
   - `years_worked`
   - `department`
     - This should be an enum key of `Department` in [`types.py`](src/trading_cards/utils/types.py)
   - `bible_verse`
   - `question_1`
   - `answer_1`
   - `question_2`
   - `answer_2`
   - `question_3`
   - `answer_3`
   - `optional_front_file`
     - This is for if a staff member needs an exclusive border asset for
       the front of the card.

2. Place your csv in the `input` directory and provide the path to it in [`main.py`](src/trading_cards/main.py)
3. Place staff images in the `images/` directory

4. Run the application:

```bash
python src/trading_cards/main.py
```

5. Run in watch mode:

```bash
python watcher.py
```

## For 2026 Trading Cards:

1. Create a new repo for 2026
2. Clone this repo, copy the code to a new dir, link up with the new 2026 repo.
3. Edit the files in `src/trading_cards/card`, taking advantage of the methods in
   `src/trading_cards/builder` and `src/trading_cards/utils`.

## Acknowledgments

- Card design by Kate Byrd
