# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`multi-md-to-pdf` is a Python CLI tool that recursively discovers all Markdown files in a directory tree and stitches them into a single PDF with a cover page and table of contents.

## Setup & Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The virtual environment lives at `.venv/`. After install, the `multi-md-to-pdf` command is available.

## Running the Tool

```bash
# With automatic timestamped output filename
multi-md-to-pdf /path/to/markdown/dir

# With custom output name (timestamp is still prepended)
multi-md-to-pdf /path/to/markdown/dir -o my-docs.pdf

# Explicit subcommand form (equivalent)
multi-md-to-pdf build /path/to/markdown/dir -o my-docs.pdf
```

Output files (both PDF and HTML) are written to `output/` by default, named `YYYY-MM-DD_HH-MM_<name>.pdf/.html`. The `output/` directory and all `*.pdf`/`*.html` files are gitignored.

## Architecture

The pipeline has three stages:

1. **`stitch.py`** — Core logic. `build_html_document()` recursively finds all `.md` files, converts each with `markdown-it-py`, generates anchor-linked TOC entries, wraps everything in a cover page, and returns a single HTML string. `build()` then writes the HTML file and renders the PDF via `weasyprint`.

2. **`html_template.py`** — All CSS and the HTML shell template are defined here (`DEFAULT_CSS` and `HTML_SHELL`). Page layout (A4, print breaks between files, typography) lives entirely in this file.

3. **`cli.py`** — `typer` app. The `main()` callback acts as both the default command and parent for the `build` subcommand. Output path resolution (directory creation, timestamp prefix) happens here before calling into `stitch.py`.

## Dependencies

- `markdown-it-py` — Markdown → HTML conversion
- `weasyprint` — HTML → PDF rendering (requires system libraries: Pango, Cairo, GDK-PixBuf)
- `typer` + `rich` — CLI and terminal output

## Tests

No tests exist yet. The `tests/` directory is empty.
