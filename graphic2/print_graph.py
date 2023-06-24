import matplotlib.pyplot as plt
import numpy as np
import print_PSNR

jpg_qality = [1, 5, 10, 20, 40, 80]
jpg_size = [194, 200, 216, 251, 367, 1022]
psnr = []
for q in jpg_qality:
    filename1 = './img/target.JPG'
    filename2 = f'./img/output/target_{q}.jpg'
    psnr.append(print_PSNR.calc_PSNR_filename(filename1, filename2))


# plt.plot(jpg_qality, psnr)
# plt.show()
fig = plt.figure()
ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.plot(jpg_qality, psnr, color='red', label='PSNR[dB]')
ax2.plot(jpg_qality, jpg_size, color='blue', label='File Size[KB]')

ax1.set_xlabel('Jpeg Quality')
ax1.set_ylabel('PSNR[dB]')
ax2.set_ylabel('File Size[KB]')

h1, l1= ax1.get_legend_handles_labels()
h2, l2= ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='lower right')
# plt.show()
plt.savefig('./img/output/result_graph.png')
