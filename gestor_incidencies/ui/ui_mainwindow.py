# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPlainTextEdit, QSizePolicy,
    QSplitter, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 244)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")

        self.filterLayout.addWidget(self.searchEdit)

        self.statusFilter = QComboBox(self.centralwidget)
        self.statusFilter.setObjectName(u"statusFilter")

        self.filterLayout.addWidget(self.statusFilter)

        self.priorityFilter = QComboBox(self.centralwidget)
        self.priorityFilter.setObjectName(u"priorityFilter")

        self.filterLayout.addWidget(self.priorityFilter)


        self.verticalLayout.addLayout(self.filterLayout)

        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.incidentsTable = QTableView(self.mainSplitter)
        self.incidentsTable.setObjectName(u"incidentsTable")
        self.mainSplitter.addWidget(self.incidentsTable)
        self.detailPanel = QPlainTextEdit(self.mainSplitter)
        self.detailPanel.setObjectName(u"detailPanel")
        self.mainSplitter.addWidget(self.detailPanel)

        self.verticalLayout.addWidget(self.mainSplitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor d'incidencies", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cerca", None))
    # retranslateUi

