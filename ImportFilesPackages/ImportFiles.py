import numpy as np
import pandas as pd

# import csv files, convert to json and save as pandas dataFrames #

stockPrices_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                             r'Data\CSV-files\SP500_Constituents_ClosePrices_csv.csv'
                             , sep=';', header=0, index_col=0)
stockPrices_df.replace(r'^\s*$', np.nan, regex=True)

stockReturns_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                              r'Data\CSV-files\SP500_Constituents_Performance_csv.csv'
                              , sep=';', header=0, index_col=0)
stockReturns_df.replace(r'^\s*$', np.nan, regex=True)

marketPricesReturns = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                  r'Data\CSV-files\SP500_ClosePrice_Return_csv.csv'
                                  , sep=';', header=0, index_col=0)

ESGScores_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                           r'Data\CSV-files\ESGScores_Reuters.csv', sep=';', header=0, index_col=0)
ESGScores_df.replace(r'^\s*$', np.nan, regex=True)

ESGScores_change_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                  r'Data\CSV-files\ESGScores_change_csv.csv', sep=';', header=0, index_col=0)
ESGScores_change_df.replace(r'^\s*$', np.nan, regex=True)

famaFrench_RiskFactors_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                        r'Data\CSV-files\FamaFrench_RiskFactors_csv.csv'
                                        , sep=';', header=0, index_col=0)

sp500_Industries = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                               r'Data\CSV-files\SP500_Constituents_Industry_csv.csv'
                               , sep=';', header=0)

industries_df = sp500_Industries.iloc[:, 1].unique()

eventList_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                           r'Data\CSV-files\EventList_SP500_Stocks_csv.csv')
eventListTypes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                r'Data\CSV-files\EventTypeList_csv.csv')

# join eventList with eventListTypes #
eventListTypes2_df = eventListTypes_df[['EventType', 'DaysToExclude']]
eventList2_df = eventList_df[['Date', 'Identifier', 'EventType']]
mergedEventList2_df = eventList2_df.merge(eventListTypes2_df, how='inner')

# extract Fama & French risk factors #
marketPremium = famaFrench_RiskFactors_df.iloc[:, 0]
SMB = famaFrench_RiskFactors_df.iloc[:, 1]
HML = famaFrench_RiskFactors_df.iloc[:, 2]
riskFree = famaFrench_RiskFactors_df.iloc[:, 3]

companyIdentifier = list(stockReturns_df)
nrOfColumns = len(stockPrices_df.columns)

# stock grouped in industries
communicationServicesStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                          r'Data\CSV-files\StockReturnsPerIndustry\'Communication Services.csv'
                                          , sep=';', header=0, index_col=0)
consumerDiscretionaryStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                          r'Data\CSV-files\StockReturnsPerIndustry\'Consumer Discretionary.csv'
                                          , sep=';', header=0, index_col=0)
consumerStaplesStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry\'Consumer Staples.csv'
                                    , sep=';', header=0, index_col=0)
energyStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                           r'Data\CSV-files\StockReturnsPerIndustry\'Energy.csv'
                           , sep=';', header=0, index_col=0)
financialsStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                               r'Data\CSV-files\StockReturnsPerIndustry\'Financials.csv'
                               , sep=';', header=0, index_col=0)
healthCareStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                               r'Data\CSV-files\StockReturnsPerIndustry\'Health Care.csv'
                               , sep=';', header=0, index_col=0)
industrialsStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                r'Data\CSV-files\StockReturnsPerIndustry\'Industrials.csv'
                                , sep=';', header=0, index_col=0)
informationTechnologyStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                          r'Data\CSV-files\StockReturnsPerIndustry\'Information Technology.csv'
                                          , sep=';', header=0, index_col=0)
materialsStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                              r'Data\CSV-files\StockReturnsPerIndustry\'Materials.csv'
                              , sep=';', header=0, index_col=0)
realEstateStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                               r'Data\CSV-files\StockReturnsPerIndustry\'Real Estate.csv'
                               , sep=';', header=0, index_col=0)
utilitiesStocks = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                              r'Data\CSV-files\StockReturnsPerIndustry\'Utilities.csv'
                              , sep=';', header=0, index_col=0)

listOfStocksPerIndustry = [communicationServicesStocks, consumerDiscretionaryStocks, consumerStaplesStocks,
                           energyStocks, financialsStocks, healthCareStocks, industrialsStocks,
                           informationTechnologyStocks, materialsStocks, realEstateStocks, utilitiesStocks]
