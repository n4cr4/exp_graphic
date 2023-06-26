import numpy as np
import cv2 as cv
import math

def median_filter(img, filter_size=3):
    width = img.shape[1]
    height = img.shape[0]
    bpp = img.shape[2]

    ret_img = np.zeros([height, width, bpp])

    n = 0
    for h in range(height):
        for w in range(width):
            for b in range(bpp):
                pixel_array = []

                for i in range(filter_size):
                    for j in range(filter_size):
                        middle = math.floor(filter_size/2)
                        px = w + j - middle
                        py = h + i - middle

                        if((px < 0) or (py < 0)):
                            pixel_array.append(0)
                            continue

                        if((px >= width) or (py >= height)):
                            pixel_array.append(0)
                            continue

                        pixel_array.append(img[py, px, b])

                ret_img[h, w, b] = np.median(pixel_array)

    return ret_img


if __name__ == '__main__':
    img_list = ['q100_s_original',
                'noise_s_whitenoise',
                'noise2_s_gomashio']
    for path in img_list:
        for i in (3, 5):
            print(f'./img/{path}.jpg')
            img = cv.imread(f'./img/{path}.jpg')
            ret_img = median_filter(img, filter_size=i)
            cv.imwrite(f'./img/output/{path}_{i}.jpg', ret_img)

