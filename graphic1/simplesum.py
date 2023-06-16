import numpy as np
import cv2 as cv

img_target = cv.imread('./img/target.JPG')
img_back = cv.imread('./img/back.jpg')

width = img_target.shape[1]
height = img_target.shape[0]
bpp = img_target.shape[2] * img_target.dtype.type(0).nbytes
imagesize = img_target.nbytes

img = np.zeros([height, width, bpp], dtype=np.uint8)

for h in range(height):
    for w in range(width):
        # img[h][w][0] = img_target[h][w][0]*0.5 + img_back[h][w][0]*0.5
        # img[h][w][1] = img_target[h][w][1]*0.5 + img_back[h][w][1]*0.5
        # img[h][w][2] = img_target[h][w][2]*0.5 + img_back[h][w][2]*0.5
        img[h][w][0] = img_target[h][w][0]*0.3 + img_back[h][w][0]*0.7
        img[h][w][1] = img_target[h][w][1]*0.3 + img_back[h][w][1]*0.7
        img[h][w][2] = img_target[h][w][2]*0.3 + img_back[h][w][2]*0.7

# cv.namedWindow('target', cv.WINDOW_NORMAL)
# cv.imshow('target' ,img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# cv.imwrite('./output/result2-1.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])
cv.imwrite('./output/result2-1-30.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])
