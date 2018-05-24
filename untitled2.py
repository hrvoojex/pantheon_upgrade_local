# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 547)
        Dialog.setMinimumSize(QtCore.QSize(401, 384))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 381, 131))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 91, 34))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 410, 381, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 371, 81))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(12, 40, 361, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 310, 381, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(10, 30, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Odabir upravo preuzete datoteke Pantheon.exe"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Klikni ovdje i odaberi upravo preuzetu datoteku Pantheon.exe"))
        self.pushButton.setText(_translate("Dialog", "Nadogradi"))
        self.groupBox_2.setTitle(_translate("Dialog", "Status"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Dialog", "Preuzimanje novije datoteke Pantheon.exe"))
        self.pushButton_2.setText(_translate("Dialog", "Preuzmi"))
        self.groupBox_4.setTitle(_translate("Dialog", "Proces"))

