# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_producto.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_VentanaProducto(object):
    def setupUi(self, VentanaProducto):
        if not VentanaProducto.objectName():
            VentanaProducto.setObjectName(u"VentanaProducto")
        VentanaProducto.resize(800, 560)
        self.layoutPrincipal = QVBoxLayout(VentanaProducto)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaProducto)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setHorizontalSpacing(14)
        self.layoutFormulario.setVerticalSpacing(10)
        self.lblNombre = QLabel(VentanaProducto)
        self.lblNombre.setObjectName(u"lblNombre")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(VentanaProducto)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setMaxLength(100)

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblDescripcion = QLabel(VentanaProducto)
        self.lblDescripcion.setObjectName(u"lblDescripcion")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDescripcion)

        self.txtDescripcion = QLineEdit(VentanaProducto)
        self.txtDescripcion.setObjectName(u"txtDescripcion")
        self.txtDescripcion.setMaxLength(255)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDescripcion)

        self.lblPrecio = QLabel(VentanaProducto)
        self.lblPrecio.setObjectName(u"lblPrecio")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPrecio)

        self.spnPrecio = QDoubleSpinBox(VentanaProducto)
        self.spnPrecio.setObjectName(u"spnPrecio")
        self.spnPrecio.setDecimals(2)
        self.spnPrecio.setMaximum(99999999.989999994635582)

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spnPrecio)

        self.lblStock = QLabel(VentanaProducto)
        self.lblStock.setObjectName(u"lblStock")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblStock)

        self.spnStock = QSpinBox(VentanaProducto)
        self.spnStock.setObjectName(u"spnStock")
        self.spnStock.setMaximum(2147483647)

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spnStock)

        self.lblCategoria = QLabel(VentanaProducto)
        self.lblCategoria.setObjectName(u"lblCategoria")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblCategoria)

        self.cmbCategoria = QComboBox(VentanaProducto)
        self.cmbCategoria.setObjectName(u"cmbCategoria")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbCategoria)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaProducto)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaProducto)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaProducto)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaProducto)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaProducto)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblProductos = QTableWidget(VentanaProducto)
        if (self.tblProductos.columnCount() < 6):
            self.tblProductos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblProductos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblProductos.setObjectName(u"tblProductos")
        self.tblProductos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblProductos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblProductos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblProductos.setAlternatingRowColors(True)
        self.tblProductos.setShowGrid(False)
        self.tblProductos.horizontalHeader().setDefaultSectionSize(150)
        self.tblProductos.horizontalHeader().setStretchLastSection(True)
        self.tblProductos.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblProductos)


        self.retranslateUi(VentanaProducto)

        QMetaObject.connectSlotsByName(VentanaProducto)
    # setupUi

    def retranslateUi(self, VentanaProducto):
        VentanaProducto.setWindowTitle(QCoreApplication.translate("VentanaProducto", u"Productos", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaProducto", u"Productos", None))
        self.lblNombre.setText(QCoreApplication.translate("VentanaProducto", u"Nombre:", None))
        self.lblDescripcion.setText(QCoreApplication.translate("VentanaProducto", u"Descripci\u00f3n:", None))
        self.lblPrecio.setText(QCoreApplication.translate("VentanaProducto", u"Precio:", None))
        self.lblStock.setText(QCoreApplication.translate("VentanaProducto", u"Stock:", None))
        self.lblCategoria.setText(QCoreApplication.translate("VentanaProducto", u"Categor\u00eda:", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaProducto", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaProducto", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaProducto", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaProducto", u"Eliminar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaProducto", u"Cerrar", None))
        ___qtablewidgetitem = self.tblProductos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaProducto", u"ID", None))
        ___qtablewidgetitem1 = self.tblProductos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaProducto", u"Nombre", None))
        ___qtablewidgetitem2 = self.tblProductos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaProducto", u"Descripci\u00f3n", None))
        ___qtablewidgetitem3 = self.tblProductos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaProducto", u"Precio", None))
        ___qtablewidgetitem4 = self.tblProductos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaProducto", u"Stock", None))
        ___qtablewidgetitem5 = self.tblProductos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaProducto", u"Categor\u00eda", None))
    # retranslateUi

