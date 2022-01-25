# To obtain correct gender based on first name

#%%
import os
# Source data from: https://www.ssa.gov/oact/babynames/limits.html :: National data
t = os.listdir('names')
print(t)

#%%
import pandas as pd
li = []

for filename in t:
    df = pd.read_csv('names/'+filename, index_col=None, header=None)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

#%%
frame.columns = ['name', 'gender', 'count']
#%%
names = frame.values.tolist()
#%%
n_dict = {}

for i in names:
    if f'{i[0]}_{i[1]}' in n_dict:
        n_dict[f'{i[0]}_{i[1]}'] += i[2]
    else:
        n_dict[f'{i[0]}_{i[1]}'] = i[2]
#%%
n_dict_a = sorted(n_dict)
#%%
# Data is sorted by smallest first so that the final value for any name and gender combination is the most common
# seen in the data (so if uncertain then choose the most likely option but risk it is incorrect)
import operator
n_dict_a = sorted(n_dict.items(), key=operator.itemgetter(1))
#%%
n_dict_2 = {}
for a, b in n_dict_a:
    name = a.split('_')[0].lower()
    gender = a.split('_')[1].lower()
    n_dict_2[name] = gender
#%%
l = []
for i in n_dict_2.items():
    m = list(i)
    l.append(m)


#%%
# Export for import into the database for final export code
import csv
with open('names.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(l)
#%%
