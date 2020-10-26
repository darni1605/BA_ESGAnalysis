import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor


def getVIF(dataFrame):
    df = dataFrame.drop(dataFrame.columns[0], axis=1)
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(axis=0, how='any', inplace=True)
    vif_data = pd.DataFrame()
    vif_data['Factor'] = df.columns

    vif_data['VIF'] = [variance_inflation_factor(df.values, i)
                       for i in range(len(df.columns))]
    return vif_data


# set limit for exclusion to either 5 or 10
def excludeMultiCollinearity(dataFrame, limit):
    vif_data = getVIF(dataFrame)
    vif_values = vif_data.values[:, 1]
    maxIndex = np.argmax(vif_values)
    if vif_values[maxIndex] > limit:
        del dataFrame[vif_data.iloc[maxIndex, 0]]
        excludeMultiCollinearity(dataFrame, limit)
        return dataFrame
    else:
        return dataFrame
