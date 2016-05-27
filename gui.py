import sys
from PyQt4 import QtCore, QtGui

from mWindow import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()

    def displayImage (self, name):
        self.ui.graphicsView.resetCachedContent()
        self.scene.addPixmap(QtGui.QPixmap(name))
        self.ui.graphicsView.setScene(self.scene)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.displayImage("mnistFile0.bmp")
    myapp.show()
    sys.exit(app.exec_())
