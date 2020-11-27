import copy

from bs4 import BeautifulSoup as Soup
from VisualizationInterface.Charts.PerformanceComparison import PerformanceComparisonChart
from VisualizationInterface.helper.stockTable import getStockTableInfo
from VisualizationInterface.helper.RegressionChart import getModelString, prepareDataSet
from VisualizationInterface.helper.industryBarChartSetup import prepareBarDataSetPerIndustry
from ImportFilesPackages.ImportFiles import *

from flask import Flask, render_template, request, json

from VisualizationInterface.helper.IndustryMatch import industryMatch

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/PerformanceComparison', methods=['GET', 'POST'])
def PerformanceComparison(chartID='chart1'):
    stock = request.args.get('stock', default='ABBV', type=str)
    comparableType = request.args.get('comparable', default='Market', type=str)
    if comparableType == 'Market':
        comparableName = comparableType
        filteredStockReturns['MeanReturn'] = filteredStockReturns.mean(axis=1)
        comparableReturns = filteredStockReturns['MeanReturn']
    else:
        comparableName, comparableReturns = industryMatch(stock)
    chart = PerformanceComparisonChart(stock, comparableName, comparableReturns, chartID)
    chart.save_file(filename='templates/PerformanceComparison')

    stockMean, stockMedian, comparableMean, comparableMedian, stockESGMean, stockESGMedian, comparableESGMean, \
    comparableESGMedian = getStockTableInfo(stock, comparableReturns, comparableName)


    soup = Soup(open('templates/PerformanceComparison.html'), 'html.parser')
    soup.head.append(soup.new_tag('style', type='text/css'))
    soup.body['style'] = 'background-color:rgb(56 54 54); margin-block-start: 1em; margin-inline-start: 40px; ' \
                         'margin-inline-end: 40px '
    changeComparable = Soup(open('VisualizationInterface/Charts/changeComparison.html'), 'html.parser')
    table = Soup(open('VisualizationInterface/Charts/performanceTable.html'), 'html.parser')
    backButton = Soup(open('VisualizationInterface/Charts/backButton.html'), 'html.parser')
    for element in table:
        soup.find('body').append(copy.deepcopy(element))
    for element in changeComparable:
        soup.find('div', {'id': 'Performance Comparison'}).append(copy.deepcopy(element))
    for element in backButton:
        soup.find('body').append(copy.deepcopy(element))
    html = soup.prettify('utf-8')
    with open('templates/PerformanceComparison.html', 'wb') as file:
        file.write(html)
    return render_template('PerformanceComparison.html', filteredStocks=listOfFilteredStockNames, stock=stock,
                           comparableName=comparableName, stockMean=stockMean, stockMedian=stockMedian,
                           comparableMean=comparableMean, comparableMedian=comparableMedian, stockESGMean=stockESGMean,
                           stockESGMedian=stockESGMedian, comparableESGMean=comparableESGMean,
                           comparableESGMedian=comparableESGMedian)


@app.route('/ESGHistogram', methods=['POST', 'GET'])
def histogramESG():
    distribution = request.args.get('distribution', default='Overall ESG Score', type=str)
    withoutOutliers = request.args.get('withoutOutliers', default=False, type=bool)
    if not withoutOutliers:
        if distribution == 'Overall ESG Score':
            data = esgBetasWithOutliers.values
            dataName = 'ESG Betas with Outliers'
            title = 'Beta Distribution ESG Score'
            tableData = ESGHistogramTableData['ESGWith'].values
        elif distribution == 'Environment Score':
            data = envBetasWithOutliers.values
            dataName = 'Environment Betas with Outliers'
            title = 'Beta Distribution Environment Score'
            tableData = ESGHistogramTableData['EnvWith'].values
        elif distribution == 'Social Score':
            data = socBetasWithOutliers.values
            dataName = 'Social Betas with Outliers'
            title = 'Beta Distribution Social Score'
            tableData = ESGHistogramTableData['SocWith'].values
        elif distribution == 'Governance Score':
            data = govBetasWithOutliers.values
            dataName = 'Governance Betas with Outliers'
            title = 'Beta Distribution Governance Score'
            tableData = ESGHistogramTableData['GovWith'].values
    else:
        if distribution == 'Overall ESG Score':
            data = esgBetasWithoutOutliers.values
            dataName = 'ESG Betas without Outliers'
            title = 'Beta Distribution ESG Score'
            tableData = ESGHistogramTableData['ESGWithout'].values
        elif distribution == 'Environment Score':
            data = envBetasWithoutOutliers.values
            dataName = 'Environment Betas without Outliers'
            title = 'Beta Distribution Environment Score'
            tableData = ESGHistogramTableData['EnvWithout'].values
        elif distribution == 'Social Score':
            data = socBetasWithoutOutliers.values
            dataName = 'Social Betas without Outliers'
            title = 'Beta Distribution Social Score'
            tableData = ESGHistogramTableData['SocWithout'].values
        elif distribution == 'Governance Score':
            data = govBetasWithoutOutliers.values
            dataName = 'Governance Betas without Outliers'
            title = 'Beta Distribution Governance Score'
            tableData = ESGHistogramTableData['GovWithout'].values
    flattenedData = [y for x in data for y in x]
    return render_template('ESGHistogram.html', data=flattenedData, title=title, dataName=dataName, tableData=tableData)


