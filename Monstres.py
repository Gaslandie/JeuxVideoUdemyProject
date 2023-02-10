import random


class Monstre:
    def __init__(self,nom,niveau):
        self.nom=nom
        self.niveau=niveau

    def defendre(self):
        return random.randint(1,12)*self.niveau

class Necromancien(Monstre): #herite des attributs de la class parent
    def __init__(self,magie,nom,niveau):
        super().__init__(nom,niveau) #pourqu'il puisse herité des methodes de la classe parent
        self.magie=magie
    def defendre(self):
        return random.randint(1,12) * (self.niveau + self.magie)

class Dragon(Monstre):
    def __init__(self,nom,niveau):
        super().__init__(nom,niveau)

    def critique(self):
        de=random.randint(1,6)
        if de == 6:
            return True
        else:
            return False

    def defendre(self):
        critique=self.critique()
        if critique:
            return self.boule_de_feu()
        else:
            return self.morsure()

    def boule_de_feu(self):
        print("coup critique")
        return (random.randint(1,12)*self.niveau)*2

    def morsure(self):
        return (random.randint(1,12)*self.niveau)*0.8