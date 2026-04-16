import pandas as pd

df1 = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
df2 = pd.DataFrame({"A":[1,2,4],"B":[4,5,6]})
df3 = pd.DataFrame({"A":[1,2,4],"C":[4,5,6]})


g = pd.merge(df1,df3,on = "A" )
h = pd.merge(df1,df3,how = "left")
i = pd.merge(df1,df3,how = "right")
j = pd.merge(df1,df3,how = "inner")
k = pd.merge(df1,df3,how = "outer")
l = pd.merge(df1,df3,how = "outer",indicator=True)
m = pd.merge(df1,df2,left_index=True,right_index=True,suffixes=("_1","_2"))


print(g)
print()
print(h)
print()
print(i)
print()
print(j)
print()
print(k)
print()
print(l)
print()
print(m)