@app.route('/LinearRegressionGraph')
def linearRegressionGraph():
    stock = request.args.get('stock', default='ABBV', type=str)
    level = request.args.get('level', default=1, type=int)
    modelString = str(getModelString(stock, level))
    dataSet = prepareDataSet(stock, level)

    return render_template('LinearRegressionChart.html', stock=stock, modelString=modelString, dataSet=dataSet,
                           stockList1stLevel=json.dumps(listOfStock1stLevel),
                           stockList2ndLevel=json.dumps(listOfStock2ndLevel))


@app.route('/IndustryBetaComparison')
def IndustryBetaComparison():
    level = request.args.get('level', default=1, type=int)
    isMean = request.args.get('MeanMedian', default=True, type=bool)
    withoutOutliers = request.args.get('withoutOutliers', default=False, type=bool)
    soup = Soup(open('templates/IndustryBarChartComparison.html'), 'html.parser')

    if level == 1:
        categories = ['ESG Beta']
        subtitle = 'Overall ESG Score Betas'
        table = Soup(open('VisualizationInterface/Charts/IndustryTable1stLevel.html'), 'html.parser')
    else:
        categories = ['Environment Beta', 'Social Beta', 'Governance Beta']
        subtitle = 'Environment, Social and Governance Score Betas'
        table = Soup(open('VisualizationInterface/Charts/IndustryTable2ndLevel.html'), 'html.parser')

    [element.extract() for element in soup('table')]
    [element.extract() for element in soup('th')]
    [element.extract() for element in soup('tr')]
    [element.extract() for element in soup('td')]

    for element in table:
        soup.find(id='industryComparisonTableContainer').append(copy.deepcopy(element))

    html = soup.prettify('utf-8')
    with open('templates/IndustryBarChartComparison.html', 'wb') as file:
        file.write(html)

    csData = prepareBarDataSetPerIndustry('Communication Services', level, isMean, withoutOutliers)
    cdData = prepareBarDataSetPerIndustry('Consumer Discretionary', level, isMean, withoutOutliers)
    cstData = prepareBarDataSetPerIndustry('Consumer Staples', level, isMean, withoutOutliers)
    eData = prepareBarDataSetPerIndustry('Energy', level, isMean, withoutOutliers)
    fData = prepareBarDataSetPerIndustry('Financials', level, isMean, withoutOutliers)
    hcData = prepareBarDataSetPerIndustry('Health Care', level, isMean, withoutOutliers)
    iData = prepareBarDataSetPerIndustry('Industrials', level, isMean, withoutOutliers)
    infData = prepareBarDataSetPerIndustry('Information Technology', level, isMean, withoutOutliers)
    mData = prepareBarDataSetPerIndustry('Materials', level, isMean, withoutOutliers)
    reData = prepareBarDataSetPerIndustry('Real Estate', level, isMean, withoutOutliers)
    uData = prepareBarDataSetPerIndustry('Utilities', level, isMean, withoutOutliers)

    return render_template('IndustryBarChartComparison.html', categories=json.dumps(categories), subtitle=subtitle,
                           csData=csData, cdData=cdData, cstData=cstData, eData=eData, fData=fData, hcData=hcData,
                           iData=iData, infData=infData, mData=mData, reData=reData, uData=json.dumps(uData))


if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True)
