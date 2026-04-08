#csv Creating using Pandas
import pandas as pd

data = {
    "ID" : ['1A','1B','1C','1D'],                                   # Create Dictionary As 2D value set
    "Name" :['sayan','Rupa','Rahul','Anik']
}
df = pd.DataFrame(data)                                             # Make 2D Frame


df.to_csv('data.csv')                                               # Create CSV File
df.to_csv('data.csv',index = False)                       # Index number False not to show inside Excel CSV
df.to_csv('data.csv',header = False)                      # Column number False not to show inside Excel CSV
df.to_csv('data.csv',header = [1,2])                      # Header Create new column name/int given
