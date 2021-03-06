# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWebEngineWidgets, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 1200)
        MainWindow.setWindowOpacity(0.6)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("file:///home/andrew/Code/Repositories/web-projects/MySite/test.html"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        MainWindow.setCentralWidget(self.centralwidget)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class TickerApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TickerApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = TickerApp()
    window.show()
    # form.showFullScreen()
    app.exec_()

if __name__ == '__main__':
    main()
