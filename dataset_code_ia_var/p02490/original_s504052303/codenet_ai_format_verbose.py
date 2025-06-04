import sys

def afficher_paires_ordonnees():
    premier_entier, deuxieme_entier = map(int, raw_input().split())

    while [premier_entier, deuxieme_entier] != [0, 0]:
        if premier_entier > deuxieme_entier:
            print deuxieme_entier, premier_entier
        else:
            print premier_entier, deuxieme_entier

        premier_entier, deuxieme_entier = map(int, raw_input().split())

if __name__ == "__main__":
    afficher_paires_ordonnees()