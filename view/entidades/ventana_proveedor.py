from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.CiudadDAO import CiudadDAO
from dao.ProveedorDAO import ProveedorDAO
from model.Proveedor import Proveedor
from service.UsuarioService import UsuarioService
from view.entidades.ui_ventana_proveedor import Ui_VentanaProveedor
from view.tema import ajustar_tabla


class VentanaProveedor(QDialog, Ui_VentanaProveedor):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.proveedor_dao = ProveedorDAO()
        self.ciudad_dao = CiudadDAO()
        self.usuario_service = UsuarioService()
        self.proveedores = []
        self.id_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblProveedores.itemSelectionChanged.connect(self.seleccionar_fila)

        puede_modificar = self.usuario_service.puede_modificar(sesion)
        self.btnAgregar.setEnabled(puede_modificar)
        self.btnEditar.setEnabled(puede_modificar)
        self.btnEliminar.setEnabled(puede_modificar)

        self.cargar_ciudades()
        self.cargar_tabla()

    def cargar_ciudades(self):
        try:
            ciudades = self.ciudad_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Proveedores", str(error))
            return
        # Cada opción del combo muestra la ciudad y guarda su ID.
        for ciudad in ciudades:
            self.cmbCiudad.addItem(f"{ciudad.CiuNombre} ({ciudad.CiuDepartamento})", ciudad.IDCiudad)

    def cargar_tabla(self):
        try:
            self.proveedores = self.proveedor_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Proveedores", str(error))
            return

        self.tblProveedores.setRowCount(len(self.proveedores))
        for fila, proveedor in enumerate(self.proveedores):
            indice = self.cmbCiudad.findData(proveedor.IDCiudad)
            self.tblProveedores.setItem(fila, 0, QTableWidgetItem(str(proveedor.IDProveedor)))
            self.tblProveedores.setItem(fila, 1, QTableWidgetItem(proveedor.ProvNit))
            self.tblProveedores.setItem(fila, 2, QTableWidgetItem(proveedor.ProvNombre))
            self.tblProveedores.setItem(fila, 3, QTableWidgetItem(proveedor.ProvDireccion))
            self.tblProveedores.setItem(fila, 4, QTableWidgetItem(proveedor.ProvTelefono))
            self.tblProveedores.setItem(fila, 5, QTableWidgetItem(proveedor.ProvEmail or ""))
            self.tblProveedores.setItem(fila, 6, QTableWidgetItem(self.cmbCiudad.itemText(indice)))
        ajustar_tabla(self.tblProveedores)

    def seleccionar_fila(self):
        filas = self.tblProveedores.selectionModel().selectedRows()
        if not filas:
            self.id_seleccionado = None
            return
        proveedor = self.proveedores[filas[0].row()]
        self.id_seleccionado = proveedor.IDProveedor
        self.txtNit.setText(proveedor.ProvNit)
        self.txtNombre.setText(proveedor.ProvNombre)
        self.txtDireccion.setText(proveedor.ProvDireccion)
        self.txtTelefono.setText(proveedor.ProvTelefono)
        self.txtEmail.setText(proveedor.ProvEmail or "")
        self.cmbCiudad.setCurrentIndex(self.cmbCiudad.findData(proveedor.IDCiudad))

    def limpiar_formulario(self):
        self.tblProveedores.clearSelection()
        self.id_seleccionado = None
        self.txtNit.clear()
        self.txtNombre.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()
        self.txtEmail.clear()
        self.cmbCiudad.setCurrentIndex(0)
        self.txtNit.setFocus()

    def agregar(self):
        if self.id_seleccionado is not None:
            QMessageBox.warning(self, "Proveedores",
                                "Presione Nuevo para registrar otro proveedor, o Editar para guardar los cambios.")
            return
        proveedor = self._leer_formulario()
        if proveedor is None:
            return
        self._ejecutar(self.proveedor_dao.agregar, proveedor)

    def editar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Proveedores", "Seleccione el proveedor que desea editar.")
            return
        proveedor = self._leer_formulario()
        if proveedor is None:
            return
        proveedor.IDProveedor = self.id_seleccionado
        self._ejecutar(self.proveedor_dao.editar, proveedor)

    def eliminar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Proveedores", "Seleccione el proveedor que desea eliminar.")
            return
        respuesta = QMessageBox.question(self, "Proveedores", "¿Desea eliminar el proveedor seleccionado?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self.proveedor_dao.eliminar, self.id_seleccionado)

    def _leer_formulario(self):
        nit = self.txtNit.text().strip()
        nombre = self.txtNombre.text().strip()
        direccion = self.txtDireccion.text().strip()
        telefono = self.txtTelefono.text().strip()
        # El email es opcional: vacío se guarda como NULL.
        email = self.txtEmail.text().strip() or None
        id_ciudad = self.cmbCiudad.currentData()
        if not nit or not nombre or not direccion or not telefono:
            QMessageBox.warning(self, "Proveedores", "Escriba el NIT, el nombre, la dirección y el teléfono.")
            return None
        if id_ciudad is None:
            QMessageBox.warning(self, "Proveedores", "Primero debe registrar una ciudad.")
            return None
        return Proveedor(None, nit, nombre, direccion, telefono, email, id_ciudad)

    # Revisa el permiso, ejecuta la operación del DAO y refresca la tabla.
    def _ejecutar(self, operacion, dato):
        if not self.usuario_service.puede_modificar(self.sesion):
            QMessageBox.warning(self, "Proveedores", "No tiene permisos para modificar proveedores.")
            return
        try:
            operacion(dato)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Proveedores", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
