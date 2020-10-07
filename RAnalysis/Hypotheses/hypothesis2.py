from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.RTools.ConductHypoTest import conductHypoTest

# group all stocks into a below & above ESG market average and test underperformance/outperformance compared to market

filteredESGDf = filterESGScores(nonMultiColList)
belowMarketESGAverageGroup, aboveMarketESGAverageGroup = groupAccordingToAverage(filteredESGDf)

print('All lists with average return are, because of fat-tails, not normally distributed. As a simplification, '
      'we assume normality as the histogram follows by eye a normal distribution.')

# H2
print('\nH2: Is there an underperformance of stocks below market ESG average compared to the market?')
conductHypoTest(belowMarketESGAverageGroup, nonMultiColList, isLow=True)
print('''RESULT: The hypothesis of an underperformance of stocks below market ESG average can be rejected with a
p-value of 0.6000. The two sample test yields a p-value of 0.426755. Both the average and median return of the below
market ESG average group is bigger than market average and median return. Additionally, only 46.7% of all stocks of
the Low group actually underperformed the market. There is therefore no evidence for an underperformance.''')

# H3
print('\nH3: Is there an outperformance of stocks above market ESG average compared to the market?')
conductHypoTest(aboveMarketESGAverageGroup, nonMultiColList, isLow=False)
print('''RESULT: There is no evidence for an outperformance of above market ESG average stocks compared to the market
return. The one sample test yields a p-value of 0.3913 and the two sample test 0.4246. Both the mean and median
return of the high group are smaller than the markets. Additionally, only 36% of all stocks of the High group
actually outperformed the market. It is interesting to note that the mean and median return of the low group are
larger than the high group. This would support the evidence found from hypothesis 1, that ESG ratings are negatively
correlated with stock returns.''')
