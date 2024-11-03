class Nodule:
    noduleStateList = ["nodulo"]
    noduleNegationBefore=["no hay"]
    noduleConfirmationBefore=["si hay", "hay otro"]
    noduleConfirmationAfter=["cordenada"]
    noduleMorphology = ["ovalado", "ovalada", "irregular" , "redondo"]
    noduleMargin = ["circusnscritos", "microlobulados", "indistintos" , "onscurecidos", "espiculados"]
    noduleDensity = ["grasa", "hipodenso", "isodenso" , "hiperdenso"]
    noduleMicroCal = ["microcal"]
    noduleBenign = ["cuatanea", "vascular", "pop corn", "gruesa", "leño", "vara", "redondas", "puntiformes", "anulares", "distroficas", "suturas"]


    def __init__(self, containsNodule, morphology, margin, density, microCal, benign):
        self.containsNodule = containsNodule
        self.morphology = morphology
        self.margin = margin 
        self.density = density 
        self.microCal = microCal
        self.benign = benign

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}" f" Margin: {self.margin}" f" Densidad: {self.density}" f" MicroCalsificaciones: {self.microCal}" f" Benigna: {self.benign}"




    
