###########################
# Splat operator 
###########################

# Fonction qui prend un nombre infinie d'arguments
def somme(*nombres):
    resultat = 0
    for nombre in nombres:
        resultat += nombre
    print(resultat)    

somme(1)
somme(1,3,5)
somme(1,3,5,9,10)

print("Salut", 5, "salut")

def soustraction(nombre, nombre2):
    print(nombre - nombre2)

soustraction(5,3)
soustraction(nombre2=3, nombre=5)


print("John","Doe", sep="->")


# Key Word ARGumentS
def test(**kwargs):
    #kwargs -> dict avec tous les parametres nommés
    print(kwargs)
    
test(nom="Salut", age=20) # test({'nom': 'salut', 'age':20})


tuples = ("Maude", "John", "Ella")

# 3 manieres de faire la meme chose
print(tuples[0], tuples[1], tuples[2])
print("Maude", "John", "Ella")
print(*tuples)

print(tuples)


print("John","Doe", sep="->", end="/end/")
print("Maude","Zarella", sep="->", end="/end/")

# produit = {'pomme': 5}
options = {
    'sep': ' x ',
    "end": '\n' # retour a la ligne,
}

# print("John","Doe", sep='->', end="\n")
print()
print("John","Doe", **options)


def multi_return():
    # return (5, 7, 8) <- tuple
    return 5, 7, 8

resultat = multi_return()
print(f'Resultat: {resultat}')
print(f'Type: { type(resultat) }')

# a,b,c = (5,7,8)
# a = 5
# b = 7
# c = 8
a,b,c = multi_return()


# Cas pratique du splat operateur avec notre classe Personnage

class Personnage:
    total_personnage = 0
    
    def __init__(self, nom, arme, pdv=100):
        self.nom = nom
        self.arme = arme
        self.pdv = pdv
        self.index = 0
        Personnage.total_personnage += 1
        print(f"Il y a {Personnage.total_personnage} personnages de crée")

    def __str__(self):
        message = f"{self.nom} combat avec {self.arme} et a {self.pdv} points de vie"
        return message
    
    def __del__(self):
        Personnage.total_personnage -= 1

# Exemple: je lis un fichier json
personnage = {
    "nom": 'John',
    "arme": "Epée",
    "pdv": 100,
}
# Donc je recupere des personnages sous forme de dictionnaire
# Je peux donc faire:

# /!\ il faut que les clefs dans le fichier json soient EXACTEMENT le nom des parametres de la methode 
# __init__().
# def __init__(self, nom, arme, pdv):
# {'nom': blabla, 'arme': blabla, pdv: 300}

p1 = Personnage(**personnage)
# la ligne 28 revient exactement à faire ça:
# p1 = Personnage(nom=personnage.get('nom'), arme=personnage.get('arme'), pdv=personnage.get('pdv'))
del p1


# Exemple réel:
import os 
import json

chemin_dossier = os.path.dirname(__file__) # 11-fichiers/02-json/
chemin_fichier = os.path.join(chemin_dossier, 'personnage.json')

liste_de_personnage = []

try:
    fichier = open(chemin_fichier, 'r', encoding='utf-8')
    contenu = json.load(fichier) # Charge le fichier
except json.decoder.JSONDecodeError as jerror:
    print(f'Erreur dans le format du fichier: {jerror}')
except OSError as error:
    print(f"Erreur: {error}")
else:
    for personnage in contenu:
        p = Personnage(**personnage)
        liste_de_personnage.append(p)
    fichier.close()

for my_personnage in liste_de_personnage:
    print(my_personnage)
    
print(liste_de_personnage[0].__dict__)