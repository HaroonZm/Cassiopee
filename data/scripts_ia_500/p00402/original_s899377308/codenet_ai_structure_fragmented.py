def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def calculer_maximum(liste):
    return max(liste)

def calculer_minimum(liste):
    return min(liste)

def calculer_somme(a, b):
    return a + b

def calculer_division_entiere(valeur, diviseur):
    return valeur // diviseur

def calculer_difference(valeur1, valeur2):
    return valeur1 - valeur2

def afficher_resultat(resultat):
    print(resultat)

def programme_principal():
    n = lire_entier()
    x = lire_liste_entiers()
    maximum = calculer_maximum(x)
    minimum = calculer_minimum(x)
    somme = calculer_somme(maximum, minimum)
    b = calculer_division_entiere(somme, 2)
    diff = calculer_difference(maximum, b)
    afficher_resultat(diff)

programme_principal()