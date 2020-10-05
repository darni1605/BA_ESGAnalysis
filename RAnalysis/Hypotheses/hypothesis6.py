from ImportFilesPackages.ImportFiles import listOfStocksPerIndustry, stockReturns_df
from RAnalysis.RTools.GenerateModels import createDFModels
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterESGScores, groupAccordingToAverage

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

# write functions to get sublist from stockReturns_df, to generate an average column, average returns and np.isnan

lowGroupReturns1, highGroupReturns1 = (stockReturns_df[lowGroup1].copy(), stockReturns_df[highGroup1].copy())
lowGroupReturns2, highGroupReturns2 = (stockReturns_df[lowGroup2].copy(), stockReturns_df[highGroup2].copy())
lowGroupReturns3, highGroupReturns3 = (stockReturns_df[lowGroup3].copy(), stockReturns_df[highGroup3].copy())
lowGroupReturns4, highGroupReturns4 = (stockReturns_df[lowGroup4].copy(), stockReturns_df[highGroup4].copy())
lowGroupReturns5, highGroupReturns5 = (stockReturns_df[lowGroup5].copy(), stockReturns_df[highGroup5].copy())
lowGroupReturns6, highGroupReturns6 = (stockReturns_df[lowGroup6].copy(), stockReturns_df[highGroup6].copy())
lowGroupReturns7, highGroupReturns7 = (stockReturns_df[lowGroup7].copy(), stockReturns_df[highGroup7].copy())
lowGroupReturns8, highGroupReturns8 = (stockReturns_df[lowGroup8].copy(), stockReturns_df[highGroup8].copy())
lowGroupReturns9, highGroupReturns9 = (stockReturns_df[lowGroup9].copy(), stockReturns_df[highGroup9].copy())
lowGroupReturns10, highGroupReturns10 = (stockReturns_df[lowGroup10].copy(), stockReturns_df[highGroup10].copy())
lowGroupReturns11, highGroupReturns11 = (stockReturns_df[lowGroup11].copy(), stockReturns_df[highGroup11].copy())

avgLowGroupReturns1, avgHighGroupReturns1 = (lowGroupReturns1.mean(axis=1).copy(),
                                             highGroupReturns1.mean(axis=1).copy())
avgLowGroupReturns2, avgHighGroupReturns2 = (lowGroupReturns2.mean(axis=1).copy(),
                                             highGroupReturns2.mean(axis=1).copy())
avgLowGroupReturns3, avgHighGroupReturns3 = (lowGroupReturns3.mean(axis=1).copy(),
                                             highGroupReturns3.mean(axis=1).copy())
avgLowGroupReturns4, avgHighGroupReturns4 = (lowGroupReturns4.mean(axis=1).copy(),
                                             highGroupReturns4.mean(axis=1).copy())
avgLowGroupReturns5, avgHighGroupReturns5 = (lowGroupReturns5.mean(axis=1).copy(),
                                             highGroupReturns5.mean(axis=1).copy())
avgLowGroupReturns6, avgHighGroupReturns6 = (lowGroupReturns6.mean(axis=1).copy(),
                                             highGroupReturns6.mean(axis=1).copy())
avgLowGroupReturns7, avgHighGroupReturns7 = (lowGroupReturns7.mean(axis=1).copy(),
                                             highGroupReturns7.mean(axis=1).copy())
avgLowGroupReturns8, avgHighGroupReturns8 = (lowGroupReturns8.mean(axis=1).copy(),
                                             highGroupReturns8.mean(axis=1).copy())
avgLowGroupReturns9, avgHighGroupReturns9 = (lowGroupReturns9.mean(axis=1).copy(),
                                             highGroupReturns9.mean(axis=1).copy())
avgLowGroupReturns10, avgHighGroupReturns10 = (lowGroupReturns10.mean(axis=1).copy(),
                                               highGroupReturns10.mean(axis=1).copy())
avgLowGroupReturns11, avgHighGroupReturns11 = (lowGroupReturns11.mean(axis=1).copy(),
                                               highGroupReturns11.mean(axis=1).copy())


