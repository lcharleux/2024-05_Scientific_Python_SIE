# PROCESSS CSV FILE WITH A CLASS

import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from processing import myfunc, CSVprocessor


processor = CSVprocessor("data.csv")
processor.apply_fit()
processor.plot("nice_fig.pdf")
