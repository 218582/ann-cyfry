import sys
from PyQt4 import QtCore, QtGui

from mWindow import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()
        self.initPainter()

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
        self.scene.clear()
        self.ui.display.setScene(self.scene)

    def drawCircle(self, point):
        self.painter.drawEllipse(point.x(), point.y(), 20, 20)
        self.scene.addPixmap(self.canvas)
        self.ui.display.setScene(self.scene)

    def initTimer(self, ms, handler):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(ms)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), handler)

    def __del__(self):
        self.endPainter()



def Pos():
    pozycja = myapp.ui.display.mapFromGlobal(QtGui.QCursor.pos())
    if pozycja.x() < myapp.ui.display.width() and pozycja.y() < myapp.ui.display.height():
        myapp.drawCircle(pozycja)

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
    myapp.initTimer(20, Pos)
    myapp.timer.start()
    # /Uzywanie timera
    myapp.show()
    sys.exit(app.exec_())
