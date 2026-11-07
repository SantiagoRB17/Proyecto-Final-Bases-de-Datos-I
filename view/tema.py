from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication


# Aplica el tema propio de la aplicación (view/tema.qss). QSS es el "CSS" de Qt.
def aplicar_tema(app):
    # Fusion y el esquema claro hacen que la aplicación se vea igual en todos
    # los computadores, sin importar si Windows está en modo claro u oscuro.
    app.setStyle("Fusion")
    QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
    carpeta = Path(__file__).parent
    hoja = carpeta.joinpath("tema.qss").read_text(encoding="utf-8")
    # El QSS necesita la ruta de las flechas (SVG) con barras normales.
    app.setStyleSheet(hoja.replace("{{RECURSOS}}", (carpeta / "recursos").as_posix()))


# Deja una tabla de resultados legible: cada columna al ancho de su contenido
# (la última ocupa el resto) y los encabezados alineados a la izquierda, igual
# que los datos. Se llama después de llenar la tabla.
def ajustar_tabla(tabla):
    tabla.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
    tabla.resizeColumnsToContents()
