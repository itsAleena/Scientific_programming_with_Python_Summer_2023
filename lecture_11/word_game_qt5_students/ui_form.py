# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitWord = QtWidgets.QPushButton(self.centralwidget)
        self.submitWord.setEnabled(False)
        self.submitWord.setGeometry(QtCore.QRect(470, 430, 100, 42))
        self.submitWord.setObjectName("submitWord")
        self.handView = QtWidgets.QGraphicsView(self.centralwidget)
        self.handView.setGeometry(QtCore.QRect(30, 80, 731, 321))
        self.handView.setObjectName("handView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label.setObjectName("label")
        self.playerName = QtWidgets.QLineEdit(self.centralwidget)
        self.playerName.setGeometry(QtCore.QRect(70, 20, 113, 21))
        self.playerName.setReadOnly(True)
        self.playerName.setObjectName("playerName")
        self.wordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.wordEdit.setEnabled(False)
        self.wordEdit.setGeometry(QtCore.QRect(310, 440, 151, 21))
        self.wordEdit.setObjectName("wordEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 440, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 10, 141, 48))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(440, 10, 101, 48))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.score_label.setFont(font)
        self.score_label.setObjectName("score_label")
        self.finishGame = QtWidgets.QPushButton(self.centralwidget)
        self.finishGame.setEnabled(False)
        self.finishGame.setGeometry(QtCore.QRect(470, 490, 100, 42))
        self.finishGame.setObjectName("finishGame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPlayers = QtWidgets.QAction(MainWindow)
        self.actionPlayers.setObjectName("actionPlayers")
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPlayers)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WordGame - physics725"))
        self.submitWord.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Player:"))
        self.label_2.setText(_translate("MainWindow", "New word:"))
        self.label_3.setText(_translate("MainWindow", "Score:"))
        self.score_label.setText(_translate("MainWindow", "0"))
        self.finishGame.setText(_translate("MainWindow", "Finish game"))
        self.menuFile.setTitle(_translate("MainWindow", "Game"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionPlayers.setText(_translate("MainWindow", "Players"))