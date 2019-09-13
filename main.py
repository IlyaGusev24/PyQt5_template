#!/usr/bin/python
# -*- coding: utf8 -*-


import sys
from PyQt5 import QtWidgets, QtCore, QtGui

import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('icon.png'))
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
