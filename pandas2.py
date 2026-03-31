import pandas as pd

dic = {
    "A":[1,2,3,4,5,6],
    "B":[7,8,9,10,11,12]
}
siris = {"A" : pd.Series([1,2,3,4]) , "B" : pd.Series([7,8,9,10]) }
list = [1,2,3,4,5,6]
list_2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

dframe = pd.DataFrame(dic)
lframe = pd.DataFrame(list)
l2frame = pd.DataFrame(list_2d)
lrcframe = pd.DataFrame(list_2d,index=["A","B","C"],columns=["D","E","F","G"])

print(dframe)
print(lframe)
print(l2frame)
print(lrcframe)
print(siris)