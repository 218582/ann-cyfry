# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from mWindow import Ui_MainWindow
import mnist_loader
from ann import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()
        self.show()
        self.ui.display.viewport().installEventFilter(self)
        self.ui.clear.setEnabled(False)
        self.ui.check.setEnabled(False)
        self.ui.clear.clicked.connect(self.clearDisplay)
        self.ui.check.clicked.connect(self.checkDigit)
        self.ui.drawable.stateChanged.connect(self.changingMode)
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
        self.isPainter = False
        self.painter.end()

    def displayImage(self, name):
        self.ui.display.resetCachedContent()
        self.scene.addPixmap(QtGui.QPixmap(name).scaled(420,420))
        self.ui.display.setScene(self.scene)

    def displayToArray(self):
        obrazek = self.canvas.scaled(28,28).toImage()
        # obrazek = obrazek.convertToFormat(QtGui.QImage.Format_Mono, flags = QtCore.Qt.MonoOnly)
        obrazek.save("obrazekZGui.bmp", "BMP")
        tablica = np.array([np.zeros(1)])
        for y in range(0, 28):
            for x in range (0, 28):
                pxl = obrazek.pixel(x,y)
                color = QtGui.QColor(pxl).getRgbF()
                tablica = np.append(tablica, [[color[0]]], axis = 0)
        tablica = np.delete (tablica, 0, 0)
        return tablica

    def checkDigit(self):
        inp = self.displayToArray()
        digit = NN.forwardPropagation(inp)
        print digit
        maxi = np.amax(digit)
        self.ui.certainty.setText("%.2f%%" % (maxi * 100))
        recognised = np.where (digit == maxi)[0][0]
        self.ui.digit.setText(str(recognised) )

    def clearDisplay(self):
        QtGui.QPixmapCache.clear()
        self.canvas.fill(color = QtCore.Qt.black)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def drawCircle(self, point):
        self.painter.drawEllipse(point.x(), point.y(), 30, 30)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def initTimer(self, ms, handler):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(ms)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), handler)

    # Obsługa klaiwatury
    def keyPressEvent (self, event):
        pass

    def changingMode(self):
        if self.ui.drawable.isChecked():
            self.drawingMode()
        else:
            self.displayMode()

    def displayMode(self):
        self.ui.clear.setEnabled(False)
        self.ui.check.setEnabled(False)
        self.ui.prv.setEnabled(True)
        self.ui.next.setEnabled(True)
        self.endPainter()

    def drawingMode(self):
        self.ui.clear.setEnabled(True)
        self.ui.check.setEnabled(True)
        self.ui.prv.setEnabled(False)
        self.ui.next.setEnabled(False)
        self.initPainter()

    def drawLoop(self):
        pozycja = self.ui.display.mapFromGlobal(QtGui.QCursor.pos())
        if pozycja.x() < myapp.ui.display.width() and pozycja.y() < myapp.ui.display.height():
            self.drawCircle(pozycja)

    def eventFilter(self, source, event):
        if self.ui.drawable.isChecked():
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
        if self.ui.drawable.isChecked():
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
    # Obsluga sieci neuronowej
    # from ann import *
    # NN = NeuralNet([3, 4, 2])

    # training_data, validation_data, data_test = mnist_loader.load_data_wrapper()
    # test = QtGui.QPixmap("mnistFile0.bmp")
    NN = NeuralNet ([784, 30, 10])
    # NN.SGD(training_data, 1, 10, 3.0, data_test=data_test)
    # obrazek = test.toImage()
    # obrazek.save("obrazekZGui.bmp", "BMP")
    # tablica = np.array([np.zeros(1)])
    # for x in range(0, 28):
    #     for y in range (0, 28):
    #         pxl = obrazek.pixel(x,y)
    #         color = QtGui.QColor(pxl).getRgbF()
    #         tablica = np.append(tablica, [[color[0]]], axis = 0)
    # tablica = np.delete (tablica, 0, 0)
    # print NN.forwardPropagation(tablica)
    # /Obsluga sieci neuronowej
    # del training_data, validation_data, data_test
    sys.exit(app.exec_())
            # print "Trzymasz"
