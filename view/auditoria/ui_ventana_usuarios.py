# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_usuarios.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaUsuarios(object):
    def setupUi(self, VentanaUsuarios):
        if not VentanaUsuarios.objectName():
            VentanaUsuarios.setObjectName(u"VentanaUsuarios")
        VentanaUsuarios.resize(860, 580)
        self.layoutPrincipal = QVBoxLayout(VentanaUsuarios)
        self.layoutPrincipal.setSpacing(12)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(24, 20, 24, 20)
        self.lblEncabezado = QLabel(VentanaUsuarios)
        self.lblEncabezado.setObjectName(u"lblEncabezado")

        self.layoutPrincipal.addWidget(self.lblEncabezado)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setHorizontalSpacing(14)
        self.layoutFormulario.setVerticalSpacing(10)
        self.lblNombreUsuario = QLabel(VentanaUsuarios)
        self.lblNombreUsuario.setObjectName(u"lblNombreUsuario")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombreUsuario)

        self.txtNombreUsuario = QLineEdit(VentanaUsuarios)
        self.txtNombreUsuario.setObjectName(u"txtNombreUsuario")
        self.txtNombreUsuario.setMaxLength(50)

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombreUsuario)

        self.lblContrasena = QLabel(VentanaUsuarios)
        self.lblContrasena.setObjectName(u"lblContrasena")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblContrasena)

        self.txtContrasena = QLineEdit(VentanaUsuarios)
        self.txtContrasena.setObjectName(u"txtContrasena")
        self.txtContrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtContrasena)

        self.lblNombres = QLabel(VentanaUsuarios)
        self.lblNombres.setObjectName(u"lblNombres")

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblNombres)

        self.txtNombres = QLineEdit(VentanaUsuarios)
        self.txtNombres.setObjectName(u"txtNombres")
        self.txtNombres.setMaxLength(75)

        self.layoutFormulario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNombres)

        self.lblApellidos = QLabel(VentanaUsuarios)
        self.lblApellidos.setObjectName(u"lblApellidos")

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblApellidos)

        self.txtApellidos = QLineEdit(VentanaUsuarios)
        self.txtApellidos.setObjectName(u"txtApellidos")
        self.txtApellidos.setMaxLength(75)

        self.layoutFormulario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtApellidos)

        self.lblTipoUsuario = QLabel(VentanaUsuarios)
        self.lblTipoUsuario.setObjectName(u"lblTipoUsuario")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblTipoUsuario)

        self.cmbTipoUsuario = QComboBox(VentanaUsuarios)
        self.cmbTipoUsuario.setObjectName(u"cmbTipoUsuario")

        self.layoutFormulario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbTipoUsuario)

        self.lblEstado = QLabel(VentanaUsuarios)
        self.lblEstado.setObjectName(u"lblEstado")

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblEstado)

        self.chkEstado = QCheckBox(VentanaUsuarios)
        self.chkEstado.setObjectName(u"chkEstado")
        self.chkEstado.setChecked(True)

        self.layoutFormulario.setWidget(5, QFormLayout.ItemRole.FieldRole, self.chkEstado)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btnNuevo = QPushButton(VentanaUsuarios)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnNuevo)

        self.btnAgregar = QPushButton(VentanaUsuarios)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton(VentanaUsuarios)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(VentanaUsuarios)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnEliminar)

        self.btnCerrar = QPushButton(VentanaUsuarios)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setAutoDefault(False)

        self.layoutBotones.addWidget(self.btnCerrar)


        self.layoutPrincipal.addLayout(self.layoutBotones)

        self.tblUsuarios = QTableWidget(VentanaUsuarios)
        if (self.tblUsuarios.columnCount() < 6):
            self.tblUsuarios.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblUsuarios.setObjectName(u"tblUsuarios")
        self.tblUsuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblUsuarios.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblUsuarios.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblUsuarios.setAlternatingRowColors(True)
        self.tblUsuarios.setShowGrid(False)
        self.tblUsuarios.horizontalHeader().setDefaultSectionSize(150)
        self.tblUsuarios.horizontalHeader().setStretchLastSection(True)
        self.tblUsuarios.verticalHeader().setVisible(False)

        self.layoutPrincipal.addWidget(self.tblUsuarios)


        self.retranslateUi(VentanaUsuarios)

        QMetaObject.connectSlotsByName(VentanaUsuarios)
    # setupUi

    def retranslateUi(self, VentanaUsuarios):
        VentanaUsuarios.setWindowTitle(QCoreApplication.translate("VentanaUsuarios", u"Gesti\u00f3n de usuarios", None))
        self.lblEncabezado.setText(QCoreApplication.translate("VentanaUsuarios", u"Gesti\u00f3n de usuarios", None))
        self.lblNombreUsuario.setText(QCoreApplication.translate("VentanaUsuarios", u"Usuario:", None))
        self.lblContrasena.setText(QCoreApplication.translate("VentanaUsuarios", u"Contrase\u00f1a:", None))
        self.txtContrasena.setPlaceholderText(QCoreApplication.translate("VentanaUsuarios", u"Obligatoria al crear. Al editar, vac\u00eda conserva la actual.", None))
        self.lblNombres.setText(QCoreApplication.translate("VentanaUsuarios", u"Nombres:", None))
        self.lblApellidos.setText(QCoreApplication.translate("VentanaUsuarios", u"Apellidos:", None))
        self.lblTipoUsuario.setText(QCoreApplication.translate("VentanaUsuarios", u"Rol:", None))
        self.lblEstado.setText(QCoreApplication.translate("VentanaUsuarios", u"Estado:", None))
        self.chkEstado.setText(QCoreApplication.translate("VentanaUsuarios", u"Activo", None))
        self.btnNuevo.setText(QCoreApplication.translate("VentanaUsuarios", u"Nuevo", None))
        self.btnAgregar.setText(QCoreApplication.translate("VentanaUsuarios", u"Agregar", None))
        self.btnEditar.setText(QCoreApplication.translate("VentanaUsuarios", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaUsuarios", u"Desactivar", None))
        self.btnCerrar.setText(QCoreApplication.translate("VentanaUsuarios", u"Cerrar", None))
        ___qtablewidgetitem = self.tblUsuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaUsuarios", u"ID", None))
        ___qtablewidgetitem1 = self.tblUsuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaUsuarios", u"Usuario", None))
        ___qtablewidgetitem2 = self.tblUsuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaUsuarios", u"Nombres", None))
        ___qtablewidgetitem3 = self.tblUsuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaUsuarios", u"Apellidos", None))
        ___qtablewidgetitem4 = self.tblUsuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaUsuarios", u"Rol", None))
        ___qtablewidgetitem5 = self.tblUsuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaUsuarios", u"Estado", None))
    # retranslateUi

