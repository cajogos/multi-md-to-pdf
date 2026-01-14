DEFAULT_CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: sans-serif; font-size: 11pt; }
pre, code { font-family: monospace; }
.file-break { break-before: page; }
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

