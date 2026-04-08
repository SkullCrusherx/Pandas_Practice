import pandas as pd

data = {
    "ID" : ['1A','1B','1C','1D'],
    "Name" :['sayan','Rupa','Rahul','Anik']
}
df = pd.DataFrame(data)
print(df)
#df.to_csv('data.csv')