from datetime import date, time

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QTableWidgetItem

from dao.CategoriaDAO import CategoriaDAO
from dao.CiudadDAO import CiudadDAO
from dao.ProductoDAO import ProductoDAO
from dao.ProveedorDAO import ProveedorDAO
from dao.ReportesDAO import ReportesDAO
from service.ReportePdfService import ReportePdfService
from view.consultas_reportes.ui_ventana_reportes import Ui_VentanaReportes


class VentanaReportes(QDialog, Ui_VentanaReportes):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.sesion = sesion
        self.reportes_dao = ReportesDAO()
        self.pdf_service = ReportePdfService()
        self.encabezados = []
        self.filas = []
        self.filtros = []

        # Cada reporte guarda qué filtros necesita (los demás se ocultan).
        self.cmbReporte.addItem("Productos de un proveedor", ("proveedor",))
        self.cmbReporte.addItem("Proveedores de una ciudad", ("ciudad",))
        self.cmbReporte.addItem("Proveedores de un producto por rango de precio",
                                ("producto", "precio_minimo", "precio_maximo"))
        self.cmbReporte.addItem("Productos de una categoría", ("categoria",))
        self.cmbReporte.addItem("Productos con stock bajo por categoría", ("categoria", "stock_maximo"))

        # Cada filtro es una pareja (etiqueta, campo) que se muestra u oculta junta.
        self.campos_filtro = {
            "proveedor": (self.lblProveedor, self.cmbProveedor),
            "ciudad": (self.lblCiudad, self.cmbCiudad),
            "producto": (self.lblProducto, self.cmbProducto),
            "categoria": (self.lblCategoria, self.cmbCategoria),
            "precio_minimo": (self.lblPrecioMinimo, self.spnPrecioMinimo),
            "precio_maximo": (self.lblPrecioMaximo, self.spnPrecioMaximo),
            "stock_maximo": (self.lblStockMaximo, self.spnStockMaximo),
        }

        self.cmbReporte.currentIndexChanged.connect(self.mostrar_filtros)
        self.btnGenerar.clicked.connect(self.generar)
        self.btnExportar.clicked.connect(self.exportar_pdf)
        self.btnCerrar.clicked.connect(self.close)
        self.btnExportar.setEnabled(False)

        self.cargar_combos()
        self.mostrar_filtros()

    def cargar_combos(self):
        try:
            for proveedor in ProveedorDAO().consultar_todos():
                self.cmbProveedor.addItem(proveedor.ProvNombre, proveedor.IDProveedor)
            for ciudad in CiudadDAO().consultar_todos():
                self.cmbCiudad.addItem(f"{ciudad.CiuNombre} ({ciudad.CiuDepartamento})", ciudad.IDCiudad)
            for producto in ProductoDAO().consultar_todos():
                self.cmbProducto.addItem(producto.ProdNombre, producto.IDProducto)
            for categoria in CategoriaDAO().consultar_todos():
                self.cmbCategoria.addItem(categoria.CatNombre, categoria.IDCategoria)
        except ConnectionError as error:
            QMessageBox.warning(self, "Reportes", str(error))

    def mostrar_filtros(self):
        necesarios = self.cmbReporte.currentData()
        # setRowVisible oculta la fila completa (etiqueta y campo) sin dejar un hueco.
        for nombre, (etiqueta, campo) in self.campos_filtro.items():
            self.layoutFormulario.setRowVisible(campo, nombre in necesarios)
        self._limpiar_resultados()

    def generar(self):
        reporte = self.cmbReporte.currentIndex()
        necesarios = self.cmbReporte.currentData()
        for nombre in necesarios:
            campo = self.campos_filtro[nombre][1]
            if hasattr(campo, "currentData") and campo.currentData() is None:
                QMessageBox.warning(self, "Reportes", "No hay datos registrados para ese filtro.")
                return
        if "precio_minimo" in necesarios and self.spnPrecioMinimo.value() > self.spnPrecioMaximo.value():
            QMessageBox.warning(self, "Reportes", "El precio mínimo no puede ser mayor que el máximo.")
            return

        try:
            if reporte == 0:
                datos = self.reportes_dao.productos_de_proveedor(self.cmbProveedor.currentData())
                self.filtros = [f"Proveedor: {self.cmbProveedor.currentText()}"]
            elif reporte == 1:
                datos = self.reportes_dao.proveedores_por_ciudad(self.cmbCiudad.currentData())
                self.filtros = [f"Ciudad: {self.cmbCiudad.currentText()}"]
            elif reporte == 2:
                datos = self.reportes_dao.proveedores_de_producto_por_precio(
                    self.cmbProducto.currentData(), self.spnPrecioMinimo.value(), self.spnPrecioMaximo.value())
                self.filtros = [f"Producto: {self.cmbProducto.currentText()}",
                                f"Precio entre {self.spnPrecioMinimo.value():.2f} y {self.spnPrecioMaximo.value():.2f}"]
            elif reporte == 3:
                datos = self.reportes_dao.productos_de_categoria(self.cmbCategoria.currentData())
                self.filtros = [f"Categoría: {self.cmbCategoria.currentText()}"]
            else:
                datos = self.reportes_dao.productos_con_stock_bajo(
                    self.cmbCategoria.currentData(), self.spnStockMaximo.value())
                self.filtros = [f"Categoría: {self.cmbCategoria.currentText()}",
                                f"Stock máximo: {self.spnStockMaximo.value()}"]
        except ConnectionError as error:
            QMessageBox.warning(self, "Reportes", str(error))
            return

        encabezados, filas = datos
        self.encabezados = encabezados
        self.filas = [[self._a_texto(valor) for valor in fila] for fila in filas]
        self._mostrar_tabla()

    def exportar_pdf(self):
        titulo = self.cmbReporte.currentText()
        nombre_sugerido = titulo.replace(" ", "_") + ".pdf"
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar reporte", nombre_sugerido, "Archivos PDF (*.pdf)")
        if not ruta:
            return
        try:
            self.pdf_service.exportar(ruta, titulo, self.filtros, self.encabezados, self.filas, self.sesion.usuario)
        except OSError as error:
            QMessageBox.warning(self, "Reportes", f"No se pudo guardar el PDF.\n{error}")
            return
        QMessageBox.information(self, "Reportes", "El reporte se guardó correctamente.")

    def _mostrar_tabla(self):
        self.tblResultados.setColumnCount(len(self.encabezados))
        self.tblResultados.setHorizontalHeaderLabels(self.encabezados)
        self.tblResultados.setRowCount(len(self.filas))
        for numero_fila, fila in enumerate(self.filas):
            for numero_columna, texto in enumerate(fila):
                self.tblResultados.setItem(numero_fila, numero_columna, QTableWidgetItem(texto))
        self.lblResultados.setText(f"Resultados: {len(self.filas)}")
        self.btnExportar.setEnabled(True)

    # Al cambiar de reporte se borra el anterior, para no exportar uno distinto al elegido.
    def _limpiar_resultados(self):
        self.encabezados = []
        self.filas = []
        self.filtros = []
        self.tblResultados.setRowCount(0)
        self.tblResultados.setColumnCount(0)
        self.lblResultados.setText("")
        self.btnExportar.setEnabled(False)

    def _a_texto(self, valor):
        if valor is None:
            return ""
        if isinstance(valor, date):
            return valor.strftime("%d/%m/%Y")
        if isinstance(valor, time):
            return valor.strftime("%H:%M:%S")
        return str(valor)
