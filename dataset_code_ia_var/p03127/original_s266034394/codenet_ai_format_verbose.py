nombre_entrees = int(input())

liste_nombres_entiers = list(map(int, input().split()))

from functools import reduce
from fractions import gcd

def calcul_plus_grand_commun_diviseur_liste(liste_de_nombres_entiers):
    return reduce(gcd, liste_de_nombres_entiers)

resultat_pgcd = calcul_plus_grand_commun_diviseur_liste(liste_nombres_entiers)

print(resultat_pgcd)