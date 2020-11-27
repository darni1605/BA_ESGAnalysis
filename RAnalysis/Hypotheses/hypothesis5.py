from ImportFilesPackages.ImportFiles import listOfStocksPerIndustry_lvl1, sp500_Industries
from RAnalysis.RTools.ExtractCoefficients import *
from RAnalysis.RTools.GenerateModels import createDFModels
from RAnalysis.RTools.tTest import oneSampleTTest

# Display amount of stocks and number of data points per industry

industryNames = sp500_Industries.iloc[:, 1].unique()

for i in range(0, len(listOfStocksPerIndustry_lvl1)):
    currentDataPointCount = 0
    countPerColumn = listOfStocksPerIndustry_lvl1[i].count()
    for count in countPerColumn:
        currentDataPointCount += count
    print(
        'The %s sector has %d stocks with %d data points' % (industryNames[i], len(listOfStocksPerIndustry_lvl1[i].columns),
                                                             currentDataPointCount))

# calculate the average & median ESG beta for each industry and test with hypothesis test
listOfExtractedESGBetas = []
listOfExtractedESGBetasPValues = []
for industry in listOfStocksPerIndustry_lvl1:
    currentListOfStockNames = []
    for stock in industry:
        currentListOfStockNames.append(stock)
    currentDfList = createDFModels(currentListOfStockNames, 1)
    cleanCurrentDfList = dropOnlyNanColumns(currentDfList)
    currentExtractedSummaries = extractSummaries(cleanCurrentDfList)
    currentExtractedCoefficients = extractCoefficients(currentExtractedSummaries)
    currentExtractedESGBetas = extractESGBetas(currentExtractedCoefficients)
    currentExtractedESGBetasPValues = extractESGBetasPValue(currentExtractedCoefficients)
    listOfExtractedESGBetas.append(currentExtractedESGBetas)
    listOfExtractedESGBetasPValues.append(currentExtractedESGBetasPValues)

communicationServicesESG = listOfExtractedESGBetas[0]
communicationServicesESG = communicationServicesESG[~np.isnan(communicationServicesESG)]
comSerWithoutOutliers = excludeOutliers(communicationServicesESG)
communicationServicesESGPValues = listOfExtractedESGBetasPValues[0]
communicationServicesESGPValues = communicationServicesESGPValues[~np.isnan(communicationServicesESGPValues)]
comSerSignificanceCount, comSerNoSignificanceCount = countSignificantFactors(communicationServicesESGPValues, 0.05)
comSerPercentageOfSignificance = 100 * comSerSignificanceCount / (comSerSignificanceCount + comSerNoSignificanceCount)

consumerDiscretionaryESG = listOfExtractedESGBetas[1]
consumerDiscretionaryESG = consumerDiscretionaryESG[~np.isnan(consumerDiscretionaryESG)]
conDisWithoutOutliers = excludeOutliers(consumerDiscretionaryESG)
consumerDiscretionaryESGPValues = listOfExtractedESGBetasPValues[1]
consumerDiscretionaryESGPValues = consumerDiscretionaryESGPValues[~np.isnan(consumerDiscretionaryESGPValues)]
conDisSignificanceCount, conDisNoSignificanceCount = countSignificantFactors(consumerDiscretionaryESGPValues, 0.05)
conDisPercentageOfSignificance = 100 * conDisSignificanceCount / (conDisSignificanceCount + conDisNoSignificanceCount)

consumerStaplesESG = listOfExtractedESGBetas[2]
consumerStaplesESG = consumerStaplesESG[~np.isnan(consumerStaplesESG)]
conStaWithoutOutliers = excludeOutliers(consumerStaplesESG)
consumerStaplesESGPValues = listOfExtractedESGBetasPValues[2]
consumerStaplesESGPValues = consumerStaplesESGPValues[~np.isnan(consumerStaplesESGPValues)]
conStaSignificanceCount, conStaNoSignificanceCount = countSignificantFactors(consumerStaplesESGPValues, 0.05)
conStaPercentageOfSignificance = 100 * conStaSignificanceCount / (conStaSignificanceCount + conStaNoSignificanceCount)

energyESG = listOfExtractedESGBetas[3]
energyESG = energyESG[~np.isnan(energyESG)]
enWithoutOutliers = excludeOutliers(energyESG)
energyESGPValues = listOfExtractedESGBetasPValues[3]
energyESGPValues = energyESGPValues[~np.isnan(energyESGPValues)]
enSignificanceCount, enNoSignificanceCount = countSignificantFactors(energyESGPValues, 0.05)
enPercentageOfSignificance = 100 * enSignificanceCount / (enSignificanceCount + enNoSignificanceCount)

