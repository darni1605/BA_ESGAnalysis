import rpy2.robjects.packages as rPackages
from rpy2.robjects.vectors import StrVector

base = rPackages.importr('base')
stats = rPackages.importr('stats')
utils = rPackages.importr('utils')
utils.chooseCRANmirror(ind=1)

packNames = ('ggplot2', 'hexbin', 'lmtest', 'sandwich', 'car')
packagesToInstall = [x for x in packNames if not rPackages.isinstalled(x)]

if packagesToInstall:
    utils.install_packages(StrVector(packagesToInstall))

