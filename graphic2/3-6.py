from calc_CIELAB import deltaE
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img_original = cv.imread('./img/q100_s.jpg')
    quality = [1,5,10,20,40,80]
    deltaE_list = []
    for i in quality:
        img = cv.imread(f'./img/output/q100s_s_{i}.jpg')
        deltaE_result = deltaE(img_original, img)
        print(f'deltaE of quality {i}: ', end='')
        print('{:.3f}'.format(deltaE_result))
        deltaE_list.append(deltaE_result)
    size = [3, 4, 5, 8, 12, 21]

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax2 = ax1.twinx()

    ax1.plot(quality, deltaE_list, color='red', label='ΔE*ab')
    ax2.plot(quality, size, color='blue', label='File Size[KB]')

    ax1.set_xlabel('Jpeg Qality')
    ax1.set_ylabel('ΔE*ab')
    ax2.set_ylabel('File Size[KB]')

    h1, l1= ax1.get_legend_handles_labels()
    h2, l2= ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc='lower right')
    plt.savefig('./img/output/result_graph_deltaE.png')
