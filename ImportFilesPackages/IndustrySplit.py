from ImportFilesPackages.ImportFiles import sp500_Industries, stockReturns_df
import pandas as pd
import numpy as np


def getIndustry(stock):
    i = 0
    while i < len(sp500_Industries):
        if stock == sp500_Industries.iloc[i, 0]:
            return sp500_Industries.iloc[i, 1]
        else:
            i += 1


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


def getStockReturnsPerIndustry(industry):
    returnsPerIndustry = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                     r'Data\CSV-files\StockReturnsPerIndustry\'' + industry + '',
                                     sep=',', header=0, index_col=0)
    returnsPerIndustry.replace(r'^\s*$', np.nan, regex=True)
    return returnsPerIndustry


def saveStockReturnsPerIndustry():
    industries = sp500_Industries.iloc[:, 1].unique()

    for industry in industries:
        currentIndustryGroup = groupPerIndustry(industry)
        industryStockReturns = []
        for stock in currentIndustryGroup:
            currentStockReturns = stockReturns_df[stock]
            industryStockReturns.append(currentStockReturns)
        currentIndustryStockReturns = pd.concat(industryStockReturns, axis=1)
        currentIndustryStockReturns.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                           r'Data\CSV-files\StockReturnsPerIndustry\'' + industry + '')
