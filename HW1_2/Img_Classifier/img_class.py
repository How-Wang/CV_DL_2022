from pickle import NONE
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torchvision
from torchvision import transforms
import torchvision.datasets as datasets
from torchsummary import summary
import cv2

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class img_classifier(object):
    def __init__(self):
        self.img_path = ''
        self.cifar_trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=None)
        self.cifar_testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=None)

    def load_img(self, img_path):
        self.img_path = img_path
        
    def show_train_img(self):
        pic_list = [NONE]*9
        class_lab_list = [NONE]*9
        cor_class_list = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        fig = plt.figure(figsize=(10, 7))
        for i in range(9):
            (pic_list[i], class_lab_list[i]) = (self.cifar_trainset.__getitem__(i)[0], cor_class_list[self.cifar_trainset.__getitem__(i)[1]])
            fig.add_subplot(3,3, i+1)
            plt.imshow(pic_list[i])
            plt.axis('off')
            plt.title(class_lab_list[i])
        plt.show()

    def show_model_stru(self):
        vgg = torchvision.models.vgg19()
        summary(vgg.cuda(), (3, 224, 224))

    def show_data_aug(self):
        fig = plt.figure(figsize=(10, 7))
        img = Image.open(self.img_path).resize((224,224), Image.ANTIALIAS)
        fig.add_subplot(3,3, (1, 6))
        plt.imshow(img)
        plt.axis('off')
        plt.title('Original')

        CJ_tranform = transforms.Compose([
            transforms.ColorJitter(brightness=(0.3,1.5),contrast=(0.3,0.5))
            ])
        CJ_img = CJ_tranform(img)
        fig.add_subplot(3, 3, 7)
        plt.imshow(CJ_img)
        plt.axis('off')
        plt.title('ColorJitter')

        RA_tranform = transforms.Compose([
            transforms.RandomAffine(degrees= (0,10) ,shear=10)
            ])
        RA_img = RA_tranform(img)
        fig.add_subplot(3,3, 8)
        plt.imshow(RA_img)
        plt.axis('off')
        plt.title('RandomAffine')

        RC_tranform = transforms.Compose([
            transforms.RandomCrop(size= (240,240), padding=30,padding_mode='symmetric')
            ])
        RC_img = RC_tranform(img)
        fig.add_subplot(3,3, 9)
        plt.imshow(RC_img)
        plt.axis('off')
        plt.title('RandomCrop')
        plt.show()

    def show_accu_loss(self):
        la_img = cv2.imread('./la.png')
        cv2.imshow('accuraccy and loss', la_img)
