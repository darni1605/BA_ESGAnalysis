import numpy as np
from ImportFilesPackages.ImportFiles import stockReturns_df
from ImportFilesPackages.ImportRandomSamples import *
from RAnalysis.FilterData.testFunctions.testGaussianNormality import isNormal
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from RAnalysis.FilterData.filterDataLevel1 import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import groupInQuantiles, filterESGScores
from RAnalysis.RTools.tTest import twoSampleTTest
from RAnalysis.RTools.Performance import countNumberOfSignificantTTests


# group all stocks into a low, medium and high ESG group (according to quantiles) and test outperformance
filteredESGScores = filterESGScores(nonMultiColList)
print(len(filteredESGScores.columns))
lowGroup, mediumGroup, highGroup = groupInQuantiles(filteredESGScores)

lowGroupReturns = stockReturns_df[lowGroup].copy()
mediumGroupReturns = stockReturns_df[mediumGroup].copy()
highGroupReturns = stockReturns_df[highGroup].copy()
lowGroupReturns['averageReturn'] = lowGroupReturns.mean(axis=1)
avgLowGroupReturns = lowGroupReturns['averageReturn'].copy()
mediumGroupReturns['averageReturn'] = mediumGroupReturns.mean(axis=1)
avgMediumGroupReturns = mediumGroupReturns['averageReturn'].copy()
highGroupReturns['averageReturn'] = highGroupReturns.mean(axis=1)
avgHighGroupReturns = highGroupReturns['averageReturn'].copy()

avgLowGroupReturns = avgLowGroupReturns[~np.isnan(avgLowGroupReturns)]
avgMediumGroupReturns = avgMediumGroupReturns[~np.isnan(avgMediumGroupReturns)]
avgHighGroupReturns = avgHighGroupReturns[~np.isnan(avgHighGroupReturns)]

avgLowGroupReturn = np.mean(lowGroupReturns['averageReturn'])
medianLowGroupReturn = np.nanmedian(lowGroupReturns['averageReturn'])
avgMediumGroupReturn = np.mean(mediumGroupReturns['averageReturn'])
medianMediumGroupReturn = np.nanmedian(mediumGroupReturns['averageReturn'])
avgHighGroupReturn = np.mean(highGroupReturns['averageReturn'])
medianHighGroupReturn = np.nanmedian(highGroupReturns['averageReturn'])

print('\nSummary of Low group average Returns:')
print('Number of stocks: ' + str(len(lowGroup)))
printDataSetSummary(avgLowGroupReturns)
print('\nSummary of Medium group average Returns:')
print('Number of stocks: ' + str(len(mediumGroup)))
printDataSetSummary(avgMediumGroupReturns)
print('\nSummary of High group average Returns:')
print('Number of stocks: ' + str(len(highGroup)))
printDataSetSummary(avgHighGroupReturns)


print('\nIs Low Group normal? ' + str(isNormal(avgLowGroupReturns, 0.90)))
print('Is Medium Group normal? ' + str(isNormal(avgMediumGroupReturns, 0.90)))
print('Is High Group normal? ' + str(isNormal(avgHighGroupReturns, 0.90)))

print('\nBecause of fat-tails, all average return lists are not normally distributed. Assumption: they are!')

print('\nH4: The stocks with on average higher ESG scores outperform stocks with on average lower ESG scores')
# REMARK: divide pValue for all test by 2 since one-tailed
# twoSampleTTest: expected bigger sample first
isOneTailed = True
# is mediumGroupReturn > lowGroupReturn
print('\nMedium vs Low group returns:')
twoSampleTTest(avgMediumGroupReturns, avgLowGroupReturns, False, isOneTailed)
# is highGroupReturn > lowGroupReturn?
print('\nHigh vs Low group returns:')
twoSampleTTest(avgHighGroupReturns, avgLowGroupReturns, False, isOneTailed)
# is highGroupReturn > lowGroupReturn?
print('\nHigh vs Medium group returns:')
twoSampleTTest(avgHighGroupReturns, avgMediumGroupReturns, False, isOneTailed)

# split all three groups into 10 random samples, conduct t test, count number of significant results
countOfSignificantTTestRandomMediumLow = countNumberOfSignificantTTests(
    randomSampleMediumGroupReturns, randomSampleLowGroupReturns, 0.05, isOneTailed)
countOfSignificantTTestRandomHighLow = countNumberOfSignificantTTests(
    randomSampleHighGroupReturns, randomSampleLowGroupReturns, 0.05, isOneTailed)
countOfSignificantTTestRandomHighMedium = countNumberOfSignificantTTests(
    randomSampleHighGroupReturns, randomSampleMediumGroupReturns, 0.05, isOneTailed)

print('\n10 random Medium group vs 10 random Low group returns')
print('Percentage of significant tests: %2.d%%' % countOfSignificantTTestRandomMediumLow)
print('\n10 random High group vs 10 random Low group returns')
print('Percentage of significant tests: %2.d%%' % countOfSignificantTTestRandomHighLow)
print('\n10 random High group vs 10 random Medium group returns')
print('Percentage of significant tests: %2.d%%' % countOfSignificantTTestRandomHighMedium)

print('''\nRESULT1: For all three tests no evidence is found to support the claim that higher average Scores lead to 
higher stock returns. Again it is interesting to note that the highest mean and median return are found in the low 
group followed by the medium group and on the last place the high group. This supports the findings from hypothesis 1 
(negative correlation between ESG scores and stock returns). To have an additional check confirming these findings, 
we randomly split all three groups into 10 random data samples each and conduct a hypothesis test for each. This 
results in a total of 300 hypothesis tests. For all three groups the percentage of significant tests when comparing 
two groups does not exceed 20% for the confidence level 95%.''')
