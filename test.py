import pandas as pd

df = pd.read_csv("data/Spotify_Youtube.csv", index_col=0)
# print(df.head())  # top 5 rows
# print(df.tail())  # bottom 5 rows
# for i, elem in df.iterrows():
#     print(i, elem)
#     break
#
# print(df[df.Artist == "SICK LEGEND"].loc[20708, 'Artist'])
# print(df[df.Artist == "SICK LEGEND"].iloc[:, 0])
# print(df.Artist == "SICK LEGEND")
#
#print(df.columns)
COLUMNS_LIST = ['Danceability', 'Energy', 'Loudness', 'Speechiness',
                'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']
#
# print(df[COLUMNS_LIST])
#
# for i, elem in df.iterrows():
#     print(elem.loc[COLUMNS_LIST].values)
#     break


df.dropna(subset=COLUMNS_LIST, inplace=True)

a = [[1, 2, 3], [4, 5, 6], [7]]
b = []
for elem in a:
    for i in elem:
        b.append(i)

b = [1, 2, 3]
print(sum(a, []))
print(df[COLUMNS_LIST].describe())


def normalize(x):
    return (x - min_x) / (max_x - min_x)


# for column in COLUMNS_LIST:
#     max_x, min_x = df[column].max(), df[column].min()
#     df[:, column] = df[column].apply(normalize)
#
# print(df['Danceability'].max())
# print(df['Danceability'].min())



# a = [int(i) for i in input().split()]
# c_null = a.count(0)
# for elem in a:
#     if elem == 0:
#         a.pop(a.index(elem))
# print(*(a + [0] * c_null))

a = list(map(int, input().split()))
i = 0
while i < len(a)-a.count(0):
    if a[i] == 0:
        a = a[:i]+a[i+1:]+[0]
    else:
        i += 1
print(a)
from math import factorial
a = [int(i) for i in input().split()]
c = 0
for elem in a:
    if a.count(elem) > 1:
        c += factorial(a.count(elem)) // (2*factorial(a.count(elem)-2))
print(c)
