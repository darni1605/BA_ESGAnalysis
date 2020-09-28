import numpy as np
from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from ImportFilesPackages.ImportFiles import ESGScores_change_df, marketPricesReturns, stockReturns_df
from scipy.stats import ttest_1samp

# group all stocks into a below & above ESG market average and test underperformance/outperformance compared to market
filteredESGDf = filterESGScores(nonMultiColList)
belowMarketESGAverageGroup, aboveMarketESGAverageGroup = groupAccordingToAverage(filteredESGDf)
lowGroupReturns = stockReturns_df[belowMarketESGAverageGroup].copy()
highGroupReturns = stockReturns_df[aboveMarketESGAverageGroup].copy()
marketReturns = marketPricesReturns['Return']

lowGroupReturns['averageReturn'] = lowGroupReturns.mean(axis=1)
averageLowGroupReturns = lowGroupReturns['averageReturn'].copy()
averageLowGroupReturns = averageLowGroupReturns[~np.isnan(averageLowGroupReturns)]
highGroupReturns['averageReturn'] = highGroupReturns.mean(axis=1)
averageHighGroupReturns = highGroupReturns['averageReturn'].copy()
averageHighGroupReturns = averageHighGroupReturns[~np.isnan(averageHighGroupReturns)]

averageLowReturn = np.mean(averageLowGroupReturns)
medianLowReturn = np.nanmedian(averageLowGroupReturns)
averageHighReturn = np.mean(averageHighGroupReturns)
medianHighReturn = np.nanmedian(averageHighGroupReturns)
averageMarketReturn = np.mean(marketReturns)
medianMarketReturn = np.nanmedian(marketReturns)

# H2
print('\nH2: Is there an underperformance of stocks below market ESG average compared to the market?')
print('Below average group mean return: ' + str(averageLowReturn))
print('Below average group median return: ' + str(medianLowReturn))
print('Market mean return: ' + str(averageMarketReturn))
print('Market median return: ' + str(medianMarketReturn))
tTest1 = ttest_1samp(averageLowGroupReturns, averageMarketReturn)
pValue = 1 - tTest1.pvalue / 2
print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
print('RESULT1: The hypothesis of an underperformance of stocks below market ESG average cannot rejected with a '
      'p-value of 0.8251')
print('But since both the average and median return of the below market ESG average group is bigger than '
      'market average and median return, there is no evidence for an underperformance')
# H3
print('\nH3: Is there an outperformance of stocks above market ESG average compared to the market?')
print('Below average group mean return: ' + str(averageHighReturn))
print('Below average group median return: ' + str(medianHighReturn))
print('Market mean return: ' + str(averageMarketReturn))
print('Market median return: ' + str(medianMarketReturn))
tTest1 = ttest_1samp(averageHighGroupReturns, averageMarketReturn)
pValue = tTest1.pvalue / 2
print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
print('RESULT 1: The hypothesis of an outperformance cannot be rejected with a p-value of 0.1102')
