import numpy as np

from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas
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

medianESGBeta = np.median(extractedESGBetas)
averageESGBeta = np.average(extractedESGBetas)
print('Median of all ESG Betas: ' + str(medianESGBeta))
print('Average of all ESG Betas: ' + str(averageESGBeta))
histogram(extractedESGBetas, 'Distribution of ESG Betas', 'ESG Betas', 'Frequency')



