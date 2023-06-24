from calc_CIELAB import deltaE, s2CIEXYZ, CIEXYZ2CIELAB
import numpy as np
import cv2 as cv

if __name__ == '__main__':
    img_original = cv.imread('./img/q100_s.jpg')
    quality = [1,5,10,20,40,80]
    for i in quality:
        img = cv.imread(f'./img/output/q100s_s_{i}.jpg')
        print(f'deltaE of quality {i}: ', end='')
        print('{:.3f}'.format(deltaE(img_original, img)))