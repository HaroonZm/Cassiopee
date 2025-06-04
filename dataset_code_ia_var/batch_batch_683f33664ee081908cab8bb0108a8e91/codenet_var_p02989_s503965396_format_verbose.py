nombre_de_elements = int(input())

liste_de_dimensions = list(map(int, input().split()))

liste_de_dimensions.sort()

if nombre_de_elements % 2 == 0:
    indice_milieu_superieur = nombre_de_elements // 2
    indice_milieu_inferieur = (nombre_de_elements // 2) - 1
    difference_entre_milieux = liste_de_dimensions[indice_milieu_superieur] - liste_de_dimensions[indice_milieu_inferieur]
    print(difference_entre_milieux)
else:
    indice_milieu = nombre_de_elements // 2
    difference_avec_voisin = liste_de_dimensions[indice_milieu + 1] - liste_de_dimensions[indice_milieu]
    print(difference_avec_voisin)