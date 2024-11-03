class Nodule:
    noduleStateList = ["nodulo", "masa"]
    noduleNegationBefore=["no hay", "no se eviden", "no se observan"]
    noduleConfirmationBefore=["si hay", "hay otro", "si se eviden", "observo"]
    noduleConfirmationAfter=["cordenada", "calcificado", "de 1mm", "de 2mm", "de 3mm", "de 4mm", "de 5mm", "de 6mm", "de 7mm", "de 8mm", "de 9mm", "de 10mm"]
    noduleMorphology = ["ovalado", "ovalada", "irregular" , "redondo"]
    noduleMargin = ["circusnscritos", "microlobulados", "indistintos" , "onscurecidos", "espiculados"]
    noduleDensity = ["grasa", "hipodenso", "isodenso" , "hiperdenso"]
    noduleMicroCal = ["microcal"]
    noduleBenign = ["cuatanea", "vascular", "pop corn", "gruesa", "leño", "vara", "redondas", "puntiformes", "anulares", "distroficas", "suturas"]
    noduleBirad = ["birad", "bi-rad", "birads", "bi-rads"]


    def __init__(self, containsNodule, morphology, margin, density, microCal, benign, birad):
        self.containsNodule = containsNodule
        self.morphology = morphology
        self.margin = margin 
        self.density = density 
        self.microCal = microCal
        self.benign = benign
        self.birad = birad

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}" f" Margin: {self.margin}" f" Densidad: {self.density}" f" MicroCalsificaciones: {self.microCal}" f" Benigna: {self.benign}" f" Birad: {self.birad}"




    
