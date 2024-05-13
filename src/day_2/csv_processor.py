# PROCESSS CSV FILE WITH A CLASS

import pandas as pd
import numpy as np
from scipy import optimize


def myfunc(x, a, b, c):
    """
    A math function.
    """
    return a * np.exp(-b * x) * np.sin(c * x)


# data = pd.read_excel("data.xlsx", header=1)
# data = pd.read_csv("data.csv")


class CSVprocessor:
    def __init__(self, path):
        data = pd.read_csv(path)
        self.data = data

    def apply_fit(self):
        data = self.data
        params, cov = optimize.curve_fit(myfunc, data.x, data.y)
        self.fit = params

    def get_a(self):
        return self.fit[0]

    a = property(get_a)


processor = CSVprocessor("data.csv")
processor.apply_fit()
