# Demande à l'utilisateur d'entrer un entier N via la fonction input()
# input() lit une ligne de texte depuis la console (par défaut)
# int() convertit la chaîne obtenue en entier décimal
N = int(input())

# Demande à l'utilisateur d'entrer une séquence d'entiers séparés par des espaces
# La première input() lit la ligne sous forme de chaîne de caractères
# split() découpe cette chaîne en une liste de sous-chaînes (ici séparées par des espaces)
# map(int, ...) applique la fonction int à chaque sous-chaîne pour la convertir en entier
# list(...) construit finalement une liste de tous ces entiers et l'affecte à la variable A
A = list(map(int, input().split()))

# On initialise la variable right à 0
# Cela représentera la borne droite du segment courant sur lequel on va optimiser
right = 0

# Initialisation de sum_n et bit_n à 0
# sum_n servira à garder la somme courante des éléments du segment A[left:right]
# bit_n contiendra le résultat xor (opérateur ^) de ce même segment
sum_n = 0
bit_n = 0

# Initialisation de ans à 0
# ans va servir à compter le nombre total de sous-tableaux qui satisfont la condition donnée
ans = 0

# On boucle sur tous les indices possibles pour le bord gauche du segment (left)
# range(N) va de 0 inclus à N exclus, c'est-à-dire de 0 à N-1
for left in range(N):
    # Cette boucle while vise à avancer le bord droit du segment aussi loin que possible
    # Tant que right reste inférieur à N (pour ne pas sortir du tableau)
    # et que l'élément qu'on voudrait ajouter à ce segment (A[right]) respecte une condition
    # La condition : la somme des éléments + A[right] doit être égale au xor de ces mêmes éléments + A[right]
    # sum_n + A[right] == sum_n ^ A[right]
    # Si la condition est vraie, on peut inclure l'élément A[right]
    while right < N and sum_n + A[right] == sum_n ^ A[right]:
        # On ajoute cet élément à la somme courante
        sum_n += A[right]
        # On fait un xor (^) avec la valeur courante bit_n pour l'actualiser
        bit_n ^= A[right]
        # On avance le bord droit du segment d'un cran vers la droite
        right += 1

    # On a trouvé un segment maximal [left, right)
    # Tous les segments commençant par left (inclus) et se terminant avant right (exclus) sont valides
    # Leur nombre est right - left
    # On ajoute ce nombre à ans
    ans += right - left

    # Maintenant, il faut préparer le prochain tour de boucle pour passer left à left+1
    # Si right et left sont au même endroit, cela signifie qu'on n'a pas avancé right, donc rien à enlever
    if right == left:
        # On avance simplement right d'un cran pour éviter un blocage infini
        right += 1
    else:
        # Sinon, on retire de sum_n et bit_n la valeur de l'élément qui sort du segment (A[left])
        # Cela permet de maintenir l'invariant que sum_n et bit_n représentent bien [left+1, right)
        sum_n -= A[left]
        bit_n ^= A[left]

# Finalement, on affiche le résultat
# print() affiche la valeur contenue dans ans sur la sortie standard (console)
print(ans)