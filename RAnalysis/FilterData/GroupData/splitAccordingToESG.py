import numpy as np
from math import isnan
from ImportFilesPackages.ImportFiles import OverallESGScores_df, stockReturns_df


# return subset of stock returns with stock model list as input
def filterReturns(stockModelList):
    tickerList = []
    for i in range(0, len(stockModelList)):
        tickerList.append(stockModelList[i].columns[0])
    filteredReturns = stockReturns_df[tickerList].copy()
    return filteredReturns


# return subset of ESG scores with stock model list as input
def filterESGScores(stockModelList):
    ESGListToExamine = []
    for i in range(0, len(stockModelList)):
        ESGListToExamine.append(stockModelList[i].columns[4])
    filteredESGDf = OverallESGScores_df[ESGListToExamine]
    return filteredESGDf


# return average of ESG scores per stock
def getAverageESGForAllStocks(ESGScores):
    listOfAvg = ESGScores.mean()
    return listOfAvg


# return average of ESG score of averages of ESG scores per stock
def getESGMarketAverage(ESGScores):
    avgPerStock = getAverageESGForAllStocks(ESGScores)
    numberOfAvg = len(avgPerStock)
    sumOfAvg = 0
    for avg in avgPerStock:
        if not isnan(avg):
            sumOfAvg += avg
    marketESGAvg = sumOfAvg / numberOfAvg
    return marketESGAvg


# split stocks in two groups: high above and low below market ESG average
def groupAccordingToAverage(ESGScoreChanges):
    avgPerStock = getAverageESGForAllStocks(ESGScoreChanges)
    marketESGAvg = getESGMarketAverage(ESGScoreChanges)
    numberOfAvg = len(avgPerStock)
    lowGroup = []
    highGroup = []
    for i in range(0, numberOfAvg):
        currentStockTicker = avgPerStock.index[i].replace('ESGScore', '')
        if avgPerStock[i] < marketESGAvg:
            lowGroup.append(currentStockTicker)
        else:
            highGroup.append(currentStockTicker)
    return lowGroup, highGroup


# split stocks in three groups according to quantiles --> all groups with almost same number of stocks
def groupInQuantiles(ESGScoreChanges):
    avgPerStock = getAverageESGForAllStocks(ESGScoreChanges)
    avgPerStock = avgPerStock[~np.isnan(avgPerStock)].copy()
    numberOfStocks = len(avgPerStock)
    oneThirdQuantile = np.nanquantile(avgPerStock, 1 / 3)
    twoThirdQuantile = np.nanquantile(avgPerStock, 2 / 3)
    lowGroup = []
    mediumGroup = []
    highGroup = []
    for i in range(0, numberOfStocks):
        currentStockTicker = avgPerStock.index[i].replace('ESGScore', '')
        currentReturn = avgPerStock[i]
        if currentReturn <= oneThirdQuantile:
            lowGroup.append(currentStockTicker)
        elif oneThirdQuantile < currentReturn <= twoThirdQuantile:
            mediumGroup.append(currentStockTicker)
        elif twoThirdQuantile < currentReturn:
            highGroup.append(currentStockTicker)
    return lowGroup, mediumGroup, highGroup
