class Nodule:
    noduleStateList = ["nodulo"]
    noduleNegationBefore=["no hay"]
    noduleConfirmationBefore=["si hay", "hay otro"]
    noduleConfirmationAfter=["cordenada"]
    noduleMorphology = ["ovalado", "ovalada", "irregular" , "redondo"]
    noduleMargin = ["circusnscritos", "microlobulados", "indistintos" , "onscurecidos", "espiculados"]

    def __init__(self, containsNodule, morphology, margin):
        self.containsNodule = containsNodule
        self.morphology = morphology
        self.margin = margin 

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}" f" Margin: {self.margin}"




    
