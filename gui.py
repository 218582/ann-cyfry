# -*- coding: utf-8 -*-
# import sys
# from PyQt4 import QtGui, QtCore, uic
#
##Aby działało należy wpisać sudo apt-get install python-qt4
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     app.setStyle("cleanlooks")
#
#     data = QtCore.QStringList()
#     data << "Jeden" << "Dwa" << "Trzy" << "Cztery"
#
#     listWidget = QtGui.QListWidget()
#     listWidget.show()
#     listWidget.addItems(data)
#
#     count = listWidget.count()
#     for i in range(count):
#         item = listWidget.item(i)
#         item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
#
#     combobox = QtGui.QComboBox()
#     combobox.show()
#     combobox.addItems(data)
#
#     sys.exit (app.exec_())


### GUI wygenerowane z QtDesignera

import sys
from PyQt4 import QtCore, QtGui

from test_gui import Ui_Form


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
