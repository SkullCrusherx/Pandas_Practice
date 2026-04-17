import pandas as pd

var = pd.DataFrame({
    "Name":['A','B','C','D','A','B','C','D','A','B','C'],
    'ID' : [11,22,33,44,55,66,77,88,99,101,201],
    'Roll' : [1,2,3,4,5,6,7,8,9,10,11]
                    })

f = var.groupby("Name")                                                            # Store into Variable and key is name (column name)

for group,data_frame in f:                                                         # for loop use for checking all Data Group name 1st and  2nd is Data
    print('*'*9,group,'*'*9)                                                       # For Group Name
    print(data_frame)                                                              # For Data frame clean sequence
    print()


print(f.get_group("B").min())                                                       # min value Get from specific Data
print()
print(f.get_group("B").max())                                                       # max value get from specific Data
print(f.min())
print(f.max())


x = list(f)                                                                         # Convert into List
print(x[0][1])