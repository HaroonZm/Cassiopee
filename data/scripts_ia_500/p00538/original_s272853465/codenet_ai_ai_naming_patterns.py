nombre_elements = int(input())
liste_valeurs = [int(input()) for _ in range(nombre_elements)]
liste_dp = [0 for _ in range(nombre_elements)]

for index_difference in range(nombre_elements):
    if index_difference % 2 == nombre_elements % 2:
        liste_dp = [liste_dp[(indice + 1) % nombre_elements] if liste_valeurs[indice] > liste_valeurs[(indice + index_difference) % nombre_elements] else liste_dp[indice] for indice in range(nombre_elements)]
    else:
        liste_dp = [max(liste_valeurs[indice] + liste_dp[(indice + 1) % nombre_elements], liste_valeurs[(indice + index_difference) % nombre_elements] + liste_dp[indice]) for indice in range(nombre_elements)]

print(max(liste_dp))