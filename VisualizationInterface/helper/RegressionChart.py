import numpy as np
from ImportFilesPackages.ImportFiles import *


def getModelString(stock, level):
    if level == 1:
        columnNames = survivingStockModels1stLevel.loc[survivingStockModels1stLevel['Stock'] == stock].values
    if level == 2:
        columnNames = survivingStockModels2ndLevel.loc[survivingStockModels2ndLevel['Stock'] == stock].values
    cleanColumnNames = [x for x in columnNames[0] if str(x) != 'nan']
    modelString = ''
    for i in range(1, len(cleanColumnNames) - 1):
        modelString = modelString + str(cleanColumnNames[i]) + ' + '
    modelString = modelString + str(cleanColumnNames[len(cleanColumnNames) - 1])
    return modelString


def prepareDataSet(stock, level):
    dataSet = []
    modelString = getModelString(stock, level)
    observedReturns = stockReturns_df[stock]

    for i in range(0, len(observedReturns) - 1):
        currentRegressionValues = []
        if not np.isnan(observedReturns[i]):
            currentRegressionValues.append(observedReturns[i] * 100)
            currentRegressionValues.append(marketPremium[i])
            currentRegressionValues.append(SMB[i])
            currentRegressionValues.append(HML[i])

        if level == 1:
            stockESG = OverallESGScores_df[stock + 'ESGScore']
            if not np.isnan(stockESG[i]):
                currentRegressionValues.append(stockESG[i])
        if level == 2:
            if stock + 'EnvironmentScore' in modelString:
                stockEnv = EnvironmentScores_df[stock + 'EnvironmentScore']
                if not np.isnan(stockEnv[i]):
                    currentRegressionValues.append(stockEnv[i])
            if stock + 'SocialScore' in modelString:
                stockSoc = SocialScores_df[stock + 'SocialScore']
                if not np.isnan(stockSoc[i]):
                    currentRegressionValues.append(stockSoc[i])
            if stock + 'GovernanceScore' in modelString:
                stockGov = GovernanceScore_df[stock + 'GovernanceScore']
                if not np.isnan(stockGov[i]):
                    currentRegressionValues.append(stockGov[i])

        if len(currentRegressionValues) != 0:
            dataSet.append(currentRegressionValues)

    return dataSet
