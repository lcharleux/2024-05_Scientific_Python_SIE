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
    print(f"Processing: {file}")
    if file.endswith(".csv") and file.startswith("data_"):
        processor = CSVprocessor(file)
        processor.apply_fit()
        processors.append(processor)
        print("  File processed.")
    else:
        print("  File rejected.")
fits = np.array([processor.fit for processor in processors])
files_names = np.array([processor.path for processor in processors])
fits = pd.DataFrame(fits, columns=list("abc"), index=files_names)
fits.sort_index(inplace=True)


# processor = CSVprocessor("data.csv")
# processor.apply_fit()
# processor.plot("nice_fig.pdf")
