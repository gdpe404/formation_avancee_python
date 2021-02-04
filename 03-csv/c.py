import csv
import os 

chemin_fichier = os.path.join(
    os.path.dirname(__file__),
    'contact.csv'
)

fichier = open(chemin_fichier, 'r', encoding="utf-8")
lecteur_csv = csv.reader(fichier, delimiter=",")
# index = 0
for index,ligne in enumerate(lecteur_csv):
    if index == 0:
        print("Le nom des colonnes: ", ligne)
    print(f"{ligne[1]} {ligne[0]}, habite a {ligne[4]} et a {ligne[3]} ans")
    # index += 1
    
fichier.close()


print(" ___ DictReader ____ ")

fichier = open(chemin_fichier, 'r', encoding="utf-8")
lecteur_csv = csv.DictReader(fichier, delimiter=",")
for ligne in lecteur_csv:
    print(f"{ligne.get('Nom')} {ligne.get('Prenom')}, habite a {ligne.get('Ville')} et a {ligne.get('Age')} ans")
    
fichier.close()

chemin_fichier = os.path.join(
    os.path.dirname(__file__),
    'contact_sortie.csv'
)

fichier = open(chemin_fichier, 'w', encoding="utf-8")
ecrire_csv = csv.writer(
    fichier, 
    delimiter=";", 
    quotechar='"',
    quoting=csv.QUOTE_NONNUMERIC,
    lineterminator="\n"
)
# ecrire_csv.writerow(
#     ['Leo', 'Pahr', 'l.pahr@exemple.fr', 33, 'Montpellier']
# )
# ecrire_csv.writerow(
#     ['Sarah', 'Crosh', 's.crosh@exemple.fr', 72, 'Lille']
# )
ecrire_csv.writerows(
    [
        ['Leo', 'Pahr', 'l.pahr@exemple.fr', 33, 'Montpellier'],
        ['Sarah', 'Crosh', 's.crosh@exemple.fr', 72, 'Lille']
    ]
)
fichier.close()


fichier = open(chemin_fichier, 'w', encoding="utf-8")
fieldnames = ["Prenom", 'Nom', 'Email', 'Age', 'Ville']
ecrire_csv = csv.DictWriter(
    fichier, 
    fieldnames=fieldnames, 
    lineterminator="\n"
)
ecrire_csv.writeheader() # Ecrit le nom des colonnes
ecrire_csv.writerow(
    {'Nom': 'Leo', 'Prenom': 'Pahr', 'Email': 'l.pahr@exemple.fr', 'Age': 33, 
        'Ville': 'Montpellier'}
)

ecrire_csv.writerows(
    [        
        {'Nom': 'Leo', 'Prenom': 'Pahr', 'Email': 'l.pahr@exemple.fr', 'Age': 33, 
            'Ville': 'Montpellier'},
        {'Nom': 'Sarah', 'Prenom': 'Crosh', 'Email': 's.crosh@exemple.fr', 'Age': 72, 
            'Ville': 'Lille'}
    ]
)
d = {}
d['nouvelle_clef'] = 'valeur'