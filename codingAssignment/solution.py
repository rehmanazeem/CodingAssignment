import pandas as pd

# importing data
data = pd.read_csv("data.csv",'|')

# dropping column -> 'H'
data1 = data.iloc[:,1:].reset_index().drop(columns='index')

# creating unique countries list
countryList = [x for x in data1['Country'].unique()]

# creating separate country tables
for x in countryList:
    df = data1[data1['Country'] == x]
    df.to_csv(f'table_{x}.csv',index=False)