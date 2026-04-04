import pandas as pd


csv = pd.read_csv("ML.csv",header=None,prefix = ["A","B"])
print(csv)