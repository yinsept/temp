from threading import Thread
import cv2
import time
class Frame:
    def __init__(self, frame = None, time = .0):
        self.frame = frame
        self.time = time
        self.status = False

class Camera:
    def __init__(self, source):
        self.source = source
        self.capture = None
        self.current_frame = Frame()
        self.cached_frames = []
        self.isOnline = False

    def connect(self):
        def t_connect():
            print ("[" + str(self.source) + "] is connecting...")
            self.capture = cv2.VideoCapture(self.source)
            if self.capture.isOpened():
                self.isOnline = True
                print ("[" + str(self.source) + "] is connected!")
                while self.isOnline:
                    self.current_frame.status, self.current_frame.frame = self.capture.read()
                    if self.current_frame.status:
                        self.current_frame.time = time.time()
                        self.cached_frames.append(self.current_frame)
                    else:
                        self.disconnect()
                    time.sleep(0.02)
        thread = Thread(target=t_connect, args=(), daemon=True)
        thread.start()
    
    def disconnect(self):
        if self.isOnline:
            self.isOnline = False
            self.capture.release()
            self.cached_frames = []
            self.current_frame = Frame()
    
    def clean_cache(self, frame):
        while True:
            t = time.time()
            for frame in self.cached_frames:
                if t - frame.time:
                    
            
    def export_cache(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        name = str(self.source) + "-" + str(time.time()) + ".avi"
        out = cv2.VideoWriter(name, fourcc, 20.0, (640,480))
        for frame in self.cached_frames:
            out.write(frame)
        out.release()
