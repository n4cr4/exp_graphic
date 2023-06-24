import cv2 as cv
import numpy as np

def f(t):
    if t > 0.008856:
        return t ** (1/3)
    else:
        return 7.7871*t + 16/116

def CIEXYZ2CIELAB(ciexyz):
    TRISTIMULUS = (95.05, 100, 108.89)
    width = ciexyz.shape[1]
    height = ciexyz.shape[0]
    cielab = np.zeros([height, width, 3], dtype=np.float32)

    for h in range(height):
        for w in range(width):
            cielab[h, w, 0] = 116*f(ciexyz[h, w, 1]/TRISTIMULUS[1])-16
            cielab[h, w, 1] = 500*(f(ciexyz[h, w, 0]/TRISTIMULUS[0])-f(ciexyz[h, w, 1]/TRISTIMULUS[1]))
            cielab[h, w, 2] = 200*(f(ciexyz[h, w, 1]/TRISTIMULUS[1])-f(ciexyz[h, w, 2]/TRISTIMULUS[2]))

    return cielab


def mean_error(array0, array1):
    width = array0.shape[1]
    height = array0.shape[0]
    sum = width*height
    error = 0
    for h in range(height):
        for w in range(width):
            error += (np.sum((array0[h, w]-array1[h, w])**2))**(1/2)
    return error / sum

def deltaE(img0, img1):
    img0 = CIEXYZ2CIELAB(s2CIEXYZ(img0))
    img1 = CIEXYZ2CIELAB(s2CIEXYZ(img1))
    return mean_error(img0, img1)


def s2CIEXYZ(img):
    img = img.astype(np.float32)
    img = (img/255)**2.2
    width = img.shape[1]
    height = img.shape[0]

    ret_img = np.zeros([height, width, 3], dtype=np.float32)

    for h in range(height):
        for w in range(width):
            D65 = np.array([[0.1805,0.3576,0.4124],[0.0722,0.7152,0.2126],[0.9504,0.1192,0.0193]])
            ret_img[h, w] = 100*np.dot(D65, img[h, w])

    return ret_img


if __name__ == '__main__':
    img0 = cv.imread('./img/q100_s.jpg')
    img1 = cv.imread('./img/noise_s.jpg')
    print(deltaE(img0, img1))
