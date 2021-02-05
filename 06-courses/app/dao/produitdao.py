import sqlite3
import logging
import os
from metiers.produit import Produit

# os.chdir(os.path.join(os.getcwd(), "courses"))


dir_path = os.getcwd()
file_log_path = os.path.join(dir_path, 'app.log')

if not os.path.exists(dir_path):
    os.mkdir('logs')

logging.basicConfig(
    level=logging.INFO,
    filename=file_log_path,
    filemode='a',
    format="%(asctime)s - [%(levelname)s]: %(filename)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class ProduitDao:
    """Produit Dao permet l'accès à la base de données et la table produits
        Les Data Access Object permettent une couche d'abstraction supplementaire.
       - constructeur pour se connecter
       - méthode create pour insérer un produit
       - méthode read pour lire un produit
       Les variables de classes, DATABASES et PRODUCT_TABLE evite la repitition.
       Si demain je veux changer le nom de ma base de donnée 
       je n'ai que cette variable a modifier """
    DATABASE = "courses.db"
    PRODUCT_TABLE = "produits"
    
    def __init__(self):
        self.__cnx = None
        try:
            self.__cnx = sqlite3.connect(ProduitDao.DATABASE)
            self.__cnx.row_factory = dict_factory
            self._init_table()
        except sqlite3.DatabaseError as e:
            logging.error(e)

    def _init_table(self):  
        cursor = self.__cnx.cursor() 
        logging.info(f"Création de la table {ProduitDao.PRODUCT_TABLE} si inexistante")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id_ INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                quantite TEXT
            )
        """)
        self.__cnx.commit()        
        cursor.close()
        
        
    def add(self, produit):
        """ Insérer produit dans la table produits de la base courses
        """
        logging.info("Ajout de " + produit.__str__() )
        cursor = self.__cnx.cursor()
        insert = "INSERT INTO produits (id_, nom, quantite) VALUES (NULL, :nom, :quantite)"
        # cursor.execute(insert, (produit.nom, produit.quantite))
        
        cursor.execute(insert, produit.__dict__)
        self.__cnx.commit()
        #permet de recuperer le dernier element auto-incrementé dans la bdd 
        produit.id_ = cursor.lastrowid
        cursor.close()
        logging.info(f"{produit.nom} à été inseré dans la table {ProduitDao.PRODUCT_TABLE}")
        return produit
    
    def delete(self, nom):
        """ Supprimer un produit dans la table produits de la base course
        """
        logging.info(f"Suppression du produit {nom}")
        query = f"DELETE FROM {ProduitDao.PRODUCT_TABLE} WHERE nom=?"
        try:
            self.__cnx.execute(query, (nom,))
            self.__cnx.commit()
        except sqlite3.OperationalError as e:
            logging.error(e)
        else:
            logging.info(f"Le produit {nom} à été supprimé de la table produits")
        
    def fake_data(self):
        self.add(Produit(None, "Pomme", 1))
        self.add(Produit(None, "Poire", 6))
        self.add(Produit(None, "Abricot", 12))
        
    def load_products(self):
        """ Récupere les produits dans la table produits de la base courses
        """
        logging.info(f"Récuperation des produits...")
        produits = []
        try:
            query = f"SELECT * FROM {ProduitDao.PRODUCT_TABLE}"
            content = self.__cnx.execute(query).fetchall()
        except sqlite3.Error as e:
            logging.error(e)
        else:
            #pour chaque produit on creer une instance et on l'ajoute dans notre tableaux.
            for p in content:
                produits.append(Produit(**p) )
            logging.info(f"Les produits ont été récupérés dans la table {ProduitDao.PRODUCT_TABLE}")
        return produits
      
    def get_product_by_name(self, nom_produit):
        """ Récupere les produits dans la table produits de la base courses
        """
        logging.info(f"Récuperation du produit {nom_produit} en cours")
        produit = None
        try:
            query = f"SELECT * FROM {ProduitDao.PRODUCT_TABLE} WHERE nom=?"
            content = self.__cnx.execute(query, (nom_produit,)).fetchall()
        except sqlite3.Error as e:
            logging.error(e)
        else:
            if content:
                produit = Produit(**content[0])
                logging.info(f"Le produit {nom_produit} a été récupéré dans la table {ProduitDao.PRODUCT_TABLE}")
        return produit 
    
    def close(self):
        self.__cnx.close()

    def __del__(self):
        self.close()