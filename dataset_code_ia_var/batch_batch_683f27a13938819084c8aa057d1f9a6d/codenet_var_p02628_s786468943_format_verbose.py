nombre_de_objets, nombre_d_objets_a_selectionner = map(int, input().split())

liste_des_valeurs_des_objets = list(map(int, input().split()))

liste_des_valeurs_des_objets.sort()

somme_des_plus_petites_valeurs_selectionnees = 0

for indice in range(nombre_d_objets_a_selectionner):
    somme_des_plus_petites_valeurs_selectionnees += liste_des_valeurs_des_objets[indice]

print(somme_des_plus_petites_valeurs_selectionnees)