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
    
    # Renvoie une chaine de caracteres
    def __str__(self):
        message = f"Personnage[nom: {self.nom}, arme: {self.arme}, pdv: {self.pdv}]"
        return message
        # return "Salut !"
        
    # p1 == p3
    def __eq__(self, personnage2):
        isEqual = (self.nom ==  personnage2.nom) # -> True ou False
        return isEqual
    
    # def __gt__(self, obj2) : >
    # def __ge__(self, obj2) : >=
    # def __lt__(self, obj2) : <
    # def __le__(self, obj2) : <=
    # def __ne__(self, obj2) : !=
    
    def __del__(self):
        Personnage.total_personnage -= 1
        

p1 = Personnage("John", "Epée", 100)
# print(p1.__str__() ) <- ce #que fait python lorsqu'on fait: print(p1)
print(p1)

liste = ["Maude", 'Rick']
print( liste.__str__() )


# Mes instances sont des objets modifiable
print( id(p1) )
p2 = p1 
print( id(p2) )
p2.nom = "Leo"

print("p1.nom = " + p1.nom)

# Pour copier un objet, je dois utiliser le module copy
import copy

p2 = copy.deepcopy(p1)
p2.nom = "Maude"
print("p2.nom = " + p2.nom)
print("p1.nom = " + p1.nom)


print("Comparer des objets: ")
# par defaut, python compare les adresses memoire des objets.

p1 = Personnage("John", "Epée", 100)
p2 = Personnage("John", "Epée", 100)
print(p1)
print(p2)
print(p1 == p2) # par defaut: 0x7f3654b1ba90 == 0x7f3654b3fe20
print(p1 == p2) # apres la redefinition de __eq__ : p1.nom == p2.nom

del p1
# print(p1) <- la variable p1 n'existe plus apres


class Period:
    def __init__(self, mois=0, jours=0):
        self.mois = mois
        self.jours = jours

    def __str__(self):
        return f"{self.mois} mois et {self.jours} jours"
    
    def __add__(self, valeur):
        new_period = Period()
        total_jours = self.jours + valeur # 20 + 11 = 31
        # 73 // 30 = 2 et il reste 13
        new_period.mois = self.mois + (total_jours // 30) # 31 // 30 = 1 et il reste 1
        new_period.jours = total_jours % 30 # 31 % 30 = 1 et il reste 1
        return new_period

per1 = Period(1, 20)
print(per1)
per2 = per1 + 11
print(per2)

# +, - , **, // , not, is ... 