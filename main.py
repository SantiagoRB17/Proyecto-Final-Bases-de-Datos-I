import sys

from PySide6.QtWidgets import QApplication

from view.ingreso.ventana_login import VentanaLogin


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())
