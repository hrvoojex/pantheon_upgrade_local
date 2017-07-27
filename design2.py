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
        Dialog.resize(401, 499)
        Dialog.setMinimumSize(QtCore.QSize(401, 384))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 381, 131))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 91, 34))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 360, 381, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 371, 81))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 361, 51))
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 260, 381, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(27, 40, 331, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Biranje datoteke za nadogradnju"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Klikni ovdje i odaberi datoteku"))
        self.pushButton.setText(_translate("Dialog", "Nadogradi"))
        self.label.setText(_translate("Dialog", "Odaberi datoteku:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Status"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Dialog", "Dohvaćanje datoteke Pantheon.exe"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_4.setTitle(_translate("Dialog", "Proces"))

