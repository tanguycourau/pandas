#coding: utf-8
import pandas as pd
import numpy as np
# un dataframe tout simple

df = pd.DataFrame.from_dict({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9],
    'C': [3.3, 5.4, 1.5]})


df.columns.name='col'

## acces direct et via loc 

df[1:3]
df[['A', 'C']]

df.loc[:,['A', 'C']]
df.loc[[0, 2], ['A', 'C']]

df['D'] = [9, 10, 11]
df.loc[3] = [11,12,13,14]

df.index= ['u','v','w', 't']
df.index.name='row' 
df.loc['v']

df['E'] = df['A']+df['B'] 


df.reset_index(drop=False)

df.transpose()



## Query
val = 5
df.loc[:, ['F']] = ['ab', 'acd', 'ef', 'az']
df.query(expr="A<@val&B>6")

## Apply
df.loc['s']=df.apply(np.sum)
df.apply(lambda x: np.square(x) if x.name != 'F' else x, axis=0)
df['F']=df.apply(lambda x:x.F+'hi', axis=1)


## Multi level columns

dico = {('eff', 'theo', 'A'): (-3.0, 'valid'), ('eff', 'exp', 'A'): (3.0, 'valid'), ('eff', 'theo', 'B'): (-5.0, 'valid'), ('eff', 'exp', 'B'): (5.0, 'valid')} 
dfm = pd.DataFrame.from_dict(dico)

dfm.columns
dfs = dfm['eff'] 

dfs['theo']
dfs['exp', 'A']
dfs.columns=dfs.columns.swaplevel(0, 1)



## Join

dfi = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})

dfi.join(other.set_index('key'), on='key')


## Pivot & duplicates


dfp = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two','two'],
                    'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'baz': [1, 2, 3, 4, 5, 6],
                    'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
dfp.drop_duplicates(subset=['baz'], keep='last')
dfp.pivot(index='foo', columns='bar', values='baz')


#dfp.drop_duplicates(subset=['brand', 'style'], keep='last')
