import json
import os

chemin_dossier = os.path.dirname(__file__)
# 01-fichiers/02-json/users.json
chemin_fichier = os.path.join(chemin_dossier, "users.json")
print(chemin_fichier)

fichier = open(chemin_fichier, 'r', encoding='utf-8')
contenu = json.load(fichier) # <- list
# print("Contenu: ", contenu)
# print("Le type de contenu: ", type(contenu) )
# print("Le type de contenu 1: ", type(contenu[0]) )

for utilisateur in contenu: 
    # utilisateur <- dict
    print("nom de l'utilisateur: " + utilisateur.get('name'))
    adresse = utilisateur.get('address')
    if adresse != None:
        print(adresse.get('street'))
    print( utilisateur.get('address').get('geo').get('lng'))
fichier.close()

try:
    fichier = open(chemin_fichier, 'r', encoding='utf-8')
    contenu = json.load(fichier) 
except FileNotFoundError as erreur:
    print("Erreur: ", erreur)
# Si il y a une erreur dans le format du fichier json, on a cette erreur
except json.decoder.JSONDecodeError as jerreur:
    print("Erreur: ", jerreur)
else:
    print(contenu)
    fichier.close()
    
    
chemin_dossier = os.path.dirname(__file__)
chemin_fichier = os.path.join(chemin_dossier, "sortie.json")

with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
    liste = []
    dictionnaire = {"id": 5}
    dictionnaire2 = {
        "id": 7, 
        'adresse': { 
            'ville': 'Paris'
        }
    }
    liste.append(dictionnaire)
    liste.append(dictionnaire2)
    json.dump(liste, fichier, indent=4)
    