import pandas as pd

var = pd.DataFrame({'A':[1,2,3,4,5],"B":[6,7,8,9,10]})
var_2 = pd.DataFrame({'C':[1,2,3,4,5],"D":[6,7,8,9,10]})

var.join(var_2)
print(var)