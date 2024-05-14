import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def myfunc(x, a, b, c):
    """
    A math function.
    """
    return a * np.exp(-b * x) * np.sin(c * x)


class CSVprocessor:
    def __init__(self, path):
        data = pd.read_csv(path)
        self.data = data
        self.path = path

    def apply_fit(self):
        data = self.data
        params, cov = optimize.curve_fit(myfunc, data.x, data.y)
        self.fit = params

    def get_a(self):
        return self.fit[0]

    a = property(get_a)

    def plot(self, path=None):
        plt.figure()
        xdata, ydata = self.data.x, self.data.y
        a, b, c = self.fit
        plt.scatter(xdata, ydata, s=2, marker="+", color="r", label="data")
        plt.plot(xdata, myfunc(xdata, a, b, c), "b-", label="fit")
        plt.legend(loc="best")
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        if path == None:
            plt.show()
        else:
            plt.savefig(path)
            plt.close()
