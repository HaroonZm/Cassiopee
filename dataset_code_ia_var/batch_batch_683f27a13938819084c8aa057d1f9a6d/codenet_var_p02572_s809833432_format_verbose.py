nombre_elements = int(input())

liste_entiers = list(map(int, input().split()))

somme_produit = 0

liste_cumulee_modulo = [liste_entiers[0]]

MODULO = 1000000007

for index_element in range(nombre_elements - 1):

    nouvel_element_cumule = (liste_cumulee_modulo[index_element] + liste_entiers[index_element + 1]) % MODULO

    liste_cumulee_modulo.append(nouvel_element_cumule)

    produit_intermediaire = liste_cumulee_modulo[index_element] * (liste_entiers[index_element + 1] % MODULO)

    somme_produit += produit_intermediaire

resultat_final = somme_produit % MODULO

print(resultat_final)