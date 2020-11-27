from scipy.stats import shapiro
import numpy as np

def isNormal(dataSet, confidenceLevel):
    testStat, p = shapiro(dataSet)
    if p > (1 - confidenceLevel):
        return True
    else:
        return False


def excludeNonNormal(dataFrame, confidenceLevel):
    dependentVariable = dataFrame.iloc[:, 0]
    dependentVariable = dependentVariable[~np.isnan(dependentVariable)].copy()
    if not isNormal(dependentVariable, confidenceLevel):
        return
    else:
        return dataFrame
