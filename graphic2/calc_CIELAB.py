import cv2 as cv
import numpy as np

## f_tを実装する

## CIEXYZ2CIELABを実装する

##平均2乗誤差を求める

## deltaEを実装する

def s2CIEXYZ(img):
    img = (img/255)**2.2
    width = img.shape[1]
    height = img.shape[0]
    print(img)
    print('--------------------')

    ret_img = np.zeros([height, width, 3], dtype=np.uint8) 
    ## uintじゃなくてfloatのやつに変える

    for h in range(height):
        for w in range(width):
            D65 = np.array([[0.1805,0.3576,0.4124],[0.0722,0.7152,0.2126],[0.9504,0.1192,0.0193]])
            ret_img[h, w] = 100*np.dot(D65, img[h, w])
            # print(100*np.dot(D65, img[h, w]))

    return ret_img


if __name__ == '__main__':
    img0 = cv.imread('./img/target.JPG')
    print(img0)
    print('--------------')
    print(s2CIEXYZ(img0))
    # print('--------------')
    # print(img0[0,0,2])
