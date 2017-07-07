# encoding = utf-8
# Liner algebra

import numpy as np
from numpy.linalg import *


def main():
    print(np.eye(3))  # 单位矩阵
    lst = np.array([[1, 2],
                    [3, 4]])
    print("Inv :")  # 求矩阵的逆
    print(inv(lst))
    print("T : ")  # 求矩阵的转置
    print(lst.transpose())
    print("Det :")  # 求矩阵的行列式
    print(det(lst))
    print(eig(lst))  # 求特征值与特征向量，第一个为特征值，第二个为特征向量

    y = np.array([[5], [7]])  # 解方程组，二元一次
    print("Solve : ")
    print(solve(lst, y))

if __name__ == '__main__':
    main()
