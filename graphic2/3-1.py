# mseは1^2, 5^2なので、それにたいするpsnrを求める
import math

mse = [1, 5]
for i in mse:
    psnr = 10*math.log10(255**2/(i**2))
    print(f'psnr of {i}: {psnr}')