DEFAULT_CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: sans-serif; font-size: 11pt; }
pre, code { font-family: monospace; }
.file-break { break-before: page; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
table th, table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
table th { background-color: #f2f2f2; font-weight: bold; }
"""

HTML_SHELL = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<h1>{title}</h1>
{body}
</body>
</html>
"""

