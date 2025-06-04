import sys

def lire_ligne_entree():
    return sys.stdin.readline().strip()

def lire_entier():
    return int(lire_ligne_entree())

def lire_liste_entiers():
    return list(map(int, lire_ligne_entree().split()))

def lire_entiers_separes():
    return map(int, lire_ligne_entree().split())

resultats_minimum_difference_consecutifs = []

while True:
    nombre_elements_sequence = lire_entier()

    if nombre_elements_sequence == 0:
        break

    liste_nombres = lire_liste_entiers()
    liste_nombres.sort()

    valeur_minimale_difference = 100000000

    for indice in range(nombre_elements_sequence - 1):
        difference_consecutifs = abs(liste_nombres[indice] - liste_nombres[indice + 1])
        valeur_minimale_difference = min(valeur_minimale_difference, difference_consecutifs)

    resultats_minimum_difference_consecutifs.append(valeur_minimale_difference)

for valeur_difference_minimale in resultats_minimum_difference_consecutifs:
    print(valeur_difference_minimale)