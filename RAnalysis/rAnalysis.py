from RAnalysis.RTools.ExtractCoefficients import extractSummaries, extractCoefficients, extractESGBetas
from RAnalysis.FilterData.filterData import nonMultiColList

# extract the stock tickers of all data filtering survivors #
listOfSurvivors = []
for stock in nonMultiColList:
    print(stock.columns[0])
    listOfSurvivors.append(stock.columns[0])




