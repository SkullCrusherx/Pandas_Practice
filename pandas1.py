#Siries
import pandas as pd

list = [1,2,3,4]

dic = {
    "name":["Sayan","Rupa","Rahul"],
    "age":[26,21,16],
    "city":["Delhi","Goa","Punjab"]
    }

Siries = pd.Series(list,index=["Sayan","Rupa","Rahul","Punjab"])
print(Siries) #Siries make 1D From List

Dic1 = pd.Series(dic)
print(Dic1) #Siries make 2D From Dictionary
