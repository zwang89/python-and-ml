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

df = pd.DataFrame(randn(6,2),hier_index,['a','b'])

df.index.names=['groups','nums']

df.loc['G1'].loc[3]['a']

# cross section

print(df.loc['G1'])
print(df.xs('G1'))

# deal with missing values

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df.dropna(thresh=1)

# fillna method
df.fillna(value = df.mean())

# group by method

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df_company = df.groupby('Company')

#have to speicific methods
print(df_company.describe().transpose())


# merging, joining, and conconcateting
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


#concatenation
# must past a iteraturable, such as list, object to concat function
pd.concat([df1,df2,df3])

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left,right,how='inner', on ='key')

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# joining, same as merging but the merging on columns will be the index instead of a column
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


left.join(right)

pd.merge(left,right)


# pandas operations
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

# find unqiue values in comlunms
print(df['col3'].nunique())
# number of unqiue values


# apply methods
def times2(x):
    return x*2
print(df['col1'].apply(times2))
print(df['col1'].apply(lambda x: x*3))
df.columns
df.index


df.sort_values(by='col2')

# pivot table
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

df.pivot_table(values='D', index=['A','B'], columns = ['C'])

# data input and output

pd.read_csv
pd.to_csv('my_outcome', index=False)

pd.read_excel('example.xlsx',sheet_name='Sheet=1')


data = pd.read_html('https://www.cdc.gov/drugoverdose/data/prescribing/prescribing-practices.html')


# use sql within sql

from sqlalchemy import create_engine
engin = create_engine('sqlite:///:memory:')
df.to_sql('df', engin)