financialsESG = listOfExtractedESGBetas[4]
financialsESG = financialsESG[~np.isnan(financialsESG)]
finWithoutOutliers = excludeOutliers(financialsESG)
financialsESGPValues = listOfExtractedESGBetasPValues[4]
financialsESGPValues = financialsESGPValues[~np.isnan(financialsESGPValues)]
finSignificanceCount, finNoSignificanceCount = countSignificantFactors(financialsESGPValues, 0.05)
finPercentageOfSignificance = 100 * finSignificanceCount / (finSignificanceCount + finNoSignificanceCount)

healthCareESG = listOfExtractedESGBetas[5]
healthCareESG = healthCareESG[~np.isnan(healthCareESG)]
heCaWithoutOutliers = excludeOutliers(healthCareESG)
healthCareESGPValues = listOfExtractedESGBetasPValues[5]
healthCareESGPValues = healthCareESGPValues[~np.isnan(healthCareESGPValues)]
heCaSignificanceCount, heCaNoSignificanceCount = countSignificantFactors(healthCareESGPValues, 0.05)
heCaPercentageOfSignificance = 100 * heCaSignificanceCount / (heCaSignificanceCount + heCaNoSignificanceCount)

industrialsESG = listOfExtractedESGBetas[6]
industrialsESG = industrialsESG[~np.isnan(industrialsESG)]
indWithoutOutliers = excludeOutliers(industrialsESG)
industrialsESGPValue = listOfExtractedESGBetasPValues[6]
industrialsESGPValue = industrialsESGPValue[~np.isnan(industrialsESGPValue)]
indSignificanceCount, indNoSignificanceCount = countSignificantFactors(industrialsESGPValue, 0.05)
indPercentageOfSignificance = 100 * indSignificanceCount / (indSignificanceCount + indNoSignificanceCount)

informationTechnologyESG = listOfExtractedESGBetas[7]
informationTechnologyESG = informationTechnologyESG[~np.isnan(informationTechnologyESG)]
itWithoutOutliers = excludeOutliers(informationTechnologyESG)
informationTechnologyESGPValues = listOfExtractedESGBetasPValues[7]
informationTechnologyESGPValues = informationTechnologyESGPValues[~np.isnan(informationTechnologyESGPValues)]
itSignificanceCount, itNoSignificanceCount = countSignificantFactors(informationTechnologyESGPValues, 0.05)
itPercentageOfSignificance = 100 * itSignificanceCount / (itSignificanceCount + itNoSignificanceCount)


materialsESG = listOfExtractedESGBetas[8]
materialsESG = materialsESG[~np.isnan(materialsESG)]
matWithoutOutliers = excludeOutliers(materialsESG)
materialsESGPValues = listOfExtractedESGBetasPValues[8]
materialsESGPValues = materialsESGPValues[~np.isnan(materialsESGPValues)]
matSignificanceCount, matNoSignificanceCount = countSignificantFactors(materialsESGPValues, 0.05)
matPercentageOfSignificance = 100 * matSignificanceCount / (matSignificanceCount + matNoSignificanceCount)

realEstateESG = listOfExtractedESGBetas[9]
realEstateESG = realEstateESG[~np.isnan(realEstateESG)]
reEsWithoutOutliers = excludeOutliers(realEstateESG)
realEstateESGPValues = listOfExtractedESGBetasPValues[9]
realEstateESGPValues = realEstateESGPValues[~np.isnan(realEstateESGPValues)]
reEsSignificanceCount, reEsNoSignificanceCount = countSignificantFactors(realEstateESGPValues, 0.05)
reEsPercentageOfSignificance = 100 * reEsSignificanceCount / (reEsSignificanceCount + reEsNoSignificanceCount)

utilitiesESG = listOfExtractedESGBetas[10]
utilitiesESG = utilitiesESG[~np.isnan(utilitiesESG)]
utWithoutOutliers = excludeOutliers(utilitiesESG)
utilitiesESGPValues = listOfExtractedESGBetasPValues[10]
utilitiesESGPValues = utilitiesESGPValues[~np.isnan(utilitiesESGPValues)]
utSignificanceCount, utNoSignificanceCount = countSignificantFactors(utilitiesESGPValues, 0.05)
utPercentageOfSignificance = 100 * utSignificanceCount / (utSignificanceCount + utNoSignificanceCount)

