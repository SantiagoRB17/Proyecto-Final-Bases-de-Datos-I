from datetime import date, time

from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from dao.ConsultasDAO import ConsultasDAO
from service.UsuarioService import UsuarioService
from view.consultas_reportes.ui_ventana_consultas import Ui_VentanaConsultas


class VentanaConsultas(QDialog, Ui_VentanaConsultas):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.consultas_dao = ConsultasDAO()
        self.usuario_service = UsuarioService()

        # Cada opción del combo guarda el método del DAO que debe ejecutar.
        self.cmbConsulta.addItem("Proveedores con su ciudad y productos (JOIN)",
                                 self.consultas_dao.proveedores_con_ciudad_y_productos)
        self.cmbConsulta.addItem("Productos con su categoría y proveedores (JOIN)",
                                 self.consultas_dao.productos_con_categoria_y_proveedores)
        # La bitácora es información de auditoría: solo la ve el Administrador.
        if self.usuario_service.es_administrador(sesion.usuario.IDUsuario):
            self.cmbConsulta.addItem("Bitácora con usuario y rol (JOIN)",
                                     self.consultas_dao.bitacora_con_usuario_y_rol)
        self.cmbConsulta.addItem("Proveedores sin productos (subconsulta)",
                                 self.consultas_dao.proveedores_sin_productos)
        self.cmbConsulta.addItem("Categorías con su cantidad de productos (subconsulta)",
                                 self.consultas_dao.categorias_con_cantidad_de_productos)

        self.cmbConsulta.currentIndexChanged.connect(self.ejecutar_consulta)
        self.btnCerrar.clicked.connect(self.close)
        self.ejecutar_consulta()

    def ejecutar_consulta(self):
        consulta = self.cmbConsulta.currentData()
        try:
            encabezados, filas = consulta()
        except ConnectionError as error:
            QMessageBox.warning(self, "Consultas", str(error))
            return

        self.tblResultados.setColumnCount(len(encabezados))
        self.tblResultados.setHorizontalHeaderLabels(encabezados)
        self.tblResultados.setRowCount(len(filas))
        for numero_fila, fila in enumerate(filas):
            for numero_columna, valor in enumerate(fila):
                self.tblResultados.setItem(numero_fila, numero_columna, QTableWidgetItem(self._a_texto(valor)))
        self.lblResultados.setText(f"Resultados: {len(filas)}")

    def _a_texto(self, valor):
        if valor is None:
            return ""
        if isinstance(valor, date):
            return valor.strftime("%d/%m/%Y")
        if isinstance(valor, time):
            return valor.strftime("%H:%M:%S")
        return str(valor)
