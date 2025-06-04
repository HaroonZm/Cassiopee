nombre_total_elements = int(input())

triangle_number_found = False

for suite_length in range(1, 100000):

    triangle_number = suite_length * (suite_length + 1) // 2

    if nombre_total_elements == triangle_number:
        nombre_sous_listes = suite_length + 1
        triangle_number_found = True
        break

if not triangle_number_found:
    print("No")
    exit()

print("Yes")
print(nombre_sous_listes)

sous_listes_tableau = [[] for _ in range(nombre_sous_listes)]

elements_disponibles = list(range(1, nombre_total_elements + 1))
elements_disponibles = elements_disponibles[::-1]

for sous_liste_indice in range(nombre_sous_listes):

    for elem_index in range(sous_liste_indice):
        valeur_a_ajouter = sous_listes_tableau[elem_index][sous_liste_indice - 1]
        sous_listes_tableau[sous_liste_indice].append(valeur_a_ajouter)

    while len(sous_listes_tableau[sous_liste_indice]) != nombre_sous_listes - 1:
        valeur_a_ajouter = elements_disponibles.pop()
        sous_listes_tableau[sous_liste_indice].append(valeur_a_ajouter)

for sous_liste in sous_listes_tableau:
    print(nombre_sous_listes - 1, *sous_liste)