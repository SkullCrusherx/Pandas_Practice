import pandas as pd

"""df1 = pd.DataFrame({"A":[1,2,3]})
df2 = pd.DataFrame({"A":[1,2,4]})
df3 = pd.DataFrame({"A":[1,2,5]})

g = pd.merge(pd.merge(df1,df2,how="left"),df3,how='left')
h = pd.merge(pd.merge(df1,df2,how="right"),df3,how='right')

print(g)
print()
print(h)
print()"""


csv = pd.read_csv('new.csv')
csv['Time'] = csv['Time'].astype('int64')
csv['Time'] = csv["Time"].interpolate()
print(csv)
