import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

class AR(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.picfiles = []
        self.objpoints = []
        self.cornerpoints = []
        self.size = ''


    def change_folder_path(self, folder_path):
        self.folder_path = folder_path
        self.picfiles = [join(self.folder_path, f) for f in listdir(self.folder_path) if isfile(join(self.folder_path, f))]

    def find_chess_board(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((11*8,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        self.objpoints = []
        self.cornerpoints = []
        for i in self.picfiles:
            img = cv2.imread(i)
            height, width, layers = img.shape
            self.size = (width, height)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (11, 8), flags= cv2.CALIB_CB_NORMALIZE_IMAGE)
            # Find out corners
            if ret:
                self.objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                self.cornerpoints.append(corners2)
            else:
                print("{} is not found chess".format(i))
        retval, self.cameraMatrix, self.distCoeffs, self.rvecs, self.tvecs = cv2.calibrateCamera(self.objpoints, self.cornerpoints, self.size, None, None)
    
    def show_from_fs(self, fs, input_text):
        self.find_chess_board()
        for pic_num in range(len(self.picfiles)):
            img = cv2.imread(self.picfiles[pic_num])
            for ch_num in range(len(input_text)):
                ch = fs.getNode(input_text[ch_num]).mat()
                for stroke_num in range(len(ch)):
                    if  (ch_num==0): axis = np.float32(ch[stroke_num]+[[7, 5, 0],[7, 5, 0]]).reshape(-1, 3)
                    elif(ch_num==1): axis = np.float32(ch[stroke_num]+[[4, 5, 0],[4, 5, 0]]).reshape(-1, 3)
                    elif(ch_num==2): axis = np.float32(ch[stroke_num]+[[1, 5, 0],[1, 5, 0]]).reshape(-1, 3)
                    elif(ch_num==3): axis = np.float32(ch[stroke_num]+[[7, 2, 0],[7, 2, 0]]).reshape(-1, 3)
                    elif(ch_num==4): axis = np.float32(ch[stroke_num]+[[4, 2, 0],[4, 2, 0]]).reshape(-1, 3)
                    elif(ch_num==5): axis = np.float32(ch[stroke_num]+[[1, 2, 0],[1, 2, 0]]).reshape(-1, 3)
                    imgpts, jac = cv2.projectPoints(axis, self.rvecs[pic_num], self.tvecs[pic_num], self.cameraMatrix, self.distCoeffs)
                    img = cv2.line(img, tuple(imgpts[0].ravel()), tuple(imgpts[1].ravel()), (0, 0, 225), 5)
            img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_AREA)
            cv2.imshow('img', img)
            cv2.waitKey(1500)
        cv2.destroyAllWindows()

    def show_wob(self, input_text):
        fs = cv2.FileStorage('./Dataset_OpenCvDl_Hw2/Q3_Image/Q2_lib/alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
        self.show_from_fs(fs, input_text)

    def show_wv(self, input_text):
        fs = cv2.FileStorage('./Dataset_OpenCvDl_Hw2/Q3_Image/Q2_lib/alphabet_lib_vertical.txt', cv2.FILE_STORAGE_READ)
        self.show_from_fs(fs, input_text)
