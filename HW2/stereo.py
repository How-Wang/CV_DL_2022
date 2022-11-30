import cv2
import numpy as np
class stereo_disparity(object):
    def __init__(self, imgl_path, imgr_path):
        self.img1_path = imgl_path
        self.img2_path = imgr_path

    def change_imgl_path(self, imgl_path):
        self.img1_path = imgl_path

    def change_imgr_path(self, imgr_path):
        self.img2_path = imgr_path

    def stereo_disparity_map(self):
        imgL_gray = cv2.imread(self.img1_path, 0)
        imgR_gray = cv2.imread(self.img2_path, 0)
        # imgL_gray = cv2.resize(imgL_gray, (0,0), fx=0.3, fy=0.3) 
        # imgR_gray = cv2.resize(imgR_gray, (0,0), fx=0.3, fy=0.3) 

        imgL = cv2.imread(self.img1_path)
        imgR = cv2.imread(self.img2_path)
        imgL = cv2.resize(imgL, (0,0), fx=0.3, fy=0.3) 
        imgR = cv2.resize(imgR, (0,0), fx=0.3, fy=0.3) 
        cv2.imshow("imgL", imgL)
        cv2.imshow("imgR", imgR)

        stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
        disparity = stereo.compute(imgL_gray, imgR_gray).astype(np.float32)/32.0
        disparity = cv2.resize(disparity, (0,0), fx=0.3, fy=0.3)
        cv2.imshow("disparity", disparity)
        # disparity[disparity < 0 ] = 0
        # disparity[disparity > 255] = 255

        def draw_right(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                ### here is wrong !!!
                # print("(x={}, y={})".format(x, y))
                print("(x={}, y={}, disparity[x,y]={})".format(x, y, disparity[y][x]))
                temp_imgR = cv2.circle(imgR.copy(), (x-int(disparity[y][x]),y), radius=10, color=(0, 0, 255), thickness=-1)
                cv2.imshow("imgR",temp_imgR)
                cv2.waitKey(500)
        
        cv2.setMouseCallback('imgL',draw_right)
        while(1):
            cv2.imshow("imgR",imgR)
            k=cv2.waitKey(1)
            if k==ord('q'):
                break
        cv2.destroyAllWindows()
