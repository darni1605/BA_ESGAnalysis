import numpy as np
from scipy.stats import ttest_1samp, ttest_ind


def oneSampleTTest(arr, testAgainst):
    avg = np.nanmean(arr)
    median = np.nanmedian(arr)
    tTest = ttest_1samp(arr, testAgainst)
    print('t-statistic = %6.3f pValue = %6.4f' % tTest)
    print('Median: ' + str(median))
    print('Average: ' + str(avg))


# Please note: if one tailed, the first sample is expected to be bigger #
def twoSampleTTest(arr1, arr2, hasEqualVar, isOneTailed):
    avg1 = np.nanmean(arr1)
    avg2 = np.nanmean(arr2)
    median1 = np.nanmedian(arr1)
    median2 = np.nanmedian(arr2)
    tStat, pValue = ttest_ind(arr1, arr2, equal_var=hasEqualVar)
    if isOneTailed:
        pValue = pValue / 2
    print('t-statistic = %6.3f pValue = %6.4f' % (tStat, pValue))
    print('Median of 1st sample: %6.6f & Median of 2nd sample: %6.6f' % (median1, median2))
    print('Average of 1st sample: %6.6f & Median of 2nd sample: %6.6f' % (avg1, avg2))
