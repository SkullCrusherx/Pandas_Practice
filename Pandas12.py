import pandas as pd

var = pd.DataFrame({'A':[1,2,3,4,5],"B":[6,7,8,9,10]},index=[2,3,4,7,9],columns=['K','Y','Z','H','J'])
var_2 = pd.DataFrame({'C':[1,2,3,4],"D":[6,7,8,9]},index=[2,3,4,7],columns=['K','L','M','N'])

print(var.join(var_2,how='outer'))
