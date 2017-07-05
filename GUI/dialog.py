from PyQt4.QtGui import QFileDialog

def openImageChooserDialog():
    return openChooserDialog(categories="Image files (*.jpg)")

def openVideoChooserDialog():
    return openChooserDialog(categories="Video files (*.mp4)")

def openChooserDialog(categories="Image files (*.jpg);;Video files (*.mp4)"):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename = QFileDialog.getOpenFileName(None, "Choose File.." , "", categories, options=options)
    return filename