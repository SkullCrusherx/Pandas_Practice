import pandas as pd

df1 = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
df2 = pd.DataFrame({"A":[1,2,4],"B":[4,5,6]})
df3 = pd.DataFrame({"A":[1,2,4],"C":[4,5,6]})


g = pd.merge(df1,df3,on = "A" )
h = pd.merge(df1,df2,how = "left")
i = pd.merge(df1,df2,how = "right")


print(g)
print()
print(h)
print()
print(i)
