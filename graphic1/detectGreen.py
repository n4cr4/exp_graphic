import numpy as np
import cv2 as cv

img_target = cv.imread('./img/target.JPG')

width = img_target.shape[1]
height = img_target.shape[0]
bpp = img_target.shape[2] * img_target.dtype.type(0).nbytes
imagesize = img_target.nbytes


for d in range(0, 51, 10):
    img = np.ones([height, width, bpp], dtype=np.uint8)*255
    for h in range(height):
        for w in range(width):
                if ((img_target[h][w][0]+d) <= img_target[h][w][1]) and ((img_target[h][w][2]+d) <= img_target[h][w][1]):
                    # print(f'rgb=({img_target[h][w][2]}, {img_target[h][w][1]}, {img_target[h][w][0]})')
                    img[h][w][0] = img[h][w][1] = img[h][w][2] = 0
    cv.imwrite(f'./output/result2-2-green/result2-2-{d}.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 100])
