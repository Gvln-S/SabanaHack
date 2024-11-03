class Nodule:
    noduleStateList = ["nodulo"]
    noduleMorphologyList = ["ovalado", "redondo", "irregular"]

    def __init__(self, containsNodule, morphology):
        self.containsNodule = containsNodule
        self.morphology = morphology

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}"




    
