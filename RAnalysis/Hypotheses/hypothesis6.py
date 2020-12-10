from ImportFilesPackages.ImportFiles import *
from RAnalysis.RTools.GenerateModels import createDFModels
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.RTools.ConductHypoTestAboveBelowGroups import *

# create models for all stocks per industry
communicationServicesModels = createDFModels(communicationServicesStocks_lvl1, 1)
consumerDiscretionaryModels = createDFModels(consumerDiscretionaryStocks_lvl1, 1)
consumerStaplesModels = createDFModels(consumerStaplesStocks_lvl1, 1)
energyModels = createDFModels(energyStocks_lvl1, 1)
financialsModels = createDFModels(financialsStocks_lvl1, 1)
healthCareModels = createDFModels(healthCareStocks_lvl1, 1)
industrialsModels = createDFModels(industrialsStocks_lvl1, 1)
informationTechnologyModels = createDFModels(informationTechnologyStocks_lvl1, 1)
materialsModels = createDFModels(materialsStocks_lvl1, 1)
realEstateModels = createDFModels(realEstateStocks_lvl1, 1)
utilitiesModels = createDFModels(utilitiesStocks_lvl1, 1)

# filter ESG scores per industry
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

# split all industries into two groups each: Low Groups with lower and High Groups
# with higher ESG scores than market average
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

print('\nH6: Is there an outperformance of stocks above industry ESG average compared to the industry?')
print('\nCommunication Services')
print('Number of stocks Above Group: ' + str(len(highGroup1)))
conductHypoTest(highGroup1, communicationServicesModels, isLow=False)

print('\nConsumer Discretionary')
print('Number of stocks Above Group: ' + str(len(highGroup2)))
conductHypoTest(highGroup2, consumerDiscretionaryModels, isLow=False)

print('\nConsumer Staples')
print('Number of stocks Above Group: ' + str(len(highGroup3)))
conductHypoTest(highGroup3, consumerStaplesModels, isLow=False)

print('\nEnergy')
print('Number of stocks Above Group: ' + str(len(highGroup4)))
conductHypoTest(highGroup4, energyModels, isLow=False)


print('\nFinancials')
print('Number of stocks Above Group: ' + str(len(highGroup5)))
conductHypoTest(highGroup5, financialsModels, isLow=False)

print('\nHealth Care')
print('Number of stocks Above Group: ' + str(len(highGroup6)))
conductHypoTest(highGroup6, healthCareModels, isLow=False)

print('\nIndustrials')
print('Number of stocks Above Group: ' + str(len(highGroup7)))
conductHypoTest(highGroup7, industrialsModels, isLow=False)

print('\nInformation Technology')
print('Number of stocks Above Group: ' + str(len(highGroup8)))

print('\nMaterials')
print('Number of stocks Above Group: ' + str(len(highGroup9)))
conductHypoTest(highGroup9, materialsModels, isLow=False)

print('\nReal Estate')
print('Number of stocks Above Group: ' + str(len(highGroup10)))
conductHypoTest(highGroup10, realEstateModels, isLow=False)

print('\nUtilities')
print('Number of stocks Above Group: ' + str(len(highGroup11)))
conductHypoTest(highGroup11, utilitiesModels, isLow=False)

# ##################################################################################################################################

print('\nH7: Is there an underperformance of stocks below industry ESG average compared to the industry?')
print('\nCommunication Services')
print('Number of stocks Below Group: ' + str(len(lowGroup1)))
conductHypoTest(lowGroup1, communicationServicesModels, isLow=True)

print('\nConsumer Discretionary')
print('Number of stocks Below Group: ' + str(len(lowGroup2)))
conductHypoTest(lowGroup2, consumerDiscretionaryModels, isLow=True)

print('\nConsumer Staples')
print('Number of stocks Below Group: ' + str(len(lowGroup3)))
conductHypoTest(lowGroup3, consumerStaplesModels, isLow=True)

print('\nEnergy')
print('Number of stocks Below Group: ' + str(len(lowGroup4)))
conductHypoTest(lowGroup4, energyModels, isLow=True)

print('\nFinancials')
print('Number of stocks Below Group: ' + str(len(lowGroup5)))
conductHypoTest(lowGroup5, financialsModels, isLow=True)

print('\nHealth Care')
print('Number of stocks Below Group: ' + str(len(lowGroup6)))
conductHypoTest(lowGroup6, healthCareModels, isLow=True)

print('\nIndustrials')
print('Number of stocks Below Group: ' + str(len(lowGroup7)))
conductHypoTest(lowGroup7, industrialsModels, isLow=True)

print('\nInformation Technology')
print('Number of stocks Below Group: ' + str(len(lowGroup8)))
conductHypoTest(lowGroup8, informationTechnologyModels, isLow=True)

print('\nMaterials')
print('Number of stocks Below Group: ' + str(len(lowGroup9)))
conductHypoTest(lowGroup9, materialsModels, isLow=True)

print('\nReal Estate')
print('Number of stocks Below Group: ' + str(len(lowGroup10)))
conductHypoTest(lowGroup10, realEstateModels, isLow=True)

print('\nUtilities')
print('Number of stocks Below Group: ' + str(len(lowGroup11)))
conductHypoTest(lowGroup11, utilitiesModels, isLow=True)

print('''\nRESULT: Overall the hypothesis of out- or underperformance of stocks with an on average higher 
respectively lower ESG rating than the average industry ESG rating cannot be confirmed. Again it actually seems as 
though the Low groups actually outperform their High groups counterpart. This is in line with the findings of the 
previous hypothesis tests.''')
