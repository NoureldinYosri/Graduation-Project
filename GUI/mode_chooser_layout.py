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
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(231, 208, 208);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240)\n"
""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.general_img_btn = QtGui.QPushButton(self.centralwidget)
        self.general_img_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.general_img_btn.setFont(font)
        self.general_img_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.general_img_btn.setObjectName(_fromUtf8("general_img_btn"))
        self.gridLayout_2.addWidget(self.general_img_btn, 3, 0, 1, 1)
        self.separate_video_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_video_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.separate_video_btn.setFont(font)
        self.separate_video_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.separate_video_btn.setObjectName(_fromUtf8("separate_video_btn"))
        self.gridLayout_2.addWidget(self.separate_video_btn, 2, 1, 1, 1)
        self.separate_img_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_img_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.separate_img_btn.setFont(font)
        self.separate_img_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.separate_img_btn.setObjectName(_fromUtf8("separate_img_btn"))
        self.gridLayout_2.addWidget(self.separate_img_btn, 3, 1, 1, 1)
        self.general_video_btn = QtGui.QPushButton(self.centralwidget)
        self.general_video_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.general_video_btn.setFont(font)
        self.general_video_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.general_video_btn.setObjectName(_fromUtf8("general_video_btn"))
        self.gridLayout_2.addWidget(self.general_video_btn, 2, 0, 1, 1)
        self.track_players_btn = QtGui.QPushButton(self.centralwidget)
        self.track_players_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.track_players_btn.setFont(font)
        self.track_players_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.track_players_btn.setObjectName(_fromUtf8("track_players_btn"))
        self.gridLayout_2.addWidget(self.track_players_btn, 4, 0, 1, 1)
        self.track_ball_btn = QtGui.QPushButton(self.centralwidget)
        self.track_ball_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.track_ball_btn.setFont(font)
        self.track_ball_btn.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(140, 171, 255);\n"
"font: 12pt \"Arial\";"))
        self.track_ball_btn.setObjectName(_fromUtf8("track_ball_btn"))
        self.gridLayout_2.addWidget(self.track_ball_btn, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.general_img_btn.setText(_translate("MainWindow", "General Image Model", None))
        self.separate_video_btn.setText(_translate("MainWindow", "Seperate Video Model", None))
        self.separate_img_btn.setText(_translate("MainWindow", "Seperate Image Model", None))
        self.general_video_btn.setText(_translate("MainWindow", "General Video Model", None))
        self.track_players_btn.setText(_translate("MainWindow", "Track Players", None))
        self.track_ball_btn.setText(_translate("MainWindow", "Track Ball", None))
        self.label.setText(_translate("MainWindow", "Choose one of the below modes of operation:", None))

