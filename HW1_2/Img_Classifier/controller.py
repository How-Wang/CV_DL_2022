from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2
from UI import Ui_MainWindow
from img_class import img_classifier

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.img_path = ''
        self.img_classifier = img_classifier()
        self.ui.Load_Img_btn.clicked.connect(self.open_img)
        self.ui.Show_Img_btn.clicked.connect(self.img_classifier.show_train_img)
        self.ui.Show_mod_btn.clicked.connect(self.img_classifier.show_model_stru)
        self.ui.Show_Dat_btn.clicked.connect(self.img_classifier.show_data_aug)
        self.ui.Show_Accu_btn.clicked.connect(self.img_classifier.show_accu_loss)
        self.ui.Infer_btn.clicked.connect(self.img_classifier.inference)

    def open_img(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.img_classifier.load_img(self.img_path)
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.Img_lab.setPixmap(QPixmap.fromImage(self.qimg))
    
        