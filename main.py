import Sorcier
from Monstres import Monstre
import random


def main():
    boucle_de_jeux()


def boucle_de_jeux():
    monstres=[Monstre('Zombi',5),Monstre('Necromancien',12),Monstre('Dragon',80)]
    sorcier=Sorcier.Sorcier('Gandalf',30)
    while True:
        monstre=random.choice(monstres)
        print(f"{monstre.nom} de niveau {monstre.niveau} apparait")
        print("voulez vous {a}ttaquer, {f}uire ou {r}echercher")
        action=input()
        action=action.lower().strip()
        if action=='a':
            resultat=sorcier.attaquer(monstre)
            if resultat:
                print('vous avez gagné')
                monstres.remove(monstre)
                if len(monstres) == 0:
                    print('vous avez gagané la partie!')
                    break
            else:
                print('vous avez perdu')
        elif action=='f':
            print("vous fuiez")
        elif action=='r':
            print("vous observer les monstres autour de vous")
            for mon in monstres:
                print(f"il ya un {mon.nom} de niveau {mon.niveau}")
        else:
            print("on quitte le jeu")
            break

main()
