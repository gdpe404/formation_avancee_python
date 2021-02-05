import tkinter
import tkinter.filedialog
import json

def importer_fichier():
    chemin_fichier = tkinter.filedialog.askopenfilename(
        title="Choisir un fichier json",
        # Liste de tuple avec les types de fichiers acceptés
        filetypes=[
            ("Fichiers json", "*.json"),
            ("Tous les fichiers", "*.*")
        ]
    )
    print(chemin_fichier)
    fichier = open(chemin_fichier, 'r', encoding='utf-8')
    utilisateurs = json.load(fichier) # list avec des dictionnaires
    for utilisateur in utilisateurs:
        nom_utilisateur_label = tkinter.Label(win)
        nom_utilisateur_label["text"] = utilisateur.get('name')
        nom_utilisateur_label.pack()
    

win = tkinter.Tk()

# Création du menu
bar_menu = tkinter.Menu()
sous_menu_fichier = tkinter.Menu(tearoff=0) # Par défaut, on peut décrocher le menu
fichier_recent = tkinter.Menu(tearoff=0) # Par défaut, on peut décrocher le menu

sous_menu_fichier.add_command(
    label="Importer un fichier JSON",
    command=importer_fichier
)
sous_menu_fichier.add_command(
    label="Exporter un fichier JSON",
    command=win.destroy
)

fichier_recent.add_command(
    label="Reouvir le fichier fermé",
    command=importer_fichier
)
sous_menu_fichier.add_cascade(label="Fichier recent", menu=fichier_recent)

# Ajout des onglets/sous-menu
bar_menu.add_cascade(label="Fichier", menu=sous_menu_fichier)
bar_menu.add_cascade(label="Editer")

# On configure le menu sur la fenetre principale
win.config(menu=bar_menu)
win.mainloop()