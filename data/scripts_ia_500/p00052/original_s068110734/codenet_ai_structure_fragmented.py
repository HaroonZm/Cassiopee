import math

def lire_entier():
    return int(input())

def condition_arret(n):
    return n == 0

def calculer_puissance(base, exposant):
    return base ** exposant

def calculer_division_entiere(n, diviseur):
    return n // diviseur

def calculer_somme_divisions(n):
    s = 0
    for i in range(1, 7):
        puissance = calculer_puissance(5, i)
        division = calculer_division_entiere(n, puissance)
        s += division
    return s

def afficher_resultat(s):
    print(s)

def boucle_principale():
    v = 0
    while True:
        n = lire_entier()
        if condition_arret(n):
            break
        s = calculer_somme_divisions(n)
        afficher_resultat(s)

boucle_principale()