from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2
from UI import Ui_MainWindow
from img_class import img_classifier
from PIL import Image
import torch
from torchvision import transforms

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
        self.ui.Infer_btn.clicked.connect(self.inference)

    def open_img(self):
        self.ui.Class_lab.setText('')
        self.img_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.img_classifier.load_img(self.img_path)
        img = cv2.imread(self.img_path)

        resize_img = cv2.resize(img, (224, 224))
        height, width, channel = resize_img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(resize_img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.Img_lab.setPixmap(QPixmap.fromImage(self.qimg))
    
    def inference(self):
        img = Image.open(self.img_path).convert('RGB').resize((224,224), Image.ANTIALIAS)
        tfms = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        # unsqueeze provides the batch dimension
        img_tensor = tfms(img).to('cuda').unsqueeze(0)

        model = torch.load('model_epoch_30.pt')
        model.eval()
        output = model(img_tensor)
        # to binarize the output since I had only 1 class
        output = (output.squeeze().cpu().detach().numpy())
        cor_class_list = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        self.ui.Class_lab.setText(cor_class_list[output.argmax(axis=0)])