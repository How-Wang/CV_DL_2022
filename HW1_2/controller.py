from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog

from UI import Ui_MainWindow
from trans import transformation
from edge_det import edge_detection

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.img_path = ''
        self.transformation = transformation(self.img_path)
        self.edge_detection = edge_detection(self.img_path)
        self.ui.Img_btn.clicked.connect(self.open_img)
        self.ui.Gau_Blur_btn.clicked.connect(self.edge_detection.gau_blur)
        self.ui.Sol_X_btn.clicked.connect(self.edge_detection.sobel_x)
        self.ui.Sol_Y_btn.clicked.connect(self.edge_detection.sobel_y)
        self.ui.Mag_btn.clicked.connect(self.edge_detection.magnitude)
        self.ui.Res_btn.clicked.connect(self.transformation.resize)
        self.ui.Tran_btn.clicked.connect(self.transformation.translation)
        self.ui.Rot_Scal_btn.clicked.connect(self.transformation.rot_scal)
        self.ui.Shea_btn.clicked.connect(self.transformation.shearing)
    
    def open_img(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.transformation.change_img_path(self.img_path)
        self.edge_detection.change_img_path(self.img_path)
        self.ui.Img_lab.setText(self.img_path) # .split('/')[-1]
        
