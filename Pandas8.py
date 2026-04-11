import pandas as pd

csv = pd.read_csv("new.csv")

print(csv.dropna())                                 # All 'Nan' drop all new data set show
print(csv.dropna(axis=0))                           # All 'Nan' drop row wise bcz axis = 0
print(csv.dropna(axis=1))                           # All 'Nan' drop column wise bcz axis = 1
print(csv.dropna(how="all"))                        # If All value of dataset Nan it will Drop
print(csv.dropna(how="any"))                        # if any data of a row is Nan it will Drop
print(csv.dropna(subset=["BHK"]))                   # All 'Nan' drop column wise bcz subset = ['column name']
print(csv.dropna(inplace=True))                     # All 'Nan' drop all new data set show
print(csv.dropna(thresh=2))                         # minimum 2 value hold in a row otherwise it will Drop

print(csv.fillna("Data"))                           # Blank Data will update or Fill with 'Data'
print(csv.fillna({'Column name':'Data'}))           # column wise empty data will fill
print(csv.fillna(method = 'ffill/bfill'))           # Fill data before data with or forward with data
print(csv.fillna(method = 'ffill/bfill',axis=0/1))  # Fill data before data with or forward with data using axis 0 means row and column means 1
print(csv.fillna("Data",inplace=True))        # All 'Nan' Fill all new data set show
print(csv.fillna("Data",limit=2))             # All 'Nan' Fill all column wise  and from top to bottom limit wise data if 2 then blank top to bottom 2 data will replace only


