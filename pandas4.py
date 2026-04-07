import pandas as pd


list = [1,2,3,4]
list_2 =  [1,2,3]
Dic = {
    "A":[1,2,3],
    "B":[2,4,6],
    "C":[3,6,9]
}
Dic_2 = {
    "A":[10,11]
}


var = pd.DataFrame(list)
var_2 = pd.DataFrame(list_2)
var_3 = pd.DataFrame(Dic)
var_4 = pd.DataFrame(Dic_2)


var_3['XX'] = var_3['A'] + var_3['B']
var_3['XY'] = var_3['A'] - var_3['B']
var_3['XZ'] = var_3['A'] / var_3['B']
var_3['XA'] = var_3['A'] * var_3['B']

var_3["<"] = var_3['A'] < var_3['B']
var_3[">"] = var_3['A'] > var_3['B']
var_3["<"] = var_3['A']*2 +1 /2 ==  var_3['B']

print(var_3)
