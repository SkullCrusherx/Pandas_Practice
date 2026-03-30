#Siries
import pandas as pd

list = [3,4,5,6]
data = 10
dic = {
    "name":["Sayan","Rupa","Rahul"],
    "age":[26,21,16],
    "city":["Delhi","Goa","Punjab","Delhi"]
    }

#-------------------------------------------------------------------------
Siries_normal = pd.Series(list) #showing Data
Siries_normal_name = pd.Series(list,name="Python")
Siries_sepcs_data = pd.Series(list[0]) #show secific element Data of Siries
Siries_index = pd.Series(list,index=["Sayan","Rupa","Rahul","Punjab"]) #index changing
Siries_type = pd.Series(type(list)) #checking datatype
Siries_ch_type = pd.Series(list,dtype=object) #change data type using dtype function like numpy
Siries_only_int = pd.Series(data,index=["Sayan","Rupa","Rahul","Punjab"]) #one int make Siries using index times
#-------------------------------------------------------------------------
print(Siries_normal) #Siries make 1D From List
print(Siries_index) #index change and update
print(Siries_type) #show data type
print(Siries_ch_type) #chnage the data type
print(Siries_only_int) #single number make series with index how much need also
print(Siries_sepcs_data)
print(Siries_normal_name)
#-------------------------------------------------------------------------
Dic1 = pd.Series(dic)
print(Dic1) #Siries make 2D From Dictionary
print(Dic1["name"]) #for specific Dictionary data
print(Dic1["age"]) 