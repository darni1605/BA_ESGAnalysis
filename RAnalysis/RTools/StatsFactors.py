import pandas as pd
import matplotlib.pyplot as plot
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from RAnalysis.RTools.GenerateModels import createDFModel


def getVIF(stock):
    dfModel = createDFModel(stock)
    dfModel.drop(labels=stock, axis=1, inplace=True)

    vif_data = pd.DataFrame()
    vif_data['Factor'] = dfModel.columns

    vif_data['VIF'] = [variance_inflation_factor(dfModel.values, i)
                       for i in range(len(dfModel.columns))]
    return vif_data

