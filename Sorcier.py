import random

class Sorcier:
    def __init__(self,nom,niveau):
        self.nom=nom
        self.niveau=niveau

    def attaquer(self,monstre):
        sorcier_jet=random.randint(1,12)*self.niveau
        monstre_jet=monstre.defendre()
        print(f"vous avez fait {sorcier_jet} et le monstre a fait {monstre_jet}")


        if sorcier_jet >= monstre_jet:
            return True
        else:
            return False