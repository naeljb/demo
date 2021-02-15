import pandas as pd
import numpy as np
import math
import scipy.stats as stats

# how to download a dataset?
d = "c:/Users/Nael/Documents/dataset.xlsx"

# how to view the first five rows?
df = pd.read_excel(d)
df.head()

# how to view the last five rows?
df.tail()
