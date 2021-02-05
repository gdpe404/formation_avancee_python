class Produit:
    def __init__(self, id_, nom, quantite):
        self. id_ = id_
        self.nom = nom
        self.quantite = quantite
    
    def __str__(self):
        return f"{self.nom} x{self.quantite}"
    
    def __eq__(self, p2):
        return self.nom == p2.nom