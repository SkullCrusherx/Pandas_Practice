import pandas as pd


csv = pd.read_csv("ML.csv",header=None,prefix = [1,2])
print(csv)