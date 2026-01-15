# Multi-MD to PDF

A Python tool that recursively finds all Markdown files in a directory and stitches them together into a single, beautifully formatted PDF document.

## Features

- 🔍 **Recursive Search**: Automatically finds all Markdown files (`.md`) in a directory tree
- 📄 **Single PDF Output**: Combines all Markdown files into one cohesive PDF document
- 📑 **Page Breaks**: Each Markdown file starts on a new page with its path as a header
- 🎨 **Clean Formatting**: Professional A4 layout with sensible margins and typography
- ⚡ **Simple CLI**: Easy-to-use command-line interface

## Installation

### Prerequisites

- Python 3.10 or higher

### Install from Source

1. Clone the repository:
```bash
git clone <repository-url>
cd multi-md-to-pdf
```

2. Install the package:
```bash
pip install -e .
```

This will install the package in editable mode along with all dependencies.

## Usage

### Basic Usage

Convert all Markdown files in a directory to a single PDF:

```bash
multi-md-to-pdf /path/to/markdown/directory
```

This will create a timestamped file like
`output/2026-01-15_10-40_multi-md-to-pdf.pdf` by default, along with a matching
HTML file that shares the same base name.

### Custom Output Path

Specify a custom output file name (a timestamp is prepended automatically, and
the `.pdf` suffix is optional):

```bash
multi-md-to-pdf /path/to/markdown/directory --output my-document.pdf
```

Or use the short form:

```bash
multi-md-to-pdf /path/to/markdown/directory -o my-document.pdf
```

This will create a file like `2026-01-15_10-40_my-document.pdf` (or
`2026-01-15_10-40_my-document.html`) and a matching HTML file with the same
timestamped base name.

If you prefer, you can still use the explicit `build` subcommand:

```bash
multi-md-to-pdf build /path/to/markdown/directory
```

### Example

If you have a directory structure like this:

```
docs/
├── chapter1/
│   ├── introduction.md
│   └── overview.md
├── chapter2/
│   └── details.md
└── appendix.md
```

Running:

```bash
multi-md-to-pdf build docs
```

Will create a PDF with all Markdown files combined, each starting on a new page.

## How It Works

1. **Discovery**: Recursively searches the input directory for all `.md` files
2. **Conversion**: Converts each Markdown file to HTML using `markdown-it-py`
3. **Assembly**: Combines all HTML sections into a single document with page breaks
4. **Rendering**: Converts the HTML to PDF using WeasyPrint with A4 page formatting

## Dependencies

- `markdown-it-py` (≥3.0.0): Markdown to HTML conversion
- `weasyprint` (≥62.0): HTML to PDF rendering
- `typer` (≥0.12.0): CLI framework
- `rich` (≥13.7.0): Enhanced terminal output

## Project Structure

```
multi-md-to-pdf/
├── src/
│   └── multi_md_to_pdf/
│       ├── __init__.py
│       ├── cli.py          # Command-line interface
│       ├── stitch.py       # Core PDF generation logic
│       └── html_template.py # HTML/CSS templates
├── tests/                  # Test files
├── output/                 # Default output directory
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## License

MIT License

## Author

Carlos Ferreira (@cajogos)
