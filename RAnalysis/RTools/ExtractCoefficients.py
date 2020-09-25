import rpy2.robjects as robjects
import pandas as pd
import numpy as np
from rpy2.robjects import pandas2ri
from RAnalysis.RTools.GenerateModels import createRModel
from ImportFilesPackages.ImportFiles import nrOfColumns, companyIdentifier


def extractSummaries():
    i = 0
    R = robjects.r
    pandas2ri.activate()
    summaries = []
    while i < nrOfColumns:
        currentCompanyIdentifier = companyIdentifier[i]
        currentRModel = createRModel(currentCompanyIdentifier)
        if not isinstance(currentRModel, bool):
            summary = R.lm(currentRModel)
            summaries.append(summary)
            i += 1
        else:
            i += 1
    return summaries


def extractCoefficients(summaries):
    coefficients = []
    for summary in summaries:
        currentCoefficients = summary.rx2('coefficients')
        coefficients.append(currentCoefficients)
    return coefficients


def extractESGBetas(coefficients):
    ESGBetas = np.empty(0)
    i = 0
    while i < len(coefficients):
        currentCoefficients = coefficients[i]
        currentESGBeta = currentCoefficients[4]
        ESGBetas = np.append(ESGBetas, currentESGBeta)
        i += 1
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
