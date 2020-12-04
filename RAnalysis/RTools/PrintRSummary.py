from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportRPackages import base, psych
from RAnalysis.RTools.GenerateModels import createRModel
from ImportFilesPackages.ImportFiles import companyIdentifier


# loop through all stocks, create dataframe per stock and print summary of all linear models
def printAllRegressionSummaries():
    i = 0
    while i < len(companyIdentifier):
        currentRModel = createRModel(companyIdentifier[i])
        print(base.summary(currentRModel))


# print R base summary for chosen stock
def printStockRegressionSummary(stock):
    rModel = createRModel(stock)
    print(base.summary(rModel))


# print R psych summary for chosen stock
def printDataSetSummary(dataframe):
    pandas2ri.activate()
    r_dataframe = pandas2ri.py2rpy(dataframe)
    print(psych.describe(r_dataframe).to_string())
