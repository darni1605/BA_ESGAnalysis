import numpy as np
from ImportFilesPackages.ImportFiles import listOfStocksPerIndustry, sp500_Industries
from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas, excludeOutliers
from RAnalysis.RTools.tTest import oneSampleTTest


# Display amount of stocks and number of data points per industry
from RAnalysis.RTools.PlotGraphs import histogram, cooksDistance

industryNames = sp500_Industries.iloc[:, 1].unique()

for i in range(0, len(listOfStocksPerIndustry)):
    currentDataPointCount = 0
    countPerColumn = listOfStocksPerIndustry[i].count()
    for count in countPerColumn:
        currentDataPointCount += count
    print(
        'The %s sector has %d stocks with %d data points' % (industryNames[i], len(listOfStocksPerIndustry[i].columns),
                                                             currentDataPointCount))

# calculate the average & median ESG beta for each industry and test with hypothesis test
listOfExtractedESGBetas = []
for industry in listOfStocksPerIndustry:
    currentListOfStockNames = []
    for stock in industry:
        currentListOfStockNames.append(stock)
    currentExtractedSummaries = extractSummaries(currentListOfStockNames)
    currentExtractedCoefficients = extractCoefficients(currentExtractedSummaries)
    currentExtractedESGBetas = extractESGBetas(currentExtractedCoefficients)
    listOfExtractedESGBetas.append(currentExtractedESGBetas)

communicationServicesESG = listOfExtractedESGBetas[0]
communicationServicesESG = communicationServicesESG[~np.isnan(communicationServicesESG)]
comSerWithoutOutliers = excludeOutliers(communicationServicesESG)
consumerDiscretionaryESG = listOfExtractedESGBetas[1]
consumerDiscretionaryESG = consumerDiscretionaryESG[~np.isnan(consumerDiscretionaryESG)]
conDisWithoutOutliers = excludeOutliers(consumerDiscretionaryESG)
consumerStaplesESG = listOfExtractedESGBetas[2]
consumerStaplesESG = consumerStaplesESG[~np.isnan(consumerStaplesESG)]
conStaWithoutOutliers = excludeOutliers(consumerStaplesESG)
energyESG = listOfExtractedESGBetas[3]
energyESG = energyESG[~np.isnan(energyESG)]
enWithoutOutliers = excludeOutliers(energyESG)
financialsESG = listOfExtractedESGBetas[4]
financialsESG = financialsESG[~np.isnan(financialsESG)]
finWithoutOutliers = excludeOutliers(financialsESG)
healthCareESG = listOfExtractedESGBetas[5]
healthCareESG = healthCareESG[~np.isnan(healthCareESG)]
heCaWithoutOutliers = excludeOutliers(healthCareESG)
industrialsESG = listOfExtractedESGBetas[6]
industrialsESG = industrialsESG[~np.isnan(industrialsESG)]
indWithoutOutliers = excludeOutliers(industrialsESG)
informationTechnologyESG = listOfExtractedESGBetas[7]
informationTechnologyESG = informationTechnologyESG[~np.isnan(informationTechnologyESG)]
itWithoutOutliers = excludeOutliers(informationTechnologyESG)
materialsESG = listOfExtractedESGBetas[8]
materialsESG = materialsESG[~np.isnan(materialsESG)]
matWithoutOutliers = excludeOutliers(materialsESG)
realEstateESG = listOfExtractedESGBetas[9]
realEstateESG = realEstateESG[~np.isnan(realEstateESG)]
reEsWithoutOutliers = excludeOutliers(realEstateESG)
utilitiesESG = listOfExtractedESGBetas[10]
utilitiesESG = utilitiesESG[~np.isnan(utilitiesESG)]
utWithoutOutliers = excludeOutliers(utilitiesESG)

print('\n T test for industry Communication Services')
oneSampleTTest(communicationServicesESG, 0.0)
oneSampleTTest(comSerWithoutOutliers, 0.0)
print('The exclusion of outliers leads to a smaller statistical significance')

print('\n T test for industry Consumer Discretionary')
oneSampleTTest(consumerDiscretionaryESG, 0.0)
oneSampleTTest(conDisWithoutOutliers, 0.0)
print('Without outliers, the ESG beta is no longer statistically significant')

print('\n T test for industry Consumer Staples')
oneSampleTTest(consumerStaplesESG, 0.0)
oneSampleTTest(conStaWithoutOutliers, 0.0)
print('Without outliers the difference to zero is less significant')

print('\n T test for industry Energy')
oneSampleTTest(energyESG, 0.0)
oneSampleTTest(enWithoutOutliers, 0.0)
print('Without outliers the difference to zero is much more significant')

print('\n T test for industry Financials')
oneSampleTTest(financialsESG, 0.0)
oneSampleTTest(finWithoutOutliers, 0.0)
print('Without outliers the difference to zero is less significant')

print('\n T test for industry Health Care')
oneSampleTTest(healthCareESG, 0.0)
oneSampleTTest(heCaWithoutOutliers, 0.0)
print('Without outliers the difference to zero has more or less the same significance')

print('\n T test for industry Industrials')
oneSampleTTest(industrialsESG, 0.0)
oneSampleTTest(indWithoutOutliers, 0.0)
print('Without outliers the difference is statistically significant on a confidence level of 90%')

print('\n T test for industry Information Technology')
oneSampleTTest(informationTechnologyESG, 0.0)
oneSampleTTest(itWithoutOutliers, 0.0)
print('Without outliers the difference to zero is much more significant')

print('\n T test for industry Materials')
oneSampleTTest(materialsESG, 0.0)
oneSampleTTest(matWithoutOutliers, 0.0)
print('Without outliers the difference is statistically significant on a confidence level of 90%')

print('\n T test for industry Real Estate')
oneSampleTTest(realEstateESG, 0.0)
oneSampleTTest(reEsWithoutOutliers, 0.0)
print('Without outliers the difference is statistically significant on a confidence level of 95%')

print('\n T test for industry Utilities')
oneSampleTTest(utilitiesESG, 0.0)
oneSampleTTest(utWithoutOutliers, 0.0)
print('Without outliers the difference to zero is less significant')

print('\nRESULT1: The average and median ESG beta is basically for all industries greater than zero')
print('RESULT2: With outliers, all ESG betas of the industries except the Consumer Discretionary sector are not '
      'significantly different from zero')
print('RESULT3: With outliers, for the Consumer Discretionary the ESG beta is significantly different from zero with '
      'a 90% confidence level')
print('RESULT4: Without outliers, the overall results are not improved as some industries get more significant and '
      'some less.')