import pandas as pd

df1 = pd.DataFrame.from_dict({"A": ["x", "y", "z", "w"], "B": ["i", "j", "k", "l"]})
df2 = pd.DataFrame.from_dict({"C": ["w", "t", "s", "x"], "D": ["n", "y", "z", "m"], "E": [1, 2, 3, 4]})

df3 = df1.merge(df2[['C', 'E']], left_on='A', right_on='B', how='left')
df3.drop('C', axis=1, inplace=True)

df3['E'] = df3['E'].fillna(df2['E'])

print(df3)
