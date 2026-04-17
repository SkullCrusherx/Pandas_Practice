#merge and Concate
import pandas as pd

df1 = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
df2 = pd.DataFrame({"A":[1,2,4],"B":[4,5,6]})
df3 = pd.DataFrame({"A":[1,2,4],"C":[4,5,6]})
df4 = pd.DataFrame({"A":[1,2],"C":[5,6]})


g = pd.merge(df1,df3,on = "A" )
h = pd.merge(df1,df3,how = "left")
i = pd.merge(df1,df3,how = "right")
j = pd.merge(df1,df3,how = "inner")
k = pd.merge(df1,df3,how = "outer")
l = pd.merge(df1,df3,how = "outer",indicator=True)
m = pd.merge(df1,df2,left_index=True,right_index=True,suffixes=("_1","_2"))

v1 = pd.concat([df1,df3],axis=0)
v2 = pd.concat([df1,df3],axis=1)
v3 = pd.concat([df1,df4],join="inner")
v4 = pd.concat([df1,df4],join="outer")
v5 = pd.concat([df1,df2],keys = ["F1","F2"])
v6 = pd.concat([df1,df2],keys = ["F1","F2"],axis=1)

print(v1)
print()
print(v2)
print()
print(v3)
print()
print(v4)
print()
print(v5)
print()
print(v6)
