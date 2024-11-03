from dataLoader.ExcelLoader import excelData


def findings():
    studyList = excelData()
    
    for studyArray in studyList:
        # index = index of each word, studyWord = all words in the array
        for index, studyWord in enumerate(studyArray):
            if 'nodulo' in studyWord:
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                if 'no' in before or 'no' in after:
                    nodule = 
                    
                elif 'si' in before:
                    print("Encontrado 'si' en 'nódulo' :", before + [studyWord] + after)
