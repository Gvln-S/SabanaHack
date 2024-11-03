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
        nodule = Nodule("Null", "Null", "Null")
        for index, studyWord in enumerate(studyArray):

            if Nodule.noduleStateList[0] in studyWord:
                before = studyArray[max(0, index - 3):index]
                after = studyArray[index + 1:min(len(studyArray), index + 4)]

                beforeText = " ".join(before)
                afterText = " ".join(after)
                if any(neg in beforeText for neg in Nodule.noduleNegationBefore):
                    nodule = Nodule("No", "No", "No")
                elif (any(conf in beforeText for conf in Nodule.noduleConfirmationBefore) or 
                    any(conf in afterText for conf in Nodule.noduleConfirmationAfter)):
                    foundMorphology = next((morph for morph in Nodule.noduleMorphology if morph in studyArray), None)
                    if foundMorphology:
                        nodule = Nodule("Yes", foundMorphology, "Null")
                        foundMargin = next((margin for margin in Nodule.noduleMargin if margin in studyArray), None)
                        if foundMargin:
                            nodule = Nodule("Yes", foundMorphology, foundMargin)

                    else:
                        nodule = Nodule("Yes", "Null", "Null") 
        table_data.append((data.iloc[row, 0], nodule.containsNodule, nodule.morphology, nodule.margin))
    return table_data    


def create_table():
    root = tk.Tk()
    root.title("Datos estructurados")
    root.geometry("700x800")
    tree = ttk.Treeview(root, columns=("ID", "Nodulo","Morphology", "Margin"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nodulo", text="Nodulo")
    tree.heading("Morphology", text="Monrphology")
    tree.heading("Margin", text="Margin")
    data = ExcelData()
    for row in data:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")
    root.mainloop()

create_table()
