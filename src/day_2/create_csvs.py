import numpy as np
import pandas as pd


def myfunc(x, a, b, c):
    """
    A math function.
    """
    return a * np.exp(-b * x) * np.sin(c * x)


x = np.linspace(0, 10, 1001)
y = myfunc(x, 1, 0.2, 3) + np.random.normal(0, 0.1, x.size)
df = pd.DataFrame({"x": x, "y": y})
df.to_csv("data.csv", index=False)
