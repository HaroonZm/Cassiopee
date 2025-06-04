# On lit la taille de la séquence S
n = int(input())
# On lit la séquence S et on la stocke dans une liste
S = list(map(int, input().split()))
# On lit la taille de la séquence T
q = int(input())
# On lit la séquence T
T = list(map(int, input().split()))

# Pour une recherche efficace, on convertit la liste S en un ensemble (set)
# Cela permet une recherche en complexité O(1) par élément de T
set_S = set(S)

# On initialise un compteur pour compter le nombre d'éléments de T présents dans S
count = 0

# Pour chaque élément de T, on vérifie s'il existe dans set_S
for x in T:
    if x in set_S:
        count += 1

# On affiche le résultat
print(count)