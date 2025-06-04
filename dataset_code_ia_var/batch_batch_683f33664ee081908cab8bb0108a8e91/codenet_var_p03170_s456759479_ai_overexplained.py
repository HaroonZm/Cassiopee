# Prendre deux entrées séparées par un espace, les convertir en entiers et les attribuer à n et k respectivement.
# 'n' représente le nombre de types de mouvements possibles (c'est-à-dire combien de valeurs différentes on peut prendre de 'a').
# 'k' représente le nombre total de pierres au début du jeu.
n, k = map(int, input().split())

# Prendre la ligne suivante comme input, la découper en éléments, les convertir en entiers et les stocker dans un tuple.
# 'a' représente un tuple contenant les valeurs possibles de pierres que l'on peut retirer à chaque coup (taille n).
a = tuple(map(int, input().split()))

# Créer une liste 'dp' avec une taille de (k + k + 1) éléments, initialisée à None.
# Chaque case de la liste représente un état possible du jeu correspondant au nombre de pierres restantes lors du prochain tour.
# dp[i] = None signifie qu'au moment de ce tour, le joueur qui joue perd si tous les autres mouvements mènent également à None.
# dp[i] = True signifie qu'il existe au moins un mouvement qui mène à la victoire pour le joueur à cet état.
dp = [None] * (k + k + 1)

# Commencer une boucle sur toutes les valeurs possibles de 'opponent_remains' allant de 0 jusqu'à (k-1) inclus.
# Ici, 'opponent_remains' représente le nombre de pierres qui resterait pour l'adversaire après que l'on ait effectué son coup.
for opponent_remains in range(k):
    # Vérifier si la position correspondant à 'opponent_remains' dans dp est None.
    # Cela signifie que l'adversaire perd dans cette configuration, c'est une "position perdante".
    if dp[opponent_remains] is None:
        # Itérer sur chaque possible nombre de pierres que l'on peut prendre, c'est-à-dire sur chaque élément de 'a'.
        for my_take in a:
            # Calculer le nombre de pierres restant après avoir effectué le mouvement 'my_take' à partir de la position 'opponent_remains'.
            # Cela donne l'état où c'est à mon tour de jouer juste après avoir pris 'my_take' pierres.
            my_remains = opponent_remains + my_take
            # Marquer cet état comme une position gagnante (True) pour moi, car je peux forcer mon adversaire à aller sur une case perdante.
            dp[my_remains] = True

# Extraire le résultat pour 'k' pierres, c'est-à-dire la position initiale du jeu avec k pierres.
ans = dp[k]

# Afficher 'First' si la variable 'ans' est True, ce qui signifie que le premier joueur peut garantir la victoire s'il joue parfaitement.
# Sinon, afficher 'Second', ce qui signifie que le deuxième joueur gagne si tous deux jouent parfaitement.
print('First' if ans else 'Second')