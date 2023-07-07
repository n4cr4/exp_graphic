import numpy as np
import cv2 as cv

KERNEL4 = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
]

KERNEL8 = [
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1],
]

def laplacian_filter(img, neighborhood=4):
    width = img.shape[1]
    height = img.shape[0]
    bpp = img.shape[2]

    ret_img = np.zeros([height, width, bpp])

    for h in range(height):
        for w in range(width):
            for b in range(bpp):
                sum = 0.0
                for i in range(3):
                    for j in range(3):
                        px = w + j - 1
                        py = h + i - 1
                        if((px < 0) or (py < 0)): continue
                        if((px >= width) or (py >= height)): continue

                        I = img[py, px, b]
                        if neighborhood == 4:
                            g = KERNEL4[j][i]
                        elif neighborhood == 8:
                            g = KERNEL8[j][i]

                        sum += I * g
                ret_img[h, w, b] = sum
    ret_img = np.clip(ret_img, 0, 255)

    return ret_img





if __name__ == '__main__':
    img_list = ['q100_s_original',
                'noise_s_whitenoise',
                'noise2_s_gomashio']
    img = cv.imread(f'./img/{img_list[0]}.jpg')
    for path in img_list:
        for i in (4, 8):
            print(f'./img/{path}.jpg')
            img = cv.imread(f'./img/{path}.jpg')
            ret_img = laplacian_filter(img, neighborhood=i)
            cv.imwrite(f'./img/output/laplacian/{path}_{i}.jpg', ret_img)


