# 3 day : Operations
# encoding = utf-8

import numpy as np


def main():
    lst_arrang = np.arange(1, 11).reshape([2, -1])  # 形成一个等差数列，范围为1～11，不包括11
    print(" exp: ")
    print(np.exp(lst_arrang))
    print(" exp2: ")
    print(np.exp2(lst_arrang))
    print(" sqrt: ")
    print(np.sqrt(lst_arrang))
    print(" sin: ")
    print(np.sin(lst_arrang))
    print(" Log: ")
    print(np.log(lst_arrang))

    lst_test = np.array([[[1, 2, 3, 4],
                          [4, 5, 6, 7]],
                         [[7, 8, 9, 10],
                          [10, 11, 12, 13]],
                         [[14, 15, 16, 17],
                          [18, 19, 20, 21]]])
    print(lst_test.shape)
    print(lst_test.sum(axis=0))  # axis 只对某个层元素进行运算
    print(lst_test.sum(axis=1))
    print(lst_test.sum(axis=2))

    print("Max :")
    print(lst_test.max(axis=0))
    print(lst_test.max(axis=1))
    print(lst_test.max(axis=2))
    print("Min :")
    print(lst_test.min(axis=0))
    print(lst_test.min(axis=1))
    print(lst_test.min(axis=2))

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("Add :")
    print(lst1 + lst2)
    print("Sub : ")
    print(lst1 - lst2)
    print("Mul : ")
    print(lst1 * lst2)
    print("Div : ")
    print(lst1 / lst2)
    print("Square : ")
    print(lst1 ** 2)
    print("Dot :")
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))

    # 数组追加
    print("Concatenate :")
    print(np.concatenate((lst1, lst2), axis=0))  # 将两个数组追加,变为一行的
    print("Vstack : ")
    print(np.vstack((lst1, lst2)))  # 两个数组何为一个数组，变为两行的
    print("Hstack : ")
    print(np.hstack((lst1, lst2)))
    print("Split : ")  # 将数组分离
    print(np.split(lst1, 4))
    print("Copy : ")  # 将数组拷贝
    print(np.copy(lst1))


if __name__ == '__main__':
    main()
