#DataFrame
import pandas as pd

list = [1,2,3,4]                                           # List Data
list_1 = [[1,2,3,4],[5,6,7,8]]                             # List Inside List
Dic = {                                                    # Dictionary
    "A" : [1,2,3,4],
    "B" : [5,6,7,8]
}


var_1 = pd.DataFrame(list)                                 # Make List 2D DataFrame
var_2 = pd.DataFrame(list_1)                               # Make list 2D Dataframe but Row is 2 and Column element of Dataset
var_3 = pd.DataFrame(Dic)                                  # Here 2D key make Column Name and values [list] which is Given is the element (equal Data length mandatory or value error reflect)
var_4 = pd.DataFrame(Dic,columns=["A"])                    # Given columns to check specific column elements
var_5 = pd.DataFrame(Dic,index=["Q","W","E","R"])          # change index number normal digit to according user Defined


print(var_1)                                                # Reflect list Data
print(var_2)                                                # Reflect whole list into 2D Table
print(var_3)                                                # Reflect Dictionary into 2D Table
print(type(var_1))                                          # Print which function used Here
print(var_2[0][0])                                          # According to List var print only specific from list to list Data then 1st whch list then row like var_2[list_number][row_number]
print(var_3["A"][1])                                        # Dictionary time 1St columns name then row index number like these
print(var_4)                                                # Reflect the column id by name
print(var_5)                                                # reflect after changing all the row(index number)
print(var_5[0][1])