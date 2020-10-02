import rpy2.robjects as robjects
import numpy as np
from rpy2.robjects import pandas2ri
from RAnalysis.RTools.GenerateModels import createRModel


# TODO: make list of stocks as parameter to extract summaries
def extractSummaries(listOfStocks, level):
    R = robjects.r
    pandas2ri.activate()
    summaries = []
    for stock in listOfStocks:
        currentRModel = createRModel(stock, level)
        if not isinstance(currentRModel, bool):
            summary = R.lm(currentRModel)
            summaries.append(summary)
    return summaries


def extractCoefficients(summaries):
    coefficients = []
    for summary in summaries:
        currentCoefficients = summary.rx2('coefficients')
        coefficients.append(currentCoefficients)
    return coefficients


def extractESGBetas(listOfCoefficients):
    ESGBetas = np.empty(0)
    for coefficient in listOfCoefficients:
        currentESGBeta = coefficient[4]
        ESGBetas = np.append(ESGBetas, currentESGBeta)
    return ESGBetas


def excludeOutliers(data):
    Q1 = np.nanquantile(data, 0.25)
    Q3 = np.nanquantile(data, 0.75)
    IQR = Q3 - Q1

    i = 0
    while i < data.size - 1:
        if data[i] == np.nan:
            i += 1
        if (data[i] > (Q3 + 1.5 * IQR)) or (data[i] < (Q1 - 1.5 * IQR)):
            data = np.delete(data, i)
            i += 1
        else:
            i += 1
    return data
