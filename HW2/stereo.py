import cv2

class stereo_disparity(object):
    def __init__(self, imgl_path, imgr_path):
        self.img1_path = imgl_path
        self.img2_path = imgr_path

    def change_imgl_path(self, imgl_path):
        self.img1_path = imgl_path

    def change_imgr_path(self, imgr_path):
        self.img2_path = imgr_path

    def stereo_disparity_map(self):
        pass