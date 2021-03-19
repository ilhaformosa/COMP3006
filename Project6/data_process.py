import math
import numpy as np
import pandas as pd

#%% part 1
# set seed to get consistent results
np.random.seed(128)
# random integer from 1 to 10, in 1000 rows x 10 columns
m = np.random.randint(1, 10, 10000).reshape(1000, 10)
# m = np.random.rand(1000, 10)

# pack array into csv file
columns = ('a, b, c, d, e, f, g, h, i, j')
np.savetxt('matrix.csv', m, delimiter = ',', header = columns)

# alternate way to set up column names
# pd.DataFrame(m, columns=list('abcdefghij')).to_csv("matrix.csv")
# but causes another problem later: read_csv will add another index column


#%% part 2
df = pd.read_csv('matrix.csv')
# if use np.savetxt method, we have to fix problem of column header '#a' from reading csv
# macos use Numbers to read csv, and automatically add '#' in front of the first header 'a'
df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#%% part 3
col_num = len(df.columns)
row_num = len(df.index)


#%%
avg = pd.Series()
std = pd.Series()
mode = pd.Series()
mda = pd.Series()

#%%
# arr = df.to_numpy()

#%%
avg = df.mean()
std = df.std()
mode = df.mode()
mda = df.median()

#%%
mode = mode.iloc[:1, :] # reduce the multiple mode to one

#%%s
# create the dataframe for integrate all statistics later
dat = pd.DataFrame([], columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# data.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#%%
dat.append(avg, ignore_index=True)
dat.append(std, ignore_index=True)
dat.append(mda, ignore_index=True)


#%% randomly choose 3 rows and append to the dataframe
np.random.seed(128)
rand_indices = np.random.choice((row_num), size=3, replace=False)
rand_rows = m[rand_indices, :]
rand_rows = pd.DataFrame(rand_rows)
rand_rows.columns = df.columns


dat.append(rand_rows, ignore_index=True)

#%% part 4

dat.to_csv('file.text', sep = ',')
