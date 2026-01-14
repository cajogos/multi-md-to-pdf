from pathlib import Path
import typer
from .stitch import build_html_document, render_pdf, render_html

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
    html = build_html_document(input_dir, "Multi MD to PDF")
    render_pdf(html, output)
    # Also output HTML file with same base name
    html_output = output.with_suffix(".html")
    render_html(html, html_output)
    typer.echo(f"Generated PDF: {output}")
    typer.echo(f"Generated HTML: {html_output}")
