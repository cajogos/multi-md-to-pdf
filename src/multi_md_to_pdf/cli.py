from datetime import datetime
from pathlib import Path
import typer
from .stitch import build_html_document, render_pdf, render_html

app = typer.Typer(add_completion=False)


def build_timestamped_output_path(output: Path) -> Path:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_name = output.stem if output.suffix else output.name
    timestamped_name = f"{timestamp}_{output_name}"
    timestamped_path = output.with_name(timestamped_name)
    return timestamped_path.with_suffix(".pdf")


def resolve_output_path(output: Path | None) -> Path:
    if output is None:
        return build_timestamped_output_path(Path("output/multi-md-to-pdf"))

    return build_timestamped_output_path(output)


def run_build(input_dir: Path, output: Path | None) -> None:
    html = build_html_document(input_dir, "Multi MD to PDF")
    output_path = resolve_output_path(output)
    render_pdf(html, output_path)
    # Also output HTML file with same base name
    html_output = output_path.with_suffix(".html")
    render_html(html, html_output)
    typer.echo(f"Generated PDF: {output_path}")
    typer.echo(f"Generated HTML: {html_output}")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    input_dir: Path | None = typer.Argument(None, exists=True, file_okay=False),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output PDF file name (timestamped, .pdf optional)",
    ),
):
    if ctx.invoked_subcommand is None:
        if input_dir is None:
            raise typer.BadParameter("Missing INPUT_DIR.")
        run_build(input_dir, output)


@app.command()
def build(
    input_dir: Path = typer.Argument(..., exists=True, file_okay=False),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output PDF file name (timestamped, .pdf optional)",
    ),
):
    run_build(input_dir, output)
