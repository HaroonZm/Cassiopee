nombre_elements = int(input())
nombre_listes = int(input())
liste_references = list(map(int, input().split()))
compteurs = [0 for index_element in range(nombre_elements)]

for index_liste in range(nombre_listes):
    liste_courante = list(map(int, input().split()))
    for index_element in range(nombre_elements):
        if liste_courante[index_element] == liste_references[index_liste]:
            compteurs[index_element] += 1
    compteurs[liste_references[index_liste] - 1] += nombre_elements - liste_courante.count(liste_references[index_liste])

for index_element in range(nombre_elements):
    print(compteurs[index_element])