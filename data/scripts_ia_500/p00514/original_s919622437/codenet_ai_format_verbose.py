import math


nombre_lignes, nombre_colonnes, valeur_r = map(int, input().split())

difference_valeur = valeur_r - nombre_lignes * nombre_colonnes


def calcul_combinaison(total_objets, objets_a_choisir):
    if objets_a_choisir < 0 or total_objets < objets_a_choisir:
        return 0
    return math.factorial(total_objets) // math.factorial(objets_a_choisir) // math.factorial(total_objets - objets_a_choisir)


if difference_valeur < 0:
    print(0)
else:
    resultat_combinaison = calcul_combinaison(difference_valeur + nombre_lignes - 1, difference_valeur)
    print(resultat_combinaison)