# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mode_chooser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.separate_video_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_video_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.separate_video_btn.setFont(font)
        self.separate_video_btn.setObjectName(_fromUtf8("separate_video_btn"))
        self.gridLayout_2.addWidget(self.separate_video_btn, 0, 1, 1, 1)
        self.general_video_btn = QtGui.QPushButton(self.centralwidget)
        self.general_video_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.general_video_btn.setFont(font)
        self.general_video_btn.setObjectName(_fromUtf8("general_video_btn"))
        self.gridLayout_2.addWidget(self.general_video_btn, 0, 0, 1, 1)
        self.general_img_btn = QtGui.QPushButton(self.centralwidget)
        self.general_img_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.general_img_btn.setFont(font)
        self.general_img_btn.setObjectName(_fromUtf8("general_img_btn"))
        self.gridLayout_2.addWidget(self.general_img_btn, 1, 0, 1, 1)
        self.separate_img_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_img_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.separate_img_btn.setFont(font)
        self.separate_img_btn.setObjectName(_fromUtf8("separate_img_btn"))
        self.gridLayout_2.addWidget(self.separate_img_btn, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.separate_video_btn.setText(_translate("MainWindow", "Seperate Video Model", None))
        self.general_video_btn.setText(_translate("MainWindow", "General Video Model", None))
        self.general_img_btn.setText(_translate("MainWindow", "General Image Model", None))
        self.separate_img_btn.setText(_translate("MainWindow", "Seperate Image Model", None))

