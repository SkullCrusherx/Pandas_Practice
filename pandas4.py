#insert and delete Element From DataFrame And Also Series
import pandas as pd

var = {
    "A" :[1,2,3,4],
    "B" :[5,6,7,8],
    "C" :[9,10,11,12],
    "D" :[13,14,15,16]
}

df = pd.DataFrame(var)
df.insert(1,"NN",[11,22,33,44])
