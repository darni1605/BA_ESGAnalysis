import numpy as np
from ImportFilesPackages.ImportFiles import stockReturns_df
from RAnalysis.FilterData.filterDataLevel1 import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.FilterData.testFunctions.testGaussianNormality import isNormal
from RAnalysis.RTools.ConductHypoTestAboveBelowGroups import conductHypoTest
from RAnalysis.RTools.PrintRSummary import printDataSetSummary


# group all stocks into a below & above ESG market average and test underperformance/outperformance compared to market

filteredESGDf = filterESGScores(nonMultiColList)
belowMarketESGAverageGroup, aboveMarketESGAverageGroup = groupAccordingToAverage(filteredESGDf)
listOfMarketStocks = []
for df in nonMultiColList:
    listOfMarketStocks.append(df.columns[0])


aboveGroupMeanReturn = stockReturns_df[aboveMarketESGAverageGroup].mean(axis=1).copy()
belowGroupMeanReturn = stockReturns_df[belowMarketESGAverageGroup].mean(axis=1).copy()
marketMeanReturn = stockReturns_df[listOfMarketStocks].mean(axis=1).copy()
aboveGroupMeanReturn = aboveGroupMeanReturn[~np.isnan(aboveGroupMeanReturn)]
belowGroupMeanReturn = belowGroupMeanReturn[~np.isnan(belowGroupMeanReturn)]
marketMeanReturn = marketMeanReturn[~np.isnan(marketMeanReturn)]

print('\nMarket Returns summary:')
print('Number of stocks: ' + str(len(nonMultiColList)))
printDataSetSummary(marketMeanReturn)

print('\nAbove Market Average group summary:')
print('Number of stocks: ' + str(len(aboveMarketESGAverageGroup)))
printDataSetSummary(aboveGroupMeanReturn)

print('\nBelow Market Average group summary:')
print('Number of stocks: ' + str(len(belowMarketESGAverageGroup)))
printDataSetSummary(belowGroupMeanReturn)


print('\nIs above group normal? ' + str(isNormal(aboveGroupMeanReturn, 0.90)))
print('Is below group normal? ' + str(isNormal(belowGroupMeanReturn, 0.90)))
print('Is market group normal? ' + str(isNormal(marketMeanReturn, 0.90)))
print('All lists with average return are, because of fat-tails, not normally distributed. As a simplification, '
      'we assume normality as the histogram follows by eye a normal distribution.')

# H2
print('\nH2: Is there an outperformance of stocks above market ESG average compared to the market?')
conductHypoTest(aboveMarketESGAverageGroup, nonMultiColList, isLow=False)
print('''RESULT: There is no evidence for an outperformance of above market ESG average stocks compared to the market
return. The one sample test yields a p-value of 0.3913 and the two sample test 0.4246. Both the mean and median
return of the high group are smaller than the markets. Additionally, only 36% of all stocks of the High group
actually outperformed the market. It is interesting to note that the mean and median return of the low group are
larger than the high group. This would support the evidence found from hypothesis 1, that ESG ratings are negatively
correlated with stock returns.''')

# H3
print('\nH3: Is there an underperformance of stocks below market ESG average compared to the market?')
conductHypoTest(belowMarketESGAverageGroup, nonMultiColList, isLow=True)
print('''RESULT: The hypothesis of an underperformance of stocks below market ESG average can be rejected with a
p-value of 0.6000. The two sample test yields a p-value of 0.426755. Both the average and median return of the below
market ESG average group is bigger than market average and median return. Additionally, only 46.7% of all stocks of
the Low group actually underperformed the market. There is therefore no evidence for an underperformance.''')

