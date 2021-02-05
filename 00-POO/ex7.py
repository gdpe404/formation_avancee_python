class Employe:
    def __init__(self, nom, prenom, age, date_entree):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.date_entree = date_entree
        
    def __str__(self):
        # print(self.__class__)
        return f"{self.__class__.__name__} {self.nom.upper() } {self.prenom}"

# class Commercial(Employe):

class Vendeur(Employe):
    def __init__(self, nom, prenom, age, date_entree):
        super().__init__(nom, prenom, age, date_entree)
        self.prime = 400
    
    def calculer_salaire(self, CA):
        return (CA * 0.2 + self.prime)

class Manutentionnaire(Employe):
    def __init__(self, *infos_employe): # Tous les arguments sont regroupés pour former un tuple
        print(infos_employe)
        # print(infos_employe[0], infos_employe[1], infos_employe[2], infos_employe[3])
        print(*infos_employe)
        # super().__init__(infos_employe[0], infos_employe[1], infos_employe[2], infos_employe[3])
        super().__init__(*infos_employe)
        self.euros = 65
    
    def calculer_salaire(self, nombre_heures):
        return (nombre_heures * self.euros)


e1 = Employe('Doe', 'John', 63, "2021-02-03")
print(e1)

v1 = Vendeur('Proviste', 'Alain', 32, "2021-01-01")
print(v1)
print( v1.calculer_salaire(20_000) )

m1 = Manutentionnaire('Zarella', 'Maude', 67, "2019-01-01")
print(m1)

salaire = m1.calculer_salaire(70)
print(f"{salaire:.0f}" )

print( m1.__dict__ )