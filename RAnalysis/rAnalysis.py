from ImportFilesPackages.ImportFiles import stockReturns_df
from ImportFilesPackages.IndustrySplit import getIndustry, getStockReturnsPerIndustry
from RAnalysis.RTools.ExtractCoefficients import extractCoefficients, excludeOutliers, extractESGBetas
from RAnalysis.RTools.GenerateModels import createDFModel
from RAnalysis.RTools.PrintRSummary import printAllRegressionSummaries, printStockRegressionSummary, printDataSetSummary
from RAnalysis.RTools.PlotGraphs import histogram, residualDiagram, cooksDistance, probabilityPlot, \
    standardizedResidualDiagram
import numpy as np

from RAnalysis.RTools.StatsFactors import getVIF

#coefficients = extractCoefficients()
#ESGCoeffs = extractESGBetas(coefficients)
#ESGCoeffsWithoutOutliers = excludeOutliers(ESGCoeffs)

#histogramTitle = 'ESG Beta Distribution'
#histogramXAxis = 'Beta'
#histogramYAxis = 'Frequency'
# histogram(ESGCoeffsWithoutOutliers, histogramTitle, histogramXAxis, histogramYAxis)


#appleModel = createDFModel('AAPL')
#cooksDistance(appleModel)

# standardizedResidualDiagram('MMM')

