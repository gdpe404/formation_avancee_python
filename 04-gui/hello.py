import tkinter

fenetre_principal = tkinter.Tk()
fenetre_principal.title("Gestionnaire Hello World !") # Titre de la fenetre
fenetre_principal.geometry("600x480") # Largeur x Hauteur

# widget
message_label = tkinter.Label(fenetre_principal, text="Hello World !")
message_label["foreground"] = "red"
# message_label["foreground"] = "#34ebab"
# message_label["text"] = "Super Text !"
message_label.pack()

fenetre_principal.mainloop()