import pandas as pd
import numpy as np

csv = pd.read_csv("ML.csv")

print(csv.index)                                                 #Showing the Detail of range index like step start end all
print(csv.columns)                                               #showing all the column name mean header also
print(csv.describe())                                            #Showing here count mean max and other values also
print(csv.head(3))                                               #3 here how much data need to show here from Top
print(csv.tail(3))                                               #3 here how much data need to show here from Bottom
print(csv[:2])                                                   #from start to end also we check print using like these [start:end]
print(type(csv[:2]))                                             #showing or reflect the data type
print(csv.index.array)                                           #showing index all number into array(pandas)
print(csv.columns.array)                                         #showing in array Column name or headers
print(csv.to_numpy())                                            #all Data element convert into numpy array
print(np.asarray(csv))                                           #import numpy 1st then np function as array call to make numpy array
print(csv.sort_index(axis=0,ascending=False))                    #sort index means index wise sort and ascending use for not required for ascending theats why False otherWise True
print("*")
print(csv.loc[["BHK","Price"]])                                  #here ican get data using which data actually need using comma [["Colum name1","Colum name2"][5]Row]
print(csv.loc[[0,1],["BHK","Price"]])                                         #here ican get data using which data actually need using slicing [[Row number ],[column name ]]
