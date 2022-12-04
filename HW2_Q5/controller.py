from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2
import matplotlib.pyplot as plt
from UI import Ui_MainWindow
from PIL import Image
from torch import nn
import torch
import torchvision
from torchvision import transforms
import torchvision.datasets as datasets
from torchsummary import summary

import cv2
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.img_path = ''
        self.ui.Load_img_btn.clicked.connect(self.open_img)
        self.ui.Show_img_btn.clicked.connect(self.show_img)
        self.ui.Show_dis_btn.clicked.connect(self.show_distribution)
        self.ui.Show_mod_btn.clicked.connect(self.show_model_stru)
        self.ui.Show_cmp_btn.clicked.connect(self.show_compare)
        self.ui.Inf_btn.clicked.connect(self.inference)

    def open_img(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        self.ui.Res_lab.setText('')
        img = cv2.imread(self.img_path)

        resize_img = cv2.resize(img, (224, 224))
        height, width, channel = resize_img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(resize_img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.Img_lab.setPixmap(QPixmap.fromImage(self.qimg))

    def show_img(self):
        cat_path = './inference_dataset/Cat/8043.jpg'
        dog_path = './inference_dataset/Dog/12051.jpg'
        fig = plt.figure(figsize=(10, 7))

        cat_img = Image.open(cat_path).resize((224,224), Image.ANTIALIAS)
        fig.add_subplot(1,2, 1)
        plt.imshow(cat_img)
        plt.axis('off')
        plt.title('Cat')

        dog_img = Image.open(dog_path).resize((224,224), Image.ANTIALIAS)
        fig.add_subplot(1,2, 2)
        plt.imshow(dog_img)
        plt.axis('off')
        plt.title('Dog')
        plt.show()

    def show_distribution(self):
        # catfiles = [f for f in listdir('./training_dataset/Cat') if isfile(join('./training_dataset/Cat', f))]
        # dogfiles = [f for f in listdir('./training_dataset/Dog') if isfile(join('./training_dataset/Dog', f))]
        # print(len(catfiles), len(dogfiles))
        data = {'Cat':5412, 'Dog':10788}
        courses = list(data.keys())
        values = list(data.values())
        # creating the bar plot
        fig = plt.figure(figsize = (7, 4))

        plt.bar(courses, values, color ='#7eb54e' , width = 0.8)
        for i in range(len(courses)):
            plt.text(i, values[i]+5, values[i], ha = 'center')
        plt.xlabel("")
        plt.ylabel("No. of Images")
        plt.title("Class Distribution")
        plt.show()

    def show_model_stru(self):
        model = torchvision.models.resnet50(pretrained = False)
        nr_filters = model.fc.in_features  #number of input features of last layer
        model.fc = nn.Linear(nr_filters, 1)
        summary(model.cuda(), (3, 224, 224))

    def show_compare(self):
        # focal 0.7477
        # BCE 0.7089
        data = {'Focal Loss':74.77, 'Binary Cross Entropy':70.89}
        courses = list(data.keys())
        values = list(data.values())
        # creating the bar plot
        fig = plt.figure(figsize = (7, 4))

        plt.bar(courses, values, color ='#7eb54e' , width = 0.8)
        for i in range(len(courses)):
            plt.text(i, values[i], values[i], ha = 'center')
        plt.xlabel("")
        plt.ylabel("Accuraccy (%)")
        plt.title("Accuraccy Comparison")
        plt.show()

    def inference(self):
        img = Image.open(self.img_path).convert('RGB').resize((224,224), Image.ANTIALIAS)
        tfms = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        # unsqueeze provides the batch dimension
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        img_tensor = tfms(img).to(device).unsqueeze(0)

        model = torch.load('./batch30_epoch30_focal.pt')
        model.eval()
        output = model(img_tensor)
        # m = nn.Sigmoid()
        # output = m(output)

        # # to binarize the output since I had only 1 class
        output = (output.squeeze().cpu().detach().numpy())
        # print(output)

        label = 'Cat' if output < 0.5 else 'Dog'
        # print(label)
        self.ui.Res_lab.setText(label)