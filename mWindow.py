# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri May 27 16:19:00 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1056, 660)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.display = QtGui.QGraphicsView(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 30, 422, 422))
        self.display.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.display.setObjectName(_fromUtf8("display"))
        self.next = QtGui.QCommandLinkButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(260, 470, 185, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setIconSize(QtCore.QSize(50, 50))
        self.next.setCheckable(True)
        self.next.setChecked(False)
        self.next.setObjectName(_fromUtf8("next"))
        self.prv = QtGui.QCommandLinkButton(self.centralwidget)
        self.prv.setGeometry(QtCore.QRect(40, 470, 185, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.prv.setFont(font)
        self.prv.setCheckable(True)
        self.prv.setChecked(False)
        self.prv.setObjectName(_fromUtf8("prv"))
        self.drawable = QtGui.QCheckBox(self.centralwidget)
        self.drawable.setGeometry(QtCore.QRect(520, 30, 97, 22))
        self.drawable.setObjectName(_fromUtf8("drawable"))
        self.check = QtGui.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(520, 80, 98, 27))
        self.check.setObjectName(_fromUtf8("check"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 150, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(670, 80, 98, 27))
        self.clear.setObjectName(_fromUtf8("clear"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSie_neuronowa = QtGui.QMenu(self.menubar)
        self.menuSie_neuronowa.setObjectName(_fromUtf8("menuSie_neuronowa"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTrenuj = QtGui.QAction(MainWindow)
        self.actionTrenuj.setObjectName(_fromUtf8("actionTrenuj"))
        self.actionWczytaj_wagi = QtGui.QAction(MainWindow)
        self.actionWczytaj_wagi.setObjectName(_fromUtf8("actionWczytaj_wagi"))
        self.menuSie_neuronowa.addAction(self.actionTrenuj)
        self.menuSie_neuronowa.addAction(self.actionWczytaj_wagi)
        self.menubar.addAction(self.menuSie_neuronowa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.next.setText(_translate("MainWindow", "Nastepny", None))
        self.prv.setText(_translate("MainWindow", "Poprzedni", None))
        self.drawable.setText(_translate("MainWindow", "Rysuj", None))
        self.check.setText(_translate("MainWindow", "Sprawdź", None))
        self.label.setText(_translate("MainWindow", "Rozpoznano cyfrę : n", None))
        self.clear.setText(_translate("MainWindow", "Wyczyść", None))
        self.menuSie_neuronowa.setTitle(_translate("MainWindow", "Sieć neuronowa", None))
        self.actionTrenuj.setText(_translate("MainWindow", "Trenuj", None))
        self.actionWczytaj_wagi.setText(_translate("MainWindow", "Wczytaj wagi", None))
