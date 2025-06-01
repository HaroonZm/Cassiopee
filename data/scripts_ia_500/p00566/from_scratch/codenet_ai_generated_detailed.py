# Lecture des entrées
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# Initialisation de la valeur minimale à une valeur très grande
min_total_distance = float('inf')

# Parcours de toutes les combinaisons possibles des deux routes principales :
# l'une dans les axes horizontaux (i de 1 à H)
# l'autre dans les axes verticaux (j de 1 à W)
for main_horizontal in range(H):
    for main_vertical in range(W):
        total_distance = 0
        # Calcul pour chaque intersection (i,j)
        for i in range(H):
            for j in range(W):
                # Calcul de la distance à la route principale horizontale
                dist_horizontal = abs(i - main_horizontal)
                # Calcul de la distance à la route principale verticale
                dist_vertical = abs(j - main_vertical)

                # Distance minimale entre l'intersection et la plus proche route principale
                min_dist = min(dist_horizontal, dist_vertical)
                # Pondération par le nombre d'habitants à cette intersection
                total_distance += A[i][j] * min_dist

                # Optimisation : abandonner si la somme dépasse déjà la meilleure trouvée
                if total_distance >= min_total_distance:
                    break
            if total_distance >= min_total_distance:
                break

        if total_distance < min_total_distance:
            min_total_distance = total_distance

# Affichage du résultat final : la somme minimale des distances pondérées
print(min_total_distance)