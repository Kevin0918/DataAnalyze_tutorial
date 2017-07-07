# 1 day
# encoding = utf-8
import numpy as np


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=float)
    # bool, int, int8, int16, int32, int64, uint, float, complex, string
    print(np_lst.shape)
    print(np_lst.ndim)  # 维数
    print(np_lst.dtype)
    print(np_lst.itemsize)  # 所占字节数
    print(np_lst.size)

if __name__ == '__main__':
    main()
