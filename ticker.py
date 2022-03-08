# coding: utf-8

import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):


    def __init__(self):
        super().__init__()


        # set the title
        self.setWindowTitle("Ticker")

        self.setWindowOpacity(0.5)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl("file:///home/andrew/Code/Repositories/web-projects/MySite/test.html"))

        self.view.show()

        # setting  the geometry of window
        self.setGeometry(60, 60, 300, 1200)

        # show all the widgets
        self.show()


# create pyqt5 app
sys.argv.append("--disable-web-security")
App = QApplication(sys.argv)

# create the instance of our Window
window = QMainWindow()

# start the app
sys.exit(App.exec())
