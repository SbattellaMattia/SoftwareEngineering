import ctypes
import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import res


class ButtonTemplate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        loadUi('ui/VendiOpera.ui',self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        self.setWindowIcon(QtGui.QIcon('ico/museum.ico'))
        self.exitButton.clicked.connect(self.close)
        self.reduceButton.clicked.connect(self.showMinimized)
        # self.immagineLabel.setMargin(12)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.width(),
                                    self.height())
            self.start = self.end

if __name__ == "__main__":

    myappid = 'museum.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    mainWidget = ButtonTemplate()
    mainWidget.show()
    sys.exit(app.exec())
