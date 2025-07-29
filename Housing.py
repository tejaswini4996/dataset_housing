from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
var = fetch_california_housing()
url="http://lib.stat.cmu.edu/datasets/boston"
data= np.hstack(url)
data.head()
print(var.keys())