nombre_elements, nombre_iterations = map(int, input().split())

liste_entiers = list(map(int, input().split()))

liste_maximum_suffixe = [liste_entiers[-1]]

for indice in range(nombre_elements - 2, -1, -1):
    
    maximum_actuel = max(liste_maximum_suffixe[-1], liste_entiers[indice])
    liste_maximum_suffixe.append(maximum_actuel)

liste_maximum_suffixe = liste_maximum_suffixe[::-1]

liste_difference_avec_maximum = [
    liste_maximum_suffixe[indice] - liste_entiers[indice]
    for indice in range(nombre_elements)
]

valeur_difference_maximale = max(liste_difference_avec_maximum)

nombre_elements_difference_maximale = 0

for indice in range(nombre_elements):
    if liste_difference_avec_maximum[indice] == valeur_difference_maximale:
        nombre_elements_difference_maximale += 1

print(nombre_elements_difference_maximale)