# Meme Generator

This project provides a meme generator tool using both a command-line interface (CLI) and a web application built with Flask.

## Features

- Create memes via command line or web interface.
- Combines an image with a quote to generate memes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/justinkumpe/Meme_Generator_Python.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command Line Interface (CLI)

Run the `meme.py` script from the terminal with the following optional arguments:

- `--body`: The quote body (string).
- `--author`: The quote author (string).
- `--path`: The image path (string).

Example usage:

```bash
python3 src/meme.py --body "Quote Body" --author "Author of Quote" --path "image.jpg"
```

### Command Line Interface (CLI) 
1. Run the `app.py`
    ```bash
    python src/app.py
    ```

2. Open browser with link http://127.0.0.1:5000/