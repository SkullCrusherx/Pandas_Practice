import pandas as pd

df1 = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
df2 = pd.DataFrame({"A":[1,2,4],"B":[4,5,6]})


g = pd.merge(df1,df2,on = "A" )
h = pd.merge(df1,df2,how = "left")
i = pd.merge(df1,df2,how = "right")


print("G",g)
print()
print("H",h)
print()
print("I",i)
