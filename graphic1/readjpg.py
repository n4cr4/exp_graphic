import numpy as np
import cv2 as cv

img = cv.imread('./img/target.JPG')

cv.namedWindow('target', cv.WINDOW_NORMAL)
cv.imshow('target' ,img)
cv.waitKey(0)
cv.destroyAllWindows()
