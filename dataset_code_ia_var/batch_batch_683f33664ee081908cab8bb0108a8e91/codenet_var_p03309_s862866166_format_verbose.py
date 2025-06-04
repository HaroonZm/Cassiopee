import statistics

nombre_d_elements = int(input())

liste_entiers = list(map(int, input().split()))

liste_corrigee_decalage = [
    valeur_element - indice_element 
    for indice_element, valeur_element in enumerate(liste_entiers)
]

valeur_mediane = int(statistics.median(liste_corrigee_decalage))

liste_sommes_distances = []

for mediane_testee in [
    valeur_mediane - 2, 
    valeur_mediane - 1, 
    valeur_mediane, 
    valeur_mediane + 1, 
    valeur_mediane + 2
]:
    somme_distances_absolues = sum(
        abs(valeur_element - mediane_testee) 
        for valeur_element in liste_corrigee_decalage
    )
    liste_sommes_distances.append(somme_distances_absolues)

cout_minimal = min(liste_sommes_distances)

print(cout_minimal)