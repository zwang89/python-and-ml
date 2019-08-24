import pandas as pd
import numpy as np
from numpy.random import randn

lables = [ 'a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

#create series

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['a', 'b', 'c', 'd', 'e'], ['w','x','y','z'])
print(df)

# a dataframe is a series
print(df['w'])

df['x']

# pass a list to multiple columns

# create a new columns
df['new_z'] = df['x'] + df['z']
print(df)
# drop a column
df.drop('new_z', axis=1, inplace =True)
print(df)
df.shape

# two ways to select the location
# choose more than one columns and raws, you have to use list
df.loc['a']
df.iloc[0]
# select files name and date values
df.loc['b','y']


# conditional selection with data frame
df[df > 0]

# when get the column conditions with sepecific conditions, there will not be 'n/a' shows
df[df['w']>0]

df[df['z']<0]

column_one = df[df['x']>0.5]['w']

# mutiple conditions should use () for each condition and connect with & |
test = df[(df['w']>0.2) | (df['x']<0.5)]


# index work

newind = 'CA NY WA OR CO'.split()
df['states'] = 'CA NY WA OR CO'.split()

# set index

df.set_index('states', inplace = True)

# mupltiple index

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

hier_index