#Arethmetic Operation
import pandas as pd

list = [1,2,3,4]                                             # List Data 4 element
list_2 = [1,2,3]                                             # List Data 3 element
list_1 = [[1,2,3,4],[5,6,7,8]]                               # List Inside List
Dic = {                                                      # Dictionary Large
    "A" : [1,2,3,4],
    "B" : [5,6,7,8]
}
Dic_2 = {                                                    # Low Value Dictionary
    'x' : [1,2]
}


var   = pd.DataFrame(Dic)                                    # Make DataFrame Dictionary
var_2 = pd.DataFrame(Dic_2)                                  # Make DataFrame Dictionary
var_1 = pd.DataFrame(list)                                   # Make DataFrame list
var_3 = pd.DataFrame(list_2)                                 # Make DataFrame List Upon List


var['X'] = var['A'] + var['B']                              # here var[x] = new variable to store the arithmetic operation An ** + - / x **
var['Y'] = var['A'] < 3                                     # Logical Code Return var A value smaller than 3 return boolean value

print(var)                                                  # Reflect after update
print(var_1 + var_3)                                        # Reflect lower value contain data time only other NAN (List)
print(var['A']+var_2['x'])                                  # Reflect lower value contain data time only other NAN (Dictionary)
