#!/usr/bin/env python3

# coding: utf-8 -*-
""" Automatska nadogradnja Pantheona za neposlušne.

Windows:
platform.win32_ver() --> ('XP', '5.1.2600', 'SP3', 'Multiprocessor Free')
uname_result(system='Windows', node='DOMAGOJ-STROJ', release='XP',
version='5.1.2600', machine='x86', processor='x86 Family 6 Model 42 Stepping 7,
GenuineIntel')
Ako je procesor 64-bitni, onda je 'processor=AMD64'

Linux:
uname_result(system='Linux', node='probook6470b', release='4.10.0-24-generic',
version='#28-Ubuntu SMP Wed Jun 14 08:14:34 UTC 2017', machine='x86_64',
processor='x86_64')
Ako je procesor 32-bitni onda je 'processor=i686'

Ovdje je objašnjeno --> url: https://pymotw.com/2/platform/
"""

import os.path
import platform
import sys
from shutil import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_Dialog  # import from my 'design.py' module


class Main(QtWidgets.QWidget):
    """The main widget with label and LineEdit."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Write a system info in label_3
        self.ui.label_3.setText(
            platform.system() + ' ' + platform.release() + '\n'
            + platform.version() + ' ' + platform.machine())
        # call 'selectfile_Dialog' method  if ClickedLineEdit object is clicked
        self.ui.lineEdit.clicked.connect(self.selectfile_Dialog)
        # call 'pushButtonAction' method when 'pushButton' is pressed
        self.ui.pushButton.clicked.connect(self.pushButtonAction)

    def selectfile_Dialog(self, event=None):
        """
        Open a dialog for choosing a file.

        Takes two positionals arguments 'self' and 'event' because
        'mouseReleaseEvent' sends two, when creating
        new method eg. 'label1.mouseReleaseEvent = self.showText1'. When
        subclassing QLineEdit as ClickableLineEdit 'event' is None"
        """
        # QFileDialog doesn't use native OS dialog like this one:
        # 'fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')'
        # to remember last opening path
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Binary executable (*.exe)', None,
            QtWidgets.QFileDialog.DontUseNativeDialog)
        # sender is object that sends the signal
        sender = self.sender()
        # write selected file name into that QLineEdit widget 'lista_lineEdit'
        sender.setText(fname)
        # set options for combobox only from 'lista_lineEdit' QLineEdit widget

    def where_to_save(self):
        my_os_version = (
            platform.system(), platform.release(), platform.win32_ver()[2],
            platform.version(), platform.machine())

        # Asign a path based on a CPU arch
        my_x86_path = "C:/Program Files/DataLab/Pantheon.exe"
        my_x64_path = "C:/Program Files (x86)/DataLab/Pantheon.exe"

        if platform.machine() == "x86" or platform.machine() == "i686":
            my_pantheon_path = my_x86_path
        elif platform.machine() == "AMD64" or platform.machine() == "x86_64":
            my_pantheon_path = my_x64_path
        else:
            my_pantheon_path = "Unknown"
            print("No CPU architecture detected...quiting")
            sys.exit()

        return(my_pantheon_path)

    def saving(self):
        my_pantheon_path = self.where_to_save()
        copy(self.ui.lineEdit.text(), my_pantheon_path)
        print("Finished succesfully.")

    def pushButtonAction(self):
        """Press the left click on pushButton."""
        self.where_to_save()
        self.saving()


class MyApp(QtWidgets.QMainWindow):
    """Main application class."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        """Initialize UI of an application."""
        # main window size, title
        self.setGeometry(400, 300, 400, 250)
        self.setWindowTitle("Pantheon - nadogradnja verzije ")

        # Create central widget and set is as centra widget
        centralWidget = Main(self)
        self.setCentralWidget(centralWidget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
