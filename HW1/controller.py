from ctypes import sizeof
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.img1_path = ''
        self.img2_path = ''
        self.ui.Load_img1_btn.clicked.connect(self.open_img1)
        self.ui.Load_img2_btn.clicked.connect(self.open_img2)
        self.ui.Color_sep_btn.clicked.connect(self.color_sep)
        self.ui.Color_tran_btn.clicked.connect(self.color_tran)
        self.ui.Color_det_btn.clicked.connect(self.color_dec)
        self.ui.Blend_btn.clicked.connect(self.blend)

    def open_img1(self):
        self.img1_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Load_img1_label.setText(self.img1_path.split('/')[-1])


    def open_img2(self):
        self.img2_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        print("img2_paht is:{}".format(self.img2_path))
        self.ui.Load_img2_label.setText(self.img2_path.split('/')[-1])

    def color_sep(self):
        img = cv2.imread(self.img1_path)
        cv2.imshow("Original", img)
        (B, G, R) = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        cv2.imshow("B channel", cv2.merge([B,zeros, zeros]))
        cv2.imshow("G channel", cv2.merge([zeros, G, zeros]))
        cv2.imshow("R channel", cv2.merge([zeros, zeros, R]))

    def color_tran(self):
        img = cv2.imread(self.img1_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("OpenCV function", gray_img)
        (B, G, R) = cv2.split(img)
        aver_img = (B/3+G/3+R/3).astype('uint8')
        cv2.imshow("Average weighted", aver_img)

    def color_dec(self):
        img = cv2.imread(self.img1_path)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        green_mask = cv2.inRange(hsv_img, np.array([40,50,20]), np.array([80, 255, 255]))
        white_mask = cv2.inRange(hsv_img, np.array([0,0,200]), np.array([180, 20, 255]))
        green_img = cv2.bitwise_and(img, img, mask=green_mask)
        white_img = cv2.bitwise_and(img, img, mask=white_mask)
        cv2.imshow("Green", green_img)
        cv2.imshow("White", white_img)
        
    def blend_update(self, val):
        img1 = cv2.imread(self.img1_path)
        img2 = cv2.imread(self.img2_path)
        new_size = (min(img1.shape[0],img2.shape[0]), min(img1.shape[1], img2.shape[1]))
        img1 = cv2.resize(img1,new_size)
        img2 = cv2.resize(img2,new_size)
        blend_img = cv2.addWeighted(img1, val/255, img2, 1-(val/255), 0)
        cv2.imshow("Blend", blend_img)

    def blend(self):
        cv2.namedWindow("Blend")
        cv2.createTrackbar('Blend', 'Blend', 0, 255, self.blend_update)
        cv2.setTrackbarPos('Blend', 'Blend', 127)


