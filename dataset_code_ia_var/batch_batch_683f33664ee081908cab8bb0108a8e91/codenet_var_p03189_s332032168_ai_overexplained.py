import sys  # Importe le module sys pour gérer les entrées/sorties avancées
import numpy as np  # Import le module numpy pour les opérations matricielles et de vecteurs

# Lecture des deux premiers entiers de la première ligne de l'entrée standard (stdin)
# map(int, ...) applique la fonction int à chaque élément du résultat de input().split(), ce qui produit une liste de chaînes transformée en entiers.
# input().split() sépare la ligne entrée en une liste de chaînes par espace
n, q = list(map(int, input().split()))  # n = nombre d'éléments, q = nombre de requêtes

# Définition d'une constante MOD, un grand nombre premier, souvent utilisé pour éviter les débordements lors de calculs modulaires en informatique.
MOD = 10 ** 9 + 7  # 10 puissance 9 plus 7

# Détermination de l'inverse multiplicatif de 2 modulo MOD.
# (MOD + 1) // 2 est toujours l'inverse modulaire de 2 quand MOD est impair.
INV2 = (MOD + 1) // 2  # Cela permet de "diviser par 2" tout en restant dans l'arithmétique modulaire

# Lecture de toutes les lignes restantes de l'entrée standard via sys.stdin.readlines()
# Cela renvoie une liste de chaînes, chaque chaîne représentant une ligne.
lines = sys.stdin.readlines()

# On lit les n premières lignes représentant les entiers de départ.
# map(int, lines[:n]) transforme chaque ligne en entier.
# np.fromiter permet de créer un array numpy à partir d'un itérable, ici les entiers lus
# dtype=np.int utilise le type entier par défaut de numpy (ce choix peut être générateur d'avertissements dans les nouvelles versions)
aaa = np.fromiter(map(int, lines[:n]), dtype=np.int)

# Construction d'une matrice booléenne puis entière
# aaa.reshape(1, -1) transforme le vecteur aaa en un vecteur ligne (dimension 1 x n)
# aaa.reshape(-1, 1) transforme le vecteur aaa en un vecteur colonne (dimension n x 1)
# En utilisant < sur ces deux tableaux via le broadcasting de numpy, on obtient une matrice de taille n x n
# Chaque élément mat[i][j] vaut True (ou 1) si aaa[i] < aaa[j], sinon False (ou 0)
# .astype(np.int64) convertit les booléens en entiers 64 bits (1 ou 0)
mat = (aaa.reshape(1, -1) < aaa.reshape(-1, 1)).astype(np.int64)

# Pour chaque requête, qui commence à la ligne d'indice n et suivantes dans la liste lines :
for line in lines[n:]:
    # line est une chaîne de caractères contenant deux entiers séparés par un espace
    # map(int, line.split()) convertit ces deux valeurs en entiers dans x et y
    x, y = map(int, line.split())
    # Les indices dans le code sont 0-based, alors qu'on considère souvent des entrées 1-based
    # Donc, on décrémente x et y de 1 pour coller à l'indexation Python
    x -= 1
    y -= 1
    # tmp va contenir la moyenne modulaire des valeurs mat[x, y] et mat[y, x], multipliée par INV2 puis modulo MOD
    # Cela correspond à (mat[x, y] + mat[y, x]) // 2 modulo MOD
    # Ces éléments correspondent à la valeur de la case de la matrice entre x et y dans les deux directions
    tmp = (mat[x, y] + mat[y, x]) * INV2 % MOD
    # On met à jour les lignes x et y de la matrice en faisant la moyenne de leurs anciennes valeurs, puis on applique INV2 et MOD
    mat[x] = mat[y] = (mat[x] + mat[y]) * INV2 % MOD
    # On fait de même pour les colonnes x et y : sont mis à jour comme la moyenne (modulaire) de leurs valeurs actuelles
    mat[:, x] = mat[:, y] = (mat[:, x] + mat[:, y]) * INV2 % MOD
    # On force à 0 les diagonales aux positions [x, x] et [y, y] (aucune auto-boucle dans la matrice)
    mat[x, x] = mat[y, y] = 0
    # On place la valeur calculée précédemment dans les deux sens de la case [x, y] et [y, x]
    mat[x, y] = mat[y, x] = tmp

# Après l'application de toutes les requêtes, on doit calculer la somme de la partie triangulaire supérieure de la matrice
# np.triu(mat) renvoie la matrice triangulaire supérieure de mat, soit tous les éléments mat[i][j] avec i <= j, les autres positions sont zéro
# .sum() fait la somme de tous ces éléments, produisant un scalaire numpy
# On applique MOD pour obtenir le résultat dans l'arithmétique modulaire prévue
ans = int(np.triu(mat).sum() % MOD)

# L'opérateur << q décale ans vers la gauche de q bits, ce qui revient à le multiplier par 2^q
# On applique à nouveau MOD pour maintenir le résultat dans la bonne plage
ans = (ans << q) % MOD

# Affichage du résultat sous forme d'entier sur la sortie standard
print(ans)