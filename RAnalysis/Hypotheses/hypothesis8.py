from RAnalysis.FilterData.filterDataLevel2 import cleanListOfDf
from RAnalysis.RTools.ExtractCoefficients import *
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from RAnalysis.RTools.tTest import *
import pandas as pd

# Extract all betas, p-values of Environment, Social and Governance factors
listOfColumnNames = []
for model in cleanListOfDf:
    listOfColumnNames.append(model.columns)
extractedSummaries = extractSummaries(cleanListOfDf)
extractedCoefficients = extractCoefficients(extractedSummaries)
envBetas, envPValues, socBetas, socPValues, govBetas, govPValues = extractSubScoresBetas(
    listOfColumnNames, extractedCoefficients)

envBetas = envBetas[~np.isnan(envBetas)]
socBetas = socBetas[~np.isnan(socBetas)]
govBetas = govBetas[~np.isnan(govBetas)]
envPValues = envPValues[~np.isnan(envPValues)]
socPValues = socPValues[~np.isnan(socPValues)]
govPValues = govPValues[~np.isnan(govPValues)]

envBetasWithoutOutliers = excludeOutliers(envBetas)
socBetasWithoutOutliers = excludeOutliers(socBetas)
govBetasWithoutOutliers = excludeOutliers(govBetas)

print('Amount of non NaN Environment betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(envBetas)), np.count_nonzero(~np.isnan(envBetasWithoutOutliers))))
print('Amount of non NaN Social betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(socBetas)), np.count_nonzero(~np.isnan(socBetasWithoutOutliers))))
print('Amount of non NaN Governance betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(govBetas)), np.count_nonzero(~np.isnan(govBetasWithoutOutliers))))

# calculate individual significance
envSignCount, envNoSignCount = countSignificantFactors(envPValues, 0.05)
envPercentage = 100 * envSignCount / (envSignCount + envNoSignCount)
socSignCount, socNoSignCount = countSignificantFactors(socPValues, 0.05)
socPercentage = 100 * socSignCount / (socSignCount + socNoSignCount)
govSignCount, govNoSignCount = countSignificantFactors(govPValues, 0.05)
govPercentage = 100 * govSignCount / (govSignCount + govNoSignCount)

# print data sample summary
envBetas_df = pd.DataFrame(envBetas)
envBetasWithoutOutliers_df = pd.DataFrame(envBetasWithoutOutliers)
socBetas_df = pd.DataFrame(socBetas)
socBetasWithoutOutliers_df = pd.DataFrame(socBetasWithoutOutliers)
govBetas_df = pd.DataFrame(govBetas)
govBetasWithoutOutliers_df = pd.DataFrame(govBetasWithoutOutliers)
print('Env Betas with outliers:')
printDataSetSummary(envBetas_df)
print('\nEnv betas without outliers')
printDataSetSummary(envBetasWithoutOutliers_df)

print('\nSoc Betas with outliers:')
printDataSetSummary(socBetas_df)
print('\n Soc betas without outliers')
printDataSetSummary(socBetasWithoutOutliers_df)

print('\nGov Betas with outliers:')
printDataSetSummary(govBetas_df)
print('\nGov betas without outliers')
printDataSetSummary(govBetasWithoutOutliers_df)


print('\nH8: The average of all Environment Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(envBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(envBetasWithoutOutliers, 0)
print('Percentage of individually significant Environment Betas of all stocks: %2.2f%%' % envPercentage)


print('\nH9: The average of all Social Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(socBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(socBetasWithoutOutliers, 0)
print('Percentage of individually significant Social Betas of all stocks: %2.2f%%' % socPercentage)


print('\nH10: The average of all Governance Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(govBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(govBetasWithoutOutliers, 0)
print('Percentage of individually significant Governance Betas of all stocks: %2.2f%%' % govPercentage)



