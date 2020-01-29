import pandas as pd
import matplotlib.pyplot as plt

file = r"F:\WACOMA\PYTHON\data\natural_disasters.csv"

df = pd.read_csv(file)

#df.plot(x='Year', y='Deaths', kind = 'box')
# df.groupby('Entity').mean().plot()

# gb = df.groupby('Entity').mean()
# gb.plot(y='Deaths' , kind= 'bar', color='blue')

# plt.show()



# gy = df.groupby('Year').mean()
# gy.plot(y='Deaths', kind='line')
# plt.show()


# gy = df.groupby('Year').sum()
# plt.show()

# Merging files
file1 = r"F:\WACOMA\PYTHON\data\d1.csv"
file2 = r"F:\WACOMA\PYTHON\data\d2.csv"

d1 = pd.read_csv(file1)
d2 = pd.read_csv(file2)

d3=d1.merge(d2, left_on='Code', right_on='Code', suffixes = ('_left_' , '_right_'))
print(d3.head())



