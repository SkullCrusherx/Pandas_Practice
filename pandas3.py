import pandas as pd


csv = pd.read_csv("ML.csv",header=None,Prefix = ["A","B"])
print(csv)