import os

import cv2
import utils

IMG_PATH = r"C:\Users\LG\Documents\GitHub\ict_2022_2\Lecture_code\day_5th\images"

if __name__=="__main__":
    img = cv2.imread(os.path.join(IMG_PATH,"load.jpg"))

    utils.show_img(img)