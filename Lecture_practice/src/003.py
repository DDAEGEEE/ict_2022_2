# pixel
import os

import cv2
import utils

IMG_PATH = "C:/Users/LG/Documents/GitHub/ict_2022_2/Lecture_practice/images"

if __name__== "__main__":
    img = cv2.imread(os.path.join(IMG_PATH, "logo.png"))

    h, w, c = img.shape
    for row in range(h):
        for col in range(w):
            b, g, r = img[row, col]
            b = 255 - b
            g = 255 - g
            r = 255 - r
            img[row, col] = [b, g, r]

    utils.show_img(img, "output image")