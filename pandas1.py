#Siries
import pandas as pd

list = [1,2,3,4,5,6,7,8,9,10]
dic = {
    "name":["Sayan","Rupa","Rahul"],
    "age":[26,21,16],
    "city":["Delhi","Goa","Punjab"]
    }


Siries = pd.Series(list)
#print(Siries)
Dic1 = pd.Series(dic)
print(Dic1["name"][:2])

print("=========================")

Dic2 = pd.DataFrame(dic)
print(Dic2)



