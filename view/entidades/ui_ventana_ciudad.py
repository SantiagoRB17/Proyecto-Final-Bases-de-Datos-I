# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_ciudad.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_VentanaCiudad(object):
    def setupUi(self, VentanaCiudad):
        if not VentanaCiudad.objectName():
            VentanaCiudad.setObjectName(u"VentanaCiudad")
        VentanaCiudad.resize(640, 480)
        self.layoutPrincipal = QVBoxLayout(VentanaCiudad)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.lblNombre = QLabel(VentanaCiudad)
        self.lblNombre.setObjectName(u"lblNombre")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(VentanaCiudad)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setMaxLength(100)

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblDepartamento = QLabel(VentanaCiudad)
        self.lblDepartamento.setObjectName(u"lblDepartamento")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDepartamento)

        self.txtDepartamento = QLineEdit(VentanaCiudad)
        self.txtDepartamento.setObjectName(u"txtDepartamento")
        self.txtDepartamento.setMaxLength(100)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDepartamento)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaCiudad)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaCiudad)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaCiudad)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaCiudad)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaCiudad)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblCiudades = QTableWidget(VentanaCiudad)
        if (self.tblCiudades.columnCount() < 3):
            self.tblCiudades.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCiudades.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCiudades.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblCiudades.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblCiudades.setObjectName(u"tblCiudades")
        self.tblCiudades.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblCiudades.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblCiudades.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCiudades.horizontalHeader().setStretchLastSection(True)

        self.layoutPrincipal.addWidget(self.tblCiudades)


        self.retranslateUi(VentanaCiudad)

        QMetaObject.connectSlotsByName(VentanaCiudad)
    # setupUi

    def retranslateUi(self, VentanaCiudad):
        VentanaCiudad.setWindowTitle(QCoreApplication.translate("VentanaCiudad", u"Ciudades", None))
        self.lblNombre.setText(QCoreApplication.translate("VentanaCiudad", u"Nombre:", None))
        self.lblDepartamento.setText(QCoreApplication.translate("VentanaCiudad", u"Departamento:", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaCiudad", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaCiudad", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaCiudad", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaCiudad", u"Eliminar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaCiudad", u"Cerrar", None))
        ___qtablewidgetitem = self.tblCiudades.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaCiudad", u"ID", None))
        ___qtablewidgetitem1 = self.tblCiudades.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaCiudad", u"Nombre", None))
        ___qtablewidgetitem2 = self.tblCiudades.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaCiudad", u"Departamento", None))
    # retranslateUi

