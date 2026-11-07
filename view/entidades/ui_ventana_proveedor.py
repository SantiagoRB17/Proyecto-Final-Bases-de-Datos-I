# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_proveedor.ui'
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
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaProveedor(object):
    def setupUi(self, VentanaProveedor):
        if not VentanaProveedor.objectName():
            VentanaProveedor.setObjectName(u"VentanaProveedor")
        VentanaProveedor.resize(900, 560)
        self.layoutPrincipal = QVBoxLayout(VentanaProveedor)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaProveedor)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setHorizontalSpacing(14)
        self.layoutFormulario.setVerticalSpacing(10)
        self.lblNit = QLabel(VentanaProveedor)
        self.lblNit.setObjectName(u"lblNit")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNit)

        self.txtNit = QLineEdit(VentanaProveedor)
        self.txtNit.setObjectName(u"txtNit")
        self.txtNit.setMaxLength(20)

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNit)

        self.lblNombre = QLabel(VentanaProveedor)
        self.lblNombre.setObjectName(u"lblNombre")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(VentanaProveedor)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setMaxLength(100)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblDireccion = QLabel(VentanaProveedor)
        self.lblDireccion.setObjectName(u"lblDireccion")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDireccion)

        self.txtDireccion = QLineEdit(VentanaProveedor)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setMaxLength(150)

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtDireccion)

        self.lblTelefono = QLabel(VentanaProveedor)
        self.lblTelefono.setObjectName(u"lblTelefono")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTelefono)

        self.txtTelefono = QLineEdit(VentanaProveedor)
        self.txtTelefono.setObjectName(u"txtTelefono")
        self.txtTelefono.setMaxLength(20)

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtTelefono)

        self.lblEmail = QLabel(VentanaProveedor)
        self.lblEmail.setObjectName(u"lblEmail")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.txtEmail = QLineEdit(VentanaProveedor)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setMaxLength(100)

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtEmail)

        self.lblCiudad = QLabel(VentanaProveedor)
        self.lblCiudad.setObjectName(u"lblCiudad")

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblCiudad)

        self.cmbCiudad = QComboBox(VentanaProveedor)
        self.cmbCiudad.setObjectName(u"cmbCiudad")

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbCiudad)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaProveedor)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaProveedor)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaProveedor)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaProveedor)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaProveedor)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblProveedores = QTableWidget(VentanaProveedor)
        if (self.tblProveedores.columnCount() < 7):
            self.tblProveedores.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblProveedores.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblProveedores.setObjectName(u"tblProveedores")
        self.tblProveedores.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblProveedores.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblProveedores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblProveedores.setAlternatingRowColors(True)
        self.tblProveedores.setShowGrid(False)
        self.tblProveedores.horizontalHeader().setDefaultSectionSize(150)
        self.tblProveedores.horizontalHeader().setStretchLastSection(True)
        self.tblProveedores.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblProveedores)


        self.retranslateUi(VentanaProveedor)

        QMetaObject.connectSlotsByName(VentanaProveedor)
    # setupUi

    def retranslateUi(self, VentanaProveedor):
        VentanaProveedor.setWindowTitle(QCoreApplication.translate("VentanaProveedor", u"Proveedores", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaProveedor", u"Proveedores", None))
        self.lblNit.setText(QCoreApplication.translate("VentanaProveedor", u"NIT:", None))
        self.lblNombre.setText(QCoreApplication.translate("VentanaProveedor", u"Nombre:", None))
        self.lblDireccion.setText(QCoreApplication.translate("VentanaProveedor", u"Direcci\u00f3n:", None))
        self.lblTelefono.setText(QCoreApplication.translate("VentanaProveedor", u"Tel\u00e9fono:", None))
        self.lblEmail.setText(QCoreApplication.translate("VentanaProveedor", u"Email:", None))
        self.lblCiudad.setText(QCoreApplication.translate("VentanaProveedor", u"Ciudad:", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaProveedor", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaProveedor", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaProveedor", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaProveedor", u"Eliminar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaProveedor", u"Cerrar", None))
        ___qtablewidgetitem = self.tblProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaProveedor", u"ID", None))
        ___qtablewidgetitem1 = self.tblProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaProveedor", u"NIT", None))
        ___qtablewidgetitem2 = self.tblProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaProveedor", u"Nombre", None))
        ___qtablewidgetitem3 = self.tblProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaProveedor", u"Direcci\u00f3n", None))
        ___qtablewidgetitem4 = self.tblProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaProveedor", u"Tel\u00e9fono", None))
        ___qtablewidgetitem5 = self.tblProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaProveedor", u"Email", None))
        ___qtablewidgetitem6 = self.tblProveedores.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VentanaProveedor", u"Ciudad", None))
    # retranslateUi

