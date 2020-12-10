from ImportFilesPackages.IndustrySplit import getIndustry
from RAnalysis.FilterData.filterDataLevel2 import cleanListOfDf
from ImportFilesPackages.ImportFiles import *
from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractSubScoresBetas, extractCoefficients, \
    excludeOutliers, countSignificantFactors
from RAnalysis.RTools.PrintRSummary import printDataSetSummary

communicationServicesModels = []
consumerDiscretionaryModels = []
consumerStaplesModels = []
energyModels = []
financialsModels = []
healthCareModels = []
industrialsModels = []
informationTechnologyModels = []
materialsModels = []
realEstateModels = []
utilitiesModels = []

# group all filtered stocks according to industry affiliation
for df in cleanListOfDf:
    ticker = df.columns[0]
    industry = getIndustry(ticker)
    if industry == 'Communication Services':
        communicationServicesModels.append(df)
    if industry == 'Consumer Discretionary':
        consumerDiscretionaryModels.append(df)
    if industry == 'Consumer Staples':
        consumerStaplesModels.append(df)
    if industry == 'Energy':
        energyModels.append(df)
    if industry == 'Financials':
        financialsModels.append(df)
    if industry == 'Health Care':
        healthCareModels.append(df)
    if industry == 'Information Technology':
        industrialsModels.append(df)
    if industry == 'Industrials':
        informationTechnologyModels.append(df)
    if industry == 'Materials':
        materialsModels.append(df)
    if industry == 'Real Estate':
        realEstateModels.append(df)
    if industry == 'Utilities':
        utilitiesModels.append(df)


# function to extract the coefficients, p-values, significance percentages and to conduct the hypothesis test
def makeH12(listOfModels, title):
    listOfColumnNames = []
    for model in listOfModels:
        listOfColumnNames.append(model.columns)
    summaries = extractSummaries(listOfModels)
    coefficients = extractCoefficients(summaries)
    envBeta, envP, socBeta, socP, govBeta, govP = extractSubScoresBetas(listOfColumnNames,
                                                                        coefficients)
    envBeta = envBeta[~np.isnan(envBeta)]
    socBeta = socBeta[~np.isnan(socBeta)]
    govBeta = govBeta[~np.isnan(govBeta)]
    envP = envP[~np.isnan(envP)]
    socP = socP[~np.isnan(socP)]
    govP = govP[~np.isnan(govP)]
    envBetaWithoutOutliers = excludeOutliers(envBeta)
    socBetaWithoutOutliers = excludeOutliers(socBeta)
    govBetaWithoutOutliers = excludeOutliers(govBeta)

    envPercentage = '-'
    socPercentage = '-'
    govPercentage = '-'
    envSignCount, envNoSignCount = countSignificantFactors(envP, 0.05)
    if envSignCount + envNoSignCount != 0:
        envPercentage = 100 * envSignCount / (envSignCount + envNoSignCount)
    socSignCount, socNoSignCount = countSignificantFactors(socP, 0.05)
    if socSignCount + socNoSignCount != 0:
        socPercentage = 100 * socSignCount / (socSignCount + socNoSignCount)
    govSignCount, govNoSignCount = countSignificantFactors(govP, 0.05)
    if govSignCount + govNoSignCount != 0:
        govPercentage = 100 * govSignCount / (govSignCount + govNoSignCount)

    envBeta_df = pd.DataFrame(envBeta)
    envBetaWithoutOutliers_df = pd.DataFrame(envBetaWithoutOutliers)
    socBeta_df = pd.DataFrame(socBeta)
    socBetaWithoutOutliers_df = pd.DataFrame(socBetaWithoutOutliers)
    govBeta_df = pd.DataFrame(govBeta)
    govBetaWithoutOutliers_df = pd.DataFrame(govBetaWithoutOutliers)

    print(title)
    print('Env Beta with and without outliers:')
    printDataSetSummary(envBeta_df)
    printDataSetSummary(envBetaWithoutOutliers_df)
    print('Percentage of individual significant Env Betas: ' + str(envPercentage) + '%')
    print('\nSoc Beta with and without outliers:')
    printDataSetSummary(socBeta_df)
    printDataSetSummary(socBetaWithoutOutliers_df)
    print('Percentage of individual significant Soc Betas: ' + str(socPercentage) + '%')
    print('\nGov Beta with and without outliers:')
    printDataSetSummary(govBeta_df)
    printDataSetSummary(govBetaWithoutOutliers_df)
    print('Percentage of individual significant Gov Betas: ' + str(govPercentage) + '%')
    print('\n')


makeH12(communicationServicesModels, 'Communication Services')
makeH12(consumerDiscretionaryModels, 'Consumer Discretionary')
makeH12(consumerStaplesModels, 'Consumer Staples')
makeH12(energyModels, 'Energy')
makeH12(financialsModels, 'Financials')
makeH12(healthCareModels, 'Health Care')
makeH12(industrialsModels, 'Industrials')
makeH12(informationTechnologyModels, 'Information Technology')
makeH12(materialsModels, 'Materials')
makeH12(realEstateModels, 'Real Estate')
makeH12(utilitiesModels, 'Utilities')
