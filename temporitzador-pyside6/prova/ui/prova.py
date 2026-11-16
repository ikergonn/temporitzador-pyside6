# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prova.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 616)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.actionAbrir.setIcon(icon)
        self.actionCerrar = QAction(MainWindow)
        self.actionCerrar.setObjectName(u"actionCerrar")
        self.actionadios = QAction(MainWindow)
        self.actionadios.setObjectName(u"actionadios")
        self.action12 = QAction(MainWindow)
        self.action12.setObjectName(u"action12")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 801, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, 30, 811, 371))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.horizontalLayoutWidget_2)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 806, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuhola = QMenu(self.menubar)
        self.menuhola.setObjectName(u"menuhola")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuhola.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addSeparator()
        self.menuhola.addAction(self.actionadios)
        self.menuhola.addSeparator()
        self.menuhola.addAction(self.action12)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.actionadios.setText(QCoreApplication.translate("MainWindow", u"adios", None))
        self.action12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuhola.setTitle(QCoreApplication.translate("MainWindow", u"hola", None))
    # retranslateUi

