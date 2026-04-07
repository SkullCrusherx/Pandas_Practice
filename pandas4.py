import pandas as pd

list = [1,2,3,4]
list2 = [5,6,7]

var = pd.DataFrame(list)
var_2 = pd.DataFrame(list2)

print(var + var_2)
print(var - var_2)
print(var * 2)