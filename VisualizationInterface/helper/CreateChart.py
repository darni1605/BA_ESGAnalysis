from highcharts import Highchart, Highstock
import highcharts.highcharts.highchart_types


def createHighchart(data, options, seriesOptions):
    chart = Highchart()
    chart.add_data_set(data[1], name=data[0])
    chart.set_dict_options(options)
    return chart


def createHighstock(listOfDataSets, options):
    chart = Highstock()
    for i in range(0, len(listOfDataSets), 2):
        chart.add_data_set(listOfDataSets[i + 1], name=listOfDataSets[i])
    chart.set_dict_options(options)
    return chart
