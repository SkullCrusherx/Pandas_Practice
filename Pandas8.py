import pandas as pd

csv = pd.read_csv("new.csv")

print(csv.dropna())                             # All Nan drop all new data set show
print(csv.dropna(axis=0))                       # 
print(csv.dropna(axis=1))                       #
print(csv.dropna(how="all"))                    #
print(csv.dropna(how="any"))                    #
print(csv.dropna(subset=["BHK"]))               #
print(csv.dropna(inplace=True))                 #
print(csv.dropna(thresh=2))                     #
