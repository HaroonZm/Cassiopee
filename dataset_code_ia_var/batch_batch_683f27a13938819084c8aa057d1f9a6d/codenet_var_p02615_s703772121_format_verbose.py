nombre_elements = int(input())

liste_nombres = list(map(int, input().split()))

liste_triee_decroissante = sorted(liste_nombres, reverse=True)

somme_resultat = 0

for index_element in range(1, nombre_elements):

    if index_element < 4:
        somme_resultat += liste_triee_decroissante[index_element - 1]

    elif index_element < 6:
        somme_resultat += liste_triee_decroissante[index_element - 3]

    else:
        indice_divise = index_element // 2
        somme_resultat += liste_triee_decroissante[indice_divise]

print(somme_resultat)