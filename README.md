# Image to ASCII Converter

A simple Python tool to convert images into ASCII art.

## Features

- Convert images (JPEG, PNG, etc.) to ASCII art
- Adjustable output width and character set
- Save ASCII art to a text file
- No external dependencies required (does not use Pillow)

## Requirements

- Python 3.x

## Usage

```bash
uv run main.py 
```

### Arguments
- `--input`: Path to the input image file
- `--output`: (Optional) Path to save the ASCII output
- `--width`: (Optional) Output width in characters (default: 100)