from PySide6.QtWidgets import QMainWindow, QMessageBox

from service.UsuarioService import UsuarioService
from view.entidades.ventana_ciudad import VentanaCiudad
from view.menu_principal.ui_ventana_menu_principal import Ui_VentanaMenuPrincipal


class VentanaMenuPrincipal(QMainWindow, Ui_VentanaMenuPrincipal):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.usuario_service = UsuarioService()

        usuario = sesion.usuario
        self.lblBienvenida.setText(
            f"Bienvenido, {usuario.UsrNombres} {usuario.UsrApellidos}\n"
            f"Rol: {sesion.tipo_usuario.TipNombre}"
        )
        self.aplicar_permisos()

        self.actionSalir.triggered.connect(self.close)
        self.actionCiudad.triggered.connect(self.abrir_ciudad)
        # Cada opción se conecta a su ventana a medida que se vayan creando.
        for opcion in (self.actionCategoria, self.actionProducto,
                       self.actionProveedor, self.actionProveedorProducto, self.actionConsultas,
                       self.actionReportes, self.actionUsuarios, self.actionBitacora):
            opcion.triggered.connect(self.mostrar_pendiente)

    def aplicar_permisos(self):
        puede_modificar = self.usuario_service.puede_modificar(self.sesion)
        es_administrador = self.usuario_service.es_administrador(self.sesion.usuario.IDUsuario)
        self.menuEntidades.setEnabled(puede_modificar)
        self.menuTransacciones.setEnabled(puede_modificar)
        self.menuAuditoria.setEnabled(es_administrador)

    def abrir_ciudad(self):
        VentanaCiudad(self.sesion).exec()

    def mostrar_pendiente(self):
        QMessageBox.information(self, "Pendiente", "Esta ventana todavía no está disponible.")

    # Se ejecuta tanto con la opción "Salir" como con la X de la ventana.
    def closeEvent(self, evento):
        try:
            self.usuario_service.cerrar_sesion(self.sesion)
        except ConnectionError as error:
            QMessageBox.warning(self, "Salir", f"No se registró la salida en la bitácora.\n{error}")
        evento.accept()
