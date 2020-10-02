import pandas as pd
import numpy as np
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportFiles import stockReturns_df, marketPremium, SMB, HML, riskFree, \
    OverallESGScores_df, EnvironmentScores_df, SocialScores_df, GovernanceScore_df
from ImportFilesPackages.ImportRPackages import stats


def createRString(stock, level):
    if level == 1:
        rString = stock + '~ MarketPremium + SMB + HML +' + stock + 'ESGScore'
    elif level == 2:
        environmentColumnName = stock + 'EnvironmentScore +'
        socialColumnName = stock + 'SocialScore +'
        governanceColumnName = stock + 'GovernanceScore'
        rString = stock + '~ MarketPremium + SMB + HML +' \
                  + environmentColumnName + socialColumnName + governanceColumnName

    return rString


def createRModel(stock, level):
    df = createDFModel(stock, level)
    hasOnlyNaNColumn = False

    if len(df.columns) > len(df.dropna(1, 'all').columns):
        hasOnlyNaNColumn = True

    if not hasOnlyNaNColumn:
        pandas2ri.activate()
        rModelString = createRString(stock, level)
        rModel = stats.lm(rModelString, data=df)
        return rModel

    else:
        return hasOnlyNaNColumn


# test with log returns #
def createDFModel(stock, level):
    stockReturns = stockReturns_df[stock]
    adjustedStockReturns = stockReturns - riskFree
    adjustedStockReturns_df = pd.DataFrame(np.log(1 + adjustedStockReturns), columns=[stock])

    if level == 1:
        ESGColumnName = stock + 'ESGScore'
        ESG = OverallESGScores_df[ESGColumnName]
        data = [adjustedStockReturns_df, marketPremium, SMB, HML, ESG]

    elif level == 2:
        environmentColumnName = stock + 'EnvironmentScore'
        environmentScores = EnvironmentScores_df[environmentColumnName]
        socialColumnName = stock + 'SocialScore'
        socialScores = SocialScores_df[socialColumnName]
        governanceColumnName = stock + 'GovernanceScore'
        governanceScores = GovernanceScore_df[governanceColumnName]
        data = [adjustedStockReturns_df, marketPremium, SMB, HML, environmentScores, socialScores, governanceScores]

    df = pd.concat(data, axis=1)

    return df
