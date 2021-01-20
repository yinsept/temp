from PyQt5 import QtCore, QtWidgets
from v1.CameraWidget import CameraWidget
from v1.Camera import Camera
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        cam1 = Camera("rtsp://admin:DERRUH@192.168.1.87:554/H.264")
        cam1.connect()
        self.cam1 = CameraWidget(cam1, self.centralwidget)
        self.cam1.setObjectName("cam1")
        self.cam1.setGeometry(QtCore.QRect(30,30,500,500))
        cam2 = Camera(0)
        cam2.connect()
        self.cam2 = CameraWidget(cam2, self.centralwidget)
        self.cam2.setObjectName("cam2")
        self.cam2.setGeometry(QtCore.QRect(560,30,500,500))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)