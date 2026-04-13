import pandas as pd

csv = pd.read_csv("inter.csv")


csv.replace(to_replace=1,value=10,inplace=True)                                                 # his is one process to replace any Value given the data and replace
csv.replace([1,2,3],pd.NA,inplace=True)                                                # List Given and replace to NAn Value 1,2,3
csv.replace([1,2,3],[44,55,66],inplace=True)                                     # List Given and replace to List Value 44,55,66
csv.replace([1,2,3],44,inplace=True)                                             # Single Value also change replace all The Data
csv.replace({"Day":[1,2,3,4,5,6,7,8,9]},44,inplace=True)                         # Dictionary Given and replace to NAn Value 44
csv = csv.astype(str)                                                                           # if i m working with int then 1st I need to convert into string using this parameter

#csv.replace(r'^\d+$','FF',regex=True,inplace=True)                                             # After I can replace old value to new value r for raw data ^ for starting \d all number + increase $ for end


#csv.interpolate()                                                                              # if Data is int or float it will work if object then it's not work
#csv[['Age','No']]=csv[['Age','No']].interpolate()                                              # objective Data Contain all str,Float,int ,but I need specific column to change like this
#csv.interpolate(limit_area='inside',inplace=True)                                              # Data will work all data liner wise change

print(csv)
