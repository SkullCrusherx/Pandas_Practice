import pandas as pd

df = pd.read_csv("ML.csv")                                                            # Read the CSV File

df_1 = pd.read_csv("ML.csv", nrows = 2)                                 # Read Number of Rows how much Need From 0 to N

df_2 = pd.read_csv("ML.csv", usecols = [0,1])                           # Read index Number of column or name how much Need using comma [0,1]
df_3 = pd.read_csv("ML.csv", usecols = ["BHK","Price"])                 # Read column or name how much Need using comma [0,1]

df_4 = pd.read_csv("ML.csv",skiprows=4)                                 # Read from 0 to skip rows number = N time skip all
df_5 = pd.read_csv("ML.csv",skiprows=[4])                               # Read from element to skip rows number which is given
df_6 = pd.read_csv("ML.csv",skiprows=[4,5])                             # Read from element to skip rows number which is given

df_7 = pd.read_csv("ML.csv",index_col=[0])                              # make column as index using this if always it works column length - 1

df_8 = pd.read_csv("ML.csv",header=None)                                # Given Another header 0 and 1
df_9 = pd.read_csv("ML.csv",header=[1])                                 # number of index given in header it goes header
df_10 = pd.read_csv("ML.csv",header=1)                                  # number of index given upon all Data will skip Both

df_11 = pd.read_csv("ML.csv",names=[2])

#print(df["Price"])                                                                    # reflect the column which column required
print(df_11)