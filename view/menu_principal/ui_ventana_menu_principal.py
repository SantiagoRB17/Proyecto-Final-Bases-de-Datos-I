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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_VentanaMenuPrincipal(object):
    def setupUi(self, VentanaMenuPrincipal):
        if not VentanaMenuPrincipal.objectName():
            VentanaMenuPrincipal.setObjectName(u"VentanaMenuPrincipal")
        VentanaMenuPrincipal.resize(1040, 700)
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
        self.layoutCentral.setSpacing(0)
        self.layoutCentral.setObjectName(u"layoutCentral")
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        self.frameEncabezado = QFrame(self.centralwidget)
        self.frameEncabezado.setObjectName(u"frameEncabezado")
        self.frameEncabezado.setMinimumSize(QSize(0, 110))
        self.frameEncabezado.setMaximumSize(QSize(16777215, 110))
        self.layoutEncabezado = QHBoxLayout(self.frameEncabezado)
        self.layoutEncabezado.setSpacing(12)
        self.layoutEncabezado.setObjectName(u"layoutEncabezado")
        self.layoutEncabezado.setContentsMargins(36, 20, 36, 20)
        self.layoutTitulos = QVBoxLayout()
        self.layoutTitulos.setSpacing(4)
        self.layoutTitulos.setObjectName(u"layoutTitulos")
        self.lblTituloApp = QLabel(self.frameEncabezado)
        self.lblTituloApp.setObjectName(u"lblTituloApp")

        self.layoutTitulos.addWidget(self.lblTituloApp)

        self.lblBienvenida = QLabel(self.frameEncabezado)
        self.lblBienvenida.setObjectName(u"lblBienvenida")

        self.layoutTitulos.addWidget(self.lblBienvenida)


        self.layoutEncabezado.addLayout(self.layoutTitulos)

        self.espaciadorEncabezado = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutEncabezado.addItem(self.espaciadorEncabezado)

        self.lblRol = QLabel(self.frameEncabezado)
        self.lblRol.setObjectName(u"lblRol")

        self.layoutEncabezado.addWidget(self.lblRol, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.layoutCentral.addWidget(self.frameEncabezado)

        self.widgetCuerpo = QWidget(self.centralwidget)
        self.widgetCuerpo.setObjectName(u"widgetCuerpo")
        self.layoutCuerpo = QVBoxLayout(self.widgetCuerpo)
        self.layoutCuerpo.setSpacing(18)
        self.layoutCuerpo.setObjectName(u"layoutCuerpo")
        self.layoutCuerpo.setContentsMargins(36, 28, 36, 24)
        self.lblSeccion = QLabel(self.widgetCuerpo)
        self.lblSeccion.setObjectName(u"lblSeccion")

        self.layoutCuerpo.addWidget(self.lblSeccion)

        self.gridTarjetas = QGridLayout()
        self.gridTarjetas.setObjectName(u"gridTarjetas")
        self.gridTarjetas.setHorizontalSpacing(20)
        self.gridTarjetas.setVerticalSpacing(20)
        self.tarjetaEntidades = QFrame(self.widgetCuerpo)
        self.tarjetaEntidades.setObjectName(u"tarjetaEntidades")
        self.tarjetaEntidades.setProperty(u"tarjeta", True)
        self.layouttarjetaEntidades = QVBoxLayout(self.tarjetaEntidades)
        self.layouttarjetaEntidades.setSpacing(10)
        self.layouttarjetaEntidades.setObjectName(u"layouttarjetaEntidades")
        self.layouttarjetaEntidades.setContentsMargins(22, 20, 22, 22)
        self.lblTituloEntidades = QLabel(self.tarjetaEntidades)
        self.lblTituloEntidades.setObjectName(u"lblTituloEntidades")
        self.lblTituloEntidades.setProperty(u"tarjetaTitulo", True)

        self.layouttarjetaEntidades.addWidget(self.lblTituloEntidades)

        self.lblTextoEntidades = QLabel(self.tarjetaEntidades)
        self.lblTextoEntidades.setObjectName(u"lblTextoEntidades")
        self.lblTextoEntidades.setProperty(u"tarjetaTexto", True)
        self.lblTextoEntidades.setWordWrap(True)

        self.layouttarjetaEntidades.addWidget(self.lblTextoEntidades)

        self.gridtarjetaEntidades = QGridLayout()
        self.gridtarjetaEntidades.setObjectName(u"gridtarjetaEntidades")
        self.gridtarjetaEntidades.setHorizontalSpacing(10)
        self.gridtarjetaEntidades.setVerticalSpacing(10)
        self.btnCiudad = QPushButton(self.tarjetaEntidades)
        self.btnCiudad.setObjectName(u"btnCiudad")
        self.btnCiudad.setAutoDefault(False)
        self.btnCiudad.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaEntidades.addWidget(self.btnCiudad, 0, 0, 1, 1)

        self.btnCategoria = QPushButton(self.tarjetaEntidades)
        self.btnCategoria.setObjectName(u"btnCategoria")
        self.btnCategoria.setAutoDefault(False)
        self.btnCategoria.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaEntidades.addWidget(self.btnCategoria, 0, 1, 1, 1)

        self.btnProducto = QPushButton(self.tarjetaEntidades)
        self.btnProducto.setObjectName(u"btnProducto")
        self.btnProducto.setAutoDefault(False)
        self.btnProducto.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaEntidades.addWidget(self.btnProducto, 1, 0, 1, 1)

        self.btnProveedor = QPushButton(self.tarjetaEntidades)
        self.btnProveedor.setObjectName(u"btnProveedor")
        self.btnProveedor.setAutoDefault(False)
        self.btnProveedor.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaEntidades.addWidget(self.btnProveedor, 1, 1, 1, 1)


        self.layouttarjetaEntidades.addLayout(self.gridtarjetaEntidades)

        self.espaciadortarjetaEntidades = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layouttarjetaEntidades.addItem(self.espaciadortarjetaEntidades)


        self.gridTarjetas.addWidget(self.tarjetaEntidades, 0, 0, 1, 1)

        self.tarjetaTransacciones = QFrame(self.widgetCuerpo)
        self.tarjetaTransacciones.setObjectName(u"tarjetaTransacciones")
        self.tarjetaTransacciones.setProperty(u"tarjeta", True)
        self.layouttarjetaTransacciones = QVBoxLayout(self.tarjetaTransacciones)
        self.layouttarjetaTransacciones.setSpacing(10)
        self.layouttarjetaTransacciones.setObjectName(u"layouttarjetaTransacciones")
        self.layouttarjetaTransacciones.setContentsMargins(22, 20, 22, 22)
        self.lblTituloTransacciones = QLabel(self.tarjetaTransacciones)
        self.lblTituloTransacciones.setObjectName(u"lblTituloTransacciones")
        self.lblTituloTransacciones.setProperty(u"tarjetaTitulo", True)

        self.layouttarjetaTransacciones.addWidget(self.lblTituloTransacciones)

        self.lblTextoTransacciones = QLabel(self.tarjetaTransacciones)
        self.lblTextoTransacciones.setObjectName(u"lblTextoTransacciones")
        self.lblTextoTransacciones.setProperty(u"tarjetaTexto", True)
        self.lblTextoTransacciones.setWordWrap(True)

        self.layouttarjetaTransacciones.addWidget(self.lblTextoTransacciones)

        self.gridtarjetaTransacciones = QGridLayout()
        self.gridtarjetaTransacciones.setObjectName(u"gridtarjetaTransacciones")
        self.gridtarjetaTransacciones.setHorizontalSpacing(10)
        self.gridtarjetaTransacciones.setVerticalSpacing(10)
        self.btnProveedorProducto = QPushButton(self.tarjetaTransacciones)
        self.btnProveedorProducto.setObjectName(u"btnProveedorProducto")
        self.btnProveedorProducto.setAutoDefault(False)
        self.btnProveedorProducto.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaTransacciones.addWidget(self.btnProveedorProducto, 0, 0, 1, 1)


        self.layouttarjetaTransacciones.addLayout(self.gridtarjetaTransacciones)

        self.espaciadortarjetaTransacciones = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layouttarjetaTransacciones.addItem(self.espaciadortarjetaTransacciones)


        self.gridTarjetas.addWidget(self.tarjetaTransacciones, 0, 1, 1, 1)

        self.tarjetaConsultas = QFrame(self.widgetCuerpo)
        self.tarjetaConsultas.setObjectName(u"tarjetaConsultas")
        self.tarjetaConsultas.setProperty(u"tarjeta", True)
        self.layouttarjetaConsultas = QVBoxLayout(self.tarjetaConsultas)
        self.layouttarjetaConsultas.setSpacing(10)
        self.layouttarjetaConsultas.setObjectName(u"layouttarjetaConsultas")
        self.layouttarjetaConsultas.setContentsMargins(22, 20, 22, 22)
        self.lblTituloConsultas = QLabel(self.tarjetaConsultas)
        self.lblTituloConsultas.setObjectName(u"lblTituloConsultas")
        self.lblTituloConsultas.setProperty(u"tarjetaTitulo", True)

        self.layouttarjetaConsultas.addWidget(self.lblTituloConsultas)

        self.lblTextoConsultas = QLabel(self.tarjetaConsultas)
        self.lblTextoConsultas.setObjectName(u"lblTextoConsultas")
        self.lblTextoConsultas.setProperty(u"tarjetaTexto", True)
        self.lblTextoConsultas.setWordWrap(True)

        self.layouttarjetaConsultas.addWidget(self.lblTextoConsultas)

        self.gridtarjetaConsultas = QGridLayout()
        self.gridtarjetaConsultas.setObjectName(u"gridtarjetaConsultas")
        self.gridtarjetaConsultas.setHorizontalSpacing(10)
        self.gridtarjetaConsultas.setVerticalSpacing(10)
        self.btnConsultas = QPushButton(self.tarjetaConsultas)
        self.btnConsultas.setObjectName(u"btnConsultas")
        self.btnConsultas.setAutoDefault(False)
        self.btnConsultas.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaConsultas.addWidget(self.btnConsultas, 0, 0, 1, 1)

        self.btnReportes = QPushButton(self.tarjetaConsultas)
        self.btnReportes.setObjectName(u"btnReportes")
        self.btnReportes.setAutoDefault(False)
        self.btnReportes.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaConsultas.addWidget(self.btnReportes, 0, 1, 1, 1)


        self.layouttarjetaConsultas.addLayout(self.gridtarjetaConsultas)

        self.espaciadortarjetaConsultas = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layouttarjetaConsultas.addItem(self.espaciadortarjetaConsultas)


        self.gridTarjetas.addWidget(self.tarjetaConsultas, 1, 0, 1, 1)

        self.tarjetaAuditoria = QFrame(self.widgetCuerpo)
        self.tarjetaAuditoria.setObjectName(u"tarjetaAuditoria")
        self.tarjetaAuditoria.setProperty(u"tarjeta", True)
        self.layouttarjetaAuditoria = QVBoxLayout(self.tarjetaAuditoria)
        self.layouttarjetaAuditoria.setSpacing(10)
        self.layouttarjetaAuditoria.setObjectName(u"layouttarjetaAuditoria")
        self.layouttarjetaAuditoria.setContentsMargins(22, 20, 22, 22)
        self.lblTituloAuditoria = QLabel(self.tarjetaAuditoria)
        self.lblTituloAuditoria.setObjectName(u"lblTituloAuditoria")
        self.lblTituloAuditoria.setProperty(u"tarjetaTitulo", True)

        self.layouttarjetaAuditoria.addWidget(self.lblTituloAuditoria)

        self.lblTextoAuditoria = QLabel(self.tarjetaAuditoria)
        self.lblTextoAuditoria.setObjectName(u"lblTextoAuditoria")
        self.lblTextoAuditoria.setProperty(u"tarjetaTexto", True)
        self.lblTextoAuditoria.setWordWrap(True)

        self.layouttarjetaAuditoria.addWidget(self.lblTextoAuditoria)

        self.gridtarjetaAuditoria = QGridLayout()
        self.gridtarjetaAuditoria.setObjectName(u"gridtarjetaAuditoria")
        self.gridtarjetaAuditoria.setHorizontalSpacing(10)
        self.gridtarjetaAuditoria.setVerticalSpacing(10)
        self.btnUsuarios = QPushButton(self.tarjetaAuditoria)
        self.btnUsuarios.setObjectName(u"btnUsuarios")
        self.btnUsuarios.setAutoDefault(False)
        self.btnUsuarios.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaAuditoria.addWidget(self.btnUsuarios, 0, 0, 1, 1)

        self.btnBitacora = QPushButton(self.tarjetaAuditoria)
        self.btnBitacora.setObjectName(u"btnBitacora")
        self.btnBitacora.setAutoDefault(False)
        self.btnBitacora.setProperty(u"tarjetaBoton", True)

        self.gridtarjetaAuditoria.addWidget(self.btnBitacora, 0, 1, 1, 1)


        self.layouttarjetaAuditoria.addLayout(self.gridtarjetaAuditoria)

        self.espaciadortarjetaAuditoria = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layouttarjetaAuditoria.addItem(self.espaciadortarjetaAuditoria)


        self.gridTarjetas.addWidget(self.tarjetaAuditoria, 1, 1, 1, 1)


        self.layoutCuerpo.addLayout(self.gridTarjetas)

        self.espaciadorCuerpo = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layoutCuerpo.addItem(self.espaciadorCuerpo)

        self.layoutSalir = QHBoxLayout()
        self.layoutSalir.setObjectName(u"layoutSalir")
        self.espaciadorSalir = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutSalir.addItem(self.espaciadorSalir)

        self.btnSalir = QPushButton(self.widgetCuerpo)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setAutoDefault(False)

        self.layoutSalir.addWidget(self.btnSalir)


        self.layoutCuerpo.addLayout(self.layoutSalir)


        self.layoutCentral.addWidget(self.widgetCuerpo)

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
        VentanaMenuPrincipal.setWindowTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Gesti\u00f3n de Proveedores y Productos", None))
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
        self.lblTituloApp.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Gesti\u00f3n de Proveedores y Productos", None))
        self.lblBienvenida.setText("")
        self.lblRol.setText("")
        self.lblSeccion.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"\u00bfQu\u00e9 desea hacer?", None))
        self.lblTituloEntidades.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Entidades", None))
        self.lblTextoEntidades.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Registre y mantenga ciudades, categor\u00edas, productos y proveedores.", None))
        self.btnCiudad.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Ciudades", None))
        self.btnCategoria.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Categor\u00edas", None))
        self.btnProducto.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Productos", None))
        self.btnProveedor.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Proveedores", None))
        self.lblTituloTransacciones.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Transacciones", None))
        self.lblTextoTransacciones.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Defina qu\u00e9 proveedor ofrece cada producto y a qu\u00e9 precio.", None))
        self.btnProveedorProducto.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Proveedor - Producto", None))
        self.lblTituloConsultas.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Consultas y Reportes", None))
        self.lblTextoConsultas.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Consulte la informaci\u00f3n y exporte reportes en PDF.", None))
        self.btnConsultas.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Consultas", None))
        self.btnReportes.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Reportes", None))
        self.lblTituloAuditoria.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Auditor\u00eda", None))
        self.lblTextoAuditoria.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Gestione los usuarios y revise los ingresos al sistema.", None))
        self.btnUsuarios.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Gesti\u00f3n de usuarios", None))
        self.btnBitacora.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Bit\u00e1cora", None))
        self.btnSalir.setText(QCoreApplication.translate("VentanaMenuPrincipal", u"Cerrar sesi\u00f3n", None))
        self.menuEntidades.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Entidades", None))
        self.menuTransacciones.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Transacciones", None))
        self.menuConsultasReportes.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Consultas y Reportes", None))
        self.menuAuditoria.setTitle(QCoreApplication.translate("VentanaMenuPrincipal", u"Auditor\u00eda", None))
    # retranslateUi

