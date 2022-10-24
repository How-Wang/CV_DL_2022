import cv2
import numpy as np
import math 

class edge_detection(object):
    def __init__(self, img_path):
        self.img_path = img_path

    def change_img_path(self, img_path):
        self.img_path = img_path

    def gau_blur(self):
        # read image file
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (height, width) = img.shape
        # padding original
        pad_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
        # kernel 
        gau_ker = np.array([[math.exp(-(x**2+y**2)) for x in range(-1,2)] for y in range(-1,2)])
        gau_ker = gau_ker/np.sum(gau_ker)
        # gaussian filter
        gau_img = np.zeros((height, width), img.dtype)
        for i in range(0, height):
            for j in range(0, width):
                temp = 0
                for k in range(0,3):
                    for p in range(0,3):
                        temp += gau_ker[k, p] * pad_img[i+k, j+p]
                gau_img[i, j] = temp
    
        cv2.imshow("Gaussian Blur", gau_img)
        cv2.imshow("Original", img)

    def sobel_x(self):
        # read image file
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (height, width) = img.shape
        # padding original
        pad_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
        # kernel 
        sobx_ker = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        # sobel x filter
        sobx_img = np.zeros((height, width))
        for i in range(0, height):
            for j in range(0, width):
                temp = 0
                for k in range(0,3):
                    for p in range(0,3):
                        temp += sobx_ker[k, p] * pad_img[i+k, j+p]
                if temp < 0:
                    temp = 0
                elif temp > 255:
                    temp = 255
                sobx_img[i, j] = temp
        sobx_img = sobx_img.astype(img.dtype)
        cv2.imshow("Sobel X", sobx_img)
        cv2.imshow("Original", img)

    def sobel_y(self):
        # read image file
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (height, width) = img.shape
        # padding original
        pad_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
        # kernel 
        soby_ker = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        # sobel y filter
        soby_img = np.zeros((height, width))
        for i in range(0, height):
            for j in range(0, width):
                temp = 0
                for k in range(0,3):
                    for p in range(0,3):
                        temp += soby_ker[k, p] * pad_img[i+k, j+p]
                if temp < 0:
                    temp = 0
                elif temp > 255:
                    temp = 255
                soby_img[i, j] = temp
        soby_img = soby_img.astype(img.dtype)
        cv2.imshow("Sobel Y", soby_img)
        cv2.imshow("Original", img)

    def magnitude(self):
        # read image file
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (height, width) = img.shape
        # padding original
        pad_img = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)

        # kernel 
        soby_ker = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        sobx_ker = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        # magnitude filter
        mag_img = np.zeros((height, width))
        for i in range(0, height):
            for j in range(0, width):
                tempy = 0
                tempx = 0
                for k in range(0,3):
                    for p in range(0,3):
                        tempy += soby_ker[k, p] * pad_img[i+k, j+p]
                        tempx += sobx_ker[k, p] * pad_img[i+k, j+p]
                if tempy < 0:
                    tempy = 0
                elif tempy > 255:
                    tempy = 255
                if tempx < 0:
                    tempx = 0
                elif tempx > 255:
                    tempx = 255
                mag_img[i, j] = math.sqrt(tempy**2 + tempx**2)
        mag_img = mag_img.astype(img.dtype)
        cv2.imshow("Original", img)
        cv2.imshow("Magnitude", mag_img)

