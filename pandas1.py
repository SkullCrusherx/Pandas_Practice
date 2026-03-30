#Siries
import pandas as pd

list = [1,2,3,4]
data = 10
dic = {
    "name":["Sayan","Rupa","Rahul"],
    "age":[26,21,16],
    "city":["Delhi","Goa","Punjab"]
    }


Siries_normal = pd.Series(list) #showing Data
Siries_index = pd.Series(list,index=["Sayan","Rupa","Rahul","Punjab"])
Siries_type = pd.Series(type(list))
Siries_ch_type = pd.Series(list,dtype=object)
Siries_only_int = pd.Series(data,index=["Sayan","Rupa","Rahul","Punjab"])

print(Siries_normal) #Siries make 1D From List
print(Siries_index) #index change and update
print(Siries_type) #show data type
print(Siries_ch_type) #chnage the data type
print("FF\n",Siries_only_int)
Dic1 = pd.Series(dic)
print(Dic1) #Siries make 2D From Dictionary
