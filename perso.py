import random

class Perso:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.level = 1
        self.survey = []
        self.pdv = 100
        self.strength = 10

    def levelUp(self, x):
        self.level += x
        if x == 1:
            print(self.name,"gagne", x, "niveau")
        else:
            print(self.name, "gagne", x, "niveaux")

        print("le niveau de",self.name, "est désormais", self.level)

    Items = ["une trousse de soin", "un fusil", "un slip", "une pièce d'or"]


    def winItem(self, nameItem):
        self.survey.append(nameItem)
        print(self.name,"trouve", nameItem, "il l'ajoute à son sac")

    def loosePdv(self, nbr):
        self.pdv -= nbr
        if nbr == 1:
            print("aie", self.name, "est blessé il perd", nbr, "point vie")
        else:
            print("aie", self.name, "est blessé il perd", nbr, "points de vie")

    def heal(self, nbr):
        self.pdv += nbr





monPerso = Perso("Ragnar", "Chasseur")

print("Bienvenue {}." .format(monPerso.name))
print("{}. se bat contre une chèvre" .format(monPerso.name))
monPerso.loosePdv(3)
monPerso.levelUp(4)
monPerso.winItem("un fusil")
monPerso.winItem("une trousse de soins")
