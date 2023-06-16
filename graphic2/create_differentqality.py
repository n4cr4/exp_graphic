import numpy as np
import cv2 as cv

img = cv.imread('./img/target.JPG')

for i in [1,5,10,20,40,80]:
    cv.imwrite(f'./img/output/target_{i}.jpg', img, [cv.IMWRITE_JPEG_QUALITY, i])