# utils_highlight.py

from pygments import highlight
from pygments.lexers import RubyLexer
from pygments.formatters import HtmlFormatter
from IPython.display import HTML, display

def mostrar_codigo_ruby_con_resaltado(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        ruby_code = f.read()

    formatter = HtmlFormatter(style="colorful")
    highlighted = highlight(ruby_code, RubyLexer(), formatter)
    style = f"<style>{formatter.get_style_defs('.highlight')}</style>"

    display(HTML(style + highlighted))
