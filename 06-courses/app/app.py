# GUI: GRaphical User Interface
# IHM : Interface Homme Machine

# tkinter : Tool Kit INTERface
import tkinter
import tkinter.font
import sqlite3
import logging
import os
import json
from dao.produitdao import ProduitDao
from metiers.produit import Produit
import tkinter.messagebox as msgbox
import tkinter.filedialog

produitDao = ProduitDao()


def import_produits():
    file_path = tkinter.filedialog.askopenfilename(
        title="Selectionner le fichier à importer",
        filetypes = [
            ('Fichier Json', '*.json')
        ]
    )
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            courses = json.load(f)
            for produit in courses:
                p = produitDao.get_product_by_name(produit.get('nom'))
                if not p:
                    produitDao.add(Produit(**produit))
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    else:
        update_products_list()
        msgbox.showinfo("Feliciation",
                    "Les produits ont bien été inserés")
    
def export_produits():
    file_ = tkinter.filedialog.asksaveasfile(
        mode='w', 
        defaultextension=".json",
        filetypes = [
            ('Fichier Json', '*.json')
        ]
    )
    if file_ is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    try:
        produits = produitDao.load_products()
        produits = [p.__dict__ for p in produits]
        json.dump(produits, file_, indent=4)
    except Exception as e:
        print(f"Erreur lors de l'ecriture du fichier: {e}")
    else:
        # help(file_)
        msgbox.showinfo("Feliciation",
                    "Les produits ont bien été crées dans " + file_.name)

def update_products_list():
    courses = produitDao.load_products()
    produits_list.delete(0, tkinter.END)
    for produit in courses:
        produits_list.insert(tkinter.END, produit)


def ajouter_produit():
    nom = name_var.get()
    quantite = quantite_var.get()
    # nom = nom_produit_entry.get()
    # quantite = int(quantite_produit_entry.get())
    produit = Produit(None, nom, quantite)
    produit = produitDao.add(produit)
    
    # logging.info(f"{nom} a bien été ajouté à la liste")
    print(f"{nom} a bien été ajouté à la liste")
    update_products_list()


def supprimer_produit():
    index = produits_list.curselection()
    selection = produits_list.get(index)
    print(selection)    
    print(type(selection))    
    parse = selection.split(' ')
    nom_produit = parse[0]
    produitDao.delete(nom_produit)
    update_products_list()


####
# GUI
####
main_window = tkinter.Tk()
main_window.title('Gestionnaire de courses')
main_window.geometry("600x480")

###############
# MENU
###############
menu_bar = tkinter.Menu(main_window)
fichier = tkinter.Menu(menu_bar, tearoff=0)
fichier.add_command(
    label="Importer un JSON",
)
fichier.add_command(
    label="Exporter un JSON",
)

editer = tkinter.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Fichier", menu=fichier)
menu_bar.add_cascade(label="Editer", menu=editer)
main_window.config(menu=menu_bar)

 ##########################
#           GUI           #
###########################

# Menu
menuBar = tkinter.Menu(main_window)
fileMenuItem = tkinter.Menu(menuBar, tearoff=0)
fileMenuItem.add_command(
    label="Importer un fichier", command=import_produits)
fileMenuItem.add_command(
    label="Exporter un fichier", command=export_produits)
menuBar.add_cascade(label="Fichier", menu=fileMenuItem)

main_window.config(menu=menuBar)

data_frame = tkinter.Frame(main_window)

# Les frames sont des panneaux intermediaires sur lesquelles on peut coller des elements
# ils permettent un meilleurs agencement.
produit_frame = tkinter.Frame(data_frame, borderwidth=2, relief=tkinter.GROOVE)

produit_lbl = tkinter.Label(produit_frame, text="Saisir un produit: ", fg="blue")
produit_lbl.pack(side=tkinter.TOP)

# Manipulation Produit
id_frame = tkinter.Frame(produit_frame)
tkinter.Label(id_frame, text="Id:").pack(side=tkinter.LEFT, padx=10, pady=20)
id_var = tkinter.IntVar()
id_entry = tkinter.Entry(id_frame, textvariable=id_var, state="disabled")
id_entry.pack(side=tkinter.LEFT, padx=10, pady=10)
id_frame.pack(side=tkinter.TOP, padx=5, pady=5)
# Nom
name_frame = tkinter.Frame(produit_frame)
tkinter.Label(name_frame, text="Nom:").pack(side=tkinter.LEFT, padx=10, pady=20)
name_var = tkinter.StringVar()
name_entry = tkinter.Entry(name_frame, textvariable=name_var)
name_entry.pack(side=tkinter.LEFT, padx=10, pady=10)
name_frame.pack(side=tkinter.TOP, padx=5, pady=5)
# quantite
quantite_frame = tkinter.Frame(produit_frame)
tkinter.Label(quantite_frame, text="Quantité:").pack(
    side=tkinter.LEFT, padx=10, pady=10)
quantite_var = tkinter.IntVar()
quantite_entry = tkinter.Entry(quantite_frame, textvariable=quantite_var)
quantite_entry.pack(side=tkinter.LEFT, padx=10, pady=10)
quantite_frame.pack(side=tkinter.TOP, padx=5, pady=5)

# Bouton ajouter
add_prod_btn = tkinter.Button(produit_frame, text="Ajouter", command=ajouter_produit)
add_prod_btn.pack(side=tkinter.TOP, padx=5, pady=5)

# Visualisation
visual_frame = tkinter.Frame(data_frame, borderwidth=2, relief=tkinter.GROOVE)
tkinter.Label(visual_frame, text="Liste des produits:",
        fg="blue").pack(side=tkinter.TOP, padx=10, pady=10)
# Produits
produits_list = tkinter.Listbox(visual_frame, selectmode=tkinter.SINGLE)
update_products_list()

update_btn = tkinter.Button(visual_frame, text="Mettre a jour",
                    command=update_products_list)
update_btn.pack(side=tkinter.TOP, padx=5, pady=5)
produits_list.pack(side=tkinter.TOP)
delete_emp_btn = tkinter.Button(
    visual_frame, text="Supprimer", command=supprimer_produit)
delete_emp_btn.pack(side=tkinter.TOP, padx=5, pady=5)

# buttons
buttons_frame = tkinter.Frame(main_window, borderwidth=2, relief=tkinter.GROOVE)

print_btn = tkinter.Button(buttons_frame, text="Imprimer", command=export_produits)
print_btn.pack(side=tkinter.LEFT, padx=5, pady=5)

quit_btn = tkinter.Button(buttons_frame, text="Quitter", command=main_window.destroy)
quit_btn.pack(side=tkinter.LEFT, padx=5, pady=5)
# buttons_frame.pack(side=TOP, padx=5, pady=5)

produit_frame.pack(side=tkinter.LEFT, padx=10, pady=10)
visual_frame.pack(side=tkinter.LEFT, padx=10, pady=10)
data_frame.pack(side=tkinter.TOP, padx=10, pady=10)
buttons_frame.pack(side=tkinter.TOP, padx=10, pady=10)

main_window.mainloop()
