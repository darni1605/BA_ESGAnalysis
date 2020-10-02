import numpy as np
from scipy.stats import ttest_1samp, ttest_ind


def oneSampleTTest(arr, testAgainst):
    avg = np.exp(np.nanmean(arr)) - 1
    median = np.exp(np.nanmedian(arr)) - 1
    tTest = ttest_1samp(arr, testAgainst)
    print('t-statistic = %6.4f pValue = %6.6f' % tTest)
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
    print('t-statistic = %6.4f pValue = %6.6f' % (tStat, pValue))
    print('Median of 1st sample: %6.6f & Median of 2nd sample: %6.6f' % (median1, median2))
    print('Average of 1st sample: %6.6f & Median of 2nd sample: %6.6f' % (avg1, avg2))
