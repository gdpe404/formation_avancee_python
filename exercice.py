###########################################################################################################
# Ajouter Une option importer la liste
# Ajouter une option exporter la liste
###########################################################################################################
import json 
import os

print('Voici le menu:')
print('\t1- Afficher la liste de courses.')
print('\t2- Ajouter un produit à la liste de courses')
print('\t3- Retirer un produit de la liste de course ')
print('\t4- Supprimer toute la liste de courses')
print('\t5- Importer (JSON) une liste de courses')
print('\t6- Exporter (JSON) la liste de courses')
print('\t7- Quitter le programme')

continuer = True
courses = []

while continuer:
    choix = input("Que voulez-vous faire ?")
    if choix == '1':
        if not courses:
            print('La liste est vide')
        else:
            i = 1
            for produit in courses:
                print(f"{i}- {produit.get('nom')} x{produit.get('quantite')}")
                i += 1
    elif choix == '2':
        nom_produit = input('Quel produit voulez-vous ajouter ? ')
        quantite_produit = int(input('Combien en voulez-vous ?'))
        produit = {
            'nom': nom_produit,
            'quantite': quantite_produit
        }
        courses.append(produit)
        print(f"{nom_produit} a bien été ajouté à la liste.")
    elif choix == '3':
        nom_produit = input('Quel produit voulez-vous retirer ? ')
        for produit in courses:
            # print(produit)
            if nom_produit in produit.values():
                courses.remove(produit)
                print(f"{nom_produit} a bien été retiré de la liste.")
        else:
            print(f"{nom_produit} n'est pas dans la liste.")
    elif choix == '4':
        # courses = []
        courses.clear()
        print("La liste a bien été vidée.")
    elif choix == '5':
        nom_fichier = input('Quel est le nom du fichier: ')
        chemin_fichier = os.path.join(
            os.path.dirname(__file__),
            nom_fichier
        )
        if os.path.exists(chemin_fichier):
            try:
                with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                    courses = json.load(fichier)
                    print("La liste a bien été importée")
            except Exception as erreur:
                print(erreur)
        else:
            print('Aucun fichier ne correpsond au chemin: ' + chemin_fichier)
    elif choix == '6':
        nom_fichier = input('Sous quel nom voulez-vous sauvegarder le fichier: ')
        chemin_fichier = os.path.join(
            os.path.dirname(__file__),
            nom_fichier
        )
        try:
            with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
                json.dump(courses, fichier, indent=4)
                print("La liste à ete sauvegardée vers " + chemin_fichier)
        except json.decoder.JSONDecodeError as jerreur:
            print(jerreur)
        except Exception as erreur:
            print(erreur)
    elif choix == '7':
        continuer = False
        print("Au revoir")