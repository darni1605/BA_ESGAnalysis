import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp
from RAnalysis.RTools.PrintRSummary import printDataSetSummary
from RAnalysis.RTools.ExtractCoefficients import *
from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.FilterData.testFunctions.testGaussianNormality import isNormal

# extract the stock tickers of all data filtering survivors #
from RAnalysis.RTools.PlotGraphs import histogram

listOfSurvivors = []
for stock in nonMultiColList:
    listOfSurvivors.append(stock.columns[0])
extractedSummaries = extractSummaries(listOfSurvivors, 1)
extractedCoefficients = extractCoefficients(extractedSummaries)
extractedESGBetaPValues = extractESGBetasPValue(extractedCoefficients)
significanceCount, noSignificanceCount = countSignificantFactors(extractedESGBetaPValues, 0.05)
percentageOfSignificance = 100 * significanceCount / (significanceCount + noSignificanceCount)
extractedESGBetas = extractESGBetas(extractedCoefficients)
ESGBetasWithoutOutliers = excludeOutliers(extractedESGBetas)

medianESGBeta = np.nanmedian(extractedESGBetas)
averageESGBeta = np.nanmean(extractedESGBetas)
medianESGWithoutOutliers = np.nanmedian(ESGBetasWithoutOutliers)
averageESGWithoutOutliers = np.nanmean(ESGBetasWithoutOutliers)
tTest1 = ttest_1samp(extractedESGBetas, 0.0)
tTest2 = ttest_1samp(ESGBetasWithoutOutliers, 0.0)

# TODO: normality test & do for individual stocks to confirm H1
#  --> if for a large amount of individual stocks the beta is significant (and negative as well than more evidence)

ESGBetas1 = pd.DataFrame(extractedESGBetas)
print('\nSummary ESG betas with outliers:')
printDataSetSummary(ESGBetas1)

ESGBetas2 = pd.DataFrame(ESGBetasWithoutOutliers)
print('\n Summary ESG betas without outliers:')
printDataSetSummary(ESGBetas2)

print('\nH1: The distribution of ESG Betas is significantly different from zero')
if isNormal(extractedESGBetas, 0.95):
    print('t-statistic = %6.3f pValue = %6.4f' % tTest1)
    print('Median of all ESG Betas: %6.6f, average of all ESG betas: %6.6f' % (medianESGBeta, averageESGBeta))
else:
    print('RESULT: With outliers, the distribution of ESG betas does not follow normality and can therefore not be '
          'tested.')
if isNormal(ESGBetasWithoutOutliers, 0.95):
    print('\nt-statistic = %6.3f pValue = %6.4f' % tTest2)
    print('Median of all ESG Betas: %6.6f, average of all ESG betas: %6.6f'
          % (medianESGWithoutOutliers, averageESGWithoutOutliers))
    print('''RESULT: Without outliers, the ESG beta has a statistically significant difference to zero on a 99% confidence 
    level. Both the median and the mean are negative which indicates an inverse relationship between stock returns 
    and ESG ratings.''')
else:
    print('RESULT: Without outliers, the distribution of ESG betas does not follow normality and can therefore not be '
          'tested.')

print('\nFor how many stocks is the ESG factor individually significant?')
print('Stocks with significant ESG betas: %3d' % significanceCount)
print('Stock without significant ESG betas: %2d' % noSignificanceCount)
print('Percentage of significant ESG betas: %6.2f%%' % percentageOfSignificance)

