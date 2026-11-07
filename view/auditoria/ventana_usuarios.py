from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from model.Usuario import Usuario
from service.UsuarioService import UsuarioService
from view.auditoria.ui_ventana_usuarios import Ui_VentanaUsuarios


# A diferencia de las entidades simples, esta ventana no usa DAO directamente:
# todo pasa por UsuarioService, que aplica las reglas de negocio de usuarios.
class VentanaUsuarios(QDialog, Ui_VentanaUsuarios):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.usuario_actual = sesion.usuario
        self.usuario_service = UsuarioService()
        self.usuarios = []
        self.id_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.desactivar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblUsuarios.itemSelectionChanged.connect(self.seleccionar_fila)

        self.cargar_tipos()
        self.cargar_tabla()

    def cargar_tipos(self):
        try:
            tipos = self.usuario_service.consultar_tipos_usuario(self.usuario_actual)
        except (PermissionError, ConnectionError) as error:
            QMessageBox.warning(self, "Usuarios", str(error))
            return
        for tipo in tipos:
            self.cmbTipoUsuario.addItem(tipo.TipNombre, tipo.IDTipoUsuario)

    def cargar_tabla(self):
        try:
            self.usuarios = self.usuario_service.consultar_todos_usuarios(self.usuario_actual)
        except (PermissionError, ConnectionError) as error:
            QMessageBox.warning(self, "Usuarios", str(error))
            return

        self.tblUsuarios.setRowCount(len(self.usuarios))
        for fila, usuario in enumerate(self.usuarios):
            rol = self.cmbTipoUsuario.itemText(self.cmbTipoUsuario.findData(usuario.IDTipoUsuario))
            estado = "Activo" if usuario.UsrEstado else "Inactivo"
            self.tblUsuarios.setItem(fila, 0, QTableWidgetItem(str(usuario.IDUsuario)))
            self.tblUsuarios.setItem(fila, 1, QTableWidgetItem(usuario.UsrNombreUsuario))
            self.tblUsuarios.setItem(fila, 2, QTableWidgetItem(usuario.UsrNombres))
            self.tblUsuarios.setItem(fila, 3, QTableWidgetItem(usuario.UsrApellidos))
            self.tblUsuarios.setItem(fila, 4, QTableWidgetItem(rol))
            self.tblUsuarios.setItem(fila, 5, QTableWidgetItem(estado))

    def seleccionar_fila(self):
        filas = self.tblUsuarios.selectionModel().selectedRows()
        if not filas:
            self.id_seleccionado = None
            return
        usuario = self.usuarios[filas[0].row()]
        self.id_seleccionado = usuario.IDUsuario
        self.txtNombreUsuario.setText(usuario.UsrNombreUsuario)
        self.txtContrasena.clear()
        self.txtNombres.setText(usuario.UsrNombres)
        self.txtApellidos.setText(usuario.UsrApellidos)
        self.cmbTipoUsuario.setCurrentIndex(self.cmbTipoUsuario.findData(usuario.IDTipoUsuario))
        self.chkEstado.setChecked(usuario.UsrEstado)

    def limpiar_formulario(self):
        self.tblUsuarios.clearSelection()
        self.id_seleccionado = None
        self.txtNombreUsuario.clear()
        self.txtContrasena.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.cmbTipoUsuario.setCurrentIndex(0)
        self.chkEstado.setChecked(True)
        self.txtNombreUsuario.setFocus()

    def agregar(self):
        if self.id_seleccionado is not None:
            QMessageBox.warning(self, "Usuarios",
                                "Presione Nuevo para registrar otro usuario, o Editar para guardar los cambios.")
            return
        usuario = self._leer_formulario()
        if usuario is None:
            return
        contrasena = self.txtContrasena.text()
        if not contrasena:
            QMessageBox.warning(self, "Usuarios", "Escriba la contraseña del nuevo usuario.")
            return
        self._ejecutar(self.usuario_service.agregar_usuario, self.usuario_actual, usuario, contrasena)

    def editar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Usuarios", "Seleccione el usuario que desea editar.")
            return
        usuario = self._leer_formulario()
        if usuario is None:
            return
        usuario.IDUsuario = self.id_seleccionado
        self._ejecutar(self.usuario_service.editar_usuario, self.usuario_actual, usuario, self.txtContrasena.text())

    def desactivar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Usuarios", "Seleccione el usuario que desea desactivar.")
            return
        respuesta = QMessageBox.question(self, "Usuarios", "¿Desea desactivar el usuario seleccionado?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self.usuario_service.eliminar_usuario, self.usuario_actual, self.id_seleccionado)

    def _leer_formulario(self):
        nombre_usuario = self.txtNombreUsuario.text().strip()
        nombres = self.txtNombres.text().strip()
        apellidos = self.txtApellidos.text().strip()
        id_tipo_usuario = self.cmbTipoUsuario.currentData()
        if not nombre_usuario or not nombres or not apellidos:
            QMessageBox.warning(self, "Usuarios", "Escriba el usuario, los nombres y los apellidos.")
            return None
        if id_tipo_usuario is None:
            QMessageBox.warning(self, "Usuarios", "No hay roles registrados.")
            return None
        return Usuario(None, nombre_usuario, "", nombres, apellidos, self.chkEstado.isChecked(), id_tipo_usuario)

    # Ejecuta la operación del service y refresca la tabla. El permiso lo revisa el service.
    def _ejecutar(self, operacion, *datos):
        try:
            operacion(*datos)
        except (ValueError, PermissionError, ConnectionError) as error:
            QMessageBox.warning(self, "Usuarios", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
