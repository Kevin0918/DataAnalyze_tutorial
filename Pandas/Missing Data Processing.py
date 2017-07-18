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
    print("df:\n", df, "\n")
    print("df2:\n", df2, "\n")
    print("第一列缺失值打印：")
    print(pd.isnull(df2['one']), "\n")
    print("第四列缺失值打印：")
    print(df2['four'].notnull(), "\n")
    print("整个表的缺失值打印：")
    print(df2.notnull(), "\n")

    # DateTime
    df3 = df.copy()
    df3['timestamp'] = pd.Timestamp('20120101')
    df3.loc[['a', 'c', 'h'], ['one', 'timestamp']] = np.nan
    print(df3, "\n")
    print(df3.get_dtype_counts(), "\n")

    # Inserting Missing data
    s = pd.Series(['a', 'b', 'c'])
    s.loc[0] = np.nan
    s.loc[1] = None
    print(s, "\n")

    # Calculations with missing data
    a = pd.DataFrame(np.random.randn(5, 2),
                     index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two'])
    a.loc[['a', 'c', 'h'], ['one', 'two']] = np.nan

    b = pd.DataFrame(np.random.randn(5, 3),
                     index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two', 'three'])
    b.loc[['a', 'c'], ['one', 'three']] = np.nan

    print("a:\n", a, "\n")
    print("b:\n", b, "\n")
    print("a+b=\n", a + b, "\n")

    # Cleaning / filling missing data
    # pandas objects are equipped with various data manipulation methods for dealing with missing data.
    print("df3:\n", df3, "\n")

    print("df3(Fill):\n", df3.fillna(0), "\n")

    print("df3(Fill):\n", df3['four'].fillna('missing'), "\n")


if __name__ == '__main__':
    main()
