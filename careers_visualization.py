import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("C:/Users/ACER/PycharmProjects/handcricket/batsmans_career.csv")
df1=pd.read_csv("C:/Users/ACER/PycharmProjects/handcricket/machines_career.csv")

plt.plot(df.index,df.iloc[:,:], label='user statistics')
plt.plot(df1.index,df1.iloc[:,:], label='machine statistics')
plt.title("statistics")
plt.xlabel("matches")
plt.ylabel("score")
plt.xticks(range(0,df.shape[0]+1))
plt.legend()
plt.show()