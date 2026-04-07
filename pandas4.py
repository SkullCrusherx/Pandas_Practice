import pandas as pd

list = [1,2,3,4]
list2 = [5,6,7]
Dic = {
    "A":1,
    "B":2,
    "C":3
}
Dic_2 = {
    "A":10
}
"""
var = pd.DataFrame(list)
var_2 = pd.DataFrame(list2)

print(var + var_2)
print(var - var_2)
print(var * 2)"""

var = pd.DataFrame(Dic)
var_2 = pd.DataFrame(Dic_2)
print(var["A"] + var_2["A"])
print(var["B"] - var_2["A"])

