import pandas 
import tkinter as tk
from tkinter import ttk
from unidecode import unidecode
from findings.Nodule import Nodule

def ExcelData():
    data = pandas.read_excel("./sources/data.xlsx", header = None)
    lastRow = data.last_valid_index()
    table_data=[]

    studyColum = 3

    for row in range(1, 950):
        studyArray = [ unidecode(word).lower() for word in data.iloc[row, studyColum].split() ]

        # index = index of each word, studyWord = all words in the array
        nodule = Nodule("Null", "Null")
        for index, studyWord in enumerate(studyArray):

            if Nodule.noduleStateList[0] in studyWord:
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                beforeText = " ".join(before)
                afterText = " ".join(after)
                if any(neg in beforeText for neg in Nodule.noduleNegationBefore):
                    nodule = Nodule("No", "Null")
                elif (any(conf in beforeText for conf in Nodule.noduleConfirmationBefore) or 
                    any(conf in afterText for conf in Nodule.noduleConfirmationAfter)):
                    found_morphology = next((morph for morph in Nodule.noduleMorphologyAfter if morph in studyArray), None)
            
                    if found_morphology:
                        nodule = Nodule("Yes", found_morphology)
                    else:
                        nodule = Nodule("Yes", "Null") 
        table_data.append((data.iloc[row, 0], nodule.containsNodule, nodule.morphology))
    return table_data    


def create_table():
    root = tk.Tk()
    root.title("Datos estructurados")
    root.geometry("500x400")
    tree = ttk.Treeview(root, columns=("ID", "Nodulo","Morphology"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nodulo", text="Nodulo")
    tree.heading("Morphology", text="Monrphology")
    data = ExcelData()
    for row in data:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")
    root.mainloop()

create_table()
