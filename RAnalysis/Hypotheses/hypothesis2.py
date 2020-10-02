import numpy as np
from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from ImportFilesPackages.ImportFiles import marketPricesReturns, stockReturns_df
from scipy.stats import ttest_1samp

# group all stocks into a below & above ESG market average and test underperformance/outperformance compared to market
from RAnalysis.RTools.tTest import twoSampleTTest

filteredESGDf = filterESGScores(nonMultiColList)
belowMarketESGAverageGroup, aboveMarketESGAverageGroup = groupAccordingToAverage(filteredESGDf)
lowGroupReturns = stockReturns_df[belowMarketESGAverageGroup].copy()
highGroupReturns = stockReturns_df[aboveMarketESGAverageGroup].copy()
marketReturns = marketPricesReturns['Return']
marketReturns = marketReturns[~np.isnan(marketReturns)]

lowGroupReturns['averageReturn'] = lowGroupReturns.mean(axis=1)
averageLowGroupReturns = lowGroupReturns['averageReturn'].copy()
averageLowGroupReturns = averageLowGroupReturns[~np.isnan(averageLowGroupReturns)]
highGroupReturns['averageReturn'] = highGroupReturns.mean(axis=1)
averageHighGroupReturns = highGroupReturns['averageReturn'].copy()
averageHighGroupReturns = averageHighGroupReturns[~np.isnan(averageHighGroupReturns)]

averageLowReturn = np.exp(np.nanmean(averageLowGroupReturns)) - 1
medianLowReturn = np.exp(np.nanmedian(averageLowGroupReturns)) - 1
averageHighReturn = np.exp(np.nanmean(averageHighGroupReturns)) - 1
medianHighReturn = np.exp(np.nanmedian(averageHighGroupReturns)) - 1
averageMarketReturn = np.exp(np.nanmean(marketReturns)) - 1
medianMarketReturn = np.exp(np.nanmedian(marketReturns)) - 1

print('\n Summary of Low group average returns:')
printDataSetSummary(averageLowGroupReturns)

print('\n Summary of High group average returns:')
printDataSetSummary(averageHighGroupReturns)

print(marketReturns)
print(lowGroupReturns)

# H2
print('\nH2: Is there an underperformance of stocks below market ESG average compared to the market?')
print('\nOne sample test: average returns of low group vs. average market return')
print('Below average group mean return: %6.6f & Market mean return: %6.6f' % (averageLowReturn, averageMarketReturn))
print('Below average group median return: %6.6f & Market median return: %6.6f' % (medianLowReturn, medianMarketReturn))
tTest1 = ttest_1samp(averageLowGroupReturns, averageMarketReturn)
pValue = 1 - tTest1.pvalue / 2
print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
print('\nTwo Sample test: average returns low group vs. average market returns')
twoSampleTTest(marketReturns, averageLowGroupReturns, False, True)
print('''RESULT: The hypothesis of an underperformance of stocks below market ESG average can be rejected with a
      p-value of 0.9358. The two sample test yields a p-value of 0.9296. Both the average and median return of the
      below market ESG average group is bigger than market average and median return, there is no evidence for an
      underperformance.''')

# H3
print('\nH3: Is there an outperformance of stocks above market ESG average compared to the market?')
print('\nOne sample test: average returns of high group vs. average market return')
print('Above average group mean return: %6.6f & Market mean return: %6.6f' % (averageHighReturn, averageMarketReturn))
print('Above average group median return: %6.6f & Market median return: %6.6f' % (medianHighReturn, medianMarketReturn))
tTest1 = ttest_1samp(averageHighGroupReturns, averageMarketReturn)
pValue = tTest1.pvalue / 2
print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
print('\nTwo Sample test: average returns high group vs. average market returns')
twoSampleTTest(averageHighGroupReturns, marketReturns, False, True)
print('''RESULT: There is no evidence for an outperformance of above market ESG average stocks compared to the market
      return. The one sample test yields a p-value of 0.1311 and the two sample test 0.112656. Nevertheless,
      both the mean and median return of the high group are bigger than the markets. Since both the low and high
      group outperform the market according to mean and median return, a possible explanation is the reduced risk of
      a diversified market compared to smaller subgroups. It is interesting to note that the mean and median return
      of the low group are larger than the high group. This would support the evidence found from hypothesis 1,
      that ESG ratings are negatively correlated with stock returns.''')