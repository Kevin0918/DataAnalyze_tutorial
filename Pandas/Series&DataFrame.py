# encoding = utf-8
# Series&&DataFrame
import numpy as np
import pandas as pd


def main():
    # Data Structure
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(type(s))
    # DataFrame
    dates = pd.date_range("20170301", periods=8)
    df1 = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df1)
    df2 = pd.DataFrame({"A": 1, "B": pd.Timestamp("20170301"),
                        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                        "D": np.array([3] * 4, dtype="float32"),
                        "E": pd.Categorical(["Police", "Student", "Teacher", "Doctor"])})
    print(df2)


if __name__ == '__main__':
    main()
