# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_consultas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFormLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_VentanaConsultas(object):
    def setupUi(self, VentanaConsultas):
        if not VentanaConsultas.objectName():
            VentanaConsultas.setObjectName(u"VentanaConsultas")
        VentanaConsultas.resize(1060, 560)
        self.layoutPrincipal = QVBoxLayout(VentanaConsultas)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaConsultas)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setHorizontalSpacing(14)
        self.layoutFormulario.setVerticalSpacing(10)
        self.lblConsulta = QLabel(VentanaConsultas)
        self.lblConsulta.setObjectName(u"lblConsulta")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblConsulta)

        self.cmbConsulta = QComboBox(VentanaConsultas)
        self.cmbConsulta.setObjectName(u"cmbConsulta")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbConsulta)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.lblResultados = QLabel(VentanaConsultas)
        self.lblResultados.setObjectName(u"lblResultados")

        self.layoutPrincipal.addWidget(self.lblResultados)

        self.tblResultados = QTableWidget(VentanaConsultas)
        self.tblResultados.setObjectName(u"tblResultados")
        self.tblResultados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblResultados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblResultados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblResultados.setAlternatingRowColors(True)
        self.tblResultados.setShowGrid(False)
        self.tblResultados.horizontalHeader().setDefaultSectionSize(150)
        self.tblResultados.horizontalHeader().setStretchLastSection(True)
        self.tblResultados.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblResultados)

        self.btnCerrar = QPushButton(VentanaConsultas)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutPrincipal.addWidget(self.btnCerrar)


        self.retranslateUi(VentanaConsultas)

        QMetaObject.connectSlotsByName(VentanaConsultas)
    # setupUi

    def retranslateUi(self, VentanaConsultas):
        VentanaConsultas.setWindowTitle(QCoreApplication.translate("VentanaConsultas", u"Consultas", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaConsultas", u"Consultas", None))
        self.lblConsulta.setText(QCoreApplication.translate("VentanaConsultas", u"Consulta:", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaConsultas", u"Cerrar", None))
    # retranslateUi

