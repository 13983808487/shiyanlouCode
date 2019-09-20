import pandas as pd

def clean():
    df = pd.read_csv('earthquake.csv')
    df_clean = df[df.columns[:5]]
    df_clean['region'] = df.place.str.split(
            ',', expand=True).fillna(method='ffill', axis=1)[2]
    df_clean = df_clean.dropna().drop_duplicates()
    return df_clean

if __name__ == '__main__':
    print(clean())
