import numpy as np
from scipy.stats import ttest_1samp
from ImportFilesPackages.ImportFiles import stockReturns_df
from RAnalysis.FilterData.GroupData.splitAccordingToESG import filterReturns
from RAnalysis.RTools.Performance import countOutUnderPerformance
from RAnalysis.RTools.tTest import twoSampleTTest


# functions for H2 and H6

# calculate mean and median of group and industry returns/return
def processLowHighGroups(groupStockReturns, industryReturns):
    avgGroupStockReturns = groupStockReturns.mean(axis=1).copy()
    avgIndustryReturns = industryReturns.mean(axis=1).copy()
    avgGroupStockReturns = avgGroupStockReturns[~np.isnan(avgGroupStockReturns)]
    avgIndustryReturns = avgIndustryReturns[~np.isnan(avgIndustryReturns)]
    avgGroup, medianGroup = getAvgMedianLowHigh(avgGroupStockReturns)
    avgIndustry, medianIndustry = getAvgMedianLowHigh(avgIndustryReturns)

    return avgGroupStockReturns, avgIndustryReturns, avgGroup, medianGroup, avgIndustry, medianIndustry


# calculate average Return --> account for previous log transformation
def getAvgMedianLowHigh(returns):
    averageReturn = np.exp(np.nanmean(returns)) - 1
    medianReturn = np.exp(np.nanmedian(returns)) - 1

    return averageReturn, medianReturn


# conduct the hypothesis test for either high or low groups
def conductHypoTest(group, models, isLow):
    groupStockReturns = stockReturns_df[group]
    industryReturns = filterReturns(models)

    avgGroupReturns, avgIndustryReturns, avgGroup, medianGroup, avgIndustry, medianIndustry \
        = processLowHighGroups(groupStockReturns, industryReturns)

    if isLow:
        percentage = countOutUnderPerformance(groupStockReturns, avgIndustry, greaterThan=False)
        print('\nOne sample test: average returns of low group vs. average comparable return')
        print('Below average group mean return: %6.6f & comparable mean return: %6.6f' % (avgGroup, avgIndustry))
        print('Below average group median return: %6.6f & comparable median return: %6.6f' % (medianGroup,
                                                                                              medianIndustry))
        tTest1 = ttest_1samp(avgGroupReturns, avgIndustry)
        pValue = 1 - tTest1.pvalue / 2
        print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
        print('\nTwo Sample test: average returns low group vs. average comparable returns')
        twoSampleTTest(avgGroupReturns, avgIndustryReturns, False, True)
        print('Percentage of Low group stocks which underperformed the comparable: %6.2f%%' % percentage)
    else:
        percentage = countOutUnderPerformance(groupStockReturns, avgIndustry, greaterThan=True)
        print('\nOne sample test: average returns of high group vs. average comparable return')
        print('Above average group mean return: %6.6f & comparable mean return: %6.6f' % (avgGroup, avgIndustry))
        print('Above average group median return: %6.6f & comparable median return: %6.6f' % (medianGroup,
                                                                                              medianIndustry))
        tTest1 = ttest_1samp(avgGroupReturns, avgIndustry)
        pValue = tTest1.pvalue / 2
        print('t-statistic = %6.3f pValue = %6.4f' % (tTest1.statistic, pValue))
        print('\nTwo Sample test: average returns high group vs. average comparable returns')
        twoSampleTTest(avgGroupReturns, avgIndustryReturns, False, True)
        print('Percentage of High group stocks which outperformed: %6.2f%%' % percentage)
