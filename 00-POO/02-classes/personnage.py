# Les variables stockent des valeurs
# Les fonctions stockent des instructions
# Les objets stockent des variables et/ou des fonctions
# Une classe est le "moule" qui permet de creer des objets.

# Pour les classes la convention veut qu'on utilise le PascalCase
# ex: NomDeMaClasse
class Personnage:
    # Constructeur: Fonction qui sera utilisée lorsqu'on va creer notre objet
    def __init__(self):
        # On veut creer 3 variables: nom, arme, pdv
        self.nom = "John"
        self.arme = "Epee"
        # p1.pdv = 100
        self.pdv = 100


# p1 = Personnage.__init__(p1)
p1 = Personnage()
print(p1.nom)

p1.nom = "Doe"
print(p1.nom)

p2 = Personnage()
p2.nom = "Maude"
print(p2.nom)