import numpy as np
import cv2 as cv

if __name__ == '__main__':
    img = cv.imread('./img/q100_s_original.jpg', cv.IMREAD_GRAYSCALE)
    h, w = img.shape

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    mask = np.ones((h, w))
    cv.ellipse(mask, (w//2, h//2), (w//4, h//4), 0, 0, 360, color=0, thickness=-1)
    fshift = fshift * mask

    ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(ishift)
    img_back = 2*np.abs(img_back)
    img_sharp = img_back + img
    img_sharp = np.clip(img_sharp, 0, 255)
    img_sharp = img_sharp.astype(np.uint16)

    cv.imwrite('./img/output/fourier/sharp.jpg', img_sharp)
    cv.imwrite('./img/output/fourier/high_path_filter.jpg', img_back)
    cv.imwrite('./img/output/fourier/original.jpg', img)
    cv.imwrite('./img/output/fourier/mask.jpg', 255*mask)



