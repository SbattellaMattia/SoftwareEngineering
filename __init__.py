import ctypes
import os
import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import myRes


class ButtonTemplate(QMainWindow):
    def __init__(self,uiFile):
        super().__init__()
        print(uiFile)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        loadUi(uiFile, self)
        # a quanto pare questo trucchetto richiede la versione 5 di pyqt
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QtGui.QIcon('ico/museum_white.ico'))
        self.exitButton.clicked.connect(self.close)
        self.maximizeButton.clicked.connect(self.maximize)
        self.reduceButton.clicked.connect(self.showMinimized)

        self.maxHeight=self.height()

        # ATTENZIONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # dopo tantissimo try&error ho scoperto che gli errori di rendering sono dovuti
        # alle seguenti cose:
        # • la superclasse DEVE essere la stessa classe dell'elemento alla radice del .ui
        # • il CSS nell'elemento radice CAUSA UN MACELLO DI PROBLEMI!
        #   PERSINO COMMENTARLO NON RISOLVE, DEVE ESSERE PROPRIO TOLTO!
        #   ce lo rimettiamo poi nel file qui sotto, ora funziona tutto.
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.setStyleSheet(open('ui/css/main.css', 'r').read())

        # poiché si perdono i margini, li setto manualmente
        for bigButton in list(filter(lambda el:'bigbutton'in el.lower(),self.__dict__.keys())):
            getattr(self,bigButton).setMargin(17)

    def maximize(self):
        if self.height() > 48:
            self.setMinimumHeight(48)
            self.setMaximumHeight(48)
            self.titoloLabel.setGeometry(self.titoloLabel.geometry().x(),9,self.geometry().width()-130,
                                         self.titoloLabel.geometry().height())
        else:
            self.setMaximumHeight(self.maxHeight)
            self.setMinimumHeight(self.maxHeight)
            self.titoloLabel.setGeometry(self.titoloLabel.geometry().x(), 57, self.geometry().width()-60,
                                         self.titoloLabel.geometry().height())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        if event.pos().y() > 50:
            return
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True
        QApplication.setOverrideCursor(Qt.SizeAllCursor)


    def mouseReleaseEvent(self, event):
        self.pressing = False
        QApplication.restoreOverrideCursor()

    def mouseMoveEvent(self, event):
        if 'pressing' in self.__dict__.keys() and self.pressing:
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

    filenames = list(filter(lambda file: '.ui' in file and 'template' not in file.lower(),
                            next(os.walk('ui'), (None, None, []))[2]))

    app = QApplication(sys.argv)
    print(len(filenames))
    mainWidget = ButtonTemplate('ui/'+filenames[23])
    mainWidget.show()
    sys.exit(app.exec())
