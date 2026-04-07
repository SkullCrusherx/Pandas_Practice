#insert and delete Element From DataFrame And Also Series
import pandas as pd

var = {
    "A" :[1,2,3,4],
    "B" :[5,6,7,8],                                      # Create Dictionary For insert Data and Delete Data also
    "C" :[9,10,11,12],
    "D" :[13,14,15,16]
}

df = pd.DataFrame(var)


df.insert(1,"NN",[11,22,33,44])        # value Return into file no need store any variable # insert(Location,Column name,list or element(data)) #equal Data required or error pop
df["FFF"] = [1,2,3]

df.pop("B")                                             # pop("column name") which column need to remove use pop
del df["C"]                                             # del df("column name) here df for dataframe which is Contain all file

print(df)                                               # reflect the Data which insert on my Dictionary DataFrame
