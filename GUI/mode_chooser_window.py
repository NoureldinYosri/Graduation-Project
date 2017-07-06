from mode_chooser_layout import Ui_MainWindow as ModeChooserUI, _translate
from PyQt4.QtGui import *
from image_nn import ImageClassifier
import sys, cv2, dialog
from commentator_window import Window as CommentWindow
from window import Manager as WindowManager
from player_tracker import tracker as PlayerTracker
import ball_detector
sys.path.insert(0, '../')
import utils
from modules import DT

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

start_comment = "*Talking about the weather and how the stadium is well secured*"
default_comment = "Normal Play"

def getComment(key):
    return comment_map.get(key, default_comment)

def load_clfs():
    dir_list = ['..', '..', 'logger', 'final']
    clfs, fclfs = DT.read_clfs(utils.join_list(dir_list))
    return clfs, fclfs

class Window(QMainWindow, ModeChooserUI):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(_translate("MainWindow", "Online Detection of Key Events in Football Matches", None))
        self.classifier = ImageClassifier()
        self.commentary = CommentWindow()
        self.general_video_btn.clicked.connect(self.onGeneralVideoClicked)
        self.general_img_btn.clicked.connect(self.onGeneralImageClicked)
        self.separate_video_btn.clicked.connect(self.onSeperateVideoClicked)
        self.separate_img_btn.clicked.connect(self.onSeperateImageClicked)
        self.track_players_btn.clicked.connect(self.onTrackPlayersClicked)
        self.track_ball_btn.clicked.connect(self.onTrackBallClicked)

    def onSeperateVideoClicked(self, event):
        path = dialog.openVideoChooserDialog()
        window = WindowManager()
        if path:
            out = None
            camera = cv2.VideoCapture(path)
            self.commentary.showComment(start_comment)
            while True:
                ret, img = camera.read()
                clfs, fclf = load_clfs()
                dt = DT.classifier(clfs, fclf)
                x = self.classifier.transform_data(img, self.classifier.som)
                event_type = dt.predict(x)
                event_type = window.add(event_type)
                self.showEvent(event_type, img)
                if not out:
                    height, width, channels = img.shape
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width,height))
                out.write(img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            camera.release()
            out.release()

    def onSeperateImageClicked(self, event):
        path = dialog.openImageChooserDialog()
        if path:
            img = cv2.imread(path)
            clfs, fclf = load_clfs()
            dt = DT.classifier(clfs, fclf)
            x = self.classifier.transform_data(img, self.classifier.som)
            event_type = getComment(dt.predict(x))
            self.showEvent(event_type, img)

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

    def onTrackBallClicked(self, event):
        path = dialog.openVideoChooserDialog()
        if path:
            ball_detector.start_detecting(path)

    def showEvent(self, event_type, img):
        self.draw_text(img, getComment(event_type))

    def draw_text(self, frame, text, x=40, y=40):
        cv2.putText(frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,255,255), 2)
        cv2.imshow("LiveStream", frame)
            

    def onGeneralVideoClicked(self, event):
        path = dialog.openVideoChooserDialog()
        windowManager = WindowManager()
        out = cv2.VideoWriter('output.mp4', VideoWriter_fourcc(*'MP4V'), 20.0, (640,480))
        if path:
            camera = cv2.VideoCapture(path)
            self.commentary.showComment(start_comment)
            while True:
                ret, img = camera.read()
                event_type = self.classifier.classify(img)
                event_type = windowManager.add(event_type)
                self.showEvent(event_type, img)
                out.write(img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        camera.release()
        out.release()

    def onGeneralImageClicked(self, event):
        path = dialog.openImageChooserDialog()
        if path:
            img = cv2.imread(path)
            event_type = self.classifier.classify(img)
            self.showEvent(event_type, img)