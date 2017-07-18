# encoding = utf-8
# Basic&Select&Set
import numpy as np
import pandas as pd


def main():
    dates = pd.date_range("20170301", periods=8)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df)

    # Basic
    print("head:\n", df.head(3))
    print("Tail:\n", df.tail(3))
    print("Index:\n", df.index)
    print("Values:\n", df.values)
    print("T:\n", df.T)  # 输出转置矩阵
    print("Sort:\n", df.sort_index(axis=1, ascending=True))
    print("Describe:\n", df.describe())
    print("\n")

    # Select
    print("A:", df["A"])
    print("A Type:\n", type(df["A"]))
    print(df[:3])
    print(df["20170301":"20170304"])
    print(df.loc[dates[0]])
    print(df.loc["20170301":"20170304", ["B", "D"]])
    print(df.at[dates[0], "C"])

    print(df.iloc[1:3, 2:4])
    print(df.iloc[1, 4])
    print(df.iat[1, 4])

    print(df[df.B > 0][df.A < 0])
    print(df[df > 0])
    print(df[df["E"].isin([1, 2])])

    # Set
    s1 = pd.Series(list(range(10, 18)), index=pd.date_range("20170301", periods=8))
    df["F"] = s1
    print(df)
    df.at[dates[0], "A"] = 0
    print(df)
    df.iat[1, 1] = 1
    df.loc[:, "D"] = np.array([4] * len(df))
    print(df)
    df2 = df.copy()
    df2[df2 > 0] = -df2
    print(df2)

if __name__ == '__main__':
    main()
