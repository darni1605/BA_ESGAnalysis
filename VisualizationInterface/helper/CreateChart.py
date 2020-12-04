from highcharts import Highchart, Highstock


# function to create highchart
def createHighchart(data, options, seriesOptions):
    chart = Highchart()
    chart.add_data_set(data[1], name=data[0])
    chart.set_dict_options(options)
    return chart


# function to create highstock (highcharts for stocks)
def createHighstock(listOfDataSets, options):
    chart = Highstock()
    for i in range(0, len(listOfDataSets), 2):
        chart.add_data_set(listOfDataSets[i + 1], name=listOfDataSets[i])
    chart.set_dict_options(options)
    return chart
