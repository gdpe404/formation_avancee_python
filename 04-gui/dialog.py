import tkinter
import tkinter.messagebox

def login():
    mdp = mdp_entry.get()
    print("Mot de passe: " + mdp)
    if mdp == "root":
        tkinter.messagebox.showinfo("Bienvenue !", "Connexion réussie !")
        reponse = tkinter.messagebox.askyesno("Sondage", "Aimez-vous les carottes ?")
        print(reponse)
    else:
        tkinter.messagebox.showerror("Attention !", "Les identifiants sont incorrects")
        
    
fenetre_principal = tkinter.Tk()

#######################
# Le Formulaire
#######################
# Panneau intermediaire pour mieux positionner les éléments entre eux.
form_group_frame = tkinter.Frame(fenetre_principal)

tkinter.Label(form_group_frame, text="Mot de passe").pack(side=tkinter.LEFT)
# Visuellement, ce qu'on saisit est remplacé par le caractere dans show=""
mdp_entry = tkinter.Entry(form_group_frame, show="*")
mdp_entry.pack(side=tkinter.LEFT)

form_group_frame.pack()


#######################
# Les boutons
#######################
btn_group_frame = tkinter.Frame(fenetre_principal)
connexion_btn = tkinter.Button(
    btn_group_frame,
    text="Se connecter",
    command=login
)
connexion_btn.pack(side=tkinter.LEFT)
quit_btn = tkinter.Button(
    btn_group_frame,
    text="Quitter",
    command=fenetre_principal.destroy 
)
quit_btn.pack(side=tkinter.LEFT, padx=20)
btn_group_frame.pack()

fenetre_principal.mainloop()