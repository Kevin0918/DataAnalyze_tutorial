# encoding = utf-8
# Many types of figures

import numpy as np
import matplotlib.pyplot as plt


def main():
    # 绘制散点图 Scatter
    fig = plt.figure()
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)  # 上色
    # plt.axes([0.025, 0.025, 0.95, 0.95])  # 指定显示范围
    ax.scatter(X, Y, s=75, c=T, alpha=.5)  # 画散点，s为点的大小，c为color，alpha为透明度
    plt.xlim(-1.5, 1.5), plt.xticks([])  # x的范围
    plt.ylim(-1.5, 1.5), plt.yticks([])  # y的范围
    plt.axis()
    plt.title("Scatter")
    plt.xlabel("x")
    plt.ylabel("y")

    # 绘制柱状图 Bar
    fig.add_subplot(332)
    n = 10
    X = np.arange(10)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#9999ff', edgecolor='white')

    plt.show()


if __name__ == '__main__':
    main()
