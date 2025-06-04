nombre_d_intervenants, nombre_de_criteres = [int(element) for element in input().split(" ")]

liste_des_intervenants = [int(input()) for indice_intervenant in range(nombre_d_intervenants)]

liste_des_criteres = [int(input()) for indice_critere in range(nombre_de_criteres)]

liste_des_votes_par_intervenant = [0 for indice_intervenant in range(nombre_d_intervenants)]

for critere in liste_des_criteres:
    for indice_intervenant in range(nombre_d_intervenants):
        if liste_des_intervenants[indice_intervenant] <= critere:
            liste_des_votes_par_intervenant[indice_intervenant] += 1
            break

indice_intervenant_avec_maximum_de_votes = liste_des_votes_par_intervenant.index(max(liste_des_votes_par_intervenant)) + 1

print(indice_intervenant_avec_maximum_de_votes)