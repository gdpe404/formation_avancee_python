import sqlite3

# Si la bdd n'existe pas il va la créer
cnx = sqlite3.connect("formation.db")
curseur = cnx.cursor() # permet d'executer des requetes sur la BDD

#Cretion d'un tableau dans la BDD
curseur.execute("CREATE TABLE IF NOT EXISTS employe (nom TEXT, prenom TEXT)")

# Inserer un employé dans la BDD
# curseur.execute("INSERT INTO employe (nom, prenom) VALUES ('Doe', 'John')")

# Deuxième méthode insertion via un dictionnaire
employe_variable = {
    'lastname' : "Zarella",
    'firstname' : "Maude" # on pourrait également le passer sous forme de viriable suite à la saisie de l'utlisateur par exmeple
}
#curseur.execute("INSERT INTO employe (nom, prenom) VALUES (:lastname, :firstname)", employe_variable)

# methode insertion avec tuple
employe_tuple= ('Hochet', 'Rick')
curseur.execute("INSERT INTO employe (nom, prenom) VALUES (? , ?)", employe_tuple)

# Lorque lon modifie les colones d'un tableau en BDD il faut sauvengarder les changements
cnx.commit()

cnx.close()
