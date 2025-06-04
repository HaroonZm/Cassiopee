import sys
import math

def lire_entree():
    return sys.stdin

def parser_ligne(ligne):
    return map(int, ligne.split())

def calculer_racine_quadratique_1(a, l):
    return 4 * l * l - a * a

def calculer_racine_quadratique_2(l, x):
    return (l + x) ** 2 - l * l

def extraire_entiers(valeurs):
    a, l, x = valeurs
    return a, l, x

def calculer_partie_1(a, racine_1):
    return a * racine_1 ** 0.5

def calculer_partie_2(l, racine_2):
    return 2 * l * racine_2 ** 0.5

def additionner_parties(partie1, partie2):
    return partie1 + partie2

def diviser_par_quatre(valeur):
    return valeur / 4

def afficher_resultat(resultat):
    print(resultat)

def traiter_ligne(ligne):
    valeurs = parser_ligne(ligne)
    a, l, x = extraire_entiers(valeurs)
    racine_1 = calculer_racine_quadratique_1(a, l)
    racine_2 = calculer_racine_quadratique_2(l, x)
    partie1 = calculer_partie_1(a, racine_1)
    partie2 = calculer_partie_2(l, racine_2)
    somme = additionner_parties(partie1, partie2)
    resultat = diviser_par_quatre(somme)
    afficher_resultat(resultat)

def main():
    lignes = lire_entree()
    for ligne in lignes:
        traiter_ligne(ligne)

main()