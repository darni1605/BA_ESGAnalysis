from ImportFilesPackages.ImportFiles import stockReturns_df, OverallESGScores_df, listOfFilteredStockNames, \
    EnvironmentScores_df, SocialScores_df, GovernanceScore_df, sp500_Industries
import numpy as np


def groupPerIndustry(industry):
    i = 0
    industryGroups = []
    while i < len(sp500_Industries):
        if industry == sp500_Industries.iloc[i, 1]:
            industryGroups.append(sp500_Industries.iloc[i, 0])
            i += 1
        else:
            i += 1

    return industryGroups


def getStockTableInfo(stock, comparable, comparableName):
    stockReturns = stockReturns_df[stock]
    stockESGScore = OverallESGScores_df[stock + 'ESGScore']
    listOfESGStockNames = []
    listOfSocStockNames = []
    listOfEnvStockNames = []
    listOfGovStockNames = []
    if comparableName == 'Market':
        for stockName in listOfFilteredStockNames:
            listOfESGStockNames.append(stockName + 'ESGScore')
            listOfEnvStockNames.append(stockName + 'EnvironmentScore')
            listOfSocStockNames.append(stockName + 'SocialScore')
            listOfGovStockNames.append(stockName + 'GovernanceScore')
        comparableESG = OverallESGScores_df[listOfESGStockNames]

    else:
        industryGroup = groupPerIndustry(comparableName)
        for industryStock in industryGroup:
            if industryStock not in listOfFilteredStockNames:
                industryGroup.remove(industryStock)
        for stockName in industryGroup:
            listOfESGStockNames.append(stockName + 'ESGScore')
            listOfEnvStockNames.append(stockName + 'EnvironmentScore')
            listOfSocStockNames.append(stockName + 'SocialScore')
            listOfGovStockNames.append(stockName + 'GovernanceScore')
        comparableESG = OverallESGScores_df[listOfESGStockNames]

    if np.isnan(np.nanmean(stockESGScore)):
        stockESGMean = 'N/A'
    else:
        stockESGMean = ('{:.4f}'.format(np.nanmean(stockESGScore)))

    if np.isnan(np.nanmedian(stockESGScore)):
        stockESGMedian = 'N/A'
    else:
        stockESGMedian = ('{:.4f}'.format(np.nanmean(stockESGScore)))

    stockMean = ('{:.4f}%'.format(100 * (np.exp(np.nanmean(stockReturns)) - 1)))
    stockMedian = ('{:.4f}%'.format(100 * (np.exp(np.nanmedian(stockReturns)) - 1)))
    comparableMean = ('{:.4f}%'.format(100 * (np.exp(np.nanmean(comparable)) - 1)))
    comparableMedian = ('{:.4f}%'.format(100 * (np.exp(np.nanmedian(comparable)) - 1)))
    comparableESGMean = ('{:.4f}'.format(np.nanmean(comparableESG.mean(axis=1))))
    comparableESGMedian = ('{:.4f}'.format(np.nanmedian(comparableESG.mean(axis=1))))

    return stockMean, stockMedian, comparableMean, comparableMedian, stockESGMean, stockESGMedian, \
           comparableESGMean, comparableESGMedian
