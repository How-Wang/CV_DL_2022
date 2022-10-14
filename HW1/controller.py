from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from img_pro import img_process
from img_smo import img_smooth
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
        self.img_pro = img_process(img1_path=self.img1_path, img2_path=self.img2_path)
        self.img_smo = img_smooth(img1_path=self.img1_path, img2_path=self.img2_path)
        self.ui.Load_img1_btn.clicked.connect(self.open_img1)
        self.ui.Load_img2_btn.clicked.connect(self.open_img2)

        self.ui.Color_sep_btn.clicked.connect(self.img_pro.color_sep)
        self.ui.Color_tran_btn.clicked.connect(self.img_pro.color_tran)
        self.ui.Color_det_btn.clicked.connect(self.img_pro.color_dec)
        self.ui.Blend_btn.clicked.connect(self.img_pro.blend)
        self.ui.Gau_btn.clicked.connect(self.img_smo.gau)
        self.ui.Bil_btn.clicked.connect(self.img_smo.bil)
        self.ui.Med_btn.clicked.connect(self.img_smo.med)

    def open_img1(self):
        self.img1_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Load_img1_label.setText(self.img1_path.split('/')[-1])
        self.img_pro.change_img1_path(self.img1_path)
        self.img_smo.change_img1_path(self.img1_path)

    def open_img2(self):
        self.img2_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Load_img2_label.setText(self.img2_path.split('/')[-1])
        self.img_pro.change_img2_path(self.img2_path)
        self.img_smo.change_img2_path(self.img2_path)
