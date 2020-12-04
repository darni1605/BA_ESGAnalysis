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

famaFrench_RiskFactors_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                        r'Data\CSV-files\FamaFrench_RiskFactors_csv.csv'
                                        , sep=';', header=0, index_col=0)

sp500_Industries = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                               r'Data\CSV-files\SP500_Constituents_Industry_csv.csv'
                               , sep=';', header=0)

industries_df = sp500_Industries.iloc[:, 1].unique()

# extract Fama & French risk factors #
marketPremium = famaFrench_RiskFactors_df.iloc[:, 0]
SMB = famaFrench_RiskFactors_df.iloc[:, 1]
HML = famaFrench_RiskFactors_df.iloc[:, 2]
riskFree = famaFrench_RiskFactors_df.iloc[:, 3]

# list of all stock tickers and original amount of input stocks
companyIdentifier = list(stockReturns_df)
nrOfColumns = len(stockPrices_df.columns)

# import stock returns grouped per industry (1st Level)
communicationServicesStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Communication '
                                               r'Services.csv '
                                               , sep=';', header=0, index_col=0)
consumerDiscretionaryStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Consumer '
                                               r'Discretionary.csv '
                                               , sep=';', header=0, index_col=0)
consumerStaplesStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                         r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Consumer Staples.csv'
                                         , sep=';', header=0, index_col=0)
energyStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Energy.csv'
                                , sep=';', header=0, index_col=0)
financialsStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Financials.csv'
                                    , sep=';', header=0, index_col=0)
healthCareStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Health Care.csv'
                                    , sep=';', header=0, index_col=0)
industrialsStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                     r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Industrials.csv'
                                     , sep=';', header=0, index_col=0)
informationTechnologyStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Information Technology.csv'
                                               , sep=';', header=0, index_col=0)
materialsStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Materials.csv'
                                   , sep=';', header=0, index_col=0)
realEstateStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Real Estate.csv'
                                    , sep=';', header=0, index_col=0)
utilitiesStocks_lvl1 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\StockReturnsPerIndustry_lvl1\'Utilities.csv'
                                   , sep=';', header=0, index_col=0)

listOfStocksPerIndustry_lvl1 = [communicationServicesStocks_lvl1, consumerDiscretionaryStocks_lvl1,
                                consumerStaplesStocks_lvl1, energyStocks_lvl1, financialsStocks_lvl1,
                                healthCareStocks_lvl1, industrialsStocks_lvl1, informationTechnologyStocks_lvl1,
                                materialsStocks_lvl1, realEstateStocks_lvl1, utilitiesStocks_lvl1]

# create list of all stock tickers per industry (1st Level)
communicationServicesStocks_lvl1 = listOfStocksPerIndustry_lvl1[0].columns
consumerDiscretionaryStocks_lvl1 = listOfStocksPerIndustry_lvl1[1].columns
consumerStaplesStocks_lvl1 = listOfStocksPerIndustry_lvl1[2].columns
energyStocks_lvl1 = listOfStocksPerIndustry_lvl1[3].columns
financialsStocks_lvl1 = listOfStocksPerIndustry_lvl1[4].columns
healthCareStocks_lvl1 = listOfStocksPerIndustry_lvl1[5].columns
industrialsStocks_lvl1 = listOfStocksPerIndustry_lvl1[6].columns
informationTechnologyStocks_lvl1 = listOfStocksPerIndustry_lvl1[7].columns
materialsStocks_lvl1 = listOfStocksPerIndustry_lvl1[8].columns
realEstateStocks_lvl1 = listOfStocksPerIndustry_lvl1[9].columns
utilitiesStocks_lvl1 = listOfStocksPerIndustry_lvl1[10].columns

# import stock returns grouped per industry (2nd Level)
communicationServicesStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Communication '
                                               r'Services.csv '
                                               , sep=';', header=0, index_col=0)
consumerDiscretionaryStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Consumer '
                                               r'Discretionary.csv '
                                               , sep=';', header=0, index_col=0)
consumerStaplesStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                         r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Consumer Staples.csv'
                                         , sep=';', header=0, index_col=0)
energyStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Energy.csv'
                                , sep=';', header=0, index_col=0)
financialsStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Financials.csv'
                                    , sep=';', header=0, index_col=0)
healthCareStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Health Care.csv'
                                    , sep=';', header=0, index_col=0)
industrialsStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                     r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Industrials.csv'
                                     , sep=';', header=0, index_col=0)
informationTechnologyStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                               r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Information '
                                               r'Technology.csv '
                                               , sep=';', header=0, index_col=0)
materialsStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Materials.csv'
                                   , sep=';', header=0, index_col=0)
realEstateStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                    r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Real Estate.csv'
                                    , sep=';', header=0, index_col=0)
utilitiesStocks_lvl2 = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\StockReturnsPerIndustry_lvl2\'Utilities.csv'
                                   , sep=';', header=0, index_col=0)

listOfStocksPerIndustry_lvl2 = [communicationServicesStocks_lvl2, consumerDiscretionaryStocks_lvl2,
                                consumerStaplesStocks_lvl2, energyStocks_lvl2, financialsStocks_lvl2,
                                healthCareStocks_lvl2, industrialsStocks_lvl2, informationTechnologyStocks_lvl2,
                                materialsStocks_lvl2, realEstateStocks_lvl2, utilitiesStocks_lvl2]

# create list for stock tickers per industry
communicationServicesStocks_lvl2 = listOfStocksPerIndustry_lvl1[0].columns
consumerDiscretionaryStocks_lvl2 = listOfStocksPerIndustry_lvl1[1].columns
consumerStaplesStocks_lvl2 = listOfStocksPerIndustry_lvl1[2].columns
energyStocks_lvl2 = listOfStocksPerIndustry_lvl1[3].columns
financialsStocks_lvl2 = listOfStocksPerIndustry_lvl1[4].columns
healthCareStocks_lvl2 = listOfStocksPerIndustry_lvl1[5].columns
industrialsStocks_lvl2 = listOfStocksPerIndustry_lvl1[6].columns
informationTechnologyStocks_lvl2 = listOfStocksPerIndustry_lvl1[7].columns
materialsStocks_lvl2 = listOfStocksPerIndustry_lvl1[8].columns
realEstateStocks_lvl2 = listOfStocksPerIndustry_lvl1[9].columns
utilitiesStocks_lvl2 = listOfStocksPerIndustry_lvl1[10].columns


# import prepared csv files for visualization interface
filteredStockReturns = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\FilteredStocks\FilteredStocksReturns.csv'
                                   , sep=';', header=0, index_col=0)
listOfFilteredStockNames = list(filteredStockReturns.columns)

esgBetasWithOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\ESGBetas\OverallScoreBetasWithOutliers.csv'
                                   , sep=';', header=0, index_col=0)
esgBetasWithoutOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                      r'Data\CSV-files\ESGBetas\OverallScoreBetasWithoutOutliers.csv'
                                      , sep=';', header=0, index_col=0)
envBetasWithOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\ESGBetas\EnvBetasWithOutliers.csv'
                                   , sep=';', header=0, index_col=0)
envBetasWithoutOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                      r'Data\CSV-files\ESGBetas\EnvBetasWithoutOutliers.csv'
                                      , sep=';', header=0, index_col=0)
socBetasWithOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\ESGBetas\SocBetasWithOutliers.csv'
                                   , sep=';', header=0, index_col=0)
socBetasWithoutOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                      r'Data\CSV-files\ESGBetas\SocBetasWithoutOutliers.csv'
                                      , sep=';', header=0, index_col=0)
govBetasWithOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\ESGBetas\GovBetasWithOutliers.csv'
                                   , sep=';', header=0, index_col=0)
govBetasWithoutOutliers = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                      r'Data\CSV-files\ESGBetas\GovBetasWithoutOutliers.csv'
                                      , sep=';', header=0, index_col=0)
ESGHistogramTableData = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Results\graphs'
                                    r'\ESGHistogramTableData.csv '
                                    , sep=';', header=0, index_col=0)

survivingStockModels1stLevel = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                           r'Data\CSV-files\1stLevelSurvivingModels_csv.csv'
                                           , sep=';', header=0, index_col=0)
survivingStockModels2ndLevel = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                           r'Data\CSV-files\2ndLevelSurvivingModels_csv.csv'
                                           , sep=';', header=0, index_col=0)

expectedReturns1stModels = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Results\graphs'
                                       r'\1stLevelExpectedReturnsForGraph.csv '
                                       , sep=';', header=0, index_col=0)
expectedReturns2ndModels = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Results\graphs'
                                       r'\2ndLevelExpectedReturnsForGraph.csv '
                                       , sep=';', header=0, index_col=0)
listOfStock1stLevel = list(expectedReturns1stModels.columns)
listOfStock2ndLevel = list(expectedReturns2ndModels.columns)

barChartData1stLevel = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Results\graphs'
                                   r'\1stLevelBarChartMeanMedian.csv '
                                   , sep=';', header=0)
barChartData2ndLevel = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Results\graphs'
                                   r'\2ndLevelBarChartMeanMedian.csv '
                                   , sep=';', header=0)
