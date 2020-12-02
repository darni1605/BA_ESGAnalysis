import numpy as np

from datetime import datetime
from ImportFilesPackages.ImportFiles import stockReturns_df
from VisualizationInterface.helper.CreateChart import createHighstock


def PerformanceComparisonChart(stock, comparableName, comparableReturns, chartID):
    stockReturns = stockReturns_df[stock]
    stockReturns = stockReturns[~np.isnan(stockReturns)]
    comparableReturns = comparableReturns[~np.isnan(comparableReturns)]
    dataList1 = []
    dataList2 = []
    for key, value in stockReturns.items():
        datetimeObject = datetime.strptime(key, '%Y-%m-%d')
        currentPair = [datetimeObject, 100 * value]
        dataList1.append(currentPair)
    for key, value in comparableReturns.items():
        datetimeObject = datetime.strptime(key, '%Y-%m-%d')
        currentPair = [datetimeObject, 100 * value]
        dataList2.append(currentPair)

    options = {
        'chart': {
            'renderTo': chartID,
            'borderWidth': 1,
            'marginRight': 50,
            'height': 500
        },
        'title': {
            'text': 'Performance Comparison'
        },
        'rangeSelector': {
            'selected': 4
        },
        'yAxis': {
            'labels': {
                'format': '{value}%',
                'align': 'left'
            },
            'plotLines': [{
                'value': 0,
                'width': 2,
                'color': 'silver',
            }],
        },
        'tooltip': {
            'pointFormat': '{series.name}: <b>{point.y:.2f}%</b>'
        },
        'legend': {
            'enabled': True
        }
    }
    listOfDataSets = [stock, dataList1, comparableName, dataList2]
    chart = createHighstock(listOfDataSets, options)
    return chart
