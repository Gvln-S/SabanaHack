import pandas 

from unidecode import unidecode

def excelData():
    data = pandas.read_excel("./sources/data.xlsx", header = None)
    lastRow = data.last_valid_index()

    studyArrayList = []

    studyColum = 3

    for row in range(1, 3):
        studyArray = [ unidecode(word).lower() for word in data.iloc[row, studyColum].split() ]
        studyArrayList.append(studyArray)
               
    return studyArrayList







