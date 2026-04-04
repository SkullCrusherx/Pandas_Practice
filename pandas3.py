import pandas as pd

csv = pd.read_csv("ML.csv")

print(csv.index)        #Showing the Detail of rangeindex like step start end all
print(csv.columns)      #showing all the column name mean header also
print(csv.describe())   # showing here count mean max and other values also
print(csv.head(3))      #3 here how much data need to show here from Top
print(csv.tail(3))      #3 here how much data need to show here from Bottom
print(csv[:2])          #from start to end also we check print using like these [start:end]
print(type(csv[:2]))    #showing or reflect the data type
print(csv.index.array)
print(csv.columns.name)