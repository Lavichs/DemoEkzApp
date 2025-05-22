# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partner_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(495, 420)
        Form.setMinimumSize(QSize(495, 420))
        Form.setMaximumSize(QSize(495, 420))
        Form.setStyleSheet(u"background:  white;\n"
"color: black;")
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 60, 471, 301))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.edt_title = QLineEdit(self.formLayoutWidget)
        self.edt_title.setObjectName(u"edt_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edt_title)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.edt_type = QLineEdit(self.formLayoutWidget)
        self.edt_type.setObjectName(u"edt_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edt_type)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.edt_headmaster = QLineEdit(self.formLayoutWidget)
        self.edt_headmaster.setObjectName(u"edt_headmaster")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edt_headmaster)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.edt_mail = QLineEdit(self.formLayoutWidget)
        self.edt_mail.setObjectName(u"edt_mail")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.edt_mail)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.edt_phone = QLineEdit(self.formLayoutWidget)
        self.edt_phone.setObjectName(u"edt_phone")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.edt_phone)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.edt_address = QLineEdit(self.formLayoutWidget)
        self.edt_address.setObjectName(u"edt_address")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.edt_address)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.edt_inn = QLineEdit(self.formLayoutWidget)
        self.edt_inn.setObjectName(u"edt_inn")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.edt_inn)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.edt_rating = QLineEdit(self.formLayoutWidget)
        self.edt_rating.setObjectName(u"edt_rating")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.edt_rating)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.btn_create = QPushButton(Form)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(30, 370, 201, 34))
        self.btn_edit = QPushButton(Form)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(260, 370, 201, 34))
        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 10, 91, 34))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"type", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"headmaster", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"mail", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"phone", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"address", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"INN", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"rating", None))
        self.label.setText(QCoreApplication.translate("Form", u"title", None))
        self.btn_create.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

