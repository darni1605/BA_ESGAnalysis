import pandas as pd
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportFiles import stockReturns_df, ESGScores_change_df, ESGScores_df, marketPremium, SMB, HML, riskFree
from ImportFilesPackages.ImportRPackages import stats


def createRModel(stock):
    df = createDFModel(stock)
    ESGColumnName = stock + 'ESGScore'
    hasOnlyNaNColumn = False

    if len(df.columns) > len(df.dropna(1, 'all').columns):
        hasOnlyNaNColumn = True

    if not hasOnlyNaNColumn:
        pandas2ri.activate()
        currentModelRString = (stock + '~ MarketPremium + SMB + HML +' + ESGColumnName)
        currentRModel = stats.lm(currentModelRString, data=df)
        return currentRModel

    else:
        return hasOnlyNaNColumn


def createDFModel(stock):
    stockReturns = stockReturns_df[stock]
    adjustedStockReturns = stockReturns - riskFree
    adjustedStockReturns_df = pd.DataFrame(adjustedStockReturns, columns=[stock])
    ESGColumnName = stock + 'ESGScore'
    ESG = ESGScores_change_df[ESGColumnName]

    data = [adjustedStockReturns_df, marketPremium, SMB, HML, ESG]
    df = pd.concat(data, axis=1)

    return df
