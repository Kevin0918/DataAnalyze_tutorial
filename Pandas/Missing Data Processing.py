# encoding = utf-8
# Missing Values
import numpy as np
import pandas as pd


def main():
    df = pd.DataFrame(np.random.randn(5, 3),
                      index=['a', 'c', 'e', 'f', 'h'],
                      columns=['one', 'two', 'three'])
    df['four'] = 'bar'
    df['five'] = df['one'] > 0
    df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    print("df:\n", df)
    print("df2:\n", df2)
    print("第一列缺失值打印：")
    print(pd.isnull(df2['one']))
    print("第四列缺失值打印：")
    print(df2['four'].notnull())
    print("整个表的缺失值打印：")
    print(df2.notnull())


if __name__ == '__main__':
    main()
