# encoding = utf-8
# Linear 线性计算与矩阵分解
import numpy as np
from scipy import linalg as lg
import matplotlib.pyplot as plt


def main():
    # 线性计算：
    arr = np.array([[1, 2], [3, 4]])
    print("Det:", lg.det(arr))
    print("Inv:", lg.inv(arr))  # 逆矩阵求解
    b = np.array([6, 14])
    print("Sol:", lg.solve(arr, b))  # 解线性方程组
    print("Eig:", lg.eig(arr))  # 特征值

    # 矩阵分解
    print("LU:", lg.lu(arr))  # 分解为两个数组，一个为上三角一个为下三角
    print("QR:", lg.qr(arr))
    print("SVD", lg.svd(arr))
    print("Schur:", lg.schur(arr))

    # Solving linear least-squares problems and pseudo-inverses
    c1, c2 = 5.0, 2.0
    i = np.r_[1:11]
    xi = 0.1 * i
    yi = c1 * np.exp(-xi) + c2 * xi
    zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi))
    A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
    c, resid, rank, sigma = lg.lstsq(A, zi)
    xi2 = np.r_[0.1:1.0:100j]
    yi2 = c[0] * np.exp(-xi2) + c[1] * xi2
    # 作图
    plt.plot(xi, zi, 'x', xi2, yi2)
    plt.axis([0, 1.1, 3.0, 5.5])
    plt.xlabel('$x_i$')
    plt.title('Data fitting with linalg.lstsq')
    plt.show()


if __name__ == '__main__':
    main()