print('\nH5: Each industry has a different ESG beta and all betas are statistically different from zero')
print('Please note: For all industries, the number of stocks is to small to be able to conduct an hypothesis test. '
      'Therefore, ignore the results of hypothesis tests and analysis the means/medians instead. Additionally, '
      'calculate the percentage of significant ESG betas per industry.')


print('\nT test for industry Communication Services with %2d respectively %2d stocks' % (len(communicationServicesESG),
                                                                                         len(comSerWithoutOutliers)))
oneSampleTTest(communicationServicesESG, 0.0)
oneSampleTTest(comSerWithoutOutliers, 0.0)
print('With outliers: no statistical significance supporting the difference of ESG betas different from zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % comSerPercentageOfSignificance)

print('\nT test for industry Consumer Discretionary with %2d respectively %2d stocks' % (len(consumerDiscretionaryESG),
                                                                                         len(conDisWithoutOutliers)))
oneSampleTTest(consumerDiscretionaryESG, 0.0)
oneSampleTTest(conDisWithoutOutliers, 0.0)
print('With and without outliers ESG beta statistically different from zero with confidence level 99%')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % conDisPercentageOfSignificance)

print('\nT test for industry Consumer Staples  with %2d respectively %2d stocks' % (len(consumerStaplesESG),
                                                                                    len(conStaWithoutOutliers)))
oneSampleTTest(consumerStaplesESG, 0.0)
oneSampleTTest(conStaWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 90% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % conStaPercentageOfSignificance)

print('\nT test for industry Energy with %2d respectively %2d stocks' % (len(energyESG),
                                                                         len(enWithoutOutliers)))
oneSampleTTest(energyESG, 0.0)
oneSampleTTest(enWithoutOutliers, 0.0)
print('Has no outliers: 95% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % enPercentageOfSignificance)

print('\nT test for industry Financials with %2d respectively %2d stocks' % (len(financialsESG),
                                                                             len(finWithoutOutliers)))
oneSampleTTest(financialsESG, 0.0)
oneSampleTTest(finWithoutOutliers, 0.0)
print('With outliers: 95% confidence for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % finPercentageOfSignificance)

print('\nT test for industry Health Care with %2d respectively %2d stocks' % (len(healthCareESG),
                                                                              len(heCaWithoutOutliers)))
oneSampleTTest(healthCareESG, 0.0)
oneSampleTTest(heCaWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % heCaPercentageOfSignificance)

print('\nT test for industry Industrials with %2d respectively %2d stocks' % (len(industrialsESG),
                                                                              len(indWithoutOutliers)))
oneSampleTTest(industrialsESG, 0.0)
oneSampleTTest(indWithoutOutliers, 0.0)
print('With and without outliers ESG beta statistically different from zero with confidence level 99%')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % indPercentageOfSignificance)

print('\nT test for industry Information Technology with %2d respectively %2d stocks' % (len(informationTechnologyESG),
                                                                                         len(itWithoutOutliers)))
oneSampleTTest(informationTechnologyESG, 0.0)
oneSampleTTest(itWithoutOutliers, 0.0)
print('With outliers: no statistical significance for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % itPercentageOfSignificance)

print('\nT test for industry Materials  with %2d respectively %2d stocks' % (len(materialsESG),
                                                                             len(matWithoutOutliers)))
oneSampleTTest(materialsESG, 0.0)
oneSampleTTest(matWithoutOutliers, 0.0)
print('With and without outliers ESG beta not statistically different from zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % matPercentageOfSignificance)

print('\nT test for industry Real Estate with %2d respectively %2d stocks' % (len(realEstateESG),
                                                                              len(reEsWithoutOutliers)))
oneSampleTTest(realEstateESG, 0.0)
oneSampleTTest(reEsWithoutOutliers, 0.0)
print('With outliers: 95% confidence for a difference to zero')
print('Without outliers: 99% confidence for a difference to zero')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % reEsPercentageOfSignificance)

print('\nT test for industry Utilities with %2d respectively %2d stocks' % (len(utilitiesESG),
                                                                            len(utWithoutOutliers)))
oneSampleTTest(utilitiesESG, 0.0)
oneSampleTTest(utWithoutOutliers, 0.0)
print('Has no outliers: there is evidence for difference to zero on a 90% confidence level')
print('Mean and average smaller than zero --> indicates negative correlation')
print('Percentage of individual stocks with significant ESG betas: %6.2f%%' % utPercentageOfSignificance)

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
