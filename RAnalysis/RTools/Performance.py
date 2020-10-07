from scipy.stats import ttest_ind


def countOutUnderPerformance(returns, comparable, greaterThan):
    avgReturnsPerStock = returns.mean(axis=0)
    count = 0
    for stockReturn in avgReturnsPerStock:
        if greaterThan:
            if stockReturn > comparable:
                count += 1
        else:
            if stockReturn < comparable:
                count += 1
    percentageTrue = 100 * count / len(avgReturnsPerStock)
    return percentageTrue


# returnsList1 is the supposedly bigger one if one tailed
def countNumberOfSignificantTTests(returnsList1, returnsList2, significanceLevel, isOneTailed):
    significanceCount = 0
    for returns1 in returnsList1:
        for returns2 in returnsList2:
            tStat, pValue = ttest_ind(returns1, returns2, equal_var=True)
            if isOneTailed:
                pValue = pValue / 2
            if pValue <= significanceLevel:
                significanceCount += 1
    return significanceCount
