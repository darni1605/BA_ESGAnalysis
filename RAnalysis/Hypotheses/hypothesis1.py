import numpy as np
from scipy.stats import ttest_1samp

from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas, excludeOutliers
from RAnalysis.FilterData.filterData import nonMultiColList

# extract the stock tickers of all data filtering survivors #
from RAnalysis.RTools.PlotGraphs import histogram

listOfSurvivors = []
for stock in nonMultiColList:
    listOfSurvivors.append(stock.columns[0])
extractedSummaries = extractSummaries(listOfSurvivors)
extractedCoefficients = extractCoefficients(extractedSummaries)
extractedESGBetas = extractESGBetas(extractedCoefficients)
extractedESGBetas = extractedESGBetas[~np.isnan(extractedESGBetas)]
ESGBetasWithoutOutliers = excludeOutliers(extractedESGBetas)

medianESGBeta = np.median(extractedESGBetas)
averageESGBeta = np.average(extractedESGBetas)
tTest1 = ttest_1samp(extractedESGBetas, 0.0)
tTest2 = ttest_1samp(ESGBetasWithoutOutliers, 0.0)

print('\nH1: The distribution of ESG Betas is significantly different from zero')
print('t-statistic = %6.3f pValue = %6.4f' % tTest1)
print('t-statistic = %6.3f pValue = %6.4f' % tTest2)
print('Median of all ESG Betas: ' + str(medianESGBeta))
print('Average of all ESG Betas: ' + str(averageESGBeta))
# histogram(extractedESGBetas, 'Distribution of ESG Betas', 'ESG Betas', 'Frequency')

print('RESULT 1: With Outliers, ESG Beta distribution not significantly different from zero')
print('RESULT 2: Without Outliers, ESG Beta distribution significantly different from zero with 99% confidence')
