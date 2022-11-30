import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

class calibration(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.img_array = []
        self.objpoints = []
        self.cornerpoints = []
        self.size = ''
        self.cameraMatrix = ''
        self.distCoeffs = ''
        self.rvecs = ''
        self.tvecs = ''
        
    def change_folder_path(self, folder_path):
        self.folder_path = folder_path
        self.picfiles = [join(self.folder_path, f) for f in listdir(self.folder_path) if isfile(join(self.folder_path, f))]
    
    def find_chess_board(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((11*8,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        self.img_array = []
        self.objpoints = []
        self.cornerpoints = []
        for i in self.picfiles:
            img = cv2.imread(i)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (11, 8), flags= cv2.CALIB_CB_NORMALIZE_IMAGE)
            # Find out corners
            if ret:
                self.objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                self.cornerpoints.append(corners2)

                img_chess = cv2.drawChessboardCorners(img, (11, 8), corners, ret)
                height, width, layers = img_chess.shape
                self.size = (width, height)
                self.img_array.append(img_chess)
                
            else:
                print("{} is not found chess".format(i))
        retval, self.cameraMatrix, self.distCoeffs, self.rvecs, self.tvecs = cv2.calibrateCamera(self.objpoints, self.cornerpoints, self.size, None, None)

    def find_corners(self):
        self.find_chess_board()
        # Create Vedio
        out = cv2.VideoWriter('find_chess_corners.avi', 0, 0.6, self.size)
        for i in range(len(self.img_array)):
            out.write(self.img_array[i])
        out.release()
        # Play Vedio
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
        self.find_chess_board()
        print("Intrinsic:")
        print(self.cameraMatrix)
        
    def find_extrinsic(self, pic_num):
        print(pic_num-1)
        self.find_chess_board()
        print("Extrinsic:")
        print(np.concatenate((cv2.Rodrigues(self.rvecs[pic_num-1])[0], self.tvecs[pic_num-1]), axis=-1))

    def find_distortion(self):
        self.find_chess_board()
        print("Distortion:")
        print(self.distCoeffs)

    def show_result(self):
        self.find_chess_board()
        for i in self.picfiles:
            img = cv2.imread(i)
            h,  w = img.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(self.cameraMatrix, self.distCoeffs, (w,h), 1, (w,h))
            # undistort
            img_undst = cv2.undistort(img, self.cameraMatrix, self.distCoeffs, None, newcameramtx)
            # crop the image
            x, y, w, h = roi
            img_undst = img_undst[y:y+h, x:x+w]
            img_undst_small = cv2.resize(img_undst, (0,0), fx=0.3, fy=0.3)
            img_small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            cv2.imshow('distorted', img_small)
            cv2.imshow('undistorted', img_undst_small)
            cv2.waitKey(1500)
        cv2.destroyAllWindows()