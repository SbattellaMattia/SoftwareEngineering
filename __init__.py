import sys

from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi


class ButtonTemplate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.Window.Dialog)
        loadUi('ui/ButtonTemplate.ui',self)
        self.setWindowIcon(QtGui.QIcon('ico/museum.ico'))
        QtGui.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWidget = ButtonTemplate()
    mainWidget.show()
    sys.exit(app.exec())
