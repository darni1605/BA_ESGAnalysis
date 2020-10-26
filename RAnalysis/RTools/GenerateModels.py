import pandas as pd
import numpy as np
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportFiles import stockReturns_df, marketPremium, SMB, HML, riskFree, \
    OverallESGScores_df, EnvironmentScores_df, SocialScores_df, GovernanceScore_df
from ImportFilesPackages.ImportRPackages import stats


def createRString(df):
    columnNames = df.columns
    rString = columnNames[0] + '~'
    for i in range(1, len(columnNames)):
        if i < len(columnNames) - 1:
            rString += columnNames[i] + '+'
        else:
            rString += columnNames[i]
    return rString


def createRModel(df):
    pandas2ri.activate()
    rModelString = createRString(df)
    rModel = stats.lm(rModelString, data=df)
    return rModel


def createDFModel(stock, level):
    stockReturns = stockReturns_df[stock]
    adjustedStockReturns = stockReturns - riskFree
    adjustedStockReturns_df = pd.DataFrame(np.log(1 + adjustedStockReturns), columns=[stock])

    if level == 1:
        ESGColumnName = stock + 'ESGScore'
        ESG = OverallESGScores_df[ESGColumnName]
        ESG = ESG[~np.isnan(ESG)]
        data = [adjustedStockReturns_df, marketPremium, SMB, HML, ESG]

    elif level == 2:
        environmentColumnName = stock + 'EnvironmentScore'
        environmentScores = EnvironmentScores_df[environmentColumnName]
        environmentScores = environmentScores[~np.isnan(environmentScores)]
        socialColumnName = stock + 'SocialScore'
        socialScores = SocialScores_df[socialColumnName]
        socialScores = socialScores[~np.isnan(socialScores)]
        governanceColumnName = stock + 'GovernanceScore'
        governanceScores = GovernanceScore_df[governanceColumnName]
        governanceScores = governanceScores[~np.isnan(governanceScores)]
        data = [adjustedStockReturns_df, marketPremium, SMB, HML, environmentScores, socialScores, governanceScores]

    df = pd.concat(data, axis=1)

    return df


def createDFModels(listOfStocks, level):
    modelList = []
    for stock in listOfStocks:
        modelList.append(createDFModel(stock, level))
    return modelList
