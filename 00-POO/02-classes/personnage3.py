# Les variables stockent des valeurs
# Les fonctions stockent des instructions
# Les objets stockent des variables(attributs) et/ou des fonctions(méthodes)
# Une classe est le "moule" qui permet de creer(Instanciation) des objets.

class Personnage:
    # Attribut de classe: Variable qui sera partagée par toutes les instances
    total_personnage = 0
    def __init__(self, p_nom, p_arme, p_pdv):
        self.nom = p_nom
        self.arme = p_arme
        self.pdv = p_pdv
        # Personnage.total_personnage = Personnage.total_personnage + 1
        Personnage.total_personnage += 1
    
    def description(self):
        message = f"{self.nom} combat avec {self.arme} et a {self.pdv} points de vie"
        return message
    
    # Méthode de classe
    @classmethod
    def afficher_total_personnage(cls):
        print(f"Il y a actuellement { cls.total_personnage } personnages ")
    # afficher_total_personnage = classmethod(afficher_total_personnage)
    
# faire une annotation
# def ma_fonction(une_fonction)
#     # traitement
#     return une_nouvelle_fonction

p1 = Personnage("John", "Epée", 100)
print(p1.nom)
print( p1.description() )

# print(f"Il y a actuellement { Personnage.total_personnage } personnages ")
Personnage.afficher_total_personnage()

p2 = Personnage("Maude", "Epée Lourde", 150)
print(p2.nom)
print( p2.description() )

# print( Personnage.nom ) <- nom est une variable d'instance, elle depend d'un objet
# print(f"Il y a actuellement { Personnage.total_personnage } personnages ")

print(p2.total_personnage)
Personnage.afficher_total_personnage()