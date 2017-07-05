from mode_chooser_window import Window as ModeChooser
import sys
from PyQt4.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModeChooser()
    window.show()
    sys.exit(app.exec_())