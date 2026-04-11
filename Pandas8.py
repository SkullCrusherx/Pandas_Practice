import pandas as pd

csv = pd.read_csv("new.csv")

print(csv.dropna())                             #
print(csv.dropna(axis=0))                       #
print(csv.dropna(axis=1))                       #
