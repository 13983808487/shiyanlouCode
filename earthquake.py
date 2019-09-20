import pandas as pd

def clean():
    df = pd.read_csv('earthquake.csv')
    df_clean = df[df.columns[:5]]
    df_clean['region'] = df.place.str.split(
            ',', expand=True).fillna(method='ffill', axis=1)[2]
    df_clean = df_clean.dropna().drop_duplicates()
    return df_clean

def mag_region():
    df = clean()
    df.mag = pd.cut(df.mag, bins=[0, 2, 5, 7, 9, 10], right=False,
            labels=['micro', 'light', 'strong', 'major', 'great'])
    df_group = df.groupby(by=['mag', 'region']).count()
    df_reindex = df_group.reset_index().dropna()
    df_sort = df_reindex.sort_values(
            by='time', ascending=False).drop_duplicates('mag')
    df_final = df_sort.set_index('mag')[['region', 'time']].rename(
            columns={'time':'times'})
    df_final.times = df_final.times.astype('int')

    return df_final

if __name__ == '__main__':
    print(mag_region())
