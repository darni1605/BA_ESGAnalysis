# normality test for stock returns #
from ImportFilesPackages.ImportFiles import companyIdentifier
from RAnalysis.FilterData.testFunctions.testGaussianNormality import excludeNonNormal
from RAnalysis.FilterData.testFunctions.testHeteroscedasticty import excludeHeteroscedasticity
from RAnalysis.FilterData.testFunctions.testMultiCollinearity import excludeMultiCollinearity
from RAnalysis.RTools.GenerateModels import createDFModel

listDf = []
for stock in companyIdentifier:
    df = createDFModel(stock)
    listDf.append(df)
normalListDf = []
for df in listDf:
    normalDf = excludeNonNormal(df, 0.99)
    normalListDf.append(normalDf)
print('Original number of stocks: ' + str(len(listDf)))
print('Number of stocks following normality: ' + str(len(normalListDf)))
# RESULT: no stock was excluded for confidence level 99% #

# heteroscedasticity test for linear regression models #
nonHeteroscedasticityList = []
for df in normalListDf:
    nonHeteroscedasticityDf = excludeHeteroscedasticity(df)
    nonHeteroscedasticityList.append(nonHeteroscedasticityDf)

# if there is Heteroscedasticity, None value is returned --> remove #
cleanNonHeteroscedasticityList = []
for df in nonHeteroscedasticityList:
    if df is not None:
        cleanNonHeteroscedasticityList.append(df)
print('Number of stocks without heteroscedasticity:' + str(len(cleanNonHeteroscedasticityList)))
# RESULT: Breusch Pagan Test lead to the exclusion of 193 stocks #

# test for multicollinearity and remove columns of dataframes a VIF factor higher than 5 #
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
