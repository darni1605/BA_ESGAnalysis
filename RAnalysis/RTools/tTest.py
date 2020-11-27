import numpy as np
from scipy.stats import ttest_1samp, ttest_ind
from RAnalysis.FilterData.testFunctions.testGaussianNormality import isNormal


def oneSampleTTest(arr, testAgainst):
    avg = np.nanmean(arr)
    median = np.nanmedian(arr)
    if isNormal(arr, 0.90):
        tTest = ttest_1samp(arr, testAgainst)
        print('t-statistic = %6.4f pValue = %6.8f' % tTest)
        print('Median: %6.6f' % median)
        print('Average: %6.6f' % avg)
    else:
        print('The sample is not normally distributed.')
        print('Median: %6.6f' % median)
        print('Average: %6.6f' % avg)


# Please note: if one tailed, the first sample is expected to be bigger #
def twoSampleTTest(arr1, arr2, hasEqualVar, isOneTailed):
    avg1 = np.exp(np.nanmean(arr1)) - 1
    avg2 = np.exp(np.nanmean(arr2)) - 1
    median1 = np.exp(np.nanmedian(arr1)) - 1
    median2 = np.exp(np.nanmedian(arr2)) - 1
    tStat, pValue = ttest_ind(arr1, arr2, equal_var=hasEqualVar)
    if isOneTailed:
        pValue = pValue / 2
    print('Average of 1st sample: %6.6f & Average of 2nd sample: %6.6f' % (avg1, avg2))
    print('Median of 1st sample: %6.6f & Median of 2nd sample: %6.6f' % (median1, median2))
    print('t-statistic = %6.4f pValue = %6.4f' % (tStat, pValue))
