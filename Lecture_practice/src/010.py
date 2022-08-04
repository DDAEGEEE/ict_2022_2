# Histogram (히스토그램)
import os

import cv2
from matplotlib import pyplot as plt

IMG_PATH = "C:/Users/LG/Documents/GitHub/ict_2022_2/Lecture_practice/images"


def image_hist(image):
    cv2.imshow("input", image)
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])    # i : 0,1,2 / 
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


    if __name__ == "__main__":
        src = cv2.imread(os.path.join(IMG_PATH, "logo.png"))

        cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        cv2.imshow("input", gray)

        # custom_hist(gray)
        image_hist(src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()