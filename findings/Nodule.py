class Nodule:
    noduleStateList = ["nodulo"]
    noduleMorphologyList = ["ovalado", "redondo", "irregular"]
    noduleConfirmationBefore = ["si hay", "hay otro"]
    noduleConfirmationAfter = ["cordenada"]

    noduleNegationBefore = ["no hay"]

    def __init__(self, containsNodule, morphology):
        self.containsNodule = containsNodule
        self.morphology = morphology

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}"




    
