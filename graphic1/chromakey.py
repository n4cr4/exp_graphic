import numpy as np
import cv2 as cv

img_target = cv.imread('./img/target.JPG')
img_back = cv.imread('./img/back.jpg')
# img_mask = cv.imread('./output/result2-2/result2-2-90.jpg')
img_mask = cv.imread('./output/result2-2-green/result2-2-20.jpg')

width = img_target.shape[1]
height = img_target.shape[0]
bpp = img_target.shape[2] * img_target.dtype.type(0).nbytes
imagesize = img_target.nbytes
mean = cv.mean(img_back)

img = np.zeros([height, width, bpp], dtype=np.uint8)

for h in range(height):
    for w in range(width):
        for c in range(3):
            if img_mask[h][w][c]:
                img[h][w][c] = img_target[h][w][c]
            else:
                img[h][w][c] = img_back[h][w][c]
# cv.imwrite(f'./output/result2-3.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])
cv.imwrite(f'./output/result2-4.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])


