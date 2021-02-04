import os

# open(): ouvrir un fichier (chemin) en mode lecture (r) ou en mode ecriture (w ou a)
# En mode ecriture (w): si le fichier n'existe pas, alors il sera crée,
#  sinon le contenu precedent est ecrasé
# En mode ajout (a): si le fichier n'existe pas, alors il sera crée,
#  sinon on ajoute le contenu a la fin du fichier

fichier = open('message.txt', 'a', encoding='utf-8')
fichier.write("Bonjour tout le monde ! é!\n") # <- \n = Retour a ligne
fichier.close()
 
print("Get Current Work Directory : " + os.getcwd() ) 


# '/home/yoles/Bureau/formation_python_appro/01-fichiers/01-txt/message.txt'
chemin_fichier = os.path.join(os.getcwd(), '01-fichiers', '01-txt', 'message.txt')
print(chemin_fichier)

fichier = open(chemin_fichier, 'w', encoding='utf-8')
fichier.write("Bonjour tout le monde ! é!\n") # <- \n = Retour a ligne
fichier.close()

chemin_dossier = os.path.join(os.getcwd(), '01-fichiers', 'messages')
if not os.path.exists(chemin_dossier):
    print("Le dosier n'existe pas")
    os.mkdir(chemin_dossier)
else:
    print("Le dossier existe deja")
    

chemin_dossier = os.path.join(os.getcwd(), '01-fichiers', 'undossier', '02-02-2021')
if not os.path.exists(chemin_dossier):
    os.makedirs(chemin_dossier) # Creer tous les dossiers qui n'existe pas dans le chemin
