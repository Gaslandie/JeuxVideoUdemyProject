import random

class Sorcier:
    def __init__(self,nom,niveau):
        self.nom=nom
        self.niveau=niveau

    def attaquer(self,monstre):
        sorcier_jet=random.randint(1,12)*self.niveau
        monstre_jet=random.randint(1,12)*monstre.niveau

        if sorcier_jet >= monstre_jet:
            return True
        else:
            return False