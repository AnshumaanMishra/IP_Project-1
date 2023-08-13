import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Programming\IP_Project\ip_data.csv")

X_axis = np.array([0.0,0.2,0.4,0.6])

  
plt.bar(X_axis, df.iloc[0,3:], 0.19, label = df.Name[0])
plt.bar(X_axis + 1, df.iloc[1,3:], 0.19, label = df.Name[1])
plt.bar(X_axis + 2, df.iloc[2,3:], 0.19, label = df.Name[2])
plt.bar(X_axis + 3, df.iloc[3,3:], 0.19, label = df.Name[3])
plt.bar(X_axis + 4, df.iloc[4,3:], 0.19, label = df.Name[4])


plt.legend(fontsize= 8)
plt.xticks([0,0.19,0.38,0.57,1,1.19,1.38,1.57,2,2.19,2.38,2.57,3,3.19,3.38,3.57,4,4.19,4.38,4.57],labels=['English', 'Maths', 'Physics', 'IP','English', 'Maths', 'Physics', 'IP','English', 'Maths', 'Physics', 'IP','English', 'Maths', 'Physics', 'IP','English', 'Maths', 'Physics', 'IP'], rotation = 90)


plt.ylabel("No. of Marks")
plt.title('Marks of 5 students in 4 subjects')
fig = plt.gcf()
fig.set_dpi(70)
plt.subplots_adjust(bottom=0.19)
plt.show()