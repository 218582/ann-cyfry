# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon May 30 03:55:27 2016
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
        MainWindow.resize(795, 576)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.display = QtGui.QGraphicsView(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 30, 422, 422))
        self.display.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.display.setObjectName(_fromUtf8("display"))
        self.drawable = QtGui.QCheckBox(self.centralwidget)
        self.drawable.setGeometry(QtCore.QRect(520, 30, 97, 22))
        self.drawable.setObjectName(_fromUtf8("drawable"))
        self.check = QtGui.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(520, 80, 111, 41))
        self.check.setObjectName(_fromUtf8("check"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 190, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(520, 140, 111, 41))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 300, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.digit = QtGui.QLabel(self.centralwidget)
        self.digit.setGeometry(QtCore.QRect(520, 270, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.digit.setFont(font)
        self.digit.setText(_fromUtf8(""))
        self.digit.setObjectName(_fromUtf8("digit"))
        self.certainty = QtGui.QLabel(self.centralwidget)
        self.certainty.setGeometry(QtCore.QRect(520, 380, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.certainty.setFont(font)
        self.certainty.setText(_fromUtf8(""))
        self.certainty.setObjectName(_fromUtf8("certainty"))
        self.prv = QtGui.QPushButton(self.centralwidget)
        self.prv.setGeometry(QtCore.QRect(30, 460, 161, 41))
        self.prv.setObjectName(_fromUtf8("prv"))
        self.next = QtGui.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(290, 460, 161, 41))
        self.next.setObjectName(_fromUtf8("next"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 25))
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
        self.actionZapisz_sie = QtGui.QAction(MainWindow)
        self.actionZapisz_sie.setObjectName(_fromUtf8("actionZapisz_sie"))
        self.menuSie_neuronowa.addAction(self.actionTrenuj)
        self.menuSie_neuronowa.addAction(self.actionWczytaj_wagi)
        self.menuSie_neuronowa.addAction(self.actionZapisz_sie)
        self.menubar.addAction(self.menuSie_neuronowa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.drawable.setText(_translate("MainWindow", "Rysuj", None))
        self.check.setText(_translate("MainWindow", "Sprawdź", None))
        self.label.setText(_translate("MainWindow", "Rozpoznano cyfrę : ", None))
        self.clear.setText(_translate("MainWindow", "Wyczyść", None))
        self.label_2.setText(_translate("MainWindow", "Pewność rozpoznania:", None))
        self.prv.setText(_translate("MainWindow", "Poprzedni", None))
        self.next.setText(_translate("MainWindow", "Nastepny", None))
        self.menuSie_neuronowa.setTitle(_translate("MainWindow", "Sieć neuronowa", None))
        self.actionTrenuj.setText(_translate("MainWindow", "Trenuj", None))
        self.actionWczytaj_wagi.setText(_translate("MainWindow", "Wczytaj sieć", None))
        self.actionZapisz_sie.setText(_translate("MainWindow", "Zapisz sieć", None))

