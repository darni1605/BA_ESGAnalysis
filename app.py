from bs4 import BeautifulSoup as Soup
from VisualizationInterface.Charts.PerformanceComparison import PerformanceComparisonChart
from ImportFilesPackages.ImportFiles import marketPricesReturns
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


@app.route('/PerformanceComparison')
def performanceComparison(chartID='chart_id'):
    stock = 'AAPL'
    comparableName = 'Market Return'
    comparableReturns = marketPricesReturns['Return']
    chart = PerformanceComparisonChart(stock, comparableName, comparableReturns, chartID)
    chart.save_file(filename='templates/PerformanceComparison')
    soup = Soup(open('templates/PerformanceComparison.html'), 'html.parser')
    htmlToAdd = open('VisualizationInterface/Charts/changeComparison.html')
    for line in htmlToAdd:
        soup.find('body').append(line.strip(""))
        with open('templates/PerformanceComparison.html', 'w') as file:
            file.write(str(soup))
    return render_template('PerformanceComparison.html')


if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True)
