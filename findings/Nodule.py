class Nodule:
    noduleList = ["nodulo"]

    noduleListValue = ["si hay", "no hay"]

    def __init__(self, containsNodule, morfologia):
        self.containsNodule = containsNodule
        self.morfologia = morfologia 

    def __str__(self):
        return f"Nodule: {self.containsNodule}"




    
