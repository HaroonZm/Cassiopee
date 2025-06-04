# Définir une constante qui représente un très grand nombre. Ici, 10 puissance 18 (un 1 suivi de 18 zéros).
# Cela sera utilisé comme une sorte d'infini, pour initialiser des valeurs dans la liste 'l'.
BIG_NUM = 10**18

# Lire une valeur depuis l'entrée standard (généralement le clavier, ou un fichier redirigé).
# Cette valeur représente un entier que l'on convertit avec int().
# Cette variable 'N' représente le nombre d'éléments (par exemple, le nombre de pierres).
N = int(input())

# Lire une ligne depuis l'entrée standard (l'utilisateur fournit tous les éléments sur une seule ligne).
# Cette ligne est séparée en éléments utilisant "split(' ')", 
# ce qui produit une liste de chaînes de caractères (séparateur : espace simple).
# 'map(int, ...)' convertit chaque élément de la liste de chaînes de caractères en un entier.
# Enfin, on met tout cela dans une liste en utilisant 'list()' pour avoir une liste d'entiers dans la variable H.
H = list(map(int, input().split(" ")))

# Créer une liste 'l' de taille N+10, initialisée avec BIG_NUM dans chaque case.
# [BIG_NUM] * (N+10) : l'opérateur * permet de créer une liste contenant N+10 copies de BIG_NUM.
# 'l' va servir comme tableau de mémorisation (DP) pour stocker les coûts minimaux pour atteindre chaque position.
l = [BIG_NUM] * (N+10)

# On initialise la première case de la liste à 0, c'est-à-dire qu'il n'y a pas de coût pour commencer (point de départ).
l[0] = 0

# Boucle for pour itérer sur les indices de 1 jusqu'à N-1 inclus (car range(1, N) donne 1, 2, ..., N-1).
# Cela signifie que chaque itération va traiter la position i, en partant de la deuxième pierre.
for i in range(1, N):
    # Pour chaque pierre i, on veut déterminer le coût minimum pour y arriver.
    # On regarde deux cas possibles :
    # - Venir de la pierre précédente (i-1) : l[i-1] + abs(H[i] - H[i-1])
    #   Cela ajoute au coût pour arriver à i-1 la différence absolue de hauteur entre les pierres i et i-1.
    # - Venir de la pierre avant la précédente (i-2) : l[i-2] + abs(H[i] - H[i-2])
    #   Cela ajoute au coût pour arriver à i-2 la différence absolue de hauteur entre les pierres i et i-2.
    # La fonction min() permet de prendre la solution la moins coûteuse des deux ci-dessus.
    l[i] = min(
        l[i-1] + abs(H[i] - H[i-1]),
        l[i-2] + abs(H[i] - H[i-2]),
    )

# Afficher le résultat final : l[N-1], c'est-à-dire le coût minimal pour atteindre la dernière pierre (position N-1).
# print() affiche la valeur dans la console (ou la sortie standard).
print(l[N-1])