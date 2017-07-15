# encoding = utf-8
# Linear 线性计算与矩阵分解
import numpy as np
from scipy import linalg as lg


def main():
    # 线性计算：
    arr = np.array([[1, 2], [3, 4]])
    print("Det:", lg.det(arr))
    print("Inv:", lg.inv(arr))
    b = np.array([6, 14])
    print("Sol:", lg.solve(arr, b))  # 解线性方程组
    print("Eig:", lg.eig(arr))  # 特征值

    # 矩阵分解
    print("LU:", lg.lu(arr))
    print("QR:", lg.qr(arr))
    print("SVD", lg.svd(arr))
    print("Schur:", lg.schur(arr))


if __name__ == '__main__':
    main()
