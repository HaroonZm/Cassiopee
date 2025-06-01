import math
def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def trouver_minimum(liste):
    return min(liste)

def trouver_maximum(liste):
    return max(liste)

def calculer_milieu(minimum, maximum):
    return (minimum + maximum) // 2

def calculer_difference_absolue(valeur1, valeur2):
    return abs(valeur1 - valeur2)

def construire_liste_differences(liste, x):
    resultat = []
    for element in liste:
        resultat.append(calculer_difference_absolue(x, element))
    return resultat

def trouver_maximum_liste(liste):
    return max(liste)

def afficher_resultat(valeur):
    print("{:.0f}".format(valeur))

def fonction_principale():
    N = lire_entier()
    a = lire_liste_entiers()
    minimum = trouver_minimum(a)
    maximum = trouver_maximum(a)
    x = calculer_milieu(minimum, maximum)
    b = construire_liste_differences(a, x)
    maximum_b = trouver_maximum_liste(b)
    afficher_resultat(maximum_b)

fonction_principale()