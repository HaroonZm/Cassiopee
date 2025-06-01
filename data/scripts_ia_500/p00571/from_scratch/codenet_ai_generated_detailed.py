import sys
input = sys.stdin.readline

# N: nombre de pièces d'art
N = int(input())
arts = []

# Lecture des données : chaque pièce avec (taille, valeur)
for _ in range(N):
    A, B = map(int, input().split())
    arts.append((A, B))

# Trie des pièces par taille croissante
arts.sort(key=lambda x: x[0])

# L'idée est de choisir un intervalle contigu d'arts triés par taille
# pour minimiser la différence A_max - A_min (car ce sera la différence
# entre la taille max et min dans cet intervalle) et maximiser la somme
# des valeurs dans cet intervalle pour que S - (A_max - A_min) soit maximal.

# Pour cela, on utilise une technique de deux pointeurs (fenêtres glissantes).
# On fait pointer j le début de l'intervalle et i la fin, tous deux croissants.

ans = -10**18  # Valeur initiale très petite pour max
sum_B = 0  # somme des valeurs dans l'intervalle courant
j = 0

for i in range(N):
    # Ajouter la valeur de la pièce i dans la somme
    sum_B += arts[i][1]

    # Tant que la différence des tailles dépasse une certaine limite,
    # on peut essayer de déplacer j pour minimiser la pénalité
    # Cependant ici on ne minimise pas une contrainte fixe,
    # mais on cherche le max de sum_B - (arts[i][0] - arts[j][0])

    # On teste si en décalant j on peut améliorer la valeur car
    # augmenter la différence (max-min) diminue le résultat.

    # Mais il est plus simple d'essayer toutes les fenêtres possibles en avançant j.

    while j <= i:
        current_val = sum_B - (arts[i][0] - arts[j][0])
        # On essaie de décaler j vers la droite si ça améliore la valeur
        # pour cela on regarde ce qu'on obtiendrait en enlevant arts[j]
        if j < i:
            sum_exclude_j = sum_B - arts[j][1]
            next_val = sum_exclude_j - (arts[i][0] - arts[j+1][0])
            if next_val >= current_val:
                # Enlever arts[j] améliore ou maintient le résultat
                sum_B = sum_exclude_j
                j += 1
                continue
        # Sinon on reste là
        ans = max(ans, current_val)
        break

print(ans)