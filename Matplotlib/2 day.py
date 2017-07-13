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
    ax = fig.add_subplot(332)
    n = 10
    X = np.arange(10)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    ax.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    ax.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='top')
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

    # Pie
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)],
            labels=['%.2f' % (i / float(n)) for i in range(n)])  # explode表示的是每个扇形离中心的距离
    plt.gca().set_aspect('equal')  # 正圆
    plt.xticks([]), plt.yticks([])

    # Polar 极坐标
    fig.add_subplot(334, polar=True)  # 将注释显示出来
    n = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / n)
    radii = 10 * np.random.rand(n)
    plt.polar(theta, radii)
    # plt.plot(theta, radii)

    # Heatmap
    from matplotlib import cm  # 上色用的
    fig.add_subplot(335)
    data = np.random.rand(3, 3)
    colormap = cm.Blues
    map = plt.imshow(data, interpolation='nearest', cmap=colormap, aspect='auto', vmin=0,
                     vmax=1)  # 使用的是插值方法'nearest'，vmin、vmax表示颜色的最大值与最小值

    # 3D
    from mpl_toolkits.mplot3d import Axes3D
    # 引入三维坐标系
    ax = fig.add_subplot(336, projecton="3d")
    ax.scatter(1, 1, 3, s=100)

    # hot map
    fig.add_subplot(313)

    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

    plt.show()


if __name__ == '__main__':
    main()
