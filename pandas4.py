#DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv = pd.read_csv("new.csv",usecols=["Day"],skiprows=0)
csv1 = pd.read_csv("new.csv",usecols=["Time"],skiprows=0)
Days = np.array(csv).reshape(-1)
Work_Time = np.array(csv1).reshape(-1)

plt.title("Office Work Entry")
plt.xlabel("Day")
plt.ylabel("Time")
plt.bar(Days,Work_Time)
plt.xticks(Days)
plt.show()



