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

pc = pc[['postcode', 'locality']]

pc1 = pc.groupby('postcode')['locality'].apply(list)

df = df.replace(np.nan, '', regex=True)

df['pcode_check'] = df.apply(lambda row: pcode_valid(row), axis=1)
