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

OverallESGScores_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                  r'Data\CSV-files\Reuters_OverallESGScores_csv.csv'
                                  , sep=';', header=0, index_col=0)
OverallESGScores_df.replace(r'^\s*$', np.nan, regex=True)

SocialScores_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                              r'Data\CSV-files\Reuters_SocialScores_csv.csv'
                              , sep=';', header=0, index_col=0)
SocialScores_df.replace(r'^\s*$', np.nan, regex=True)

EnvironmentScores_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\Reuters_EnvironmentScores_csv.csv'
                                   , sep=';', header=0, index_col=0)
EnvironmentScores_df.replace(r'^\s*$', np.nan, regex=True)

GovernanceScore_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                 r'Data\CSV-files\Reuters_GovernanceScores_csv.csv'
                                 , sep=';', header=0, index_col=0)
GovernanceScore_df.replace(r'^\s*$', np.nan, regex=True)

OverallESGScores_changes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                          r'Data\CSV-files\Reuters_OverallESGScores_changes_csv.csv', sep=';', header=0,
                                          index_col=0)
OverallESGScores_changes_df.replace(r'^\s*$', np.nan, regex=True)

EnvironmentScores_changes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                           r'Data\CSV-files\Reuters_EnvironmentScores_changes_csv.csv', sep=';',
                                           header=0, index_col=0)
EnvironmentScores_changes_df.replace(r'^\s*$', np.nan, regex=True)

SocialScores_changes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                      r'Data\CSV-files\Reuters_SocialScores_changes_csv.csv', sep=';',
                                      header=0, index_col=0)
SocialScores_changes_df.replace(r'^\s*$', np.nan, regex=True)

GovernanceScores_changes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                          r'Data\CSV-files\Reuters_GovernanceScores_changes_csv.csv', sep=';',
                                          header=0, index_col=0)
GovernanceScores_changes_df.replace(r'^\s*$', np.nan, regex=True)

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
