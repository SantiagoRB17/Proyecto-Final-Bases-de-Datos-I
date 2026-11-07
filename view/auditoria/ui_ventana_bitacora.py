# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_bitacora.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaBitacora(object):
    def setupUi(self, VentanaBitacora):
        if not VentanaBitacora.objectName():
            VentanaBitacora.setObjectName(u"VentanaBitacora")
        VentanaBitacora.resize(1060, 580)
        self.layoutPrincipal = QVBoxLayout(VentanaBitacora)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaBitacora)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.lblResultados = QLabel(VentanaBitacora)
        self.lblResultados.setObjectName(u"lblResultados")

        self.layoutPrincipal.addWidget(self.lblResultados)

        self.tblBitacora = QTableWidget(VentanaBitacora)
        self.tblBitacora.setObjectName(u"tblBitacora")
        self.tblBitacora.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblBitacora.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblBitacora.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblBitacora.setAlternatingRowColors(True)
        self.tblBitacora.setShowGrid(False)
        self.tblBitacora.horizontalHeader().setDefaultSectionSize(150)
        self.tblBitacora.horizontalHeader().setStretchLastSection(True)
        self.tblBitacora.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblBitacora)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnActualizar = QPushButton(VentanaBitacora)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnActualizar)

        self.btnCerrar = QPushButton(VentanaBitacora)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)


        self.retranslateUi(VentanaBitacora)

        QMetaObject.connectSlotsByName(VentanaBitacora)
    # setupUi

    def retranslateUi(self, VentanaBitacora):
        VentanaBitacora.setWindowTitle(QCoreApplication.translate("VentanaBitacora", u"Bit\u00e1cora de entradas y salidas", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaBitacora", u"Bit\u00e1cora de entradas y salidas", None))
        self.btnActualizar.setText(QCoreApplication.translate("VentanaBitacora", u"Actualizar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaBitacora", u"Cerrar", None))
    # retranslateUi

