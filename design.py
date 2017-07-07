# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 246)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 131))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = ClickableLineEdit(self.groupBox)  # My subclassed
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 91, 34))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 381, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 341, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Biranje datoteke"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Klikni ovdje i odaberi datoteku"))
        self.pushButton.setText(_translate("Dialog", "Nadogradi"))
        self.label.setText(_translate("Dialog", "Odaberi datoteku:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Status"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))


class ClickableLineEdit(QtWidgets.QLineEdit):
    """Subclassing QLineEdit class to make it clickable."""
    clicked = QtCore.pyqtSignal()  # signal when the text entry is left clicked

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)
