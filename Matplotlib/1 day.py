# encoding = utf-8
# line

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)
    plt.plot(x, s, "r.", label="SIN")
    plt.title("COS & SIN")

    ax = plt.gca()  # 轴的编辑器
    ax.spines["right"].set_color("none")  # 将right的边隐藏
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))  # 将left设置到0位置
    ax.spines["bottom"].set_position(("data", 0))

    # 横纵轴上数字的位置
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    # 横纵轴的单位还有内容
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

    # 设置大小
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))  # 小方块的格式
    plt.legend(loc="upper left")  # 标注
    plt.grid()  # 网格线
    # plt.axes([-1, 1, -0.5, 1])  # 指定现实范围

    # 填充功能
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha=0.25)

    # 注释
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linewidth=3, linestyle="--")
    plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad = .2"))
    plt.show()


if __name__ == '__main__':
    main()
