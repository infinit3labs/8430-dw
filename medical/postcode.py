import pandas as pd
import numpy as np

def pcode_valid(row):
    if row['postcode'] != '' and row['suburb'] != '':
        try:
            pcode_src = row['postcode']
            suburb_src = row['suburb']
            suburbs_lookup = [x.lower() for x in pc1[pcode_src]]
            if suburb_src in suburbs_lookup:
                return 1
            else:
                return 0
        except KeyError:
            return 'invalid postcode'

df = pd.read_csv('medical_clean.csv', dtype=str)

pc = pd.read_csv('australian_postcodes.csv', dtype=str)

pc = pc[['postcode', 'locality', 'state']]

pc1 = pc.groupby('postcode')['locality'].apply(list)

df = df.replace(np.nan, '', regex=True)

df['pcode_check'] = df.apply(lambda row: pcode_valid(row), axis=1)

def suburb_valid(row):
    if row['postcode'] != '' and row['suburb'] != '' and row['state'] != '':
        pcode_src = row['postcode']
        suburb_src = row['suburb']
        state_src = row['state']
        src_key = suburb_src + state_src
        try:
            postcode_lookup = pc2.loc[pc2['key'] == src_key]['postcode'].values[0]
            if pcode_src == postcode_lookup:
                return 1
            else:
                return 0
        except IndexError:
            return 'invalid locality'

pc2 = pc
pc2['key'] = pc.locality + pc.state
pc2['key'] = pc2.key.str.lower()


df['suburb_check'] = df.apply(lambda row: suburb_valid(row), axis=1)

t = df.loc[df['rec_id'] == 'rec-49632'].copy()
t['suburb_check'] = t.apply(lambda row: suburb_valid(row), axis=1)

print('x')