import pandas 

from unidecode import unidecode
from findings.Nodule import Nodule

def excelData():
    data = pandas.read_excel("./sources/data.xlsx", header = None)
    lastRow = data.last_valid_index()

    studyArrayList = []

    studyColum = 3

    for row in range(0, 100):
        studyArray = [ unidecode(word).lower() for word in data.iloc[row, studyColum].split() ]

            # index = index of each word, studyWord = all words in the array
        for index, studyWord in enumerate(studyArray):
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                if Nodule.noduleList[0] in studyWord:
                    beforeText = " ".join(before)
                

                    if  'no hay' in beforeText:
                        nodule = Nodule("No", "")
                        print(data.iloc[row, 0], end=' | ')
                        print(nodule)
                    
                    
                    elif 'si hay' in beforeText:
                        nodule = Nodule("Yes", "")
                        print(data.iloc[row, 0], end=' | ')
                        print(nodule)









