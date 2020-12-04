from scipy.stats import shapiro
import numpy as np

# Shapiro-Wilk Normality Test

# return bool if dataset is or is not normal
def isNormal(dataSet, confidenceLevel):
    testStat, p = shapiro(dataSet)
    if p > (1 - confidenceLevel):
        return True
    else:
        return False


# loop through dataframe and remove all stocks which are not normal
def excludeNonNormal(dataFrame, confidenceLevel):
    dependentVariable = dataFrame.iloc[:, 0]
    dependentVariable = dependentVariable[~np.isnan(dependentVariable)].copy()
    if not isNormal(dependentVariable, confidenceLevel):
        return
    else:
        return dataFrame
