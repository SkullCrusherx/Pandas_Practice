import pandas as pd


list = [1,2,3,4]
list_2 =  [1,2,3]
Dic = {
    "A":[1,2,3],
    "B":[2,4,6],
    "C":[3,6,9]
}
Dic_2 = {
    "A":[10]
}
var = pd.DataFrame(list)
print(var)
var_2 = pd.DataFrame(list_2)
print(var_2)
var_f = pd.DataFrame(Dic)
print(var_f)