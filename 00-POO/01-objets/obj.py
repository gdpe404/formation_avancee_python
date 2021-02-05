# Les variables stockent des valeurs
# Les fonctions stockent des instructions
# Les objets stockent des variables et/ou des fonctions

prenoms = ["Ella", "Rick", "Maude"]
print(prenoms)

# Liste est un objet
# La methode (fonction) append appartient l'objet liste.
prenoms.append('Alain')


prenom = "Leo"
print( prenom.upper() )

resultat = prenom.startswith('El')
print(resultat)

resultat = prenom.endswith('eo')
print(resultat)

nouvelle_chaine = prenom.replace('Le', 'Paul')
print(nouvelle_chaine)

nouvelle_chaine = prenom.lower()
print(nouvelle_chaine)

print(prenom)

phrase = "Salut {} !"
print(phrase)
resultat = phrase.format(prenom)
print(resultat)