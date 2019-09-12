#!/usr/bin/env python3

import pandas as pd

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    countries = pd.read_excel('ClimateChange.xlsx', sheetname='Country')

    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data.drop(data.columns[:5], axis=1, inplace=True)
    data.replace('..', pd.np.nan, axis=1, inplace=True)
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data.dropna(how='all', inplace=True)
    data['Sum emissions'] = data.sum(axis=1)
    data = data['Sum emissions']

    countries.drop(['Capital city', 'Region', 'Lending category'], 
            axis=1, inplace=True)
    countries.set_index('Country code', inplace=True)

    return pd.concat([data,countries], axis=1, join='inner')

def co2():
    df = data_clean()

    df_sum = df.groupby('Income group').sum()
    df_max = df.sort_values('Sum emissions', ascending=False
            ).groupby('Income group').head(1).set_index('Income group')
    df_max.columns = ['Highest emissions', 'Highest emission country']
    df_max = df_max.reindex(columns=['Highest emission country', 'Highest emissions'])
    df_min = df.sort_values('Sum emissions'
            ).groupby('Income group').head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions', 'Lowest emission country']
    df_min = df_min.reindex(columns=['Lowest emission country', 'Lowest emissions'])

    result = pd.concat([df_sum,df_max,df_min], axis=1)
    return result


if __name__ == '__main__':
    print(co2())





