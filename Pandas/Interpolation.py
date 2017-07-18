# encoding=utf-8
import pandas as pd
from pylab import *


def main():
    dates = pd.date_range("2000-01-01", periods=100)
    ts = pd.DataFrame(np.random.randn(100), index=dates, columns=list("A"))
    print(ts)
    # dates = pd.date_range("20170301", periods=8)
    # df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    # print(df)
    print(ts.count())
    print(ts.interpolate().count())
    ts.interpolate().plot()
    show()

if __name__ == '__main__':
    main()
