from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.CategoriaDAO import CategoriaDAO
from model.Categoria import Categoria
from service.UsuarioService import UsuarioService
from view.entidades.ui_ventana_categoria import Ui_VentanaCategoria


class VentanaCategoria(QDialog, Ui_VentanaCategoria):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.categoria_dao = CategoriaDAO()
        self.usuario_service = UsuarioService()
        self.id_seleccionado = None

        self.btnNuevo.clicked.connect(self.limpiar_formulario)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCerrar.clicked.connect(self.close)
        self.tblCategorias.itemSelectionChanged.connect(self.seleccionar_fila)

        puede_modificar = self.usuario_service.puede_modificar(sesion)
        self.btnAgregar.setEnabled(puede_modificar)
        self.btnEditar.setEnabled(puede_modificar)
        self.btnEliminar.setEnabled(puede_modificar)

        self.cargar_tabla()

    def cargar_tabla(self):
        try:
            categorias = self.categoria_dao.consultar_todos()
        except ConnectionError as error:
            QMessageBox.warning(self, "Categorías", str(error))
            return

        self.tblCategorias.setRowCount(len(categorias))
        for fila, categoria in enumerate(categorias):
            self.tblCategorias.setItem(fila, 0, QTableWidgetItem(str(categoria.IDCategoria)))
            self.tblCategorias.setItem(fila, 1, QTableWidgetItem(categoria.CatNombre))
            self.tblCategorias.setItem(fila, 2, QTableWidgetItem(categoria.CatDescripcion or ""))

    def seleccionar_fila(self):
        filas = self.tblCategorias.selectionModel().selectedRows()
        if not filas:
            self.id_seleccionado = None
            return
        fila = filas[0].row()
        self.id_seleccionado = int(self.tblCategorias.item(fila, 0).text())
        self.txtNombre.setText(self.tblCategorias.item(fila, 1).text())
        self.txtDescripcion.setText(self.tblCategorias.item(fila, 2).text())

    def limpiar_formulario(self):
        self.tblCategorias.clearSelection()
        self.id_seleccionado = None
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtNombre.setFocus()

    def agregar(self):
        categoria = self._leer_formulario()
        if categoria is None:
            return
        self._ejecutar(self.categoria_dao.agregar, categoria)

    def editar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Categorías", "Seleccione la categoría que desea editar.")
            return
        categoria = self._leer_formulario()
        if categoria is None:
            return
        categoria.IDCategoria = self.id_seleccionado
        self._ejecutar(self.categoria_dao.editar, categoria)

    def eliminar(self):
        if self.id_seleccionado is None:
            QMessageBox.warning(self, "Categorías", "Seleccione la categoría que desea eliminar.")
            return
        respuesta = QMessageBox.question(self, "Categorías", "¿Desea eliminar la categoría seleccionada?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self._ejecutar(self.categoria_dao.eliminar, self.id_seleccionado)

    def _leer_formulario(self):
        nombre = self.txtNombre.text().strip()
        # La descripción es opcional: vacía se guarda como NULL.
        descripcion = self.txtDescripcion.text().strip() or None
        if not nombre:
            QMessageBox.warning(self, "Categorías", "Escriba el nombre de la categoría.")
            return None
        return Categoria(None, nombre, descripcion)

    # Revisa el permiso, ejecuta la operación del DAO y refresca la tabla.
    def _ejecutar(self, operacion, dato):
        if not self.usuario_service.puede_modificar(self.sesion):
            QMessageBox.warning(self, "Categorías", "No tiene permisos para modificar categorías.")
            return
        try:
            operacion(dato)
        except (ValueError, ConnectionError) as error:
            QMessageBox.warning(self, "Categorías", str(error))
            return
        self.limpiar_formulario()
        self.cargar_tabla()
