class Personnage:
    total_personnage = 0    
    def __init__(self, p_nom, p_arme, p_pdv):
        self.nom = p_nom
        self.arme = p_arme
        self.pdv = p_pdv
        Personnage.total_personnage += 1
    
    def description(self):
        message = f"{self.nom} combat avec {self.arme} et a {self.pdv} points de vie"
        return message
        

class Mage(Personnage):
    def __init__(self, p_nom, p_arme, p_pdv, balais):
        super().__init__(p_nom, p_arme, p_pdv)
        self.balais = balais
        
    def description(self):
        message = super().description()
        message += f" et un balais en {self.balais}"
        return message
        
    def combattre(self):
        print("Quelque chose")

m1 = Mage("John", "Epée", 100, "bois")
print(m1.nom)
m1.combattre()

print( m1.description() ) 