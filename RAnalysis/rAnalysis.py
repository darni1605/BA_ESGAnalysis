import numpy as np
from RAnalysis.RTools.ExtractCoefficients import dropOnlyNanColumns, extractSummaries, extractAdjustedRSquared, \
    distributionOfRSquared, dropESGScoresFromModel
from RAnalysis.FilterData.filterDataLevel1 import nonMultiColList
from RAnalysis.FilterData.filterDataLevel2 import cleanListOfDf

# Check how the inclusion of ESG factors changes the models predictive expressiveness

# R squared distribution: 1st Level
listOfDf1 = dropOnlyNanColumns(nonMultiColList)
listOfDf1WithoutESG = dropESGScoresFromModel(listOfDf1, level=1)
summaries1 = extractSummaries(listOfDf1)
summariesWithoutESG1 = extractSummaries(listOfDf1WithoutESG)
listOfRSquared1 = extractAdjustedRSquared(summaries1)
listOfRSquared1WithoutESG1 = extractAdjustedRSquared(summariesWithoutESG1)

meanOfRSquared = np.nanmean(listOfRSquared1)
medianOfRSquared = np.nanmedian(listOfRSquared1)
meanOfRSquaredWithoutESG = np.nanmean(listOfRSquared1WithoutESG1)
medianOfRSquaredWithoutESG = np.nanmedian(listOfRSquared1WithoutESG1)

perDistR1, perDistR2, perDistR3, perDistR4 = distributionOfRSquared(listOfRSquared1)
perDistR1WithoutESG, perDistR2WithoutESG, perDistR3WithoutESG, perDistR4WithoutESG = distributionOfRSquared(
    listOfRSquared1WithoutESG1)

print('For the first level models:')
print('The mean and median of all R squared: %2.6f & %2.6f' % (meanOfRSquared, medianOfRSquared))
print('The mean and median of all R squared without ESG: %2.6f & %2.6f' % (meanOfRSquaredWithoutESG,
                                                                           medianOfRSquaredWithoutESG))
print('Percentages R Squared with and without ESG <= 0.25: %2.2f%% & %2.2f%%' % (perDistR1, perDistR1WithoutESG))
print('Percentages R Squared with and without ESG > 0.25, <= 0.5 : %2.2f%% & %2.2f%%' % (perDistR2, perDistR2WithoutESG))
print('Percentages R Squared with and without ESG > 0.5, <= 0.75: %2.2f%% & %2.2f%%' % (perDistR3, perDistR3WithoutESG))
print('Percentages R Squared with and without ESG > 0.75: %2.2f%% & %2.2f%%' % (perDistR4, perDistR4WithoutESG))


# R squared distribution: 2nd Level
listOfDf2 = dropOnlyNanColumns(cleanListOfDf)
listOfDf2WithoutESG = dropESGScoresFromModel(listOfDf2, level=2)
summaries2 = extractSummaries(listOfDf2)
summaries2WithoutESG = extractSummaries(listOfDf2WithoutESG)
listOfRSquared2 = extractAdjustedRSquared(summaries2)
listOfRSquared2WithoutESG = extractAdjustedRSquared(summaries2WithoutESG)

meanOfRSquared = np.nanmean(listOfRSquared2)
medianOfRSquared = np.nanmedian(listOfRSquared2)
meanOfRSquaredWithoutESG = np.nanmean(listOfRSquared2WithoutESG)
medianOfRSquaredWithoutESG = np.nanmedian(listOfRSquared2WithoutESG)

perDistR1, perDistR2, perDistR3, perDistR4 = distributionOfRSquared(listOfRSquared2)
perDistR1WithoutESG, perDistR2WithoutESG, perDistR3WithoutESG, perDistR4WithoutESG = distributionOfRSquared(
    listOfRSquared2WithoutESG)

print('\nFor the second level models:')
print('The mean and median of all R squared: %2.6f & %2.6f' % (meanOfRSquared, medianOfRSquared))
print('The mean and median of all R squared without ESG: %2.6f & %2.6f' % (meanOfRSquaredWithoutESG,
                                                                           medianOfRSquaredWithoutESG))
print('Percentages R Squared with and without ESG <= 0.25: %2.2f%% & %2.2f%%' % (perDistR1, perDistR1WithoutESG))
print('Percentages R Squared with and without ESG > 0.25, <= 0.5 : %2.2f%% & %2.2f%%' % (perDistR2, perDistR2WithoutESG))
print('Percentages R Squared with and without ESG > 0.5, <= 0.75: %2.2f%% & %2.2f%%' % (perDistR3, perDistR3WithoutESG))
print('Percentages R Squared with and without ESG > 0.75: %2.2f%% & %2.2f%%' % (perDistR4, perDistR4WithoutESG))


