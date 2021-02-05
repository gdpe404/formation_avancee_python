import logging

# Les logs permettent d'enregistrer des evenements pour les applications.
# Lorsqu'on construit avec une interface graphique on a pas acces au terminal
# Donc si ca crash chez un utilisateur, on pourra lui demander de nous envoyer
# son fichier de log pour voir où est le problème

# Different niveau de logs: 
# DEBUG: Mode developpement, tracer des variables,fonction etc..
# INFO: Tracer des actions, Engristrement de l'utilisateur, on entre sur le menu
# WARNING: Dectection d'erreur, qui peut entrainer des problemes de fonctionnement
# ERROR: Dectection d'erreur, qui ne fait pas planter le programme tout de suite
# CRITICAL: Erreur, crash du programme

# logging.debug("Attention, erreur !")
# logging.warning("Attention, erreur !")

# os.path.dirname(__file__) ... 

# configuration du logger
logging.basicConfig(
    level=logging.INFO, # niveau a partir duquel ecrire les logs. (par defaut: WARNING)
    filename="app.log", # Chemin vers le fichier
    filemode="a" # mode d'ecriture
)

logging.debug("Attention, erreur !")
logging.warning("Attention, erreur !")
