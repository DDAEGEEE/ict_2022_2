# Image Pyramids
import os

import cv2

IMG_PATH = "../images"

# todo
# 새로운 img 불러와서    #  img = cv2.imread(os.path.join(filepath, IMG_PATH, "summit.jpeg"))
# lower를 한번더 lower    # lowerAgain = cv2.pryDown(lower_reso)
# higher를 한번더 higher  # higherAgain = cv2.pryUp(higher_reso)
# imwrite로 모두 저장     # 



if __name__ == "__main__":
    img = cv2.imread(os.path.join(IMG_PATH, "lena.jpeg"))

    lower_reso = cv2.pryDown(img)
    higher_reso = cv2.pyrUp(img)

    cv2.imshow("img", img)
    cv2.imshow("lower", lower_reso)
    cv2.imshow("higher", higher_reso)

    cv2.waitKey(0)
    cv2.destroyAllWindows()