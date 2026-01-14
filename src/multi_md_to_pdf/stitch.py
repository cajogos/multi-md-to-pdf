from pathlib import Path
from markdown_it import MarkdownIt
from weasyprint import HTML
from .html_template import DEFAULT_CSS, HTML_SHELL


def build_html_document(input_dir: Path, title: str) -> str:
    md = MarkdownIt().enable(['table'])
    
    # Collect all markdown files first
    md_files = sorted(input_dir.rglob("*.md"))
    
    # Generate table of contents
    toc_items = []
    content_sections = []
    
    for idx, path in enumerate(md_files):
        section_id = f"section-{idx}"
        toc_items.append(f'<li><a href="#{section_id}">{path}</a></li>')
        
        # Render markdown to HTML
        html = md.render(path.read_text(encoding="utf-8"))
        content_sections.append(
            f'<section class="file-break"><p class="file-name" id="{section_id}"><em>{path}</em></p>{html}</section>'
        )
    
    # Build cover page with TOC
    toc_html = f'<ul class="toc">{"".join(toc_items)}</ul>' if toc_items else '<p>No markdown files found.</p>'
    
    cover_page = f'''<section class="cover-page">
  <h1>{title}</h1>
  <p class="github-link">Generated using <a href="https://github.com/cajogos/multi-md-to-pdf">multi-md-to-pdf</a></p>
  <h2>Table of Contents</h2>
  {toc_html}
</section>'''
    
    # Combine cover page and content sections
    body = cover_page + "\n" + "\n".join(content_sections)
    
    return HTML_SHELL.format(
        title=title,
        css=DEFAULT_CSS,
        body=body,
    )


def render_pdf(html: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(output)


def render_html(html: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
