nombre_resultats = int(input())
resultats = [0] * nombre_resultats
nombre_elements = int(input())
liste_elements = list(map(int, input().split()))

for indice_element in range(nombre_elements):
    element_cible = liste_elements[indice_element]
    liste_resultat = list(map(int, input().split()))
    for indice_resultat, valeur_resultat in enumerate(liste_resultat):
        if valeur_resultat == element_cible:
            resultats[indice_resultat] += 1
    resultats[element_cible - 1] += len(resultats) - liste_resultat.count(element_cible)

print(*resultats, sep="\n")