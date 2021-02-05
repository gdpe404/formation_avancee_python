# Les variables stockent des valeurs
# Les fonctions stockent des instructions
# Les objets stockent des variables(attributs) et/ou des fonctions(méthodes)
# Une classe est le "moule" qui permet de creer(Instanciation) des objets.

# Pour les classes la convention veut qu'on utilise le PascalCase
# ex: NomDeMaClasse
class Personnage:
    # Constructeur: Fonction qui sera utilisée lorsqu'on va creer notre objet
    def __init__(self, p_nom, p_arme, p_pdv):
        # p1.nom = "John"
        # p2.nom = "Maude"
        self.nom = p_nom
        self.arme = p_arme
        self.pdv = p_pdv
    
    def description(self):
        message = f"{self.nom} combat avec {self.arme} et a {self.pdv} points de vie"
        return message


# p1 est une instance de la classe Personnage
# p1 = Personnage.__init__(p1, "John", "Epée", 100)
p1 = Personnage("John", "Epée", 100)
print(p1.nom)
# Personnage.description(p1)
print( p1.description() )

# p2 = Personnage.__init__(p2, "John", "Epée", 100)
p2 = Personnage("Maude", "Epée Lourde", 150)
print(p2.nom)
# Personnage.description(p2)
print( p2.description() )