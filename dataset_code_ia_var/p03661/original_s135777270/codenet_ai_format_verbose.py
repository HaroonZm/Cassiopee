nombre_entiers = int(input())

liste_entiers = list(map(int, input().split()))

for indice_somme in range(nombre_entiers - 1):
    liste_entiers[indice_somme + 1] = liste_entiers[indice_somme + 1] + liste_entiers[indice_somme]

valeur_difference_minimale = 10 ** 12

for indice_partition in range(nombre_entiers - 1):
    somme_gauche = liste_entiers[indice_partition]
    somme_droite = liste_entiers[-1] - liste_entiers[indice_partition]
    difference_absolue = abs(somme_gauche - somme_droite)
    valeur_difference_minimale = min(valeur_difference_minimale, difference_absolue)

print(valeur_difference_minimale)