import numpy as np
import cv2 as cv 
import math

def mse(img0, img1):
    width = img0.shape[1]
    height = img0.shape[0]
    bpp = img0.shape[2]*img0.dtype.type(0).nbytes

    sum = 0
    for h in range(height):
        for w in range(width):
            for c in range(3):
                sum += ((int(img0[h][w][c]) - int(img1[h][w][c]))**2)
    return sum / (3*width*height)


def psnr(img0, img1):
    res = 255**2 / mse(img0, img1)
    return 10*math.log10(res)



if __name__ == '__main__':
    img0 = cv.imread('./img/noise_s.jpg')
    img1 = cv.imread('./img/q100_s.jpg')

    print(f'psnr: {psnr(img0, img1)}')


