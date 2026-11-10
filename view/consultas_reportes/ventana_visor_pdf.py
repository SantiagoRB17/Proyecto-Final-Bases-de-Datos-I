import os
import shutil

from PySide6.QtCore import QBuffer, QByteArray, QIODevice
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from view.consultas_reportes.ui_ventana_visor_pdf import Ui_VentanaVisorPdf


# Visor de PDF dentro de la aplicación (QPdfView, incluido en PySide6).
# El PDF se lee a memoria: así el archivo no queda bloqueado en Windows y, si
# viene de una carpeta temporal ("Ver PDF"), esa carpeta se borra de inmediato.
class VentanaVisorPdf(QDialog, Ui_VentanaVisorPdf):
    FACTOR_ZOOM = 1.25

    def __init__(self, ruta_pdf, titulo, carpeta_temporal=None):
        super().__init__()
        self.setupUi(self)
        self.nombre_pdf = os.path.basename(ruta_pdf)
        self.factor = 1.0
        self.lblEncabezado.setText(titulo)

        try:
            with open(ruta_pdf, "rb") as archivo:
                self.contenido = QByteArray(archivo.read())
        except OSError:
            self.contenido = None
        finally:
            if carpeta_temporal:
                shutil.rmtree(carpeta_temporal, ignore_errors=True)

        self.documento = QPdfDocument(self)
        self.buffer = QBuffer(self)
        if self.contenido is None:
            raise ValueError("No se pudo abrir el archivo PDF.")
        self.buffer.setData(self.contenido)
        self.buffer.open(QIODevice.OpenModeFlag.ReadOnly)
        # load(QIODevice) no devuelve el resultado: se revisa el estado del documento.
        self.documento.load(self.buffer)
        if self.documento.status() != QPdfDocument.Status.Ready:
            raise ValueError("No se pudo abrir el archivo PDF.")

        self.visor = QPdfView(self)
        self.visor.setDocument(self.documento)
        self.visor.setPageMode(QPdfView.PageMode.MultiPage)
        self.visor.setZoomMode(QPdfView.ZoomMode.FitToWidth)
        self.layoutContenedorPdf.addWidget(self.visor)

        self.btnAcercar.clicked.connect(lambda: self.cambiar_zoom(self.FACTOR_ZOOM))
        self.btnAlejar.clicked.connect(lambda: self.cambiar_zoom(1 / self.FACTOR_ZOOM))
        self.btnAjustar.clicked.connect(self.ajustar_al_ancho)
        self.btnExportar.clicked.connect(self.guardar_como)
        self.btnCerrar.clicked.connect(self.close)
        self.visor.pageNavigator().currentPageChanged.connect(self.mostrar_pagina)
        self.mostrar_pagina(0)

    def cambiar_zoom(self, multiplicador):
        self.factor = min(max(self.factor * multiplicador, 0.25), 4.0)
        self.visor.setZoomMode(QPdfView.ZoomMode.Custom)
        self.visor.setZoomFactor(self.factor)

    def ajustar_al_ancho(self):
        self.factor = 1.0
        self.visor.setZoomMode(QPdfView.ZoomMode.FitToWidth)

    def mostrar_pagina(self, pagina):
        self.lblPagina.setText(f"Página {pagina + 1} de {self.documento.pageCount()}")

    def guardar_como(self):
        destino, _ = QFileDialog.getSaveFileName(self, "Guardar reporte", self.nombre_pdf, "Archivos PDF (*.pdf)")
        if not destino:
            return
        try:
            with open(destino, "wb") as archivo:
                archivo.write(self.contenido.data())
        except OSError as error:
            QMessageBox.warning(self, "Reportes", f"No se pudo guardar el PDF.\n{error}")
            return
        QMessageBox.information(self, "Reportes", "El reporte se guardó correctamente.")
