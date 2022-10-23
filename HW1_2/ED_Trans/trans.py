import cv2
import numpy as np
class transformation(object):
    def __init__(self, img_path):
        self.img_path = img_path

    def change_img_path(self, img_path):
        self.img_path = img_path

    def resize(self):
        img = cv2.imread(self.img_path)
        (height, width, channel) = img.shape
        new_h = int(height/2)
        new_w = int(width/2)
        resize_img = cv2.resize(img, (new_h, new_w))
        resize_img = cv2.copyMakeBorder(resize_img,0,new_h,0,new_w,cv2.BORDER_CONSTANT,value=0)
        back_img = np.zeros((height, width, channel), img.dtype)
        resize_img += back_img
        cv2.imshow("Resize", resize_img)
        cv2.imwrite('resize.png', resize_img)
    
    def translation(self):
        img = cv2.imread("./resize.png")
        (height, width, channel) = img.shape
        transM = np.float32([[1, 0, width/2], [0, 1, height/2]])
        trans_img = cv2.warpAffine(img, transM, (width, height))
        trans_img += img
        cv2.imshow("Translation", trans_img)
        cv2.imwrite('translation.png', trans_img)

    def rot_scal(self):
        img = cv2.imread("./translation.png")
        (height, width, channel) = img.shape
        new_h = int(height/2)
        new_w = int(width/2)
        rotM = cv2.getRotationMatrix2D((new_w, new_h), 45, 0.5)
        rot_img = cv2.warpAffine(img, rotM, (width, height))
        cv2.imshow("rotation and scale", rot_img)
        cv2.imwrite('rotation_scale.png', rot_img)

    def shearing(self):
        img = cv2.imread("./rotation_scale.png")
        (height, width, channel) = img.shape
        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[100,50],[100,250]])
        shearM = cv2.getAffineTransform(pts1,pts2)
        shear_img = cv2.warpAffine(img, shearM, (width, height))
        cv2.imshow("shearing", shear_img)
        cv2.imwrite('shearing.png', shear_img)
