# normality test for stock returns #
from ImportFilesPackages.ImportFiles import companyIdentifier
from RAnalysis.FilterData.testFunctions.testGaussianNormality import excludeNonNormal
from RAnalysis.FilterData.testFunctions.testHeteroscedasticty import excludeHeteroscedasticity
from RAnalysis.FilterData.testFunctions.testMultiCollinearity import excludeMultiCollinearity
from RAnalysis.RTools.ExtractCoefficients import dropOnlyNanColumns
from RAnalysis.RTools.GenerateModels import createDFModel

listDf = []
for stock in companyIdentifier:
    df = createDFModel(stock, 2)
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
# RESULT: Breusch Pagan Test led to the exclusion of 193 stocks #

# test for multicollinearity and remove columns of dataframes a VIF factor higher than 5 #
numberOfColumnsBefore = 0
nonMultiColList = []
for df in cleanNonHeteroscedasticityList:
    numberOfColumnsBefore += len(df.columns)
    nonMultiColDf = excludeMultiCollinearity(df, 10)
    nonMultiColList.append(nonMultiColDf)
numberOfColumnsAfter = 0
for df in nonMultiColList:
    try:
        numberOfColumnsAfter += len(df.columns)
    except AttributeError:
        pass


print('Number of columns before removing multicollinearity ' + str(numberOfColumnsBefore))
print('Number of columns after removing multicollinearity ' + str(numberOfColumnsAfter))
# RESULT: no factors were removed due to multicollinearity #

cleanListOfDf = dropOnlyNanColumns(nonMultiColList)

listOfSurvivors = []
for df in cleanListOfDf:
    stock = df.columns[0]
    listOfSurvivors.append(stock)

envCount = 0
socCount = 0
govCount = 0
for i in range(0, len(cleanListOfDf)):
    stock = listOfSurvivors[i]
    env = stock + 'EnvironmentScore'
    soc = stock + 'SocialScore'
    gov = stock + 'GovernanceScore'
    if env in cleanListOfDf[i].columns:
        envCount += 1
    if soc in cleanListOfDf[i].columns:
        socCount += 1
    if gov in cleanListOfDf[i].columns:
        govCount += 1

print('# Env scores: ' + str(envCount))
print('# Soc scores: ' + str(socCount))
print('# Gov scores: ' + str(govCount) + '\n')

