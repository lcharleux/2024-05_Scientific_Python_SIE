# PROCESSS CSV FILE WITH A CLASS

import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from processing import myfunc, CSVprocessor
import os

processors = []
files = os.listdir("./")
for file in files:
    if file.endswith(".csv"):
        processor = CSVprocessor(file)
        processor.apply_fit()
        processors.append(processor)

fits = np.array([processor.fit for processor in processors])
fits = pd.DataFrame(fits, columns=list("abc"))


# processor = CSVprocessor("data.csv")
# processor.apply_fit()
# processor.plot("nice_fig.pdf")
