import pandas as pd
from rpy2 import robjects
from rpy2.robjects import Environment
from rpy2.robjects import pandas2ri
from importFilesPackages.importData import stockPrices_df, famaFrench_RiskFactors_df, ESGScores_df
from importFilesPackages.importRPackages import base, stats


def whatisthis(s):
    if isinstance(s, str):
        print(s + " is ordinary string")
    elif isinstance(s, 'utf-8'):
        print(s + " is utf-8 string")
    else:
        print(s + " not a string")


# extract Fama & French risk factors #
marketPremium = famaFrench_RiskFactors_df.iloc[:, 0]
SMB = famaFrench_RiskFactors_df.iloc[:, 1]
HML = famaFrench_RiskFactors_df.iloc[:, 2]
riskFree = famaFrench_RiskFactors_df.iloc[:, 3]

# loop through all stocks, create dataframe per stock and print summary of all linear models #
companyIdentifier = list(stockPrices_df)
nrOfColumns = len(stockPrices_df.columns)
i = 0

R = robjects.r
pandas2ri.activate()
while i < nrOfColumns - 1:
    currentStock = stockPrices_df.iloc[:, i]
    currentStockESG = ESGScores_df.iloc[:, i * 5]
    currentCompanyIdentifier = companyIdentifier[i]
    currentESGColumnName = companyIdentifier[i] + 'ESGScore'
    print(currentCompanyIdentifier + "  ------  " + currentESGColumnName)

    data = [currentStock, marketPremium, SMB, HML, riskFree, currentStockESG]
    currentDataFrame = pd.concat(data, axis=1)
    hasOnlyNaN = False
    if len(currentDataFrame.columns) > len(currentDataFrame.dropna(1, 'all').columns):
        hasOnlyNaN = True

    if not hasOnlyNaN:
        currentModelRString = (currentCompanyIdentifier + '~ MarketPremium + SMB + HML + RF + ' + currentESGColumnName)
        currentRModel = R.lm(currentModelRString, data=currentDataFrame)
        print(base.summary(currentRModel))
        i += 1
    else:
        i += 1
