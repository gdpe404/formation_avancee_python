import sqlite3

# Si la bdd n'existe pas il va la créer
cnx = sqlite3.connect("formation.db")
curseur = cnx.cursor() # permet d'executer des requetes sur la BDD

#Cretion d'un tableau dans la BDD
curseur.execute("CREATE TABLE IF NOT EXISTS employe (nom TEXT, prenom TEXT")


cnx.close()
