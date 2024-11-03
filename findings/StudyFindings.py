from dataLoader.ExcelLoader import excelData

from .Nodule import Nodule

def findings():
    studyList = excelData()
    
    for studyArray in studyList:
        # index = index of each word, studyWord = all words in the array
        for index, studyWord in enumerate(studyArray):
            if 'nodulo' in studyWord:

                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                print(studyWord)
                before_text = " ".join(before)

                if  'no hay' in before_text:
                    nodule = Nodule("No")
                    print(nodule)
                    
                    
                elif 'si' in before and 'hay' in before:
                    nodule = Nodule("Yes")
                    print(nodule)

                print()

