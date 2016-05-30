# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from mWindow import Ui_MainWindow
import mnist_loader
from ann import *
import mnistHandwriting as mh
NUMBER_OF_PICTURE = 10000

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()
        self.show()
        self.pictureNumber = 0
        self.ui.display.viewport().installEventFilter(self)
        self.displayMode()
        self.ui.prv.clicked.connect(self.previousPicture)
        self.ui.next.clicked.connect(self.nextPicture)
        self.ui.clear.clicked.connect(self.clearDisplay)
        self.ui.check.clicked.connect(self.checkDigit)
        self.ui.drawable.stateChanged.connect(self.changingMode)

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
        self.scene.addPixmap(QtGui.QPixmap("data/" + name).scaled(420,420))
        self.ui.display.setScene(self.scene)

    def displayToArray(self):
        obrazek = self.canvas.scaled(28,28).toImage()
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
        self.convertVectorToDigits(inp)

    def convertVectorToDigits(self, inp):
        digit = NN.forwardPropagation(inp)
        maxi = np.amax(digit)
        self.ui.certainty.setText("%.2f%%" % (maxi * 100))
        recognised = np.where (digit == maxi)[0][0]
        self.ui.digit.setText(str(recognised))

    def clearDisplay(self):
        QtGui.QPixmapCache.clear()
        self.canvas.fill(color = QtCore.Qt.black)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def previousPicture(self):
        self.pictureNumber -= 1
        self.updateDisplayAndStats()

    def nextPicture(self):
        self.pictureNumber += 1
        self.updateDisplayAndStats()

    def updateDisplayAndStats(self):
        self.displayImage("mnistFile%i.bmp" % self.pictureNumber)
        self.setButtons()
        data_part = mh.MNISTexample(self.pictureNumber, 1, bTrain = False, only01 = False)
        self.convertVectorToDigits(mhToLoader(data_part[0][0]))

    def drawCircle(self, point):
        self.painter.drawEllipse(point.x(), point.y(), 30, 30)
        self.scene.addPixmap(self.canvas)


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
            self.initPainter()
        else:
            self.displayMode()
            self.endPainter()

    def setButtons(self):
        if self.pictureNumber == 0:
            self.ui.prv.setEnabled(False)
            self.ui.next.setEnabled(True)
        elif self.pictureNumber == NUMBER_OF_PICTURE:
            self.ui.prv.setEnabled(True)
            self.ui.next.setEnabled(False)
        else:
            self.ui.prv.setEnabled(True)
            self.ui.next.setEnabled(True)

    def displayMode(self):
        self.ui.clear.setEnabled(False)
        self.ui.check.setEnabled(False)
        self.setButtons()
        self.updateDisplayAndStats()
        self.displayImage("mnistFile%i.bmp" % self.pictureNumber)


    def drawingMode(self):
        self.ui.clear.setEnabled(True)
        self.ui.check.setEnabled(True)
        self.ui.prv.setEnabled(False)
        self.ui.next.setEnabled(False)


    def drawLoop(self):
        pozycja = self.ui.display.mapFromGlobal(QtGui.QCursor.pos())
        if pozycja.x() < myapp.ui.display.width() and pozycja.y() < myapp.ui.display.height():
            self.drawCircle(pozycja)

    def eventFilter(self, source, event):
        if self.ui.drawable.isChecked():
            if event.type() == QtCore.QEvent.MouseButtonRelease and source is self.ui.display.viewport():
                self.timer.stop()
            elif event.type() == QtCore.QEvent.MouseButtonPress and source is self.ui.display.viewport():
                self.drawLoop()
                self.initTimer(0,self.drawLoop)
                self.timer.start()
        return QtGui.QWidget.eventFilter(self, source, event)

    def __del__(self):
        if self.ui.drawable.isChecked():
            self.endPainter()


## Funkcja zamienia dane pobieranie z mnistHandwriting na format przyjmowany prze
# sieć neuronową.
# \input mnist - tablica zawierajace dane TYLKO o obrazku
#
# \return tablica, które może zostac podana na wejscie sieci neuronowej
def mhToLoader(mnist):
    tablica = np.array([np.zeros(1)])
    for index in range(0, len(mnist)):
        tablica = np.append(tablica, [[mnist[index]]], axis = 0)
    tablica = np.delete (tablica, 0, 0)
    return tablica
    # result = NN.forwardPropagation(tablica)
    # maxi = np.amax(result)
    # return np.where (result == maxi)[0][0]


if __name__ == "__main__":
    NN = NeuralNet ([784, 30, 10])
    data_part = mh.MNISTexample(0, 1, bTrain = False, only01 = False)
    training_data, validation_data, data_test = mnist_loader.load_data_wrapper()
    NN.SGD(training_data, 1, 10, 3.0, data_test=data_test)
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
    # test = QtGui.QPixmap("mnistFile0.bmp")
    # print inp.shape()
    # print NN.forwardPropagation(inp)
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
