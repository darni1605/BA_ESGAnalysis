from ImportFilesPackages.ImportFiles import sp500_Industries
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


# def saveStockReturnsPerIndustry():
#     industries = sp500_Industries.iloc[:, 1].unique()
#     filteredStockList = []
#     for stock in cleanListOfDf:
#         filteredStockList.append(stock.columns[0])
#     for industry in industries:
#         currentIndustryGroup = groupPerIndustry(industry)
#         industryStockReturns = []
#         for stock in currentIndustryGroup:
#             if stock in filteredStockList:
#                 currentStockReturns = stockReturns_df[stock]
#                 industryStockReturns.append(currentStockReturns)
#         currentIndustryStockReturns = pd.concat(industryStockReturns, axis=1)
#         currentIndustryStockReturns.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                            r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'' + industry + '.csv'
#                                            , sep=';')
#
#
# def saveFilteredStocks():
#     filteredStockList = []
#     for stock in nonMultiColList:
#         filteredStockList.append(stock.columns[0])
#     filteredStocks = stockReturns_df[filteredStockList]
#     filteredStocks.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                           r'Data\CSV-files\FilteredStocks\FilteredStocksReturns.csv'
#                           , sep=';')
#
#
# def saveESGBetas():
#     esgBetasWithOutliers_df = pd.DataFrame(data=extractedESGBetas, columns=['ESGBetasWithOutliers'])
#     esgBetasWithoutOutliers_df = pd.DataFrame(data=ESGBetasWithoutOutliers,
#                                               columns=['ESGBetasWithoutOutliers'])
#     esgBetasWithOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                    r'Data\CSV-files\ESGBetas\OverallScoreBetasWithOutliers.csv', sep=';')
#     esgBetasWithoutOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                       r'Data\CSV-files\ESGBetas\OverallScoreBetasWithoutOutliers.csv', sep=';')
#
#     envBetasWithOutliers_df = pd.DataFrame(data=envBetas, columns=['EnvBetasWithOutliers'])
#     socBetasWithOutliers_df = pd.DataFrame(data=socBetas, columns=['SocBetasWithOutliers'])
#     govBetasWithOutliers_df = pd.DataFrame(data=govBetas, columns=['GovBetasWithOutliers'])
#     envBetasWithoutOutliers_df = pd.DataFrame(data=envBetasWithoutOutliers, columns=['EnvBetasWithoutOutliers'])
#     socBetasWithoutOutliers_df = pd.DataFrame(data=socBetasWithoutOutliers, columns=['SocBetasWithoutOutliers'])
#     govBetasWithoutOutliers_df = pd.DataFrame(data=govBetasWithoutOutliers, columns=['GovBetasWithoutOutliers'])
#
#     envBetasWithOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                    r'Data\CSV-files\ESGBetas\EnvBetasWithOutliers.csv'
#                                    , sep=';')
#     socBetasWithOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                    r'Data\CSV-files\FilteredStocks\SocBetasWithOutliers.csv'
#                                    , sep=';')
#     govBetasWithOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                    r'Data\CSV-files\FilteredStocks\GovBetasWithOutliers.csv'
#                                    , sep=';')
#
#     envBetasWithoutOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                       r'Data\CSV-files\ESGBetas\EnvBetasWithoutOutliers.csv'
#                                       , sep=';')
#     socBetasWithoutOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                       r'Data\CSV-files\FilteredStocks\SocBetasWithoutOutliers.csv'
#                                       , sep=';')
#     govBetasWithoutOutliers_df.to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
#                                       r'Data\CSV-files\FilteredStocks\GovBetasWithoutOutliers.csv'
#                                       , sep=';')
