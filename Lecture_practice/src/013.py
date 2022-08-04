import os

import cv2
from matplotlib import pyplot as plt

# IMG_PATH = "C:/Users/LG/Documents/GitHub/ict_2022_2/Lecture_practice/images"    # 절대경로

filepath = "C:/Users/LG/Documents/GitHub/ict_2022_2/Lecture_practice" 
IMG_PATH = "./images"                                                           # ../A  <- 상위 폴더 위치에서 <A>폴더 내,   ./A   <- 현재 폴더 위치에서, <A>폴더 내

if __name__ == "__main__":
    img = cv2.imread(os.path.join(filepath, IMG_PATH, "lena.jpeg"))             # 절대 or 상대
    
    # pyplot를 사용하기 위해서 BGR을 RGB로 변환.
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])

    dst1 = cv2.blur(img, (7, 7))

    dst2 = cv2.GaussianBlur(img, (5, 5), 0)

    dst3 = cv2.medianBlur(img, 9)

    dst4 = cv2.bilateralFilter(img, 9, 75, 75)

    images = [img, dst1, dst2, dst3, dst4]
    titles = ["Original", "Blur(7X7)", "Gaussian Blur(5X5)", "Median Blur", "Bilateral"]

    for i in range(5):
        plt.subplot(3, 2, i + 1), plt.imshow(images[i]), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    #    i = 0
    #   for img, title in zip():
    #        plt.subplot(3, 2, i + 1)
    #        plt.imshow(img)
    #        plt.title(title)
    #        i = i + 1
    #        plt.xticks([])
    #        plt.yticks([])
    plt.show()