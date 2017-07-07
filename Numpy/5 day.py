# encoding = utf-8
# 5 day Others
import numpy as np


def main():
    print(" FFT : ")  # 傅立叶变换
    print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, 1])))
    print(" Coef : ")  # 相关系数计算
    print(np.corrcoef([1, 0, 1], [0, 2, 1]))
    print(" Poly: ")  # 生成一元多次函数
    print(np.poly1d([2, 1, 3]))

if __name__ == '__main__':
    main()
