import pandas as pd


Dic = {
    "A":[1,2,3],
    "B":[2,4,6],
    "C":[3,6,9]
}
Dic_2 = {
    "A":[10]
}

var_f = pd.DataFrame(Dic)
print(var_f)