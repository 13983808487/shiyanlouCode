import pandas as pd
import matplotlib.pyplot as plt

'''
def data_select_scode_allyears_quantum(codename):
    data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
    data = data[data['Series code']==codename].set_index('Country code')
    data.drop(data.columns[:5], axis=1, inplace=True)
    data.replace({'..':pd.np.nan}, inplace=True)
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data.dropna(how='all',inplace=True)
    data = data.sum(axis=1)
    data = data.fillna(value=0)

    return data
'''

def co2_gdp_plot():
    def data_select_scode_allyears_quantum(codename):
        data = pd.read_excel('ClimateChange.xlsx', sheetname='Data')
        data = data[data['Series code']==codename].set_index('Country code')
        data.drop(data.columns[:5], axis=1, inplace=True)
        data.replace({'..':pd.np.nan}, inplace=True)
        data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
        data.dropna(how='all',inplace=True)
        data = data.sum(axis=1)
        data = data.fillna(value=0)

        return data

    # TODO
    data_gdp = data_select_scode_allyears_quantum('NY.GDP.MKTP.CD')
    data_co2 = data_select_scode_allyears_quantum('EN.ATM.CO2E.KT')

    data = pd.concat([data_co2,data_gdp],axis=1)
    #data.columns = ['CO2-SUM', 'GDP-SUM']
    data.columns = ['GDP-SUM', 'CO2-SUM']

    data_max_min = (data - data.min()) /\
            (data.max() - data.min())

    china = []
    china.extend(pd.np.round(data_max_min.loc['CHN'].values,3).tolist())

    countries_labels = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    sticks_labels = []
    labels_position = []
    for i in range(len(data_max_min)):
        if data_max_min.index[i] in countries_labels:
            #sticks_labels.append(data_max_min[i])
            sticks_labels.append(data_max_min.index[i])
            labels_position.append(i)
    
    fig = plt.subplot()
    data_max_min.plot(
            kind='line',
            title='GDP-CO2',
            ax=fig
            )
    plt.xlabel('Counties')
    plt.ylabel('Values')

    plt.xticks(labels_position, sticks_labels, rotation='vertical')
    plt.show()

    return fig, china

if __name__ == '__main__':
    print(co2_gdp_plot())
