from scipy.stats import shapiro


def isNormal(dataSet, confidenceLevel):
    testStat, p = shapiro(dataSet)
    if p > (1 - confidenceLevel):
        return True
    else:
        return False


def excludeNonNormal(dataFrame, confidenceLevel):
    if not isNormal(dataFrame.iloc[:, 0], confidenceLevel):
        return
    else:
        return dataFrame
