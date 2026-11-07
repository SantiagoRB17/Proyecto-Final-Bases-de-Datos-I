from datetime import date, time

from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from service.UsuarioService import UsuarioService
from view.auditoria.ui_ventana_bitacora import Ui_VentanaBitacora
from view.tema import ajustar_tabla


# Solo lectura: la bitácora la escribe el sistema al entrar y salir, nadie la edita.
class VentanaBitacora(QDialog, Ui_VentanaBitacora):
    def __init__(self, sesion):
        super().__init__()
        self.setupUi(self)
        self.usuario_actual = sesion.usuario
        self.usuario_service = UsuarioService()

        self.btnActualizar.clicked.connect(self.cargar_tabla)
        self.btnCerrar.clicked.connect(self.close)
        self.cargar_tabla()

    def cargar_tabla(self):
        try:
            encabezados, filas = self.usuario_service.consultar_bitacora(self.usuario_actual)
        except (PermissionError, ConnectionError) as error:
            QMessageBox.warning(self, "Bitácora", str(error))
            return

        self.tblBitacora.setColumnCount(len(encabezados))
        self.tblBitacora.setHorizontalHeaderLabels(encabezados)
        self.tblBitacora.setRowCount(len(filas))
        for numero_fila, fila in enumerate(filas):
            for numero_columna, valor in enumerate(fila):
                self.tblBitacora.setItem(numero_fila, numero_columna, QTableWidgetItem(self._a_texto(valor)))
        ajustar_tabla(self.tblBitacora)
        self.lblResultados.setText(f"Registros: {len(filas)}")

    def _a_texto(self, valor):
        # Una fecha u hora de salida vacía significa que la sesión sigue abierta.
        if valor is None:
            return ""
        if isinstance(valor, date):
            return valor.strftime("%d/%m/%Y")
        if isinstance(valor, time):
            return valor.strftime("%H:%M:%S")
        return str(valor)
