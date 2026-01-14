from pathlib import Path
from markdown_it import MarkdownIt
from weasyprint import HTML
from .html_template import DEFAULT_CSS, HTML_SHELL


def build_html_document(input_dir: Path, title: str) -> str:
    md = MarkdownIt()
    sections = []

    for path in sorted(input_dir.rglob("*.md")):
        html = md.render(path.read_text(encoding="utf-8"))
        sections.append(f'<section class="file-break"><h2>{path}</h2>{html}</section>')

    return HTML_SHELL.format(
        title=title,
        css=DEFAULT_CSS,
        body="\n".join(sections),
    )


def render_pdf(html: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(output)
