from PySide6.QtWidgets import QMainWindow, QMessageBox

from service.UsuarioService import UsuarioService
from view.auditoria.ventana_bitacora import VentanaBitacora
from view.auditoria.ventana_usuarios import VentanaUsuarios
from view.consultas_reportes.ventana_consultas import VentanaConsultas
from view.consultas_reportes.ventana_reportes import VentanaReportes
from view.entidades.ventana_categoria import VentanaCategoria
from view.entidades.ventana_ciudad import VentanaCiudad
from view.entidades.ventana_producto import VentanaProducto
from view.entidades.ventana_proveedor import VentanaProveedor
from view.menu_principal.ui_ventana_menu_principal import Ui_VentanaMenuPrincipal
from view.transacciones.ventana_detalle_proveedor_producto import VentanaDetalleProveedorProducto


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
        self.actionCategoria.triggered.connect(self.abrir_categoria)
        self.actionProducto.triggered.connect(self.abrir_producto)
        self.actionProveedor.triggered.connect(self.abrir_proveedor)
        self.actionProveedorProducto.triggered.connect(self.abrir_proveedor_producto)
        self.actionConsultas.triggered.connect(self.abrir_consultas)
        self.actionUsuarios.triggered.connect(self.abrir_usuarios)
        self.actionBitacora.triggered.connect(self.abrir_bitacora)
        self.actionReportes.triggered.connect(self.abrir_reportes)

    def aplicar_permisos(self):
        puede_modificar = self.usuario_service.puede_modificar(self.sesion)
        es_administrador = self.usuario_service.es_administrador(self.sesion.usuario.IDUsuario)
        self.menuEntidades.setEnabled(puede_modificar)
        self.menuTransacciones.setEnabled(puede_modificar)
        self.menuAuditoria.setEnabled(es_administrador)

    def abrir_ciudad(self):
        VentanaCiudad(self.sesion).exec()

    def abrir_categoria(self):
        VentanaCategoria(self.sesion).exec()

    def abrir_producto(self):
        VentanaProducto(self.sesion).exec()

    def abrir_proveedor(self):
        VentanaProveedor(self.sesion).exec()

    def abrir_proveedor_producto(self):
        VentanaDetalleProveedorProducto(self.sesion).exec()

    def abrir_consultas(self):
        # Esta ventana consulta la base de datos desde que se crea.
        try:
            VentanaConsultas(self.sesion).exec()
        except ConnectionError as error:
            QMessageBox.warning(self, "Consultas", str(error))

    def abrir_reportes(self):
        # Esta ventana consulta la base de datos desde que se crea.
        try:
            VentanaReportes(self.sesion).exec()
        except ConnectionError as error:
            QMessageBox.warning(self, "Reportes", str(error))

    def abrir_usuarios(self):
        VentanaUsuarios(self.sesion).exec()

    def abrir_bitacora(self):
        VentanaBitacora(self.sesion).exec()

    # Se ejecuta tanto con la opción "Salir" como con la X de la ventana.
    def closeEvent(self, evento):
        try:
            self.usuario_service.cerrar_sesion(self.sesion)
        except ConnectionError as error:
            QMessageBox.warning(self, "Salir", f"No se registró la salida en la bitácora.\n{error}")
        evento.accept()
