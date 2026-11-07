# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_reportes.ui'
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
    QDoubleSpinBox, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaReportes(object):
    def setupUi(self, VentanaReportes):
        if not VentanaReportes.objectName():
            VentanaReportes.setObjectName(u"VentanaReportes")
        VentanaReportes.resize(900, 620)
        self.layoutPrincipal = QVBoxLayout(VentanaReportes)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.lblReporte = QLabel(VentanaReportes)
        self.lblReporte.setObjectName(u"lblReporte")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblReporte)

        self.cmbReporte = QComboBox(VentanaReportes)
        self.cmbReporte.setObjectName(u"cmbReporte")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbReporte)

        self.lblProveedor = QLabel(VentanaReportes)
        self.lblProveedor.setObjectName(u"lblProveedor")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblProveedor)

        self.cmbProveedor = QComboBox(VentanaReportes)
        self.cmbProveedor.setObjectName(u"cmbProveedor")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbProveedor)

        self.lblCiudad = QLabel(VentanaReportes)
        self.lblCiudad.setObjectName(u"lblCiudad")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCiudad)

        self.cmbCiudad = QComboBox(VentanaReportes)
        self.cmbCiudad.setObjectName(u"cmbCiudad")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbCiudad)

        self.lblProducto = QLabel(VentanaReportes)
        self.lblProducto.setObjectName(u"lblProducto")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblProducto)

        self.cmbProducto = QComboBox(VentanaReportes)
        self.cmbProducto.setObjectName(u"cmbProducto")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbProducto)

        self.lblCategoria = QLabel(VentanaReportes)
        self.lblCategoria.setObjectName(u"lblCategoria")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblCategoria)

        self.cmbCategoria = QComboBox(VentanaReportes)
        self.cmbCategoria.setObjectName(u"cmbCategoria")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbCategoria)

        self.lblPrecioMinimo = QLabel(VentanaReportes)
        self.lblPrecioMinimo.setObjectName(u"lblPrecioMinimo")

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblPrecioMinimo)

        self.spnPrecioMinimo = QDoubleSpinBox(VentanaReportes)
        self.spnPrecioMinimo.setObjectName(u"spnPrecioMinimo")
        self.spnPrecioMinimo.setDecimals(2)
        self.spnPrecioMinimo.setMaximum(99999999.989999994635582)
        self.spnPrecioMinimo.setValue(0.000000000000000)

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spnPrecioMinimo)

        self.lblPrecioMaximo = QLabel(VentanaReportes)
        self.lblPrecioMaximo.setObjectName(u"lblPrecioMaximo")

        self.layoutFormulario.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblPrecioMaximo)

        self.spnPrecioMaximo = QDoubleSpinBox(VentanaReportes)
        self.spnPrecioMaximo.setObjectName(u"spnPrecioMaximo")
        self.spnPrecioMaximo.setDecimals(2)
        self.spnPrecioMaximo.setMaximum(99999999.989999994635582)
        self.spnPrecioMaximo.setValue(99999999.989999994635582)

        self.layoutFormulario.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spnPrecioMaximo)

        self.lblStockMaximo = QLabel(VentanaReportes)
        self.lblStockMaximo.setObjectName(u"lblStockMaximo")

        self.layoutFormulario.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblStockMaximo)

        self.spnStockMaximo = QSpinBox(VentanaReportes)
        self.spnStockMaximo.setObjectName(u"spnStockMaximo")
        self.spnStockMaximo.setMaximum(2147483647)
        self.spnStockMaximo.setValue(10)

        self.layoutFormulario.setWidget(7, QFormLayout.ItemRole.FieldRole, self.spnStockMaximo)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnGenerar = QPushButton(VentanaReportes)
        self.btnGenerar.setObjectName(u"btnGenerar")
        self.btnGenerar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnGenerar)

        self.btnExportar = QPushButton(VentanaReportes)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnExportar)

        self.btnCerrar = QPushButton(VentanaReportes)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.lblResultados = QLabel(VentanaReportes)
        self.lblResultados.setObjectName(u"lblResultados")

        self.layoutPrincipal.addWidget(self.lblResultados)

        self.tblResultados = QTableWidget(VentanaReportes)
        self.tblResultados.setObjectName(u"tblResultados")
        self.tblResultados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblResultados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblResultados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblResultados.horizontalHeader().setStretchLastSection(True)

        self.layoutPrincipal.addWidget(self.tblResultados)


        self.retranslateUi(VentanaReportes)

        QMetaObject.connectSlotsByName(VentanaReportes)
    # setupUi

    def retranslateUi(self, VentanaReportes):
        VentanaReportes.setWindowTitle(QCoreApplication.translate("VentanaReportes", u"Reportes", None))
        self.lblReporte.setText(QCoreApplication.translate("VentanaReportes", u"Reporte:", None))
        self.lblProveedor.setText(QCoreApplication.translate("VentanaReportes", u"Proveedor:", None))
        self.lblCiudad.setText(QCoreApplication.translate("VentanaReportes", u"Ciudad:", None))
        self.lblProducto.setText(QCoreApplication.translate("VentanaReportes", u"Producto:", None))
        self.lblCategoria.setText(QCoreApplication.translate("VentanaReportes", u"Categor\u00eda:", None))
        self.lblPrecioMinimo.setText(QCoreApplication.translate("VentanaReportes", u"Precio m\u00ednimo:", None))
        self.lblPrecioMaximo.setText(QCoreApplication.translate("VentanaReportes", u"Precio m\u00e1ximo:", None))
        self.lblStockMaximo.setText(QCoreApplication.translate("VentanaReportes", u"Stock m\u00e1ximo:", None))
        self.btnGenerar.setText(QCoreApplication.translate("VentanaReportes", u"Generar", None))
        self.btnExportar.setText(QCoreApplication.translate("VentanaReportes", u"Exportar a PDF", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaReportes", u"Cerrar", None))
    # retranslateUi

