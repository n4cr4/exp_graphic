import numpy as np
import cv2 as cv

img_target = cv.imread('./img/target.JPG')
img_back = cv.imread('./img/back.jpg')

width = img_target.shape[1]
height = img_target.shape[0]
bpp = img_target.shape[2] * img_target.dtype.type(0).nbytes
imagesize = img_target.nbytes
mean = cv.mean(img_back)

img = np.ones([height, width, bpp], dtype=np.uint8)*255

print(f'(BGR)={mean[0]:.2f},{mean[1]:.2f},{mean[2]:.2f}')

for d in range(0, 100, 10):
    for h in range(height):
        for w in range(width):
            for c in range(3):
                if not(mean[c]-d <= img_target[h][w][c] and img_target[h][w][c] <= mean[c]+d):
                     break
            else:
                img[h][w][0] = img[h][w][1] = img[h][w][2] = 0
    cv.imwrite(f'./output/result2-2/result2-2-{d}.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])

