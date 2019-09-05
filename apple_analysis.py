import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv')
    df = pd.Series(data['Volume'].values,
            index=pd.to_datetime(data['Date'].values))
    volume = df.resample('Q').sum()
    second_volume = volume.sort_values(ascending=False)[1]
    time = volume.sort_values(ascending=False).index[1]
    print(time)
    return second_volume
if __name__ == "__main__":
    print(quarter_volume())
