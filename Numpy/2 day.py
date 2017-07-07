# 2 day : Some Arrays
# encoding = utf-8

import numpy as np


def main():
    print(np.zeros([3, 3]))
    print(np.ones([3, 5]))
    print(np.random.rand(2, 4))  # 随机数
    print(np.random.rand())
    print(" RandInit: ")
    print(np.random.randint(1, 10, 3))  # 随机整数与范围,及个数
    print(" RandN: ")
    print(np.random.randn(2, 4))  # 标准正态的随机数，几行几列
    print(" Choice: ")
    print(np.random.choice([10, 20, 30, 40]))  # 在限定的几个数里进行随机取数
    print(" Distribute ")
    print(np.random.beta(1, 10, 100))  # 生成Beta分布，常见分布都可以


if __name__ == '__main__':
    main()
