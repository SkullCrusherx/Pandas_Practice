import pandas as pd

csv = pd.read_csv("new.csv")

print(csv.dropna())                             # All 'Nan' drop all new data set show
print(csv.dropna(axis=0))                       # All 'Nan' drop row wise bcz axis = 0
print(csv.dropna(axis=1))                       # All 'Nan' drop column wise bcz axis = 1
print(csv.dropna(how="all"))                    # If All value of dataset Nan it will Drop
print(csv.dropna(how="any"))                    # if any data of a row is Nan it will Drop
print(csv.dropna(subset=["BHK"]))               # All 'Nan' drop column wise bcz subset = ['column name']
print(csv.dropna(inplace=True))                 # All 'Nan' drop all new data set show
print(csv.dropna(thresh=2))                     # minimum 2 value hold in a row otherwise it will Drop


