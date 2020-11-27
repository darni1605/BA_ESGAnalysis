from ImportFilesPackages.ImportFiles import *
from RAnalysis.RTools.GenerateModels import createDFModels
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage
from RAnalysis.RTools.ConductHypoTest import *


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

print(len(lowGroup1)), print(len(highGroup1))
print(len(lowGroup2)), print(len(highGroup2))
print(len(lowGroup3)), print(len(highGroup3))
print(len(lowGroup4)), print(len(highGroup4))
print(len(lowGroup5)), print(len(highGroup5))
print(len(lowGroup6)), print(len(highGroup6))
print(len(lowGroup7)), print(len(highGroup7))
print(len(lowGroup8)), print(len(highGroup8))
print(len(lowGroup9)), print(len(highGroup9))
print(len(lowGroup10)), print(len(highGroup10))
print(len(lowGroup11)), print(len(highGroup11))


print('\nH6: Is there an underperformance of stocks below industry ESG average compared to the industry?')
print('\nCommunication Services')
conductHypoTest(lowGroup1, communicationServicesModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.6748 and 0.3629. Although the mean and median 
returns are lower than the industrys, only 50% of all stocks actually underperformed the industry.''')

print('\nConsumer Discretionary')
conductHypoTest(lowGroup2, consumerDiscretionaryModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.6208 and 0.4095. The mean and median returns are 
higher than the industrys and only 38.46% of all stocks actually underperformed the industry.''')

print('\nConsumer Staples')
conductHypoTest(lowGroup3, consumerStaplesModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5634 and 0.4532. The mean and median returns are 
higher than the industrys but 71.43% of all stocks actually underperformed the industry.''')

print('\nEnergy')
conductHypoTest(lowGroup4, energyModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.7050 and 0.3626. Although the mean and median 
returns are lower than the industrys and 100% of all stocks actually underperformed the industry.''')

print('\nFinancials')
conductHypoTest(lowGroup5, financialsModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5853 and 0.4361. Although the mean and median 
returns are lower than the industrys and 100% of all stocks actually underperformed the industry.''')

print('\nHealth Care')
conductHypoTest(lowGroup6, healthCareModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5972 and 0.4279. The mean and median returns are 
higher than the industrys and 43.75% of all stocks actually underperformed the industry.''')

print('\nIndustrials')
conductHypoTest(lowGroup7, industrialsModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5768 and 0.4442. The mean and median returns are 
higher than the industrys and 44.44% of all stocks actually underperformed the industry.''')

print('\nInformation Technology')
conductHypoTest(lowGroup8, informationTechnologyModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5024 and 0.4986. The mean and median returns are 
basically the same as the industrys but 55.56% of all stocks actually underperformed the industry.''')

print('\nMaterials')
conductHypoTest(lowGroup9, materialsModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.5933 and 0.4271. The mean is lower and median is 
higher than the industrys and 66.67% of all stocks actually underperformed the industry.''')

print('\nReal Estate')
conductHypoTest(lowGroup10, realEstateModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.6697 and 0.3499. The mean and median returns are 
higher than the industrys and 0% of all stocks actually underperformed the industry.''')

print('\nUtilities')
conductHypoTest(lowGroup11, utilitiesModels, isLow=True)
print('''RESULT: No evidence for underperformance with p-values of 0.6245 and 0.4087. Although the mean and median 
returns are lower than the industrys and 66.67% of all stocks actually underperformed the industry.''')


print('\nH7: Is there an outperformance of stocks above industry ESG average compared to the industry?')
print('\nCommunication Services')
conductHypoTest(highGroup1, communicationServicesModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3486 and 0.3911. Both median and mean return 
are higher than the industrys but only 30% of stocks actually outperformed the industry.''')

print('\nConsumer Discretionary')
conductHypoTest(highGroup2, consumerDiscretionaryModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3687 and 0.4084. Both median and mean return 
are lower than the industrys and only 28.57% of stocks actually outperformed the industry.''')

print('\nConsumer Staples')
conductHypoTest(highGroup3, consumerStaplesModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.4409 and 0.4567. The median is higher and mean return 
lower than the industrys and only 37.5% of stocks actually outperformed the industry.''')

print('\nEnergy')
conductHypoTest(highGroup4, energyModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3922 and 0.4170. Although both median and mean return 
are higher than the industrys and only 50% of stocks actually outperformed the industry.''')

print('\nFinancials')
conductHypoTest(highGroup5, financialsModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.4897 and 0.4925. Mean is higher and median is lower 
than the industrys and only 50% of stocks actually outperformed the industry.''')

print('\nHealth Care')
conductHypoTest(highGroup6, healthCareModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3099 and 0.3651. Although both median and mean return 
are lower than the industrys and only 33.33% of stocks actually outperformed the industry.''')

print('\nIndustrials')
conductHypoTest(highGroup7, industrialsModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3952 and 0.4253. Median is higher and mean lower 
than the industrys and only 57.14% of stocks actually outperformed the industry.''')

print('\nInformation Technology')
conductHypoTest(highGroup8, informationTechnologyModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.4784 and 0.4845. Mean return is higher and median 
lower than the industrys and only 57.14% of stocks actually outperformed the industry.''')

print('\nMaterials')
conductHypoTest(highGroup9, materialsModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.4407 and 0.4577. Median is lower and mean is higher 
than the industrys and only 50% of stocks actually outperformed the industry.''')

print('\nReal Estate')
conductHypoTest(highGroup10, realEstateModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.4102 and 0.4403. Median is higher and mean is lower 
than the industrys and only 50% of stocks actually outperformed the industry.''')

print('\nUtilities')
conductHypoTest(highGroup11, utilitiesModels, isLow=False)
print('''RESULT: No evidence for outperformance with p-values of 0.3091 and 0.3614. Median is lower and mean is higher 
than the industrys and only 50% of stocks actually outperformed the industry.''')

print('''\nRESULT: Overall the hypothesis of out- or underperformance of stocks with an on average higher 
respectively lower ESG rating than the average industry ESG rating cannot be confirmed. Again it actually seems as 
though the Low groups actually outperform their High groups counterpart. This is in line with the findings of the 
previous hypothesis tests.''')