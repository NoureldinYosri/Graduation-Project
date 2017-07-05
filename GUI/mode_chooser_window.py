from mode_chooser_layout import Ui_MainWindow as ModeChooserUI, _translate
from PyQt4.QtGui import *
from image_nn import ImageClassifier
import cv2, dialog
from commentator_window import Window as CommentWindow
from window import Manager as WindowManager
from player_tracker import tracker as PlayerTracker

comment_map = {
    0: "Ball maybe out!", 
    1: "Ball is out!",
    3: "Celebration!",
    4: "Goal!",
    6: "Replay!",
    7: "Free Kick!",
    8: "Goal Kick!",
    10: "Pitch Invasion!",
    11: "Non-Offensive Assault",
    13: "Offensive Assault"
}

default_comment = "*Talking about the weather and how the stadium is well secured*"

def getComment(key):
    return comment_map.get(key, default_comment)

class Window(QMainWindow, ModeChooserUI):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", "Online Detection of Key Events in Football Matches", None))
        self.classifier = ImageClassifier()
        self.commentary = CommentWindow()
        self.general_video_btn.clicked.connect(self.onGeneralVideoClicked)
        self.general_img_btn.clicked.connect(self.onGeneralImageClicked)
        # self.separate_video_btn.clicked.connect(self.onSeperateVideoClicked)
        # self.separate_img_btn.clicked.connect(self.onSeperateImageClicked)
        self.track_players_btn.clicked.connect(self.onTrackPlayersClicked)
        # self.track_ball_btn.clicked.connect(self.onTrackBallClicked)

    def onTrackPlayersClicked(self, event):
        player_tracker = PlayerTracker()
        path = dialog.openVideoChooserDialog()
        if path:
            camera = cv2.VideoCapture(path)
            while True:
                ret, img = camera.read()
                img = player_tracker.update_and_draw_box(img) 
                cv2.imshow("Player Tracking", img)       
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def showEvent(self, event_type, img):
        cv2.imshow("LiveStream", img)
        if event_type != None:
            self.commentary.showComment(getComment(event_type))
            self.commentary.show()

    def onGeneralVideoClicked(self, event):
        path = dialog.openVideoChooserDialog()
        windowManager = WindowManager()
        if path:
            camera = cv2.VideoCapture(path)
            self.commentary.showComment(default_comment)
            while True:
                ret, img = camera.read()
                event_type = self.classifier.classify(img)
                event_type = windowManager.add(event_type)
                self.showEvent(event_type, img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def onGeneralImageClicked(self, event):
        path = dialog.openImageChooserDialog()
        if path:
            img = cv2.imread(path)
            event_type = self.classifier.classify(img)
            self.showEvent(event_type, img)