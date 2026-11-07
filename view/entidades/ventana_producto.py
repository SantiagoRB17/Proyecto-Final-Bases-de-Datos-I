from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.CategoriaDAO import CategoriaDAO
from dao.ProductoDAO import ProductoDAO
from model.Producto import Producto
from service.UsuarioService import UsuarioService
from view.entidades.ui_ventana_producto import Ui_VentanaProducto
from view.tema import ajustar_tabla


class VentanaProducto(QDialog, Ui_VentanaProducto):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.producto_dao = ProductoDAO()
        self.categoria_dao = CategoriaDAO()
        self.usuario_service = UsuarioService()
        self.productos = []
        self.id_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblProductos.itemSelectionChanged.connect(self.seleccionar_fila)

        puede_modificar = self.usuario_service.puede_modificar(sesion)
        self.btnAgregar.setEnabled(puede_modificar)
        self.btnEditar.setEnabled(puede_modificar)
        self.btnEliminar.setEnabled(puede_modificar)

        self.cargar_categorias()
        self.cargar_tabla()

    def cargar_categorias(self):
        try:
            categorias = self.categoria_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Productos", str(error))
            return
        # Cada opción del combo muestra el nombre y guarda el ID de la categoría.
        for categoria in categorias:
            self.cmbCategoria.addItem(categoria.CatNombre, categoria.IDCategoria)

    def cargar_tabla(self):
        try:
            self.productos = self.producto_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Productos", str(error))
            return

        self.tblProductos.setRowCount(len(self.productos))
        for fila, producto in enumerate(self.productos):
            indice = self.cmbCategoria.findData(producto.IDCategoria)
            self.tblProductos.setItem(fila, 0, QTableWidgetItem(str(producto.IDProducto)))
            self.tblProductos.setItem(fila, 1, QTableWidgetItem(producto.ProdNombre))
            self.tblProductos.setItem(fila, 2, QTableWidgetItem(producto.ProdDescripcion or ""))
            self.tblProductos.setItem(fila, 3, QTableWidgetItem(str(producto.ProdPrecio)))
            self.tblProductos.setItem(fila, 4, QTableWidgetItem(str(producto.ProdStock)))
            self.tblProductos.setItem(fila, 5, QTableWidgetItem(self.cmbCategoria.itemText(indice)))
        ajustar_tabla(self.tblProductos)

    def seleccionar_fila(self):
        filas = self.tblProductos.selectionModel().selectedRows()
        if not filas:
            self.id_seleccionado = None
            return
        producto = self.productos[filas[0].row()]
        self.id_seleccionado = producto.IDProducto
        self.txtNombre.setText(producto.ProdNombre)
        self.txtDescripcion.setText(producto.ProdDescripcion or "")
        self.spnPrecio.setValue(float(producto.ProdPrecio))
        self.spnStock.setValue(producto.ProdStock)
        self.cmbCategoria.setCurrentIndex(self.cmbCategoria.findData(producto.IDCategoria))

    def limpiar_formulario(self):
        self.tblProductos.clearSelection()
        self.id_seleccionado = None
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.spnPrecio.setValue(0)
        self.spnStock.setValue(0)
        self.cmbCategoria.setCurrentIndex(0)
        self.txtNombre.setFocus()

    def agregar(self):
        if self.id_seleccionado is not None:
            QMessageBox.warning(self, "Productos",
                                "Presione Nuevo para registrar otro producto, o Editar para guardar los cambios.")
            return
        producto = self._leer_formulario()
        if producto is None:
            return
        self._ejecutar(self.producto_dao.agregar, producto)

    def editar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Productos", "Seleccione el producto que desea editar.")
            return
        producto = self._leer_formulario()
        if producto is None:
            return
        producto.IDProducto = self.id_seleccionado
        self._ejecutar(self.producto_dao.editar, producto)

    def eliminar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Productos", "Seleccione el producto que desea eliminar.")
            return
        respuesta = QMessageBox.question(self, "Productos", "¿Desea eliminar el producto seleccionado?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self.producto_dao.eliminar, self.id_seleccionado)

    def _leer_formulario(self):
        nombre = self.txtNombre.text().strip()
        # La descripción es opcional: vacía se guarda como NULL.
        descripcion = self.txtDescripcion.text().strip() or None
        id_categoria = self.cmbCategoria.currentData()
        if not nombre:
            QMessageBox.warning(self, "Productos", "Escriba el nombre del producto.")
            return None
        if self.spnPrecio.value() <= 0:
            QMessageBox.warning(self, "Productos", "El precio debe ser mayor que cero.")
            return None
        if id_categoria is None:
            QMessageBox.warning(self, "Productos", "Primero debe registrar una categoría.")
            return None
        return Producto(None, nombre, descripcion, self.spnPrecio.value(), self.spnStock.value(), id_categoria)

    # Revisa el permiso, ejecuta la operación del DAO y refresca la tabla.
    def _ejecutar(self, operacion, dato):
        if not self.usuario_service.puede_modificar(self.sesion):
            QMessageBox.warning(self, "Productos", "No tiene permisos para modificar productos.")
            return
        try:
            operacion(dato)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Productos", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
