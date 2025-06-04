nombre_elements = int(input())

liste_entiers = list(map(int, input().split(' ')))

somme_totale = sum(liste_entiers)

somme_courante = liste_entiers[0]

difference_minimale = abs(somme_totale - 2 * somme_courante)

for index_element in range(1, len(liste_entiers) - 1):

    somme_courante += liste_entiers[index_element]

    difference_actuelle = abs(somme_totale - 2 * somme_courante)

    difference_minimale = min(difference_actuelle, difference_minimale)

print(difference_minimale)