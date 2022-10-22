import cv2

class img_smooth(object):
    def __init__(self, img1_path, img2_path):
        self.img1_path = img1_path
        self.img2_path = img2_path
    
    def change_img1_path(self, img1_path):
        self.img1_path = img1_path

    def change_img2_path(self, img2_path):
        self.img2_path = img2_path

    def gau_update(self, val):
        img = cv2.imread(self.img1_path)
        if val>0:
            k = val*2 + 1
            gau_img = cv2.GaussianBlur(img, (k, k), 0)
            cv2.imshow("Gaussian", gau_img)
        else: 
            cv2.imshow("Gaussian", img)
        
    def gau(self):
        cv2.namedWindow("Gaussian")
        img = cv2.imread(self.img1_path)
        cv2.imshow("Gaussian", img)
        cv2.createTrackbar('magnitude', 'Gaussian', 0, 10, self.gau_update)
        cv2.setTrackbarPos('magnitude', 'Gaussian', 0)

    def bil_update(self, val):
        img = cv2.imread(self.img1_path)
        if val>0:
            k = val*2 + 1
            bil_img = cv2.bilateralFilter(img, k, 90, 90)
            cv2.imshow("Bilateral", bil_img)
        else: 
            cv2.imshow("Bilateral", img)

    def bil(self):
        cv2.namedWindow("Bilateral")
        img = cv2.imread(self.img1_path)
        cv2.imshow("Bilateral", img)
        cv2.createTrackbar('magnitude', 'Bilateral', 0, 10, self.bil_update)
        cv2.setTrackbarPos('magnitude', 'Bilateral', 0)

    def med_update(self, val):
        img = cv2.imread(self.img1_path)
        if val>0:
            k = val*2 + 1
            med_img = cv2.medianBlur(img, k)
            cv2.imshow("Median", med_img)
        else: 
            cv2.imshow("Median", img)

    def med(self):
        cv2.namedWindow("Median")
        img = cv2.imread(self.img1_path)
        cv2.imshow("Median", img)
        cv2.createTrackbar('magnitude', 'Median', 0, 10, self.med_update)
        cv2.setTrackbarPos('magnitude', 'Median', 0) 