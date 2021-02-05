import sqlite3

# Elle existe, donc on va se connecter
cnx = sqlite3.connect("formation.db")
curseur = cnx.cursor()

#  SELECTIONNE TOUTES LES COLONNES DEPUIS MON TABLEAU employe
curseur.execute("SELECT * FROM employe")
# print( curseur.fetchall() ) <- attention au curseur
contenu = curseur.fetchall() # 1 liste avec 3 tuples a l'interieur
print("Contenu: ", contenu)

# curseur.fetchone() 

# for nom, prenom in contenu:
for utilisateur in contenu:
    # print(utilisateur) # <- tuple
    # print(f"Utilisateur {utilisateur[0].upper() } {utilisateur[1]}")
    
    # nom, prenom = ('Zarella', 'Maude')
    nom, prenom = utilisateur
    print(f"Utilisateur {nom.upper() } {prenom}")

# Recupere tous les employe OU le nom est egal a 'Hochet'
curseur.execute("SELECT nom, prenom FROM employe WHERE nom='Hochet'")
resultat = curseur.fetchall() # Meme s'il n'y a qu'une seule valeur qui correpsond
# fecthall() renvoie toujours une liste de tuple
print("Resultat:", resultat)
print(f"Utilisateur {resultat[0][0].upper() } {resultat[0][1]}")

cnx.close()

print("Récuperer des dictionnaires à la place de tuple")

def dict_factory(cursor, row):
    d = {}
    # cursor.description renvoie le nom des colonnes 
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect("formation.db")
con.row_factory = dict_factory
# con.row_factory = sqlite3.Row <- ressemble a dictionnaire mais on ne peut pas faire .get()
# On peut faire uniquement: resultat['nom'] 
cur = con.cursor()
cur.execute("SELECT * FROM employe")
resultat = cur.fetchone()
print(f"Resutat: {resultat}")
print(resultat["nom"], resultat.get('prenom'))

con.close()