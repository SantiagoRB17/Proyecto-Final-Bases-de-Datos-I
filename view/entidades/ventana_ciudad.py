from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.CiudadDAO import CiudadDAO
from model.Ciudad import Ciudad
from service.UsuarioService import UsuarioService
from view.entidades.ui_ventana_ciudad import Ui_VentanaCiudad


class VentanaCiudad(QDialog, Ui_VentanaCiudad):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.ciudad_dao = CiudadDAO()
        self.usuario_service = UsuarioService()
        self.id_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblCiudades.itemSelectionChanged.connect(self.seleccionar_fila)

        puede_modificar = self.usuario_service.puede_modificar(sesion)
        self.btnAgregar.setEnabled(puede_modificar)
        self.btnEditar.setEnabled(puede_modificar)
        self.btnEliminar.setEnabled(puede_modificar)

        self.cargar_tabla()

    def cargar_tabla(self):
        try:
            ciudades = self.ciudad_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Ciudades", str(error))
            return

        self.tblCiudades.setRowCount(len(ciudades))
        for fila, ciudad in enumerate(ciudades):
            self.tblCiudades.setItem(fila, 0, QTableWidgetItem(str(ciudad.IDCiudad)))
            self.tblCiudades.setItem(fila, 1, QTableWidgetItem(ciudad.CiuNombre))
            self.tblCiudades.setItem(fila, 2, QTableWidgetItem(ciudad.CiuDepartamento))

    def seleccionar_fila(self):
        filas = self.tblCiudades.selectionModel().selectedRows()
        if not filas:
            self.id_seleccionado = None
            return
        fila = filas[0].row()
        self.id_seleccionado = int(self.tblCiudades.item(fila, 0).text())
        self.txtNombre.setText(self.tblCiudades.item(fila, 1).text())
        self.txtDepartamento.setText(self.tblCiudades.item(fila, 2).text())

    def limpiar_formulario(self):
        self.tblCiudades.clearSelection()
        self.id_seleccionado = None
        self.txtNombre.clear()
        self.txtDepartamento.clear()
        self.txtNombre.setFocus()

    def agregar(self):
        if self.id_seleccionado is not None:
            QMessageBox.warning(self, "Ciudades",
                                "Presione Nuevo para registrar otra ciudad, o Editar para guardar los cambios.")
            return
        ciudad = self._leer_formulario()
        if ciudad is None:
            return
        self._ejecutar(self.ciudad_dao.agregar, ciudad)

    def editar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Ciudades", "Seleccione la ciudad que desea editar.")
            return
        ciudad = self._leer_formulario()
        if ciudad is None:
            return
        ciudad.IDCiudad = self.id_seleccionado
        self._ejecutar(self.ciudad_dao.editar, ciudad)

    def eliminar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Ciudades", "Seleccione la ciudad que desea eliminar.")
            return
        respuesta = QMessageBox.question(self, "Ciudades", "¿Desea eliminar la ciudad seleccionada?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self.ciudad_dao.eliminar, self.id_seleccionado)

    def _leer_formulario(self):
        nombre = self.txtNombre.text().strip()
        departamento = self.txtDepartamento.text().strip()
        if not nombre or not departamento:
            QMessageBox.warning(self, "Ciudades", "Escriba el nombre y el departamento.")
            return None
        return Ciudad(None, nombre, departamento)

    # Revisa el permiso, ejecuta la operación del DAO y refresca la tabla.
    def _ejecutar(self, operacion, dato):
        if not self.usuario_service.puede_modificar(self.sesion):
            QMessageBox.warning(self, "Ciudades", "No tiene permisos para modificar ciudades.")
            return
        try:
            operacion(dato)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Ciudades", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
