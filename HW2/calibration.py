import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

class calibration(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def change_folder_path(self, folder_path):
        self.folder_path = folder_path
        self.picfiles = [join(self.folder_path, f) for f in listdir(self.folder_path) if isfile(join(self.folder_path, f))]
    
    def find_corners(self):
        img_array = []
        for i in self.picfiles:
            img = cv2.imread(i)
            ret, corners = cv2.findChessboardCorners(img, (11, 8), flags= cv2.CALIB_CB_FAST_CHECK)
            if ret:
                img_chess = cv2.drawChessboardCorners(img, (11, 8), corners, ret)
                height, width, layers = img_chess.shape
                size = (width, height)
                img_array.append(img_chess)
        out = cv2.VideoWriter('find_chess_corners.avi', 0, 0.6, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture('find_chess_corners.avi')
        if (cap.isOpened()== False):
            print("Error opening video file")
        while(cap.isOpened()):
        # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                frame_small = cv2.resize(frame, (0,0), fx=0.3, fy=0.3) 
                cv2.imshow('Frame', frame_small)
                if cv2.waitKey(1500) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def find_instrinsic(self):
        pass

    def find_extrinsic(self):
        pass

    def find_distortion(self):
        pass

    def show_result(self):
        pass