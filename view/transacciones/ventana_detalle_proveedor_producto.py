from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.DetalleProveedorProductoDAO import DetalleProveedorProductoDAO
from dao.ProductoDAO import ProductoDAO
from dao.ProveedorDAO import ProveedorDAO
from model.DetalleProveedorProducto import DetalleProveedorProducto
from service.UsuarioService import UsuarioService
from view.tema import ajustar_tabla
from view.transacciones.ui_ventana_detalle_proveedor_producto import Ui_VentanaDetalleProveedorProducto


class VentanaDetalleProveedorProducto(QDialog, Ui_VentanaDetalleProveedorProducto):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.detalle_dao = DetalleProveedorProductoDAO()
        self.proveedor_dao = ProveedorDAO()
        self.producto_dao = ProductoDAO()
        self.usuario_service = UsuarioService()
        self.detalles = []
        self.detalle_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblDetalles.itemSelectionChanged.connect(self.seleccionar_fila)

        puede_modificar = self.usuario_service.puede_modificar(sesion)
        self.btnAgregar.setEnabled(puede_modificar)
        self.btnEditar.setEnabled(puede_modificar)
        self.btnEliminar.setEnabled(puede_modificar)

        self.dteFecha.setDate(QDate.currentDate())
        self.cargar_combos()
        self.cargar_tabla()

    def cargar_combos(self):
        try:
            proveedores = self.proveedor_dao.consultar_todos()
            productos = self.producto_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Proveedor - Producto", str(error))
            return
        for proveedor in proveedores:
            self.cmbProveedor.addItem(proveedor.ProvNombre, proveedor.IDProveedor)
        for producto in productos:
            self.cmbProducto.addItem(producto.ProdNombre, producto.IDProducto)

    def cargar_tabla(self):
        try:
            self.detalles = self.detalle_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Proveedor - Producto", str(error))
            return

        self.tblDetalles.setRowCount(len(self.detalles))
        for fila, detalle in enumerate(self.detalles):
            proveedor = self.cmbProveedor.itemText(self.cmbProveedor.findData(detalle.IDProveedor))
            producto = self.cmbProducto.itemText(self.cmbProducto.findData(detalle.IDProducto))
            self.tblDetalles.setItem(fila, 0, QTableWidgetItem(proveedor))
            self.tblDetalles.setItem(fila, 1, QTableWidgetItem(producto))
            self.tblDetalles.setItem(fila, 2, QTableWidgetItem(detalle.DeFechaRegistro.strftime("%d/%m/%Y")))
            self.tblDetalles.setItem(fila, 3, QTableWidgetItem(str(detalle.DePrecioProveedor)))
        ajustar_tabla(self.tblDetalles)

    def seleccionar_fila(self):
        filas = self.tblDetalles.selectionModel().selectedRows()
        if not filas:
            self.detalle_seleccionado = None
            self._bloquear_llave(False)
            return
        detalle = self.detalles[filas[0].row()]
        self.detalle_seleccionado = detalle
        self.cmbProveedor.setCurrentIndex(self.cmbProveedor.findData(detalle.IDProveedor))
        self.cmbProducto.setCurrentIndex(self.cmbProducto.findData(detalle.IDProducto))
        self.dteFecha.setDate(detalle.DeFechaRegistro)
        self.spnPrecio.setValue(float(detalle.DePrecioProveedor))
        self._bloquear_llave(True)

    def limpiar_formulario(self):
        self.tblDetalles.clearSelection()
        self.detalle_seleccionado = None
        self._bloquear_llave(False)
        self.cmbProveedor.setCurrentIndex(0)
        self.cmbProducto.setCurrentIndex(0)
        self.dteFecha.setDate(QDate.currentDate())
        self.spnPrecio.setValue(0)

    def agregar(self):
        if self.detalle_seleccionado is not None:
            QMessageBox.warning(self, "Proveedor - Producto",
                                "Presione Nuevo para registrar otra relación, o Editar para guardar los cambios.")
            return
        detalle = self._leer_formulario()
        if detalle is None:
            return
        self._ejecutar(self.detalle_dao.agregar, detalle)

    def editar(self):
        if self.detalle_seleccionado is None:
            QMessageBox.warning(self, "Proveedor - Producto", "Seleccione la relación que desea editar.")
            return
        detalle = self._leer_formulario()
        if detalle is None:
            return
        self._ejecutar(self.detalle_dao.editar, detalle)

    def eliminar(self):
        if self.detalle_seleccionado is None:
            QMessageBox.warning(self, "Proveedor - Producto", "Seleccione la relación que desea eliminar.")
            return
        respuesta = QMessageBox.question(self, "Proveedor - Producto", "¿Desea eliminar la relación seleccionada?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self._eliminar_seleccionado, None)

    def _eliminar_seleccionado(self, _):
        # La llave es compuesta: se elimina con los dos IDs.
        self.detalle_dao.eliminar(self.detalle_seleccionado.IDProveedor, self.detalle_seleccionado.IDProducto)

    # Proveedor y producto forman la llave primaria: una relación ya registrada
    # no los cambia, solo su fecha y su precio.
    def _bloquear_llave(self, bloquear):
        self.cmbProveedor.setEnabled(not bloquear)
        self.cmbProducto.setEnabled(not bloquear)

    def _leer_formulario(self):
        id_proveedor = self.cmbProveedor.currentData()
        id_producto = self.cmbProducto.currentData()
        if id_proveedor is None or id_producto is None:
            QMessageBox.warning(self, "Proveedor - Producto", "Primero debe registrar proveedores y productos.")
            return None
        if self.spnPrecio.value() <= 0:
            QMessageBox.warning(self, "Proveedor - Producto", "El precio debe ser mayor que cero.")
            return None
        return DetalleProveedorProducto(id_proveedor, id_producto, self.dteFecha.date().toPython(),
                                        self.spnPrecio.value())

    # Revisa el permiso, ejecuta la operación del DAO y refresca la tabla.
    def _ejecutar(self, operacion, dato):
        if not self.usuario_service.puede_modificar(self.sesion):
            QMessageBox.warning(self, "Proveedor - Producto", "No tiene permisos para modificar esta información.")
            return
        try:
            operacion(dato)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Proveedor - Producto", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
