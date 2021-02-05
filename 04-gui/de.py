import tkinter
import random

def lancer_le_de():
    nombre = random.randint(1, 6)
    resultat.set(f"Resultat: {nombre}")
    # resultat = f"Resultat: {nombre}"
    # resultat_label["text"] = f"Resultat: {nombre}" 
    # resultat_label2["text"] = f"Resultat: {nombre}" 

fenetre_principal = tkinter.Tk()
fenetre_principal.title("Lancer de dé")
fenetre_principal.geometry("300x150")

resultat = tkinter.StringVar(value="Aucun résultat")
# resultat = "Aucun résultat"

resultat_label = tkinter.Label(fenetre_principal, textvariable=resultat)
resultat_label["bg"] = "red"
# padx: laisse une marge sur l'axe x
# ipadx: laisse une marge interne sur l'axe x
resultat_label.pack(side=tkinter.LEFT, padx=16, ipadx=20)

resultat_label2 = tkinter.Label(fenetre_principal, textvariable=resultat)
resultat_label2.pack()

# resultat_label = tkinter.Label(fenetre_principal, text="Aucun Résultat")
# resultat_label.pack()

# resultat_label2 = tkinter.Label(fenetre_principal, text="Aucun Résultat")
# resultat_label2.pack()

# Les fonction sont des objets "callable"
print( lancer_le_de )

# Lorsqu'on va appuyer sur le bouton. Le bouton executera la fonction
start_btn = tkinter.Button(
    fenetre_principal, 
    text="Lancer le dé",
    command=lancer_le_de
)
start_btn.pack()

fenetre_principal.mainloop()