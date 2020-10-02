import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas, excludeOutliers
from RAnalysis.FilterData.filterData import nonMultiColList

# extract the stock tickers of all data filtering survivors #
from RAnalysis.RTools.PlotGraphs import histogram

listOfSurvivors = []
for stock in nonMultiColList:
    listOfSurvivors.append(stock.columns[0])
extractedSummaries = extractSummaries(listOfSurvivors, 1)
extractedCoefficients = extractCoefficients(extractedSummaries)
extractedESGBetas = extractESGBetas(extractedCoefficients)
extractedESGBetas = extractedESGBetas[~np.isnan(extractedESGBetas)]
ESGBetasWithoutOutliers = excludeOutliers(extractedESGBetas)

medianESGBeta = np.nanmedian(extractedESGBetas)
averageESGBeta = np.nanmean(extractedESGBetas)
medianESGWithoutOutliers = np.nanmedian(ESGBetasWithoutOutliers)
averageESGWithoutOutliers = np.nanmean(ESGBetasWithoutOutliers)
tTest1 = ttest_1samp(extractedESGBetas, 0.0)
tTest2 = ttest_1samp(ESGBetasWithoutOutliers, 0.0)

ESGBetas1 = pd.DataFrame(extractedESGBetas)
print('\nSummary ESG betas with outliers:')
printDataSetSummary(ESGBetas1)

ESGBetas2 = pd.DataFrame(ESGBetasWithoutOutliers)
print('\n Summary ESG betas without outliers:')
printDataSetSummary(ESGBetas2)


# TODO: think about how to handle stocks with less than 50 return data points
#  and where there are more ESG scores than returns
print('\nH1: The distribution of ESG Betas is significantly different from zero')
print('t-statistic = %6.3f pValue = %6.4f' % tTest1)
print('Median of all ESG Betas: %6.6f, average of all ESG betas: %6.6f' % (medianESGBeta, averageESGBeta))
print('t-statistic = %6.3f pValue = %6.4f' % tTest2)
print('Median of all ESG Betas: %6.6f, average of all ESG betas: %6.6f'
      % (medianESGWithoutOutliers, averageESGWithoutOutliers))
# histogram(extractedESGBetas, 'Distribution of ESG Betas', 'ESG Betas', 'Frequency')

print('''RESULT: With and without outliers, the ESG beta has a statistically significant difference to zero on a 99%
      confidence level. Both the median and the mean are negative which indicates an inverse relationship between
      stock returns and ESG ratings.''')
