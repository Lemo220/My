import dxcam
import cv2
import numpy as np


class ScreenCapture:
    def __init__(self):
        self.cam = dxcam.create()
        self.cam.start()

    def get_frame(self):
        frame = self.cam.get_latest_frame()
        if frame is not None:
            return cv2.cvtColor(np.array(frame), cv2.COLOR_BGRA2BGR)
        return None

    def stop(self):
        self.cam.stop()
