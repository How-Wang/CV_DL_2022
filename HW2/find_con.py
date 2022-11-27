import cv2

class find_contour(object):
    def __init__(self, imgl_path, imgr_path):
        self.img1_path = imgl_path
        self.img2_path = imgr_path
    
    def change_imgl_path(self, imgl_path):
        self.img1_path = imgl_path

    def change_imgr_path(self, imgr_path):
        self.img2_path = imgr_path

    def draw_contour(self):
        img1 = cv2.imread(self.img1_path)
        img2 = cv2.imread(self.img2_path)
        img1_small = cv2.resize(img1, (0,0), fx=0.5, fy=0.5) 
        img2_small = cv2.resize(img2, (0,0), fx=0.5, fy=0.5) 
        img1_gray = cv2.cvtColor(img1_small, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2_small, cv2.COLOR_BGR2GRAY)
        img1_blurred = cv2.GaussianBlur(img1_gray, (11, 11), 0)
        img2_blurred = cv2.GaussianBlur(img2_gray, (11, 11), 0)
        img1_binary = cv2.Canny(img1_blurred, 20, 160)
        img2_binary = cv2.Canny(img2_blurred, 20, 160)
        _ , thresh1 = cv2.threshold(img1_binary, 127, 255, 0)
        _ , thresh2 = cv2.threshold(img2_binary, 127, 255, 0)
        _, contours1, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours2, _ = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        img1_con = cv2.drawContours(img1_small, contours1, -1, (0,255,0), 3)
        img2_con = cv2.drawContours(img2_small, contours2, -1, (0,255,0), 3)
        cv2.imshow("img1", img1_con)
        cv2.imshow("img2", img2_con)
     
        