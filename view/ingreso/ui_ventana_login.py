# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_VentanaLogin(object):
    def setupUi(self, VentanaLogin):
        if not VentanaLogin.objectName():
            VentanaLogin.setObjectName(u"VentanaLogin")
        VentanaLogin.resize(380, 220)
        self.layoutPrincipal = QVBoxLayout(VentanaLogin)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.lblTitulo = QLabel(VentanaLogin)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutPrincipal.addWidget(self.lblTitulo)

        self.layoutFormulario = QFormLayout()
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.lblUsuario = QLabel(VentanaLogin)
        self.lblUsuario.setObjectName(u"lblUsuario")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUsuario)

        self.txtUsuario = QLineEdit(VentanaLogin)
        self.txtUsuario.setObjectName(u"txtUsuario")

        self.layoutFormulario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtUsuario)

        self.lblContrasena = QLabel(VentanaLogin)
        self.lblContrasena.setObjectName(u"lblContrasena")

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblContrasena)

        self.txtContrasena = QLineEdit(VentanaLogin)
        self.txtContrasena.setObjectName(u"txtContrasena")
        self.txtContrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.layoutFormulario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtContrasena)


        self.layoutPrincipal.addLayout(self.layoutFormulario)

        self.btnIngresar = QPushButton(VentanaLogin)
        self.btnIngresar.setObjectName(u"btnIngresar")

        self.layoutPrincipal.addWidget(self.btnIngresar)


        self.retranslateUi(VentanaLogin)

        self.btnIngresar.setDefault(True)


        QMetaObject.connectSlotsByName(VentanaLogin)
    # setupUi

    def retranslateUi(self, VentanaLogin):
        VentanaLogin.setWindowTitle(QCoreApplication.translate("VentanaLogin", u"Ingreso al sistema", None))
        self.lblTitulo.setText(QCoreApplication.translate("VentanaLogin", u"Gesti\u00f3n de Proveedores y Productos", None))
        self.lblUsuario.setText(QCoreApplication.translate("VentanaLogin", u"Usuario:", None))
        self.lblContrasena.setText(QCoreApplication.translate("VentanaLogin", u"Contrase\u00f1a:", None))
        self.btnIngresar.setText(QCoreApplication.translate("VentanaLogin", u"Ingresar", None))
    # retranslateUi

