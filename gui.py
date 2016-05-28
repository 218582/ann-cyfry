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

    def endPainter(self):
        self.painter.end()

    def displayImage (self, name):
        self.ui.display.resetCachedContent()
        self.scene.addPixmap(QtGui.QPixmap(name).scaled(420,420))
        self.ui.display.setScene(self.scene)

    def __del__(self):
        self.endPainter()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    # #Rysowanie
    # myapp.painter.drawEllipse(210, 210, 20, 20)
    # myapp.scene.addPixmap(myapp.canvas)
    # myapp.ui.display.setScene(myapp.scene)
    # myapp.ui.display.resetCachedContent()
    # #/Rysowanie
    # # Wyswietlanie
    # myapp.displayImage("mnistFile0.bmp")
    # # /Wyswietlanie
    myapp.show()
    sys.exit(app.exec_())
