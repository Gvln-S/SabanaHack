import pandas 

from unidecode import unidecode
from findings.Nodule import Nodule

def ExcelData():
    data = pandas.read_excel("./sources/data.xlsx", header = None)
    lastRow = data.last_valid_index()

    studyColum = 3

    for row in range(1, 50):
        studyArray = [ unidecode(word).lower() for word in data.iloc[row, studyColum].split() ]
        print(data.iloc[row, 0], end=' | ')

        # index = index of each word, studyWord = all words in the array
        nodule = Nodule("Null", "Null")
        for index, studyWord in enumerate(studyArray):

            if Nodule.noduleStateList[0] in studyWord:
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

#               beforeText = " ".join(before)
                if 'no' in before:
                    nodule = Nodule("No", "Null")
                elif 'si' in before:
                    nodule = Nodule("Si", "Null")
                    for noduleMorphology in Nodule.noduleMorphologyList:
                        if noduleMorphology in studyWord:
                            nodule = Nodule("Yes", noduleMorphology) 
                        else:
                            nodule = Nodule("Yes", "Null") 
        print(nodule)



