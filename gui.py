# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from mWindow import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()
        self.show()
        self.ui.display.viewport().installEventFilter(self)
        self.initPainter()
        self.ui.clear.clicked.connect(self.clearDisplay)
        self.LeftButtonPressed = False

    def initPainter(self):
        self.canvas = QtGui.QPixmap(420,420)
        self.brush = QtGui.QBrush(QtCore.Qt.white)
        self.painter = QtGui.QPainter(self.canvas)
        self.painter.setBrush(self.brush)
        self.painter.setPen(QtCore.Qt.NoPen)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def endPainter(self):
        self.painter.end()

    def displayImage(self, name):
        self.ui.display.resetCachedContent()
        self.scene.addPixmap(QtGui.QPixmap(name).scaled(420,420))
        self.ui.display.setScene(self.scene)

    def clearDisplay(self):
        QtGui.QPixmapCache.clear()
        self.canvas.fill(color = QtCore.Qt.black)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def drawCircle(self, point):
        self.painter.drawEllipse(point.x(), point.y(), 20, 20)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def initTimer(self, ms, handler):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(ms)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), handler)

    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton:
    #         self.LeftButtonPressed = True
    #         self.drawLoop()
    #         self.initTimer(0,self.drawLoop)
    #         self.timer.start()

    # Obsługa klaiwatury
    def keyPressEvent (self, event):
        print "Przycisk"

    def drawLoop(self):
        pozycja = self.ui.display.mapFromGlobal(QtGui.QCursor.pos())
        if pozycja.x() < myapp.ui.display.width() and pozycja.y() < myapp.ui.display.height():
            self.drawCircle(pozycja)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonRelease and source is self.ui.display.viewport():
            self.LeftButtonPressed = False
            self.timer.stop()
        elif event.type() == QtCore.QEvent.MouseButtonPress and source is self.ui.display.viewport():
            self.LeftButtonPressed = True
            self.drawLoop()
            self.initTimer(0,self.drawLoop)
            self.timer.start()
        return QtGui.QWidget.eventFilter(self, source, event)

    def __del__(self):
        self.endPainter()



def Pos():
    pozycja = myapp.ui.display.mapFromGlobal(QtGui.QCursor.pos())
    if pozycja.x() < myapp.ui.display.width() and pozycja.y() < myapp.ui.display.height():
        myapp.drawCircle(pozycja)

def printClickedPos():
    if QtGui.QMouseEvent.button() == QtCore.Qt.MouseButton.LeftButton:
        print myapp.ui.display.mapFromGlobal(QtGui.QCursor.pos())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    # #Rysowanie
    # punkt = QtCore.QPoint(200,200)
    # myapp.drawCircle(punkt)
    # #/Rysowanie
    # # Wyswietlanie
    # myapp.displayImage("mnistFile0.bmp")
    # # /Wyswietlanie
    # Uzywanie timera
    # myapp.initTimer(20, Pos)
    # myapp.timer.start()
    # /Uzywanie timera
    sys.exit(app.exec_())
            # print "Trzymasz"
