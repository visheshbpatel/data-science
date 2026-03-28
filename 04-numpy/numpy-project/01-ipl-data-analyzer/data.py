import pandas as pd
import numpy as np



data = np.genfromtxt(
    '04-numpy/numpy-project/01-ipl-data-analyzer/dataset/runs.csv',
    delimiter=',',
    dtype=str
)

players = data[1:, 0]
runs = data[1:, 1:].astype(int)
