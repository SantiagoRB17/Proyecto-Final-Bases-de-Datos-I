# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_menu_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaMenuPrincipal(object):
    def setupUi(self, VentanaMenuPrincipal):
        if not VentanaMenuPrincipal.objectName():
            VentanaMenuPrincipal.setObjectName(u"VentanaMenuPrincipal")
        VentanaMenuPrincipal.resize(800, 500)
        self.actionCiudad = QAction(VentanaMenuPrincipal)
        self.actionCiudad.setObjectName(u"actionCiudad")
        self.actionCategoria = QAction(VentanaMenuPrincipal)
        self.actionCategoria.setObjectName(u"actionCategoria")
        self.actionProducto = QAction(VentanaMenuPrincipal)
        self.actionProducto.setObjectName(u"actionProducto")
        self.actionProveedor = QAction(VentanaMenuPrincipal)
        self.actionProveedor.setObjectName(u"actionProveedor")
        self.actionProveedorProducto = QAction(VentanaMenuPrincipal)
        self.actionProveedorProducto.setObjectName(u"actionProveedorProducto")
        self.actionConsultas = QAction(VentanaMenuPrincipal)
        self.actionConsultas.setObjectName(u"actionConsultas")
        self.actionReportes = QAction(VentanaMenuPrincipal)
        self.actionReportes.setObjectName(u"actionReportes")
        self.actionUsuarios = QAction(VentanaMenuPrincipal)
        self.actionUsuarios.setObjectName(u"actionUsuarios")
        self.actionBitacora = QAction(VentanaMenuPrincipal)
        self.actionBitacora.setObjectName(u"actionBitacora")
        self.actionSalir = QAction(VentanaMenuPrincipal)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(VentanaMenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutCentral = QVBoxLayout(self.centralwidget)
        self.layoutCentral.setObjectName(u"layoutCentral")
        self.lblBienvenida = QLabel(self.centralwidget)
        self.lblBienvenida.setObjectName(u"lblBienvenida")
        font = QFont()
        font.setPointSize(14)
        self.lblBienvenida.setFont(font)
        self.lblBienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutCentral.addWidget(self.lblBienvenida)

        VentanaMenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaMenuPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menuEntidades = QMenu(self.menubar)
        self.menuEntidades.setObjectName(u"menuEntidades")
        self.menuTransacciones = QMenu(self.menubar)
        self.menuTransacciones.setObjectName(u"menuTransacciones")
        self.menuConsultasReportes = QMenu(self.menubar)
        self.menuConsultasReportes.setObjectName(u"menuConsultasReportes")
        self.menuAuditoria = QMenu(self.menubar)
        self.menuAuditoria.setObjectName(u"menuAuditoria")
        VentanaMenuPrincipal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuEntidades.menuAction())
        self.menubar.addAction(self.menuTransacciones.menuAction())
        self.menubar.addAction(self.menuConsultasReportes.menuAction())
        self.menubar.addAction(self.menuAuditoria.menuAction())
        self.menubar.addAction(self.actionSalir)
        self.menuEntidades.addAction(self.actionCiudad)
        self.menuEntidades.addAction(self.actionCategoria)
        self.menuEntidades.addAction(self.actionProducto)
        self.menuEntidades.addAction(self.actionProveedor)
        self.menuTransacciones.addAction(self.actionProveedorProducto)
        self.menuConsultasReportes.addAction(self.actionConsultas)
        self.menuConsultasReportes.addAction(self.actionReportes)
        self.menuAuditoria.addAction(self.actionUsuarios)
        self.menuAuditoria.addAction(self.actionBitacora)

        self.retranslateUi(VentanaMenuPrincipal)

        QMetaObject.connectSlotsByName(VentanaMenuPrincipal)
    # setupUi

    def retranslateUi(self, VentanaMenuPrincipal):
        VentanaMenuPrincipal.setWindowTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Men\u00fa principal", None))
        self.actionCiudad.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Ciudad", None))
        self.actionCategoria.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Categor\u00eda", None))
        self.actionProducto.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Producto", None))
        self.actionProveedor.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Proveedor", None))
        self.actionProveedorProducto.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Proveedor - Producto", None))
        self.actionConsultas.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Consultas", None))
        self.actionReportes.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Reportes", None))
        self.actionUsuarios.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Gesti\u00f3n de usuarios", None))
        self.actionBitacora.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Bit\u00e1cora", None))
        self.actionSalir.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Salir", None))
        self.menuEntidades.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Entidades", None))
        self.menuTransacciones.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Transacciones", None))
        self.menuConsultasReportes.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Consultas y Reportes", None))
        self.menuAuditoria.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Auditor\u00eda", None))
    # retranslateUi

