from highcharts import Highchart, Highstock


def createHighchart(data, options):
    chart = Highchart()
    chart.set_dict_options(options)
    chart.add_data_set(data)
    return chart


def createHighstock(listOfDataSets, options):
    chart = Highstock()
    for i in range(0, len(listOfDataSets), 2):
        chart.add_data_set(listOfDataSets[i + 1], name=listOfDataSets[i])
    chart.set_dict_options(options)
    return chart
