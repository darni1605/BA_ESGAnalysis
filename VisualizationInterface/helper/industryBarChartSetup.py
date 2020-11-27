from bs4 import BeautifulSoup as Soup
import numpy as np
from ImportFilesPackages.ImportFiles import barChartData1stLevel, barChartData2ndLevel


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


def createIndustryPercentageTable(level):
    soup = Soup()
    if level == 1:
        htmlString = """
            <tr>
                <th>
                Industry
                </th>
                <th>
                Number of Betas
                </th>
                <th>
                Percentage of Significance
                </th>
            </tr>
            <tr>
                <td>
                Communication Services
                </td>
                 <td>
                     14
                 </td>
                 <td>
                    71.43%
                 </td>
            </tr>
            <tr>
                 <td>
                    Consumer Discretionary
                 </td>
                 <td>
                     26
                 </td>
                 <td>
                    84.62%
                 </td>
            </tr>
            <tr>
                 <td>
                    Consumer Staples
                 </td>
                 <td>
                     15
                 </td>
                 <td>
                    66.67%
                 </td>
            </tr>
            <tr>
                 <td>
                    Energy
                 </td>
                 <td>
                     6
                 </td>
                 <td>
                    66.67%
                 </td>
            </tr>
            <tr>
                 <td>
                  Financials
                 </td>
                 <td>
                     9
                 </td>
                 <td>
                  100.0%
                 </td>
            </tr>
            <tr>
                 <td>
                  Health Care
                 </td>
                 <td>
                     25
                 </td>
                 <td>
                  88.00%
                 </td>
            </tr>
            <tr>
                 <td>
                  Industrials
                 </td>
                 <td>
                     32
                 </td>
                 <td>
                  90.62%
                 </td>
            </tr>
            <tr>
                 <td>
                  Information Technology
                 </td>
                 <td>
                     31
                 </td>
                 <td>
                  83.87%
                 </td>
            </tr>
            <tr>
                 <td>
                  Materials
                 </td>
                 <td>
                     9
                 </td>
                 <td>
                  77.78%
                 </td>
            </tr>
            <tr>
                 <td>
                  Real Estate
                 </td>
                 <td>
                     5
                 </td>
                 <td>
                  100.0%
                 </td>
            </tr>
            <tr>
                 <td>
                  Utilities
                 </td>
                 <td>
                     5
                 </td>
                 <td>
                  80.00%
                 </td>
            </tr>
        """
    if level == 2:
        htmlString = """
        """

    return htmlString

