#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_plot(file):
    try:
        df = pd.read_json(file)
    except ValueError:
        print('file not found')
        return 0
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('StudyData')
    x_ticks = np.arange(0, 250000, 50000)
    y_ticks = np.arange(0, 3500, 500)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    x = df.groupby('minutes').sum()
    y = df.groupby('user_id').sum()
    #ax.plot(df.groupby('user_id').sum())
    #ax = y.plot.line()
    plt.show()

    return ax
if __name__ == "__main__":
    data_plot('user_study.json')
