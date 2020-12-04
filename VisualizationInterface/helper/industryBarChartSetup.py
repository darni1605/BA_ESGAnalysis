from bs4 import BeautifulSoup as Soup
import numpy as np
from ImportFilesPackages.ImportFiles import barChartData1stLevel, barChartData2ndLevel


# prepare data set to be displayed in bar chart for chosen industry, model level, mean or median,
# with or without outliers
def prepareBarDataSetPerIndustry(industry, level, isMean, withoutOutliers):
    barDataSet = []
    if level == 1:
        industryRow = barChartData1stLevel.loc[barChartData1stLevel['Industry'] == industry]
        if not withoutOutliers:
            if isMean:
                barDataSet.append(industryRow['MeanESGBeta'].item())
            else:
                barDataSet.append(industryRow['MedianESGBeta'].item())
        else:
            if isMean:
                barDataSet.append(industryRow['MeanESGBetaWithoutOutliers'].item())
            else:
                print(industryRow['MedianESGBetaWithoutOutliers'].item())
                barDataSet.append(industryRow['MedianESGBetaWithoutOutliers'])
    else:
        industryRow = barChartData2ndLevel.loc[barChartData1stLevel['Industry'] == industry]
        if not withoutOutliers:
            if isMean:
                barDataSet.append(industryRow['MeanEnvBeta'].item())
                barDataSet.append(industryRow['MeanSocBeta'].item())
                barDataSet.append(industryRow['MeanGovBeta'].item())
            else:
                barDataSet.append(industryRow['MedianEnvBeta'].item())
                barDataSet.append(industryRow['MedianSocBeta'].item())
                barDataSet.append(industryRow['MedianGovBeta'].item())
        else:
            if isMean:
                barDataSet.append(industryRow['MeanEnvBetaWithoutOutliers'].item())
                barDataSet.append(industryRow['MeanSocBetaWithoutOutliers'].item())
                barDataSet.append(industryRow['MeanGovBetaWithoutOutliers'].item())
            else:
                barDataSet.append(industryRow['MedianEnvBetaWithoutOutliers'].item())
                barDataSet.append(industryRow['MedianSocBetaWithoutOutliers'].item())
                barDataSet.append(industryRow['MedianGovBetaWithoutOutliers'].item())

    for i in range(0, len(barDataSet)):
        if np.isnan(barDataSet[i]):
            barDataSet[i] = None

    return barDataSet

