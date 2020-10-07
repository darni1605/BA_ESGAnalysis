from ImportFilesPackages.ImportFiles import listOfStocksPerIndustry, stockReturns_df
from RAnalysis.RTools.GenerateModels import createDFModels
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.RTools.Performance import countOutUnderPerformance
from RAnalysis.RTools.ConductHypoTest import *

communicationServicesStocks = listOfStocksPerIndustry[0].columns
consumerDiscretionaryStocks = listOfStocksPerIndustry[1].columns
consumerStaplesStocks = listOfStocksPerIndustry[2].columns
energyStocks = listOfStocksPerIndustry[3].columns
financialsStocks = listOfStocksPerIndustry[4].columns
healthCareStocks = listOfStocksPerIndustry[5].columns
industrialsStocks = listOfStocksPerIndustry[6].columns
informationTechnologyStocks = listOfStocksPerIndustry[7].columns
materialsStocks = listOfStocksPerIndustry[8].columns
realEstateStocks = listOfStocksPerIndustry[9].columns
utilitiesStocks = listOfStocksPerIndustry[10].columns

communicationServicesModels = createDFModels(communicationServicesStocks, 1)
consumerDiscretionaryModels = createDFModels(consumerDiscretionaryStocks, 1)
consumerStaplesModels = createDFModels(consumerStaplesStocks, 1)
energyModels = createDFModels(energyStocks, 1)
financialsModels = createDFModels(financialsStocks, 1)
healthCareModels = createDFModels(healthCareStocks, 1)
industrialsModels = createDFModels(industrialsStocks, 1)
informationTechnologyModels = createDFModels(informationTechnologyStocks, 1)
materialsModels = createDFModels(materialsStocks, 1)
realEstateModels = createDFModels(realEstateStocks, 1)
utilitiesModels = createDFModels(utilitiesStocks, 1)

filteredESG1 = filterESGScores(communicationServicesModels)
filteredESG2 = filterESGScores(consumerDiscretionaryModels)
filteredESG3 = filterESGScores(consumerStaplesModels)
filteredESG4 = filterESGScores(energyModels)
filteredESG5 = filterESGScores(financialsModels)
filteredESG6 = filterESGScores(healthCareModels)
filteredESG7 = filterESGScores(industrialsModels)
filteredESG8 = filterESGScores(informationTechnologyModels)
filteredESG9 = filterESGScores(materialsModels)
filteredESG10 = filterESGScores(realEstateModels)
filteredESG11 = filterESGScores(utilitiesModels)

lowGroup1, highGroup1 = groupAccordingToAverage(filteredESG1)
lowGroup2, highGroup2 = groupAccordingToAverage(filteredESG2)
lowGroup3, highGroup3 = groupAccordingToAverage(filteredESG3)
lowGroup4, highGroup4 = groupAccordingToAverage(filteredESG4)
lowGroup5, highGroup5 = groupAccordingToAverage(filteredESG5)
lowGroup6, highGroup6 = groupAccordingToAverage(filteredESG6)
lowGroup7, highGroup7 = groupAccordingToAverage(filteredESG7)
lowGroup8, highGroup8 = groupAccordingToAverage(filteredESG8)
lowGroup9, highGroup9 = groupAccordingToAverage(filteredESG9)
lowGroup10, highGroup10 = groupAccordingToAverage(filteredESG10)
lowGroup11, highGroup11 = groupAccordingToAverage(filteredESG11)

print('\nH6: Is there an underperformance of stocks below industry ESG average compared to the industry?')
print('\nCommunication Services')
conductHypoTest(lowGroup1, communicationServicesModels, isLow=True)
print('\nConsumer Discretionary')
conductHypoTest(lowGroup2, consumerDiscretionaryModels, isLow=True)
print('\nConsumer Staples')
conductHypoTest(lowGroup3, consumerStaplesModels, isLow=True)
print('\nEnergy')
conductHypoTest(lowGroup4, energyModels, isLow=True)
print('\nFinancials')
conductHypoTest(lowGroup5, financialsModels, isLow=True)
print('\nHealth Care')
conductHypoTest(lowGroup6, healthCareModels, isLow=True)
print('\nIndustrials')
conductHypoTest(lowGroup7, industrialsModels, isLow=True)
print('\nInformation Technology')
conductHypoTest(lowGroup8, informationTechnologyModels, isLow=True)
print('\nMaterials')
conductHypoTest(lowGroup9, materialsModels, isLow=True)
print('\nReal Estate')
conductHypoTest(lowGroup10, realEstateModels, isLow=True)
print('\nUtilities')
conductHypoTest(lowGroup11, utilitiesModels, isLow=True)

print('\nH7: Is there an outperformance of stocks above industry ESG average compared to the industry?')
print('\nCommunication Services')
conductHypoTest(highGroup1, communicationServicesModels, isLow=False)
print('\nConsumer Discretionary')
conductHypoTest(highGroup2, consumerDiscretionaryModels, isLow=False)
print('\nConsumer Staples')
conductHypoTest(highGroup3, consumerStaplesModels, isLow=False)
print('\nEnergy')
conductHypoTest(highGroup4, energyModels, isLow=False)
print('\nFinancials')
conductHypoTest(highGroup5, financialsModels, isLow=False)
print('\nHealth Care')
conductHypoTest(highGroup6, healthCareModels, isLow=False)
print('\nIndustrials')
conductHypoTest(highGroup7, industrialsModels, isLow=False)
print('\nInformation Technology')
conductHypoTest(highGroup8, informationTechnologyModels, isLow=False)
print('\nMaterials')
conductHypoTest(highGroup9, materialsModels, isLow=False)
print('\nReal Estate')
conductHypoTest(highGroup10, realEstateModels, isLow=False)
print('\nUtilities')
conductHypoTest(highGroup11, utilitiesModels, isLow=False)
