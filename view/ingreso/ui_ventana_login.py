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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_VentanaLogin(object):
    def setupUi(self, VentanaLogin):
        if not VentanaLogin.objectName():
            VentanaLogin.setObjectName(u"VentanaLogin")
        VentanaLogin.resize(780, 460)
        self.layoutPrincipal = QHBoxLayout(VentanaLogin)
        self.layoutPrincipal.setSpacing(0)
        self.layoutPrincipal.setObjectName(u"layoutPrincipal")
        self.layoutPrincipal.setContentsMargins(0, 0, 0, 0)
        self.frameMarca = QFrame(VentanaLogin)
        self.frameMarca.setObjectName(u"frameMarca")
        self.frameMarca.setMinimumSize(QSize(320, 0))
        self.frameMarca.setMaximumSize(QSize(320, 16777215))
        self.layoutMarca = QVBoxLayout(self.frameMarca)
        self.layoutMarca.setSpacing(12)
        self.layoutMarca.setObjectName(u"layoutMarca")
        self.layoutMarca.setContentsMargins(36, 36, 36, 36)
        self.espaciadorMarcaArriba = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutMarca.addItem(self.espaciadorMarcaArriba)

        self.lblMarcaTitulo = QLabel(self.frameMarca)
        self.lblMarcaTitulo.setObjectName(u"lblMarcaTitulo")
        self.lblMarcaTitulo.setWordWrap(True)

        self.layoutMarca.addWidget(self.lblMarcaTitulo)

        self.lblMarcaTexto = QLabel(self.frameMarca)
        self.lblMarcaTexto.setObjectName(u"lblMarcaTexto")
        self.lblMarcaTexto.setWordWrap(True)

        self.layoutMarca.addWidget(self.lblMarcaTexto)

        self.espaciadorMarcaAbajo = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutMarca.addItem(self.espaciadorMarcaAbajo)


        self.layoutPrincipal.addWidget(self.frameMarca)

        self.widgetFormulario = QWidget(VentanaLogin)
        self.widgetFormulario.setObjectName(u"widgetFormulario")
        self.layoutFormulario = QVBoxLayout(self.widgetFormulario)
        self.layoutFormulario.setSpacing(8)
        self.layoutFormulario.setObjectName(u"layoutFormulario")
        self.layoutFormulario.setContentsMargins(48, 40, 48, 40)
        self.espaciadorFormularioArriba = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutFormulario.addItem(self.espaciadorFormularioArriba)

        self.lblLoginTitulo = QLabel(self.widgetFormulario)
        self.lblLoginTitulo.setObjectName(u"lblLoginTitulo")

        self.layoutFormulario.addWidget(self.lblLoginTitulo)

        self.lblLoginTexto = QLabel(self.widgetFormulario)
        self.lblLoginTexto.setObjectName(u"lblLoginTexto")

        self.layoutFormulario.addWidget(self.lblLoginTexto)

        self.espaciadorTitulo = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutFormulario.addItem(self.espaciadorTitulo)

        self.lblUsuario = QLabel(self.widgetFormulario)
        self.lblUsuario.setObjectName(u"lblUsuario")

        self.layoutFormulario.addWidget(self.lblUsuario)

        self.txtUsuario = QLineEdit(self.widgetFormulario)
        self.txtUsuario.setObjectName(u"txtUsuario")

        self.layoutFormulario.addWidget(self.txtUsuario)

        self.espaciadorCampos = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutFormulario.addItem(self.espaciadorCampos)

        self.lblContrasena = QLabel(self.widgetFormulario)
        self.lblContrasena.setObjectName(u"lblContrasena")

        self.layoutFormulario.addWidget(self.lblContrasena)

        self.txtContrasena = QLineEdit(self.widgetFormulario)
        self.txtContrasena.setObjectName(u"txtContrasena")
        self.txtContrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.layoutFormulario.addWidget(self.txtContrasena)

        self.espaciadorBoton = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutFormulario.addItem(self.espaciadorBoton)

        self.btnIngresar = QPushButton(self.widgetFormulario)
        self.btnIngresar.setObjectName(u"btnIngresar")

        self.layoutFormulario.addWidget(self.btnIngresar)

        self.espaciadorFormularioAbajo = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutFormulario.addItem(self.espaciadorFormularioAbajo)


        self.layoutPrincipal.addWidget(self.widgetFormulario)


        self.retranslateUi(VentanaLogin)

        self.btnIngresar.setDefault(True)


        QMetaObject.connectSlotsByName(VentanaLogin)
    # setupUi

    def retranslateUi(self, VentanaLogin):
        VentanaLogin.setWindowTitle(QCoreApplication.translate("VentanaLogin", u"Ingreso al sistema", None))
        self.lblMarcaTitulo.setText(QCoreApplication.translate("VentanaLogin", u"Gesti\u00f3n de Proveedores y Productos", None))
        self.lblMarcaTexto.setText(QCoreApplication.translate("VentanaLogin", u"Proyecto final de Bases de Datos I", None))
        self.lblLoginTitulo.setText(QCoreApplication.translate("VentanaLogin", u"Bienvenido", None))
        self.lblLoginTexto.setText(QCoreApplication.translate("VentanaLogin", u"Inicie sesi\u00f3n para continuar", None))
        self.lblUsuario.setText(QCoreApplication.translate("VentanaLogin", u"Usuario", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("VentanaLogin", u"Su nombre de usuario", None))
        self.lblContrasena.setText(QCoreApplication.translate("VentanaLogin", u"Contrase\u00f1a", None))
        self.txtContrasena.setPlaceholderText(QCoreApplication.translate("VentanaLogin", u"Su contrase\u00f1a", None))
        self.btnIngresar.setText(QCoreApplication.translate("VentanaLogin", u"Ingresar", None))
    # retranslateUi

