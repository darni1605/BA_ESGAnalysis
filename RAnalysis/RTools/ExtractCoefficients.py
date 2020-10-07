import rpy2.robjects as robjects
import numpy as np
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportRPackages import base
from RAnalysis.RTools.GenerateModels import createRModel


def extractSummaries(listOfStocks, level):
    pandas2ri.activate()
    summaries = []
    for stock in listOfStocks:
        currentRModel = createRModel(stock, level)
        if not isinstance(currentRModel, bool):
            summary = base.summary(currentRModel)
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
        try:
            currentESGBeta = coefficient[4, 0]
            ESGBetas = np.append(ESGBetas, currentESGBeta)
        except IndexError:
            pass
    return ESGBetas


def extractESGBetasPValue(listOfCoefficients):
    pValues = np.empty(0)
    for coefficient in listOfCoefficients:
        try:
            currentPValue = coefficient[4, 3]
            pValues = np.append(pValues, currentPValue)
        except IndexError:
            pass
    return pValues


def countSignificantFactors(pValueList, significanceLevel):
    significanceCount = 0
    noSignificanceCount = 0
    for pValue in pValueList:
        if pValue <= significanceLevel:
            significanceCount += 1
        else:
            noSignificanceCount += 1
    return significanceCount, noSignificanceCount


def excludeOutliers(data):
    Q1 = np.nanquantile(data, 0.25)
    Q3 = np.nanquantile(data, 0.75)
    IQR = Q3 - Q1

    i = 0
    while i < len(data) - 1:
        if data[i] == np.nan:
            i += 1
        if (data[i] > (Q3 + 1.5 * IQR)) or (data[i] < (Q1 - 1.5 * IQR)):
            data = np.delete(data, i)
            i += 1
        else:
            i += 1
    return data
