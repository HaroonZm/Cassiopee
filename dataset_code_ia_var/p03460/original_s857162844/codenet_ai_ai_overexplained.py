from itertools import accumulate          # Importe accumulate, qui permet de faire des sommes cumulées sur des listes
from operator import add                  # Importe add, une fonction qui additionne deux valeurs (a+b)

N, K = map(int, input().split())          # Lit une ligne de l'entrée, la sépare en deux chaînes, puis les convertit en entiers; N est le nombre de points, K est un paramètre du problème

L = 2 * K                                 # Définit L comme deux fois K, cela va servir de taille à une grille/plateau

# Crée une matrice Map de taille LxL initialisée à 0
# La syntaxe [[0]*L for i in range(L)] fabrique une liste de L éléments, où chaque élément est une liste contenant L zéros
Map = [[0] * L for i in range(L)]

# Boucle pour lire les coordonnées et la couleur de chaque point donné dans l'entrée
for i in range(N):                                            
    x, y, c = input().split()              # Lit une ligne, la coupe en 3 chaînes: x, y sont les coordonnées, c est la couleur ("B" ou "W")
    x, y = int(x), int(y)                  # Transforme x et y en entiers (par défaut tout ce qui vient de input() est du texte)
    if c == "W":                           # Si le point est de couleur blanche
        x -= K                             # On retranche K à la coordonnée x; c'est un décalage spécifique au problème
    x, y = x % L, y % L                    # On prend x modulo L et y modulo L pour qu'ils restent dans la grille [0, L-1]
    
    if y >= K:                             # Si y est supérieur ou égal à K
        x, y = (x - K) % L, y - K          # On décale aussi x de -K modulo L et y de -K; ceci fait "basculer" le point dans une autre partie de la grille
    
    Map[x][y] += 1                         # Incrémente la cellule [x][y] de la grille de 1
    Map[x][y - K] += -1                    # Décrémente la cellule [x][y-K] de 1 (modifie la ligne/le segment du problème)
    
    if x != K:                             # Si x n'est pas exactement égal à K, on fait d'autres ajustements
        Map[x - K][y - K] += 1             # Incrémente la cellule [x-K][y-K] de la grille de 1
        Map[x - K][y] += -1                # Décrémente la cellule [x-K][y] de 1
    
    if x > K:                              # Si x est strictement supérieur à K (donc plus à droite)
        Map[0][y] += 1                     # Incrémente la première colonne de y de 1
        Map[0][y - K] += -1                # Décrémente la première colonne de y-K de 1

# Calcule d'abord les sommes cumulées ligne par ligne
Map = [list(accumulate(row)) for row in Map]
# zip(*Map) "transpose" la matrice, c'est-à-dire transforme les lignes en colonnes et vice-versa
# Calcule ensuite les sommes cumulées colonne par colonne (en fait sur chaque ancienne colonne)
Map = [list(accumulate(col)) for col in zip(*Map)]
# "Dé-transpose" la matrice pour revenir à la forme ligne/colonne originale
Map = list(map(list, zip(*Map)))

# Cette instruction crée une nouvelle grille (toujours LxL)
# map(add, Map[i][:K], Map[i-K][K:]) additionne, élément à élément, les K premiers éléments de la ligne i avec les K derniers éléments de la ligne i-K
# On fait cela pour chaque i dans [0, L-1]; cela produit une nouvelle structure de données avec les bons scores
Map = [list(map(add, Map[i][:K], Map[i - K][K:])) for i in range(L)]

# Calcul du maximum global parmi toutes les lignes de la matrice
# map(max, Map) trouve le maximum de chaque ligne; max trouve ainsi le maximum de la matrice entière
print(max(map(max, Map)))                  # Affiche ce maximum final, qui est la réponse au problème