import math

def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def calculer_minimum(liste):
    minimum = liste[0]
    for element in liste:
        if element < minimum:
            minimum = element
    return minimum

def calculer_maximum(liste):
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    return maximum

def somme_deux_entiers(a, b):
    return a + b

def division_entiere_avec_arrondi_vers_haut(valeur):
    return math.ceil(valeur)

def soustraction(a, b):
    return a - b

def fonction_principale():
    n = lire_entier()
    a = lire_liste_entiers()
    mn = calculer_minimum(a)
    mx = calculer_maximum(a)
    somme = somme_deux_entiers(mn, mx)
    division = division_entiere_avec_arrondi_vers_haut(somme / 2)
    resultat = soustraction(division, mn)
    print(resultat)

fonction_principale()