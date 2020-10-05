import numpy as np
from ImportFilesPackages.ImportFiles import listOfStocksPerIndustry, sp500_Industries
from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas, excludeOutliers
from RAnalysis.RTools.tTest import oneSampleTTest

# TODO: update saved industry csv files

# Display amount of stocks and number of data points per industry

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
    currentExtractedSummaries = extractSummaries(currentListOfStockNames, 1)
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

print('\nH5: Each industry has a different ESG beta and all betas are statistically different from zero')

print('\nT test for industry Communication Services')
oneSampleTTest(communicationServicesESG, 0.0)
oneSampleTTest(comSerWithoutOutliers, 0.0)
print('With outliers: no statistical significance supporting the difference of ESG betas different from zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Consumer Discretionary')
oneSampleTTest(consumerDiscretionaryESG, 0.0)
oneSampleTTest(conDisWithoutOutliers, 0.0)
print('With and without outliers ESG beta statistically different from zero with confidence level 99%')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Consumer Staples')
oneSampleTTest(consumerStaplesESG, 0.0)
oneSampleTTest(conStaWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 90% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Energy')
oneSampleTTest(energyESG, 0.0)
oneSampleTTest(enWithoutOutliers, 0.0)
print('Has no outliers: 95% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Financials')
oneSampleTTest(financialsESG, 0.0)
oneSampleTTest(finWithoutOutliers, 0.0)
print('With outliers: 95% confidence for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Health Care')
oneSampleTTest(healthCareESG, 0.0)
oneSampleTTest(heCaWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Industrials')
oneSampleTTest(industrialsESG, 0.0)
oneSampleTTest(indWithoutOutliers, 0.0)
print('With and without outliers ESG beta statistically different from zero with confidence level 99%')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Information Technology')
oneSampleTTest(informationTechnologyESG, 0.0)
oneSampleTTest(itWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Materials')
oneSampleTTest(materialsESG, 0.0)
oneSampleTTest(matWithoutOutliers, 0.0)
print('With and without outliers ESG beta not statistically different from zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Real Estate')
oneSampleTTest(realEstateESG, 0.0)
oneSampleTTest(reEsWithoutOutliers, 0.0)
print('With outliers: 95% confidence for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nT test for industry Utilities')
oneSampleTTest(utilitiesESG, 0.0)
oneSampleTTest(utWithoutOutliers, 0.0)
print('Has no outliers: there is evidence for difference to zero on a 90% confidence level')
print('Mean and average smaller than zero --> indicates negative correlation')

print('\nRESULT 1: The average and median ESG beta are for all industries smaller than zero')
print('RESULT 2: With outliers, the ESG betas of all industries except Communication Services, Consumer Staples, '
      'Health Care, IT and Materials are statistically different from zero')
print('RESULT 3: Without outliers, the ESG betas of all industries except Materials are significantly different from '
      'zero')
print('RESULT 4: With outliers, in the Consumer Staples industry with a ESG beta of -0.000392 the ESG ratings seem to '
      'have the largest impact, the least impact is in IT with a slightly positive beta of 0.000034.')
print('RESULT 5: Without outliers, the lowest beta is in the energy industry with a mean of -0.000303. The highest '
      'beta has Materials with -0.000047.')
print('RESULT 6: Again the findings from the hypothesis before are in line with the findings of this hypothesis --> '
      'negative correlation ESG ratings & stock return')
