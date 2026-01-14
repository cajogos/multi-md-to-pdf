from pathlib import Path
import typer
from .stitch import build_html_document, render_pdf

app = typer.Typer(add_completion=False)


@app.command()
def build(
    input_dir: Path = typer.Argument(..., exists=True, file_okay=False),
    output: Path = typer.Option(
        Path("output/stitched.pdf"),
        "--output",
        "-o",
        help="Output PDF file",
    ),
):
    html = build_html_document(input_dir, "Stitched Markdown")
    render_pdf(html, output)
