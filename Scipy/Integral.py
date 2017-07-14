# encoding = utf-8
# Integral 积分模块
import numpy as np
from scipy.integrate import quad, dblquad, nquad  # 引入积分模块


def main():
    print(quad(lambda x: np.exp(-x), 0, np.inf))  # 一元积分，生成两个数，第二个数是误差范围
    print(dblquad(lambda t, x: np.exp(-x * t) / t ** 3, 0, np.inf, lambda x: 1, lambda x: np.inf))  # 二元积分

    def f(x, y):
        return x * y

    # 定义x，y的边界：
    def bound_y():
        return [0, 0.5]

    def bound_x(y):
        return [0, 1 - 2 * y]

    print(nquad(f, [bound_x, bound_y]))


if __name__ == '__main__':
    main()
