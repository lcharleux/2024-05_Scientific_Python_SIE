import numpy as np
import pandas as pd


def myfunc(x, a, b, c):
    """
    A math function.
    """
    return a * np.exp(-b * x) * np.sin(c * x)


x = np.linspace(0, 10, 1001)

for n in range(10):
    y = myfunc(x, 1, 0.2, 3) + np.random.normal(0, 0.1, x.size)
    df = pd.DataFrame({"x": x, "y": y})
    file_name = f"data_{n}.csv"
    print(f"Creating file {file_name}")
    df.to_csv(file_name, index=False)
    # df.to_excel("data.xlsx", index=False)  # mamba install -y openpyxl xlrd xlwt xlsxwriter
