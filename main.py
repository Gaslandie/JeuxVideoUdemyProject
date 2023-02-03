import Sorcier
import Monstres


def main():
    boucle_de_jeux()


def boucle_de_jeux():
    while True:
        print("voulez vous {a}ttaquer, {f}uire ou {r}echercher")
        action=input()
        action=action.lower().strip()
        if action=='a':
            print("vous attaquez")
        elif action=='f':
            print("vous fuiez")
        elif action=='r':
            print("vous rechercher")
        else:
            print("on quitte le jeu")
            break

main()
