from dataLoader.ExcelLoader import excelData

from .Nodule import Nodule

def findings():
    studyList = excelData()
    
    for position, studyArray in enumerate(studyList):
        # index = index of each word, studyWord = all words in the array
        for index, studyWord in enumerate(studyArray):
            before = studyArray[max(0, index - 3):index]
            after = studyArray[index + 1:min(len(studyArray), index + 4)]

            if Nodule.noduleList[0] in studyWord:
                beforeText = " ".join(before)
                

                if  'no hay' in beforeText:
                    nodule = Nodule("No", "")
                    print(f"{position+1}", end=' | ')
                    print(nodule)
                    
                    
                elif 'si hay' in beforeText:
                    nodule = Nodule("Yes", "")
                    print(f"{position+1}", end=' | ')
                    print(nodule)


