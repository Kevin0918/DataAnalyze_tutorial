# encoding = utf-8

import numpy as np
from scipy.optimize import minimize  # 计算最小值


def main():
    def rosen(x):
        return sum(100.0 * (x[1:] - x[:-1] ** 2.0 + (1 - x[:-1]) ** 2.0))


if __name__ == '__main__':
    main()
