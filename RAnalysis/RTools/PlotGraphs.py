import matplotlib.pyplot as plot
import numpy as np
import statsmodels.api as sm
from scipy.stats import probplot
import seaborn as sns
from statsmodels.formula.api import ols

from RAnalysis.RTools.GenerateModels import createDFModel


def histogram(dataToPlot, title, xLabel, yLabel):
    plot.hist(dataToPlot, density=True, range=[-0.0005, 0.0005], bins='auto')
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.title(title)
    plot.show()


# make all plots using matplotlib, r plots crash ##

def residualDiagram(stock, columnNrToPlot):
    stockDF = createDFModel(stock)
    y = stockDF.columns[0]
    x1 = stockDF.columns[1]
    x2 = stockDF.columns[2]
    x3 = stockDF.columns[3]
    x4 = stockDF.columns[4]

    model_fit = ols(y + '~' + x1 + '+' + x2 + '+' + x3 + '+' + x4, data=stockDF).fit()
    fig = plot.figure(figsize=(12, 8))
    fig = sm.graphics.plot_regress_exog(model_fit, stockDF.columns[columnNrToPlot], fig=fig)
    fig.show()


def standardizedResidualDiagram(stock):
    stockDF = createDFModel(stock)
    y = stockDF.columns[0]
    x1 = stockDF.columns[1]
    x2 = stockDF.columns[2]
    x3 = stockDF.columns[3]
    x4 = stockDF.columns[4]

    model_fit = ols(y + '~' + x1 + '+' + x2 + '+' + x3 + '+' + x4, data=stockDF).fit()
    model_fitted_y = model_fit.fittedvalues
    model_norm_residuals = model_fit.get_influence().resid_studentized_internal
    model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))

    srPlot = plot.figure(figsize=(20, 15))

    plot.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5)
    sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt,
                scatter=False,
                ci=False,
                lowess=True,
                line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
    srPlot.axes[0].set_title('Scale Location')
    srPlot.axes[0].set_xlabel('Fitted values')
    srPlot.axes[0].set_ylabel('$\\sqrt{|Standardized Residuals|}$')

    abs_sq_norm_resid = np.flip(np.argsort(model_norm_residuals_abs_sqrt), 0)
    abs_sq_norm_resid_top_3 = abs_sq_norm_resid[:3]

    for i in abs_sq_norm_resid_top_3:
        srPlot.axes[0].annotate(i,
                                xy=(model_fitted_y[i],
                                    model_norm_residuals_abs_sqrt[i]))
    plot.show()

def cooksDistance(dataFrame):
    y = dataFrame.columns[0]
    x1 = dataFrame.columns[1]
    x2 = dataFrame.columns[2]
    x3 = dataFrame.columns[3]
    x4 = dataFrame.columns[4]

    model = ols(y + '~' + x1 + '+' + x2 + '+' + x3 + '+' + x4, data=dataFrame).fit()
    fig = plot.figure(figsize=(20, 15))
    fig = sm.graphics.influence_plot(model, fig=fig)
    fig.show()


def probabilityPlot(stock, factorToPlot):
    stockDF = createDFModel(stock)
    probplot(stockDF[factorToPlot], dist='norm', plot=plot)
    plot.show()
