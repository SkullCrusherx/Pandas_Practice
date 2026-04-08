import pandas as pd

df = pd.read_csv("ML.csv")                                          # Read the CSV File
df_1 = pd.read_csv("ML.csv", nrows = 2)               # Read Number of Rows how much Need From 0 to N
df_2 = pd.read_csv("ML.csv", usecols = [2])             # Read Number of Rows how much Need From 0 to N


print(df_2)