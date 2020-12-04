import pandas as pd
import glob


# after saving randomly split stock returns for H4, reimport
path = r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw Data\RandomSamples'
allFiles = glob.glob(path + '/*.csv')

listOfAllFiles = []

for fileName in allFiles:
    df = pd.read_csv(fileName, sep=';', header=0, index_col=0)
    listOfAllFiles.append(df)


randomSampleHighGroupReturns = listOfAllFiles[:10]
randomSampleLowGroupReturns = listOfAllFiles[10:20]
randomSampleMediumGroupReturns = listOfAllFiles[20:]
