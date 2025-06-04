nombre_elements = int(input())

liste_entiers = list(map(int, input().split()))

prochain_nombre_attendu = 1

compteur_elements_a_supprimer = 0

au_moins_un_element_trouve = False

for element in liste_entiers:

    if element == prochain_nombre_attendu:

        prochain_nombre_attendu += 1

        au_moins_un_element_trouve = True

    else:

        compteur_elements_a_supprimer += 1

if au_moins_un_element_trouve:

    print(compteur_elements_a_supprimer)

else:

    print("-1")