import pandas 
import tkinter as tk
from tkinter import ttk
from unidecode import unidecode
from findings.Nodule import Nodule
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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


def create_table_and_chart():
    root = tk.Tk()
    root.title("Datos Estructurados")
    root.geometry("700x500")

    # Crear y configurar el estilo
    style = ttk.Style()
    style.configure("Treeview",
                    background="lightgrey",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="lightgray")
    style.map("Treeview",
              background=[("selected", "blue")],
              foreground=[("selected", "white")])

    # Crear la tabla
    tree = ttk.Treeview(root, columns=("ID", "Nodulo", "Morphology"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nodulo", text="Nodulo")
    tree.heading("Morphology", text="Morphology")

    # Llenar la tabla con datos
    data = ExcelData()  # Asegúrate de que esta función esté definida y retorne datos válidos
    for row in data:
        tree.insert("", "end", values=row)

    # Ajustar el ancho de las columnas
    tree.column("ID", width=100, anchor='center')
    tree.column("Nodulo", width=200, anchor='w')
    tree.column("Morphology", width=200, anchor='w')

    # Empaquetar el Treeview
    tree.pack(expand=True, fill="both")

    # Contar nodulos "Sí" y "No"
    count_si = sum(1 for row in data if row[1] == "Sí")
    count_no = sum(1 for row in data if row[1] == "No")

    # Crear la gráfica de barras
    fig, ax = plt.subplots()
    ax.bar(['Sí', 'No'], [count_si, count_no], color=['green', 'red'])
    ax.set_ylabel('Cantidad de Nódulos')
    ax.set_title('Comparación de Nódulos: Sí vs No')

    # Integrar la gráfica de barras en la interfaz
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()

create_table_and_chart()
