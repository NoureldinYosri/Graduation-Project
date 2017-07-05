from mode_chooser_layout import Ui_MainWindow as ModeChooserUI, _translate
from PyQt4.QtGui import *
from image_nn import ImageClassifier
import cv2, dialog
from commentator_window import Window as CommentWindow

class Window(QMainWindow, ModeChooserUI):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", "Online Detection of Key Events in Football Matches", None))
        self.classifier = ImageClassifier()
        self.general_video_btn.clicked.connect(self.onGeneralVideoClicked)
        self.general_img_btn.clicked.connect(self.onGeneralImageClicked)
        # self.separate_video_btn.clicked.connect(self.onSeperateVideoClicked)
        # self.separate_img_btn.clicked.connect(self.onSeperateImageClicked)

    def onGeneralVideoClicked(self, event):
        path = dialog.openVideoChooserDialog()
        commentWindow = CommentWindow()
        commentWindow.show()
        if path:
            camera = cv2.VideoCapture(path)
            while True:
                ret, img = camera.read()
                cv2.imshow('Selected Video', img)
                event_type = self.classifier.classify(img)
                commentWindow.showComment(str(event_type))
                while (cv2.waitKey(1) & 0xFF) != ord('q'):
                        continue;
                

    def onGeneralImageClicked(self, event):
        path = dialog.openImageChooserDialog()
        if path:
            img = cv2.imread(path)
            print(self.classifier.classify(img))