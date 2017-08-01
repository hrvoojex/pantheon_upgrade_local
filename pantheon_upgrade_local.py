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

import sys, os, platform
from PyQt5 import QtWidgets, QtCore, QtGui
from design2 import Ui_Dialog  # import from my 'design2.py' module


class Main(QtWidgets.QWidget):
    """The main widget with label and LineEdit."""

    # Create a signal
    #copied_percent_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Local changes of design2.py file
        self.ui.lineEdit = ClickableLineEdit(self.ui.groupBox)
        self.ui.lineEdit.setGeometry(QtCore.QRect(140, 30, 231, 31))
        self.ui.lineEdit.setObjectName("lineEdit")

        # Write a system info in label_3
        self.ui.label_3.setText(
            platform.system() + ' ' + platform.release() + '\n'
            + platform.version() + ' ' + '\n' + platform.machine())
        # call 'selectfile_Dialog' method  if ClickedLineEdit object is clicked
        self.ui.lineEdit.clicked.connect(self.selectfile_Dialog)
        # call 'pushButtonAction' method when 'pushButton' is pressed
        self.ui.pushButton.clicked.connect(self.pushButtonAction)
        # Open a link in a default browser
        self.ui.label_2.linkActivated.connect(self.link)
        self.ui.label_2.setText(
            '<a href="https://drive.google.com/drive/folders/'
            '0B_fNrhELg9mKSnFyU0JIQVNqZmc">Download link - Pantheon.exe</a>')
        self.ui.label_2.setAlignment(QtCore.Qt.AlignCenter)

    def link(self, linkStr):

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(linkStr))

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
            self, 'Open File', '', 'Binary executable (*.exe)', None)
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

    def pushButtonAction(self):
        """Press the left click on pushButton."""
        self.ui.pushButton.setDisabled(True)
        self.src_file = self.ui.lineEdit.text()
        self.dst_file = self.where_to_save()
        self.file_size = os.stat(self.src_file).st_size
        self.copyfileobj(self.src_file, self.dst_file, self.my_callback)
        #self.copied_percent_signal.connect(self.on_count_change)
        print("Finished succesfully.")
        self.ui.label_3.setText("Nadogradna uspješno završena!")

    def on_count_change(self, value):
        self.ui.progressBar.setValue(value)

    def my_callback(self, temp_file_size):
        percent = int(temp_file_size/self.file_size*100)
        print("Copiedd: {}".format(percent))
        #self.copied_percent_signal.emit(percent)
        self.ui.progressBar.setValue(percent)

    def copyfileobj(self, fsrc, fdst, callback, length=16*1024):
        copied = 0
        with open(fsrc, "rb") as fr, open(fdst, "wb") as fw:
            while True:
                buff = fr.read(length)
                if not buff:
                    break
                fw.write(buff)
                copied += len(buff)
                callback(copied)


class ClickableLineEdit(QtWidgets.QLineEdit):
    """Subclassing QLineEdit class to make it clickable."""
    clicked = QtCore.pyqtSignal()  # signal when the text entry is left clicked

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)


class About(QtWidgets.QWidget):
    """Widget for about information"""

    def __init__(self, parent=None):
        super().__init__(parent)

        #aboutWidget = QtWidgets.QWidget()
        aboutLabel = QtWidgets.QLabel(self)
        aboutLabel.setText("Autor: Hrvoje T.\nDatum: srpanj, 2017.\n")


class MyApp(QtWidgets.QMainWindow):
    """Main application class."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        """Initialize UI of an application."""
        # main window size, title
        self.setGeometry(400, 300, 400, 525)
        self.setWindowTitle("Pantheon - nadogradnja verzije ")
        self.setWindowIcon(QtGui.QIcon('pan_ico.png'))

        # Create central widget and set is as centra widget
        self.centralWidget = Main(self)
        self.setCentralWidget(self.centralWidget)

        # Create menubar with actions
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Zatvori aplikaciju')
        exitAction.triggered.connect(QtWidgets.qApp.quit)

        aboutAction = QtWidgets.QAction(QtGui.QIcon('about.png'), 'About', self)
        aboutAction.setShortcut('Ctrl+B')
        aboutAction.setStatusTip('O aplikaciji')
        aboutAction.triggered.connect(self.showAbout)

        programAction = QtWidgets.QAction(QtGui.QIcon('program.png'), 'Program', self)
        programAction.setShortcut('Ctrl+P')
        programAction.setStatusTip('Pokreni program')
        programAction.triggered.connect(self.showMain)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(programAction)
        fileMenu.addAction(exitAction)
        aboutMenu = menubar.addMenu('&About')
        aboutMenu.addAction(aboutAction)

    def showAbout(self):
        """Show the About widget"""
        self.about = About(self)
        self.about.show()
        self.setCentralWidget(self.about)


    def showMain(self):
        """Hide the About widget"""
        self.centralWidget = Main(self)
        self.setCentralWidget(self.centralWidget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
