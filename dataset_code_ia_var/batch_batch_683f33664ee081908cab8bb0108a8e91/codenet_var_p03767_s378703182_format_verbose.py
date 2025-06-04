nombre_entiers = int(input())

liste_entiers = list(map(int, input().split()))

liste_entiers.sort(reverse=True)

somme_valeurs_selectionnees = 0

for indice in range(nombre_entiers):

    position_valeur = 2 * indice + 1

    somme_valeurs_selectionnees += liste_entiers[position_valeur]

print(somme_valeurs_selectionnees)