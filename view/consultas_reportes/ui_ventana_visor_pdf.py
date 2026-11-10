# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_visor_pdf.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_VentanaVisorPdf(object):
    def setupUi(self, VentanaVisorPdf):
        if not VentanaVisorPdf.objectName():
            VentanaVisorPdf.setObjectName(u"VentanaVisorPdf")
        VentanaVisorPdf.resize(980, 740)
        self.layoutPrincipal = QVBoxLayout(VentanaVisorPdf)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaVisorPdf)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutHerramientas = QHBoxLayout()
        self.layoutHerramientas.setObjectName(u"layoutHerramientas")
        self.btnAlejar = QPushButton(VentanaVisorPdf)
        self.btnAlejar.setObjectName(u"btnAlejar")
        self.btnAlejar.setAutoDefault(False)

        self.layoutHerramientas.addWidget(self.btnAlejar)

        self.btnAcercar = QPushButton(VentanaVisorPdf)
        self.btnAcercar.setObjectName(u"btnAcercar")
        self.btnAcercar.setAutoDefault(False)

        self.layoutHerramientas.addWidget(self.btnAcercar)

        self.btnAjustar = QPushButton(VentanaVisorPdf)
        self.btnAjustar.setObjectName(u"btnAjustar")
        self.btnAjustar.setAutoDefault(False)

        self.layoutHerramientas.addWidget(self.btnAjustar)

        self.lblPagina = QLabel(VentanaVisorPdf)
        self.lblPagina.setObjectName(u"lblPagina")

        self.layoutHerramientas.addWidget(self.lblPagina)

        self.espaciadorHerramientas = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutHerramientas.addItem(self.espaciadorHerramientas)

        self.btnExportar = QPushButton(VentanaVisorPdf)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setAutoDefault(False)

        self.layoutHerramientas.addWidget(self.btnExportar)

        self.btnCerrar = QPushButton(VentanaVisorPdf)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutHerramientas.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutHerramientas)

        self.contenedorPdf = QFrame(VentanaVisorPdf)
        self.contenedorPdf.setObjectName(u"contenedorPdf")
        self.layoutContenedorPdf = QVBoxLayout(self.contenedorPdf)
        self.layoutContenedorPdf.setSpacing(0)
        self.layoutContenedorPdf.setObjectName(u"layoutContenedorPdf")
        self.layoutContenedorPdf.setContentsMargins(1, 1, 1, 1)

        self.layoutPrincipal.addWidget(self.contenedorPdf)


        self.retranslateUi(VentanaVisorPdf)

        QMetaObject.connectSlotsByName(VentanaVisorPdf)
    # setupUi

    def retranslateUi(self, VentanaVisorPdf):
        VentanaVisorPdf.setWindowTitle(QCoreApplication.translate("VentanaVisorPdf", u"Vista previa del reporte", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaVisorPdf", u"Vista previa del reporte", None))
        self.btnAlejar.setText(QCoreApplication.translate("VentanaVisorPdf", u"Alejar", None))
        self.btnAcercar.setText(QCoreApplication.translate("VentanaVisorPdf", u"Acercar", None))
        self.btnAjustar.setText(QCoreApplication.translate("VentanaVisorPdf", u"Ajustar al ancho", None))
        self.lblPagina.setText("")
        self.btnExportar.setText(QCoreApplication.translate("VentanaVisorPdf", u"Guardar como...", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaVisorPdf", u"Cerrar", None))
    # retranslateUi

