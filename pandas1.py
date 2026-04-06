#Siries
import pandas as pd

list = [3,4,5,6]
data = 10
dic = {
    "A":["Sayan","Rupa","Rahul"],
    "B":[1,2,3],
    "C":["Delhi","Goa","Punjab","Delhi"]
    }


Siries_normal = pd.Series(list)                                                                     #showing Data
Siries_normal_name = pd.Series(list,name="Python")                                                  #Given Name
Siries_sepcs_data = pd.Series(list[0])                                                              #show specific element Data of Siries
Siries_index = pd.Series(list,index=["AA","BB","CC","DD"])                                          #index changing
Siries_type = pd.Series(type(list))                                                                 #checking datatype
Siries_ch_type = pd.Series(list,dtype=object)                                                       #change data type using dtype function like numpy
Siries_only_int = pd.Series(data,index=[1,2,3,4,5])                                                 #one int make Siries using index times
Dic1 = pd.Series(dic)
p1 = pd.Series(10,index=[1,2,3,4,5])
p2 = pd.Series(10,index=[1,2,3,4,5,6,7,8])




print(Siries_normal)                                                                                #Siries make 1D From List
print(Siries_index)                                                                                 #index change and update
print(Siries_type)                                                                                  #show data type
print(Siries_ch_type)                                                                               #chnage the data type
print(Siries_only_int)                                                                              #single number make series with index how much need also
print(Siries_sepcs_data)
print(Siries_normal_name)
print(Dic1)                                                                                         #Siries make 2D From Dictionary
print(Dic1["name"][1])                                                                              #for specific Dictionary data ["name"] for Dictionary [] next one index value to show element for the data
print(Dic1["age"])                                                                                  #For specific Dictionary age
print(p1 + p2)                                                                                      #no broadcasting error numpy but lowest data only operation possible then show none

