import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class ButtonTemplate(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowFlags(QtCore.Qt.WindowType.Window.Dialog)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        loadUi('ui/ButtonTemplate.ui',self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        self.setWindowIcon(QtGui.QIcon('ico/museum.ico'))
        self.setStatusBar(None)
        self.setMenuBar(None)
        # QtGui.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.close)
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWidget = ButtonTemplate()
    mainWidget.show()
    sys.exit(app.exec())
