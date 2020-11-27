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


def extractAdjustedRSquared(summaries):
    listOfRSquared = []
    for summary in summaries:
        listOfRSquared.append(float(summary[8]))
    return listOfRSquared


def distributionOfRSquared(listOfRSquared):
    limit1 = 0.25
    limit2 = 0.5
    limit3 = 0.75
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    totalAmount = len(listOfRSquared)

    for rSquared in listOfRSquared:
        if limit1 >= rSquared:
            group1.append(rSquared)
        elif limit1 < rSquared <= limit2:
            group2.append(rSquared)
        elif limit2 < rSquared <= limit3:
            group3.append(rSquared)
        else:
            group4.append(rSquared)

    perGroup1 = 100 * len(group1) / totalAmount
    perGroup2 = 100 * len(group2) / totalAmount
    perGroup3 = 100 * len(group3) / totalAmount
    perGroup4 = 100 * len(group4) / totalAmount

    return perGroup1, perGroup2, perGroup3, perGroup4


def dropESGScoresFromModel(listOfDfs, level):
    newListOfDfs = []
    if level == 1:
        for df in listOfDfs:
            currentESGColumnName = df.columns[0] + 'ESGScore'
            if currentESGColumnName in df.columns:
                dfWithoutESG = df.drop(columns=[currentESGColumnName])
                newListOfDfs.append(dfWithoutESG)
    if level == 2:
        for df in listOfDfs:
            dfWithoutESG = df
            currentEnvColumnName = df.columns[0] + 'EnvironmentScore'
            currentSocColumnName = df.columns[0] + 'SocialScore'
            currentGovColumnName = df.columns[0] + 'GovernanceScore'
            if currentEnvColumnName in df.columns:
                dfWithoutESG = dfWithoutESG.drop(columns=[currentEnvColumnName])
            if currentSocColumnName in df.columns:
                dfWithoutESG = dfWithoutESG.drop(columns=[currentSocColumnName])
            if currentGovColumnName in df.columns:
                dfWithoutESG = dfWithoutESG.drop(columns=[currentGovColumnName])
            newListOfDfs.append(dfWithoutESG)
    return newListOfDfs


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
