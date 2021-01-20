import time
from PyQt5 import QtGui, QtWidgets
from threading import Thread
class CameraWidget(QtWidgets.QLabel):
    def __init__(self, camera, parent=None):
        super(CameraWidget, self).__init__(parent)
        self.camera = camera
        Thread(target=self.display, args=(), daemon=True).start()
    def display(self):
        print ("Start stream [" + str(self.camera.source) + "]")
        while True:
            time.sleep(0.02)
            if self.camera.isOnline:
                try:
                    frame = self.camera.current_frame
                    rgbImage = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                    resizeImage = QtGui.QPixmap.fromImage(rgbImage)
                    self.setPixmap(resizeImage)
                except Exception:
                    pass
            else:
                print ("[" + str(self.camera.source) + "] is offline")