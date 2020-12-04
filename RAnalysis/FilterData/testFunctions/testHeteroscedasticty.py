from statsmodels.compat import lzip
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.formula.api import ols


# Breusch-Pagan Test for Heteroscedasticity

# return bool whether model has heteroscedasticity
def hasHeteroscedasticity(dataFrame):
    columns = dataFrame.columns
    f = columns[0] + '~'
    i = 1
    while i < len(columns):
        f += '+' + columns[i]
        i += 1
    try:
        model = ols(formula=f, data=dataFrame).fit()
        bpTest = het_breuschpagan(model.resid, model.model.exog)

        labels = ['LMStatistic', 'LMTestPValue', 'FStatistic', 'FTestPValue']
        resultDict = lzip(labels, bpTest)

        if resultDict[3][1] < 0.05:
            return True
        else:
            return False
    except ValueError:
        pass


# return dataFrame if homoscedastic and None otherwise
def excludeHeteroscedasticity(dataFrame):
    if not hasHeteroscedasticity(dataFrame):
        return dataFrame
    else:
        pass
