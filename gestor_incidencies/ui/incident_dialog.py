# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'incident_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_IncidentDialog(object):
    def setupUi(self, IncidentDialog):
        if not IncidentDialog.objectName():
            IncidentDialog.setObjectName(u"IncidentDialog")
        IncidentDialog.resize(520, 430)
        self.vertical_layout = QVBoxLayout(IncidentDialog)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.form_layout = QFormLayout()
        self.form_layout.setObjectName(u"form_layout")
        self.title_label = QLabel(IncidentDialog)
        self.title_label.setObjectName(u"title_label")

        self.form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.title_label)

        self.title_edit = QLineEdit(IncidentDialog)
        self.title_edit.setObjectName(u"title_edit")

        self.form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.title_edit)

        self.description_label = QLabel(IncidentDialog)
        self.description_label.setObjectName(u"description_label")

        self.form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.description_label)

        self.description_edit = QTextEdit(IncidentDialog)
        self.description_edit.setObjectName(u"description_edit")

        self.form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.description_edit)

        self.category_label = QLabel(IncidentDialog)
        self.category_label.setObjectName(u"category_label")

        self.form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.category_label)

        self.category_edit = QLineEdit(IncidentDialog)
        self.category_edit.setObjectName(u"category_edit")

        self.form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.category_edit)

        self.priority_label = QLabel(IncidentDialog)
        self.priority_label.setObjectName(u"priority_label")

        self.form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.priority_label)

        self.priority_combo = QComboBox(IncidentDialog)
        self.priority_combo.setObjectName(u"priority_combo")

        self.form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.priority_combo)

        self.status_label = QLabel(IncidentDialog)
        self.status_label.setObjectName(u"status_label")

        self.form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.status_label)

        self.status_combo = QComboBox(IncidentDialog)
        self.status_combo.setObjectName(u"status_combo")

        self.form_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.status_combo)

        self.assignee_label = QLabel(IncidentDialog)
        self.assignee_label.setObjectName(u"assignee_label")

        self.form_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.assignee_label)

        self.assignee_edit = QLineEdit(IncidentDialog)
        self.assignee_edit.setObjectName(u"assignee_edit")

        self.form_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.assignee_edit)

        self.due_date_label = QLabel(IncidentDialog)
        self.due_date_label.setObjectName(u"due_date_label")

        self.form_layout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.due_date_label)

        self.due_date_edit = QLineEdit(IncidentDialog)
        self.due_date_edit.setObjectName(u"due_date_edit")

        self.form_layout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.due_date_edit)

        self.tags_label = QLabel(IncidentDialog)
        self.tags_label.setObjectName(u"tags_label")

        self.form_layout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.tags_label)

        self.tags_edit = QLineEdit(IncidentDialog)
        self.tags_edit.setObjectName(u"tags_edit")

        self.form_layout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.tags_edit)


        self.vertical_layout.addLayout(self.form_layout)

        self.buttons = QDialogButtonBox(IncidentDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Orientation.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.vertical_layout.addWidget(self.buttons)


        self.retranslateUi(IncidentDialog)
        self.buttons.accepted.connect(IncidentDialog.accept)
        self.buttons.rejected.connect(IncidentDialog.reject)

        QMetaObject.connectSlotsByName(IncidentDialog)
    # setupUi

    def retranslateUi(self, IncidentDialog):
        IncidentDialog.setWindowTitle(QCoreApplication.translate("IncidentDialog", u"Incidencia", None))
        self.title_label.setText(QCoreApplication.translate("IncidentDialog", u"Titol", None))
        self.description_label.setText(QCoreApplication.translate("IncidentDialog", u"Descripcio", None))
        self.category_label.setText(QCoreApplication.translate("IncidentDialog", u"Categoria", None))
        self.priority_label.setText(QCoreApplication.translate("IncidentDialog", u"Prioritat", None))
        self.status_label.setText(QCoreApplication.translate("IncidentDialog", u"Estat", None))
        self.assignee_label.setText(QCoreApplication.translate("IncidentDialog", u"Responsable", None))
        self.due_date_label.setText(QCoreApplication.translate("IncidentDialog", u"Venciment", None))
        self.tags_label.setText(QCoreApplication.translate("IncidentDialog", u"Etiquetes", None))
    # retranslateUi

