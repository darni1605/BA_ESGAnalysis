import rpy2.robjects as robjects
import pandas as pd
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportRPackages import base, stats, psych
from RAnalysis.RTools.GenerateModels import createRModel
from ImportFilesPackages.ImportFiles import nrOfColumns, stockPrices_df, ESGScores_df, companyIdentifier \
    , marketPremium, SMB, HML, riskFree


# loop through all stocks, create dataframe per stock and print summary of all linear models #
def printAllRegressionSummaries():
    i = 0
    while i < len(companyIdentifier):
        currentRModel = createRModel(companyIdentifier[i])
        print(base.summary(currentRModel))


def printStockRegressionSummary(stock):
    rModel = createRModel(stock)
    print(base.summary(rModel))


def printDataSetSummary(dataframe):
    pandas2ri.activate()
    r_dataframe = pandas2ri.py2rpy(dataframe)
    print(psych.describe(r_dataframe))
