# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_categoria.ui'
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

class Ui_VentanaCategoria(object):
    def setupUi(self, VentanaCategoria):
        if not VentanaCategoria.objectName():
            VentanaCategoria.setObjectName(u"VentanaCategoria")
        VentanaCategoria.resize(640, 560)
        self.layoutPrincipal = QVBoxLayout(VentanaCategoria)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaCategoria)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setHorizontalSpacing(14)
        self.layoutFormulario.setVerticalSpacing(10)
        self.lblNombre = QLabel(VentanaCategoria)
        self.lblNombre.setObjectName(u"lblNombre")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(VentanaCategoria)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setMaxLength(100)

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblDescripcion = QLabel(VentanaCategoria)
        self.lblDescripcion.setObjectName(u"lblDescripcion")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDescripcion)

        self.txtDescripcion = QLineEdit(VentanaCategoria)
        self.txtDescripcion.setObjectName(u"txtDescripcion")
        self.txtDescripcion.setMaxLength(255)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDescripcion)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaCategoria)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaCategoria)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaCategoria)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaCategoria)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaCategoria)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblCategorias = QTableWidget(VentanaCategoria)
        if (self.tblCategorias.columnCount() < 3):
            self.tblCategorias.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCategorias.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCategorias.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblCategorias.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblCategorias.setObjectName(u"tblCategorias")
        self.tblCategorias.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblCategorias.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblCategorias.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCategorias.setAlternatingRowColors(True)
        self.tblCategorias.setShowGrid(False)
        self.tblCategorias.horizontalHeader().setDefaultSectionSize(150)
        self.tblCategorias.horizontalHeader().setStretchLastSection(True)
        self.tblCategorias.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblCategorias)


        self.retranslateUi(VentanaCategoria)

        QMetaObject.connectSlotsByName(VentanaCategoria)
    # setupUi

    def retranslateUi(self, VentanaCategoria):
        VentanaCategoria.setWindowTitle(QCoreApplication.translate("VentanaCategoria", u"Categor\u00edas", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaCategoria", u"Categor\u00edas", None))
        self.lblNombre.setText(QCoreApplication.translate("VentanaCategoria", u"Nombre:", None))
        self.lblDescripcion.setText(QCoreApplication.translate("VentanaCategoria", u"Descripci\u00f3n:", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaCategoria", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaCategoria", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaCategoria", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaCategoria", u"Eliminar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaCategoria", u"Cerrar", None))
        ___qtablewidgetitem = self.tblCategorias.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaCategoria", u"ID", None))
        ___qtablewidgetitem1 = self.tblCategorias.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaCategoria", u"Nombre", None))
        ___qtablewidgetitem2 = self.tblCategorias.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaCategoria", u"Descripci\u00f3n", None))
    # retranslateUi

