import numpy as np
from rpy2.robjects import pandas2ri
from ImportFilesPackages.ImportRPackages import base
from RAnalysis.RTools.GenerateModels import createRModel


def dropOnlyNanColumns(listOfDf):
    cleanListOfDf = []
    for df in listOfDf:
        hasOneNaNPerRow = True
        for column in df.columns:
            if np.isnan(df[column]).all():
                df.drop(columns=column, axis=1, inplace=True)
        for index, row in df.iterrows():
            boolList = np.isnan(row)
            if not any(boolList):
                hasOneNaNPerRow = False
        if not hasOneNaNPerRow:
            cleanListOfDf.append(df)
    return cleanListOfDf


def extractSummaries(listOfDf):
    pandas2ri.activate()
    summaries = []
    for df in listOfDf:
        currentRModel = createRModel(df)
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


def extractSubScorePValue(coefficient, position):
    try:
        subScoreBetaPValue = coefficient[position, 3]
    except IndexError:
        subScoreBetaPValue = np.nan
    return subScoreBetaPValue


def extractSubScore(coefficient, position):
    try:
        subScoreBeta = coefficient[position, 0]
    except IndexError:
        subScoreBeta = np.nan
    return subScoreBeta


def extractSubScores(listOfColumnNames, extractedCoefficients):
    envBetas = np.empty(0)
    envPValues = np.empty(0)
    socBetas = np.empty(0)
    socPValues = np.empty(0)
    govBetas = np.empty(0)
    govPValues = np.empty(0)
    for i in range(0, len(listOfColumnNames)):
        stock = listOfColumnNames[i][0]
        currentEnvColumnName = stock + 'EnvironmentScore'
        currentSocColumnName = stock + 'SocialScore'
        currentGovColumnName = stock + 'GovernanceScore'
        if len(listOfColumnNames[i]) == 7:
            envBetas = np.append(envBetas, extractSubScore(extractedCoefficients[i], 4))
            envPValues = np.append(envPValues, extractSubScorePValue(extractedCoefficients[i], 4))
            socBetas = np.append(socBetas, extractSubScore(extractedCoefficients[i], 5))
            socPValues = np.append(socPValues, extractSubScorePValue(extractedCoefficients[i], 5))
            govBetas = np.append(govBetas, extractSubScore(extractedCoefficients[i], 6))
            govPValues = np.append(govPValues, extractSubScorePValue(extractedCoefficients[i], 6))
        if len(listOfColumnNames[i]) == 6:
            if currentEnvColumnName not in listOfColumnNames[i]:
                socBetas = np.append(socBetas, extractSubScore(extractedCoefficients[i], 4))
                socPValues = np.append(socPValues, extractSubScorePValue(extractedCoefficients[i], 4))
                govBetas = np.append(govBetas, extractSubScore(extractedCoefficients[i], 5))
                govPValues = np.append(govPValues, extractSubScorePValue(extractedCoefficients[i], 5))
            elif currentSocColumnName not in listOfColumnNames[i]:
                envBetas = np.append(envBetas, extractSubScore(extractedCoefficients[i], 4))
                envPValues = np.append(envPValues, extractSubScorePValue(extractedCoefficients[i], 4))
                govBetas = np.append(govBetas, extractSubScore(extractedCoefficients[i], 5))
                govPValues = np.append(govPValues, extractSubScorePValue(extractedCoefficients[i], 5))
            elif currentGovColumnName not in listOfColumnNames[i]:
                envBetas = np.append(envBetas, extractSubScore(extractedCoefficients[i], 4))
                envPValues = np.append(envPValues, extractSubScorePValue(extractedCoefficients[i], 4))
                socBetas = np.append(socBetas, extractSubScore(extractedCoefficients[i], 5))
                socPValues = np.append(socPValues, extractSubScorePValue(extractedCoefficients[i], 5))
        elif len(listOfColumnNames[i]) == 5:
            if currentEnvColumnName in listOfColumnNames[i]:
                envBetas = np.append(envBetas, extractSubScore(extractedCoefficients[i], 4))
                envPValues = np.append(envPValues, extractSubScorePValue(extractedCoefficients[i], 4))
            elif currentSocColumnName in listOfColumnNames[i]:
                socBetas = np.append(socBetas, extractSubScore(extractedCoefficients[i], 4))
                socPValues = np.append(socPValues, extractSubScorePValue(extractedCoefficients[i], 4))
            elif currentGovColumnName in listOfColumnNames[i]:
                govBetas = np.append(govBetas, extractSubScore(extractedCoefficients[i], 4))
                govPValues = np.append(govPValues, extractSubScorePValue(extractedCoefficients[i], 4))
    return envBetas, envPValues, socBetas, socPValues, govBetas, govPValues


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
