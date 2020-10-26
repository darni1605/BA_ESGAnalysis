from RAnalysis.FilterData.filterDataLevel2 import cleanListOfDf
from RAnalysis.RTools.ExtractCoefficients import *
from RAnalysis.RTools.tTest import *


listOfColumnNames = []
for model in cleanListOfDf:
    listOfColumnNames.append(model.columns)
extractedSummaries = extractSummaries(cleanListOfDf)
extractedCoefficients = extractCoefficients(extractedSummaries)
envBetas, envPValues, socBetas, socPValues, govBetas, govPValues = extractSubScores(
    listOfColumnNames, extractedCoefficients)

envBetas = envBetas[~np.isnan(envBetas)]
socBetas = socBetas[~np.isnan(socBetas)]
govBetas = govBetas[~np.isnan(govBetas)]

envBetasWithoutOutliers = excludeOutliers(envBetas)
socBetasWithoutOutliers = excludeOutliers(socBetas)
govBetasWithoutOutliers = excludeOutliers(govBetas)

print('Amount of non NaN Environment betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(envBetas)), np.count_nonzero(~np.isnan(envBetasWithoutOutliers))))
print('Amount of non NaN Social betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(socBetas)), np.count_nonzero(~np.isnan(socBetasWithoutOutliers))))
print('Amount of non NaN Governance betas with and without outliers: %2d & %2d'
      % (np.count_nonzero(~np.isnan(govBetas)), np.count_nonzero(~np.isnan(govBetasWithoutOutliers))))

envSignCount, envNoSignCount = countSignificantFactors(envBetas, 0.05)
envPercentage = 100 * envSignCount / (envSignCount + envNoSignCount)
socSignCount, socNoSignCount = countSignificantFactors(socBetas, 0.05)
socPercentage = 100 * socSignCount / (socSignCount + socNoSignCount)
govSignCount, govNoSignCount = countSignificantFactors(govBetas, 0.05)
govPercentage = 100 * govSignCount / (govSignCount + govNoSignCount)


print('\nH8: The average of all Environment Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(envBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(envBetasWithoutOutliers, 0)
print('Percentage of individually significant Environment Betas of all stocks: %2d%%' % envPercentage)


print('\nH9: The average of all Social Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(socBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(socBetasWithoutOutliers, 0)
print('Percentage of individually significant Social Betas of all stocks: %2d%%' % socPercentage)


print('\nH10: The average of all Governance Betas is different to zero')
print('\nWith outliers:')
oneSampleTTest(govBetas, 0)
print('\nWithout outliers:')
oneSampleTTest(govBetasWithoutOutliers, 0)
print('Percentage of individually significant Governance Betas of all stocks: %2d%%' % govPercentage)



