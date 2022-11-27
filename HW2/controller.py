from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog

from UI import Ui_MainWindow
from find_con import find_contour
from calibration import calibration
from augmented import AR
from stereo import stereo_disparity

import cv2

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.folder_path = ''
        self.imgl_path = ''
        self.imgr_path = ''
        self.find_contour = find_contour(self.imgl_path, self.imgr_path)
        self.calibration = calibration(self.folder_path)
        self.AR = AR(self.folder_path)
        self.stereo_disparity = stereo_disparity(self.imgl_path, self.imgr_path)

        self.ui.Load_folder_btn.clicked.connect(self.open_folder)
        self.ui.Load_imgl_btn.clicked.connect(self.open_imgl)
        self.ui.Load_imgr_btn.clicked.connect(self.open_imgr)
        self.ui.Draw_con_btn.clicked.connect(self.find_contour.draw_contour)
        self.ui.Count_ring_btn.clicked.connect(self.count_rings)
        self.ui.Find_cor_btn.clicked.connect(self.calibration.find_corners)
        self.ui.Find_intrin_btn.clicked.connect(self.calibration.find_instrinsic)
        self.ui.Find_extrin_btn.clicked.connect(self.calibration.find_extrinsic)
        self.ui.Find_dis_btn.clicked.connect(self.calibration.find_distortion)
        self.ui.Show_res_btn.clicked.connect(self.calibration.show_result)
        self.ui.Show_wob_btn.clicked.connect(self.AR.show_wob)
        self.ui.Show_wv_btn.clicked.connect(self.AR.show_wv)
        self.ui.Stereo_dis_btn.clicked.connect(self.stereo_disparity.stereo_disparity_map)

    def open_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Open file", "./")
        self.ui.Load_folder_lab.setText(self.folder_path.split('/')[-1])
        self.calibration.change_folder_path(self.folder_path)
        self.AR.change_folder_path(self.folder_path)

    def open_imgl(self):
        self.imgl_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Load_imgl_lab.setText(self.imgl_path.split('/')[-1])
        self.find_contour.change_imgl_path(self.imgl_path)
        self.stereo_disparity.change_imgl_path(self.imgl_path)

    def open_imgr(self):
        self.imgr_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Load_imgr_lab.setText(self.imgr_path.split('/')[-1])
        self.find_contour.change_imgr_path(self.imgr_path)
        self.stereo_disparity.change_imgr_path(self.imgr_path)

    def count_rings(self):
        img1 = cv2.imread(self.imgl_path)
        img2 = cv2.imread(self.imgr_path)
        img1_small = cv2.resize(img1, (0,0), fx=0.5, fy=0.5) 
        img2_small = cv2.resize(img2, (0,0), fx=0.5, fy=0.5) 
        img1_gray = cv2.cvtColor(img1_small, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2_small, cv2.COLOR_BGR2GRAY)
        img1_blurred = cv2.GaussianBlur(img1_gray, (11, 11), 0)
        img2_blurred = cv2.GaussianBlur(img2_gray, (11, 11), 0)
        img1_binary = cv2.Canny(img1_blurred, 20, 160)
        img2_binary = cv2.Canny(img2_blurred, 20, 160)
        _ , thresh1 = cv2.threshold(img1_binary, 127, 255, 0)
        _ , thresh2 = cv2.threshold(img2_binary, 127, 255, 0)
        _, contours1, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours2, _ = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.ui.Show_img1_lab.setText("There are {} rings in {}".format(int(len(contours1)/4), self.imgl_path.split('/')[-1]))
        self.ui.Show_img2_lab.setText("There are {} rings in {}".format(int(len(contours2)/4), self.imgr_path.split('/')[-1]))