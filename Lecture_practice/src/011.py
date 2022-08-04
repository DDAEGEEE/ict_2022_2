import cv2
import numpy as np
import utils

IMG_PATH = "C:/Users/LG/Documents/GitHub/ict_2022_2/Lecture_practice/images"


if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    imag = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    utils.show_img(img)

    img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    utils.show_img(img)

    img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    utils.show_img(img)

    img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    utils.show_img(img)

