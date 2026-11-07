import sys

from PySide6.QtWidgets import QApplication

from view.ingreso.ventana_login import VentanaLogin
from view.tema import aplicar_tema


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicar_tema(app)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())
