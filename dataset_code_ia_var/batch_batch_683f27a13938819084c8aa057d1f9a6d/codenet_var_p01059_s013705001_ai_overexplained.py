# Lire deux entiers n et m depuis l'entrée standard séparés par un espace
# n représente la taille maximale d'une plage de positions (par exemple 100 pour 1 à 100)
# m représente le nombre d'éléments dans la liste suivante  
n, m = map(int, input().split())

# Lire la liste de m entiers, séparés par des espaces, toujours depuis l'entrée standard
# Ces entiers représentent, par exemple, des positions de lampadaires ou d'obstacles
li = list(map(int, input().split()))

# Calculer les distances entre les éléments pour déterminer la solution désirée
# Première partie : calculer la distance du début (1) au premier élément de la liste li
# li[0] - 1 donne le nombre de positions entre 1 (début) et le premier élément
distance_debut = li[0] - 1

# Deuxième partie : calculer la distance du dernier élément jusqu'à la fin (n)
# n - li[-1] donne le nombre de positions entre le dernier élément et n (fin)
distance_fin = n - li[-1]

# Troisième partie : calculer les distances "au milieu" entre chaque élément consécutif de la liste li
# Pour chaque voisin consécutif (li[i-1], li[i]), calculer l'écart puis diviser par 2 (division entière)
mid_distances = []
for i in range(1, m):  # i commence à 1 et va jusqu'à m-1 (parce que on regarde li[i-1] et li[i])
    ecart = li[i] - li[i-1]  # calculer la différence entre deux positions consécutives
    mid_distance = ecart // 2  # obtenir la moitié de cette différence, division entière
    mid_distances.append(mid_distance)  # ajouter ce résultat à la liste des écarts du "milieu"

# Maintenant, parmi toutes ces distances (début, fin et au milieu), on recherche la valeur maximale
# Cela donne la "plus grande distance minimale" à traiter (en fonction du contexte du problème)
resultat = max(
    distance_debut,           # distance du début à li[0]
    distance_fin,             # distance de li[-1] à la fin
    *mid_distances            # distances intermédiaires entre chaque paire d'éléments consécutifs
)

# Afficher le résultat final à l'utilisateur
print(resultat)