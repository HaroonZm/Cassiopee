nombre_elements = int(input())
nombre_listes = int(input())

liste_principale = list(map(int, input().split()))
compteurs = [0] * nombre_elements

for index_liste in range(nombre_listes):
    liste_courante = list(map(int, input().split()))
    for index_element in range(nombre_elements):
        if liste_principale[index_liste] == liste_courante[index_element]:
            compteurs[index_element] += 1
        else:
            compteurs[liste_principale[index_liste] - 1] += 1

for compteur in compteurs:
    print(compteur)