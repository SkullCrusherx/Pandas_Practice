import pandas as pd

data = {
    "ID" : ['1A','1B','1C','1D'],                                   # Create Dictionary As 2D value set
    "Name" :['sayan','Rupa','Rahul','Anik']
}
df = pd.DataFrame(data,index=None)                                             # Make 2D Frame

print(df)

#df.to_csv('data.csv')