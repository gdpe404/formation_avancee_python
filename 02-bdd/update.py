import sqlite3

cnx = sqlite3.connect("formation.db")
curseur = cnx.cursor()

# UPDATE mon_tzbleau SET champ1='nouvelle-valeur', champs2 etc.
curseur.execute("""
    UPDATE emplye SET nom=:lastname, prenom=:firstname WHERE nom 



""")

curseur.close()
cnx.close()