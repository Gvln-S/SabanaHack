import pandas as pd
import tkinter as tk
from tkinter import ttk
from unidecode import unidecode
from findings.Nodule import Nodule
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import Optional, List, Tuple
from findings.Nodule import Nodule, NoduleConfig

class NoduleAnalyzer:
    def __init__(self, config: NoduleConfig = NoduleConfig()):
        self.config = config
    
    def find_attribute(self, words: List[str], attributes: List[str]) -> Optional[str]:
        """Busca un atributo específico en la lista de palabras"""
        return next((word for word in words if word in attributes), None)
    
    def extract_birad(self, words: List[str], index: Optional[int]) -> Optional[str]:
        if index is None:
            return None
            
        if index + 1 < len(words):
            next_word = words[index + 1]
            return next_word.split(",")[0].split(".")[0].split(":")[0].split(")")[0].split("m")[0]
        return None

    def analyze_text(self, text: str) -> Nodule:
        words = [unidecode(word).lower() for word in text.split()]
        nodule = Nodule()
        
        for i, word in enumerate(words):
            if any(state in word for state in self.config.STATES):
                before = " ".join(words[max(0, i - 9):i])
                after = " ".join(words[i + 1:min(len(words), i + 4)])
                
                if self._is_nodule_confirmed(before, after):
                    nodule = self._process_confirmed_nodule(words)
                elif any(neg in before for neg in self.config.NEGATION_BEFORE):
                    nodule = self._process_negative_nodule(words)
                    
        return nodule

    def _is_nodule_confirmed(self, before: str, after: str) -> bool:
        return (any(conf in before for conf in self.config.CONFIRMATION_BEFORE) or
                any(conf in after for conf in self.config.CONFIRMATION_AFTER))

    def _process_confirmed_nodule(self, words: List[str]) -> Nodule:
        nodule = Nodule(contains_nodule="Yes")
        
        morphology = self.find_attribute(words, self.config.MORPHOLOGY)
        margin = self.find_attribute(words, self.config.MARGIN)
        density = self.find_attribute(words, self.config.DENSITY)
        micro_cal = self.find_attribute(words, self.config.MICRO_CAL)
        benign = self.find_attribute(words, self.config.BENIGN)
        
        birad_index = next((i for i, word in enumerate(words) 
                           if word in self.config.BIRAD), None)
        birad = self.extract_birad(words, birad_index)
        
        if morphology: nodule.morphology = morphology
        if margin: nodule.margin = margin
        if density: nodule.density = density
        if micro_cal: nodule.micro_cal = "Yes"
        if benign: nodule.benign = benign
        if birad: nodule.birad = birad
        
        return nodule

    def _process_negative_nodule(self, words: List[str]) -> Nodule:
        """Procesa un caso donde se niega la presencia de un nódulo"""
        birad_index = next((i for i, word in enumerate(words) 
                           if word in self.config.BIRAD), None)
        birad = self.extract_birad(words, birad_index)
        
        return Nodule(
            contains_nodule="No",
            morphology="No",
            margin="No",
            density="No",
            micro_cal="No",
            benign="No",
            birad=birad if birad else "No"
        )

def process_excel_data(file_path: str, study_column: int = 3) -> List[Tuple]:
    data = pd.read_excel(file_path, header=None)
    analyzer = NoduleAnalyzer()
    table_data = []
    
    for row in range(1, 15001):
        study_text = data.iloc[row, study_column]
        nodule = analyzer.analyze_text(study_text)
        
        table_data.append((
            data.iloc[row, 0],
            *nodule.to_tuple()
        ))
    
    return table_data

def create_table_and_chart():
    root = tk.Tk()
    root.title("Datos estructurados")
    root.geometry("1700x1000")

    style = ttk.Style()
    style.configure("Treeview",
                    background="lightgrey",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="lightgray")
    style.map("Treeview",
              background=[("selected", "blue")],
              foreground=[("selected", "white")])


    tree = ttk.Treeview(root, columns=("ID", "Nodulo","Morphology", "Margin", "Density", "Microcalcificaciones", "Benigno", "BIRAD"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nodulo", text="Nodulo")
    tree.heading("Morphology", text="Monrphology")
    tree.heading("Margin", text="Margin")
    tree.heading("Density", text="Density")
    tree.heading("Microcalcificaciones", text="Microcalcificaciones")
    tree.heading("Benigno", text="Benigno")
    tree.heading("BIRAD", text="BIRAD")
    file_path = "./sources/data.xlsx"
    results = process_excel_data(file_path)
    for row in results:
        tree.insert("", "end", values=row)

    tree.column("ID", width=100, anchor='center')
    tree.column("Nodulo", width=200, anchor='w')
    tree.column("Morphology", width=200, anchor='w')

    tree.pack(expand=True, fill="both")

    count_si = sum(1 for row in results if row[1] == "Yes")
    count_no = sum(1 for row in results if row[1] == "No")

    fig, ax = plt.subplots()
    ax.bar(['Sí', 'No'], [count_si, count_no], color=['green', 'red'])
    ax.set_ylabel('Cantidad de Nódulos')
    ax.set_title('Comparación de Nódulos: Sí vs No')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    root.protocol("WM_DELETE_WINDOW", root.quit)

    root.mainloop()
    root.destroy()

create_table_and_chart()
