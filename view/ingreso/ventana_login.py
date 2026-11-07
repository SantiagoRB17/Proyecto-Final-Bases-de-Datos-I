from PySide6.QtWidgets import QDialog, QMessageBox

from service.UsuarioService import UsuarioService
from view.ingreso.ui_ventana_login import Ui_VentanaLogin
from view.menu_principal.ventana_menu_principal import VentanaMenuPrincipal


# Hereda de la UI generada por Qt Designer, como "extends JFrame" en Java.
class VentanaLogin(QDialog, Ui_VentanaLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuario_service = UsuarioService()
        self.ventana_menu = None
        self.btnIngresar.clicked.connect(self.ingresar)

    def ingresar(self):
        nombre_usuario = self.txtUsuario.text().strip()
        contrasena = self.txtContrasena.text()
        if not nombre_usuario or not contrasena:
            QMessageBox.warning(self, "Ingreso", "Escriba el usuario y la contraseña.")
            return

        try:
            sesion = self.usuario_service.iniciar_sesion(nombre_usuario, contrasena)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Ingreso", str(error))
            self.txtContrasena.clear()
            return

        self.ventana_menu = VentanaMenuPrincipal(sesion)
        self.ventana_menu.show()
        self.close()
