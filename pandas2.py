import pandas as pd

dic = {
    "A":[1,2,3,4,5,6],
    "B":[7,8,9,10,11,12]
}
list = [1,2,3,4,5,6]
list_2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
dframe = pd.DataFrame(dic)
frame = pd.DataFrame(list)
Gmm = pd.DataFrame(list_2d)
print(dframe)
print("=============" * 3)
print(frame)
print("=============" * 3)
print(Gmm)