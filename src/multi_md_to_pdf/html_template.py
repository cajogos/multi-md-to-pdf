DEFAULT_CSS = """
@page { 
    size: A4; 
    margin: 20mm 18mm; 
}

body { 
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt; 
    line-height: 1.6;
    color: #333;
}

/* Cover Page */
.cover-page {
    break-after: page;
    text-align: center;
    padding: 40mm 0;
}

.cover-page h1 {
    font-size: 36pt;
    font-weight: 700;
    margin-bottom: 20pt;
    color: #2c3e50;
}

.cover-page .github-link {
    font-size: 12pt;
    margin-bottom: 40pt;
    color: #666;
}

.cover-page .github-link a {
    color: #0366d6;
    text-decoration: none;
}

.cover-page .github-link a:hover {
    text-decoration: underline;
}

.cover-page h2 {
    font-size: 20pt;
    font-weight: 600;
    margin-top: 40pt;
    margin-bottom: 20pt;
    color: #2c3e50;
    text-align: left;
}

/* Table of Contents */
.toc {
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: left;
}

.toc li {
    margin: 8pt 0;
    padding-left: 0;
}

.toc a {
    color: #0366d6;
    text-decoration: none;
    font-size: 11pt;
    line-height: 1.8;
}

.toc a:hover {
    text-decoration: underline;
}

/* Headings */
h1 {
    font-size: 28pt;
    font-weight: 700;
    margin-top: 24pt;
    margin-bottom: 16pt;
    color: #2c3e50;
    page-break-after: avoid;
}

h2 {
    font-size: 22pt;
    font-weight: 600;
    margin-top: 20pt;
    margin-bottom: 12pt;
    color: #34495e;
    page-break-after: avoid;
}

h3 {
    font-size: 18pt;
    font-weight: 600;
    margin-top: 16pt;
    margin-bottom: 10pt;
    color: #34495e;
    page-break-after: avoid;
}

h4 {
    font-size: 14pt;
    font-weight: 600;
    margin-top: 14pt;
    margin-bottom: 8pt;
    color: #34495e;
    page-break-after: avoid;
}

h5, h6 {
    font-size: 12pt;
    font-weight: 600;
    margin-top: 12pt;
    margin-bottom: 6pt;
    color: #34495e;
    page-break-after: avoid;
}

/* File break sections */
.file-break { 
    break-before: page; 
}

.file-name {
    font-style: italic;
    color: #666;
    margin-top: 0;
    margin-bottom: 16pt;
    font-size: 10pt;
}

/* Paragraphs */
p {
    margin: 10pt 0;
    text-align: justify;
}

/* Links */
a {
    color: #0366d6;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Code */
code {
    font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
    font-size: 10pt;
    background-color: #f5f5f5;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    padding: 2pt 4pt;
    color: #e83e8c;
}

pre {
    font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
    font-size: 10pt;
    background-color: #f8f8f8;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 12pt;
    margin: 12pt 0;
    overflow-x: auto;
    line-height: 1.5;
    page-break-inside: avoid;
}

pre code {
    background-color: transparent;
    border: none;
    padding: 0;
    color: #333;
    font-size: inherit;
}

/* Lists */
ul, ol {
    margin: 10pt 0;
    padding-left: 24pt;
}

li {
    margin: 6pt 0;
    line-height: 1.6;
}

ul ul, ol ol, ul ol, ol ul {
    margin-top: 4pt;
    margin-bottom: 4pt;
}

/* Tables */
table { 
    border-collapse: collapse; 
    width: 100%; 
    margin: 16pt 0;
    page-break-inside: avoid;
}

table th, table td { 
    border: 1px solid #ddd; 
    padding: 10pt 12pt; 
    text-align: left;
}

table th { 
    background-color: #f8f9fa;
    font-weight: 600;
    color: #2c3e50;
}

table tr:nth-child(even) {
    background-color: #f9f9f9;
}

table tr:hover {
    background-color: #f5f5f5;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #ddd;
    margin: 12pt 0;
    padding: 8pt 16pt;
    background-color: #f9f9f9;
    color: #666;
    font-style: italic;
}

blockquote p {
    margin: 6pt 0;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    margin: 12pt 0;
    page-break-inside: avoid;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 1px solid #e0e0e0;
    margin: 20pt 0;
}
"""

HTML_SHELL = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""

