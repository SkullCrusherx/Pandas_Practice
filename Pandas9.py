import pandas as pd

csv = pd.read_csv("new.csv")

csv.interpolate(inplace=True)

print(csv)