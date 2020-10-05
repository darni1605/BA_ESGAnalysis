import numpy as np
from ImportFilesPackages.ImportFiles import stockReturns_df
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import groupInQuantiles, filterESGScores
from RAnalysis.RTools.tTest import twoSampleTTest
from scipy.stats import ttest_ind

# group all stocks into a low, medium and high ESG group (according to quantiles) and test outperformance
filteredESGScores = filterESGScores(nonMultiColList)
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
printDataSetSummary(avgLowGroupReturns)
print('\nSummary of Medium group average Returns:')
printDataSetSummary(avgMediumGroupReturns)
print('\nSummary of High group average Returns:')
printDataSetSummary(avgHighGroupReturns)

# TODO: check for normality again

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

print('''\nRESULT1: For all three tests no evidence is found to support the claim that higher average Scores lead to 
higher stock returns. Again it is interesting to note that the highest mean and median return are found in the low 
group followed by the medium group and on the last place the high group. This supports the findings from hypothesis 1 
(negative correlation between ESG scores and stock returns)''')
