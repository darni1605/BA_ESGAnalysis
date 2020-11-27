from ImportFilesPackages.ImportFiles import *


def getMeanReturnColumn(industryStocks):
    industryStockReturns = stockReturns_df[industryStocks].copy()
    industryStockReturns['MeanReturn'] = industryStockReturns.mean(axis=1)
    return industryStockReturns['MeanReturn']


def industryMatch(stock):
    if stock in communicationServicesStocks_lvl1:
        return 'Communication Services', getMeanReturnColumn(communicationServicesStocks_lvl1)
    if stock in consumerDiscretionaryStocks_lvl1:
        return 'Consumer Discretionary', getMeanReturnColumn(consumerDiscretionaryStocks_lvl1)
    if stock in consumerStaplesStocks_lvl1:
        return 'Consumer Staples', getMeanReturnColumn(consumerStaplesStocks_lvl1)
    if stock in energyStocks_lvl1:
        return 'Energy', getMeanReturnColumn(energyStocks_lvl1)
    if stock in financialsStocks_lvl1:
        return 'Financials', getMeanReturnColumn(financialsStocks_lvl1)
    if stock in healthCareStocks_lvl1:
        return 'Health Care', getMeanReturnColumn(healthCareStocks_lvl1)
    if stock in industrialsStocks_lvl1:
        return 'Industrials', getMeanReturnColumn(industrialsStocks_lvl1)
    if stock in informationTechnologyStocks_lvl1:
        return 'Information Technology', getMeanReturnColumn(informationTechnologyStocks_lvl1)
    if stock in materialsStocks_lvl1:
        return 'Materials', getMeanReturnColumn(materialsStocks_lvl1)
    if stock in realEstateStocks_lvl1:
        return 'Real Estate', getMeanReturnColumn(realEstateStocks_lvl1)
    if stock in utilitiesStocks_lvl1:
        return 'Utilities', getMeanReturnColumn(utilitiesStocks_lvl1)
