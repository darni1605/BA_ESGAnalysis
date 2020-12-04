import numpy as np


# randomly split a df in numberOfFrac sub-dfs
def randomlySplitDf(dataFrame, numberOfFrac):
    shuffledDf = dataFrame.sample(frac=1)
    listOfFrac = np.array_split(shuffledDf, numberOfFrac)

    return listOfFrac


# save the randomly split dfs
def saveRandomSplit(dataFrame, numberOfFrac, filename):
    listOfFrac = randomlySplitDf(dataFrame, numberOfFrac)
    for i in range(0, len(listOfFrac)):
        iterationString = str(i)
        listOfFrac[i].to_csv(r'C:\Users\domin\UniversitaetZuerich\Bachelorarbeit\Raw Data\RandomSamples\''
                             + filename + iterationString + '.csv '
                             , sep=';')
