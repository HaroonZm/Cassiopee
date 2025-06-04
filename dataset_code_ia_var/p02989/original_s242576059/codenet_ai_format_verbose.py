nombre_entree = int(input())

liste_entiers = list(map(int, input().split()))

liste_entiers.sort()

indice_central_superieur = nombre_entree // 2
indice_central_inferieur = (nombre_entree - 1) // 2

valeur_centrale_superieure = liste_entiers[indice_central_superieur]
valeur_centrale_inferieure = liste_entiers[indice_central_inferieur]

difference_valeurs_centrales = valeur_centrale_superieure - valeur_centrale_inferieure

print(difference_valeurs_centrales)