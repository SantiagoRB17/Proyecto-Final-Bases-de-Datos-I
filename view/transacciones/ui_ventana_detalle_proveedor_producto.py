# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_detalle_proveedor_producto.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QDialog, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaDetalleProveedorProducto(object):
    def setupUi(self, VentanaDetalleProveedorProducto):
        if not VentanaDetalleProveedorProducto.objectName():
            VentanaDetalleProveedorProducto.setObjectName(u"VentanaDetalleProveedorProducto")
        VentanaDetalleProveedorProducto.resize(800, 560)
        self.layoutPrincipal = QVBoxLayout(VentanaDetalleProveedorProducto)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.lblProveedor = QLabel(VentanaDetalleProveedorProducto)
        self.lblProveedor.setObjectName(u"lblProveedor")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblProveedor)

        self.cmbProveedor = QComboBox(VentanaDetalleProveedorProducto)
        self.cmbProveedor.setObjectName(u"cmbProveedor")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbProveedor)

        self.lblProducto = QLabel(VentanaDetalleProveedorProducto)
        self.lblProducto.setObjectName(u"lblProducto")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblProducto)

        self.cmbProducto = QComboBox(VentanaDetalleProveedorProducto)
        self.cmbProducto.setObjectName(u"cmbProducto")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbProducto)

        self.lblFecha = QLabel(VentanaDetalleProveedorProducto)
        self.lblFecha.setObjectName(u"lblFecha")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblFecha)

        self.dteFecha = QDateEdit(VentanaDetalleProveedorProducto)
        self.dteFecha.setObjectName(u"dteFecha")
        self.dteFecha.setCalendarPopup(True)

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dteFecha)

        self.lblPrecio = QLabel(VentanaDetalleProveedorProducto)
        self.lblPrecio.setObjectName(u"lblPrecio")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblPrecio)

        self.spnPrecio = QDoubleSpinBox(VentanaDetalleProveedorProducto)
        self.spnPrecio.setObjectName(u"spnPrecio")
        self.spnPrecio.setDecimals(2)
        self.spnPrecio.setMaximum(99999999.989999994635582)

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spnPrecio)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaDetalleProveedorProducto)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaDetalleProveedorProducto)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaDetalleProveedorProducto)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaDetalleProveedorProducto)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaDetalleProveedorProducto)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblDetalles = QTableWidget(VentanaDetalleProveedorProducto)
        if (self.tblDetalles.columnCount() < 4):
            self.tblDetalles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDetalles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDetalles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblDetalles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblDetalles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblDetalles.setObjectName(u"tblDetalles")
        self.tblDetalles.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblDetalles.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblDetalles.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblDetalles.horizontalHeader().setStretchLastSection(True)

        self.layoutPrincipal.addWidget(self.tblDetalles)


        self.retranslateUi(VentanaDetalleProveedorProducto)

        QMetaObject.connectSlotsByName(VentanaDetalleProveedorProducto)
    # setupUi

    def retranslateUi(self, VentanaDetalleProveedorProducto):
        VentanaDetalleProveedorProducto.setWindowTitle(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Proveedor - Producto", None))
        self.lblProveedor.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Proveedor:", None))
        self.lblProducto.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Producto:", None))
        self.lblFecha.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Fecha de registro:", None))
        self.dteFecha.setDisplayFormat(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"dd/MM/yyyy", None))
        self.lblPrecio.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Precio del proveedor:", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Eliminar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Cerrar", None))
        ___qtablewidgetitem = self.tblDetalles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Proveedor", None))
        ___qtablewidgetitem1 = self.tblDetalles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Producto", None))
        ___qtablewidgetitem2 = self.tblDetalles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Fecha de registro", None))
        ___qtablewidgetitem3 = self.tblDetalles.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaDetalleProveedorProducto", u"Precio del proveedor", None))
    # retranslateUi

