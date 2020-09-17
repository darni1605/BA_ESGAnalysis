import rpy2.robjects.packages as rPackages
from rpy2.robjects.vectors import StrVector

base = rPackages.importr('base')
lattice = rPackages.importr('lattice')
stats = rPackages.importr('stats')
utils = rPackages.importr('utils')
psych = rPackages.importr('psych')
utils.chooseCRANmirror(ind=1)

packNames = ('ggplot2', 'hexbin', 'lmtest', 'sandwich', 'car', 'psych')
packagesToInstall = [x for x in packNames if not rPackages.isinstalled(x)]

if packagesToInstall:
    utils.install_packages(StrVector(packagesToInstall))

