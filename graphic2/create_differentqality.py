import numpy as np
import cv2 as cv

img = cv.imread('./img/q100_s.jpg')

for i in [1,5,10,20,40,80]:
    cv.imwrite(f'./img/output/q100s_s_{i}.jpg', img, [cv.IMWRITE_JPEG_QUALITY, i])