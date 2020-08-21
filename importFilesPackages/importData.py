import rpy2.robjects as robject
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import pandas2ri
import numpy as np
import pandas as pd

# import csv files, convert to json and save as pandas dataFrames #

stockPrices_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                             r'Data\CSV-files\SP500_Constituents_ClosePrices_csv.csv'
                             , sep=';', header=0, index_col=0)
stockPrices_df.replace(r'^\s*$', np.nan, regex=True)

companyIndustries_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                   r'Data\CSV-files\SP500_Constituents_Industries_csv.csv', sep=';', header=0
                                   , index_col=0)

ESGScores_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                           r'Data\CSV-files\ESGScores_Reuters.csv', sep=';', header=0, index_col=0)
ESGScores_df.replace(r'^\s*$', np.nan, regex=True)


famaFrench_RiskFactors_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                        r'Data\CSV-files\FamaFrench_RiskFactors_csv.csv'
                                        , sep=';', header=0, index_col=0)

eventList_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                           r'Data\CSV-files\EventList_SP500_Stocks_csv.csv')
eventListTypes_df = pd.read_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw '
                                r'Data\CSV-files\EventTypeList_csv.csv')

# join eventList with eventListTypes #

eventListTypes2_df = eventListTypes_df[['EventType', 'DaysToExclude']]
eventList2_df = eventList_df[['Date', 'Identifier', 'EventType']]
mergedEventList2_df = eventList2_df.merge(eventListTypes2_df, how='inner')
