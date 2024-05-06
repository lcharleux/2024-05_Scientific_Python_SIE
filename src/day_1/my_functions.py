import numpy as np


def myfunc(x, a, b, c):
    """
    A math function.
    """
    return a * np.exp(-b * x) * np.sin(c * x)
