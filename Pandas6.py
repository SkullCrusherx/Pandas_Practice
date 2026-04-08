import pandas as pd

df = pd.read_csv("ML.csv")                                                            # Read the CSV File
df_1 = pd.read_csv("ML.csv", nrows = 2)                                 # Read Number of Rows how much Need From 0 to N
df_2 = pd.read_csv("ML.csv", usecols = [0,1])                           # Read index Number of column or name how much Need using comma [0,1]
df_3 = pd.read_csv("ML.csv", usecols = ["BHK","Price"])                 # Read column or name how much Need using comma [0,1]
df_4 = pd.read_csv("ML.csv",skiprows=2)

print(df["Price"])                                                                    # reflect the column which column required
#print(df_3)