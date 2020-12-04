from ImportFilesPackages.ImportFiles import companyIdentifier
from RAnalysis.FilterData.testFunctions.testGaussianNormality import excludeNonNormal
from RAnalysis.FilterData.testFunctions.testHeteroscedasticty import excludeHeteroscedasticity
from RAnalysis.FilterData.testFunctions.testMultiCollinearity import excludeMultiCollinearity
from RAnalysis.RTools.GenerateModels import createDFModel


# To be applied for all 1st Level Models

# Exclude all non normal dependent variables (stock returns)
listDf = []
for stock in companyIdentifier:
    df = createDFModel(stock, 1)
    listDf.append(df)
normalListDf = []
for df in listDf:
    normalDf = excludeNonNormal(df, 0.95)
    normalListDf.append(normalDf)
print('Original number of stocks: ' + str(len(listDf)))
print('Number of stocks following normality: ' + str(len(normalListDf)))
# RESULT: all stock were excluded --> fat tail problematic --> normality assumed

# Exclude all heteroscedastic Models
nonHeteroscedasticityList = []
for df in listDf:
    nonHeteroscedasticityDf = excludeHeteroscedasticity(df)
    nonHeteroscedasticityList.append(nonHeteroscedasticityDf)

# if there is Heteroscedasticity, None value is returned --> remove None objects
cleanNonHeteroscedasticityList = []
for df in nonHeteroscedasticityList:
    if df is not None:
        cleanNonHeteroscedasticityList.append(df)
print('Number of stocks without heteroscedasticity:' + str(len(cleanNonHeteroscedasticityList)))
# RESULT: Breusch Pagan Test led to the exclusion of 316 stocks #

# test for multicollinearity and remove columns of dataframes with a VIF factor higher than 5 #
numberOfColumnsBefore = 0
nonMultiColList = []
for df in cleanNonHeteroscedasticityList:
    numberOfColumnsBefore += len(df.columns)
    nonMultiColDf = excludeMultiCollinearity(df, 5)
    nonMultiColList.append(nonMultiColDf)
numberOfColumnsAfter = 0
for df in nonMultiColList:
    numberOfColumnsAfter += len(df.columns)

print('Number of columns before removing multicollinearity ' + str(numberOfColumnsBefore))
print('Number of columns after removing multicollinearity ' + str(numberOfColumnsAfter))
# RESULT: no factors were removed due to multicollinearity #
