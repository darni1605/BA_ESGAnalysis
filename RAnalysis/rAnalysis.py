from RAnalysis.FilterData.filterData import nonMultiColList
from RAnalysis.Hypotheses import hypothesis4
from RAnalysis.FilterData.GroupData.splitAccordingToESG import groupInQuantiles, filterESGScores


# group all stocks into a low, medium and high ESG group (according to quantiles) and test outperformance
filteredESGScores = filterESGScores(nonMultiColList)
lowGroup, mediumGroup, highGroup = groupInQuantiles(filteredESGScores)
