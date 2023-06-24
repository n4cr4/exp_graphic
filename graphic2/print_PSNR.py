import cv2 as cv
import calc_PSNR

def calc_PSNR_filename(filename1, filename2):
    img0 = cv.imread(filename1)
    img1 = cv.imread(filename2)
    return calc_PSNR.psnr(img0, img1)

if __name__ == '__main__':
    filename1 = input('filename1: ')
    filename2 = input('filename2: ')
    print(calc_PSNR_filename(filename1, filename2))
