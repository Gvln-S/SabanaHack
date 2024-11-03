import pandas 

from unidecode import unidecode
from findings.Nodule import Nodule

def ExcelData():
    data = pandas.read_excel("./sources/data.xlsx", header = None)
    lastRow = data.last_valid_index()

    studyColum = 3

    for row in range(1, 950):
        studyArray = [ unidecode(word).lower() for word in data.iloc[row, studyColum].split() ]
        print(data.iloc[row, 0], end=' | ')

        # index = index of each word, studyWord = all words in the array
        nodule = Nodule("Null", "Null")
        for index, studyWord in enumerate(studyArray):

            if Nodule.noduleStateList[0] in studyWord:
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                beforeText = " ".join(before)
                afterText = " ".join(after)
                if 'no hay' in beforeText:
                    nodule = Nodule("No", "Null")
                elif 'si hay' in beforeText or 'hay otro' in beforeText or 'cordenada' in afterText:
                    nodule = Nodule("Yes", "Null")
                    if "ovalado" in afterText or "redondo" in afterText or "irregular" in afterText:
                        nodule = Nodule("Yes", "Hay morfologia") 
                    else:
                        nodule = Nodule("Yes", "Null") 
        print(nodule)



