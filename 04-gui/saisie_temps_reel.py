import tkinter

def afficher_lettre(name, index, mode):
    print(nom_var.get())
    
fenetre_principale = tkinter.Tk()

nom_var = tkinter.StringVar()
nom_var.trace_add("write", afficher_lettre)

nom_entry = tkinter.Entry(fenetre_principale, textvariable=nom_var)
nom_entry.pack()

fenetre_principale.mainloop()