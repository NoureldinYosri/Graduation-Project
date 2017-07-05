from commentator_layout import Ui_MainWindow as CommentatorUI, _translate
from PyQt4.QtGui import *

class Window(QMainWindow, CommentatorUI):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", "Event Detected", None))

    def showComment(self, comment):
        self.comment_label.setText(comment)

    