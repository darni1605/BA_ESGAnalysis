import pandas as pd
from RAnalysis.RTools.ExtractCoefficients import extractCoefficients, extractSummaries, dropOnlyNanColumns
from RAnalysis.RTools.GenerateModels import createDFModel
from RAnalysis.RTools.PrintRSummary import printStockRegressionSummary
from VisualizationInterface.helper.industryBarChartSetup import prepareBarDataSetPerIndustry
from ImportFilesPackages.ImportFiles import *


print(prepareBarDataSetPerIndustry('Communication Services', 2, isMean=True, withoutOutliers=False))
print(prepareBarDataSetPerIndustry('Communication Services', 2, True, True))
print(prepareBarDataSetPerIndustry('Communication Services', 2, False, True))
print(prepareBarDataSetPerIndustry('Communication Services', 2, False, False))

