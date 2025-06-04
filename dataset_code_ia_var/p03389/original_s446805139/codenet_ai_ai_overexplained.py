# Définition de la fonction dist qui prend deux arguments x et y
def dist(x, y):
    # On vérifie si x est strictement supérieur à y
    if x > y:
        # Si c'est le cas, on retourne la différence (x-y) : c'est-à-dire le nombre à soustraire de x pour atteindre y
        return x - y
    else:
        # Si x n'est pas supérieur à y (donc x <= y), on calcule d comme étant la différence entre y et x
        d = y - x
        # On vérifie si d est un nombre pair (donc si d modulo 2 est égal à 0)
        if d % 2 == 0:
            # Si d est pair, on retourne la moitié de d, c'est-à-dire une division entière par 2
            return d // 2
        else:
            # Si d est impair (d modulo 2 différent de 0), on retourne la moitié entière de d plus 2 (// signifiant division entière)
            # On ajoute 2 pour compenser l'arrondi vers le bas de la division entière dans le contexte du problème
            return d // 2 + 2

# On lit une ligne de l'entrée standard (input), l'utilisateur doit entrer trois entiers séparés par des espaces
# input() lit la ligne en tant que chaîne de caractères
# .split() sépare cette chaîne en une liste de sous-chaînes selon les espaces
# map(int, ...) applique la conversion en entier à chaque sous-chaîne trouvée
# list(...) convertit l'objet map en liste afin d'obtenir une liste de 3 entiers
A, B, C = list(map(int, input().split()))

# On initialise la variable aa avec une valeur très grande (ici 100000)
# Cela va servir à garder le minimum trouvé ensuite dans la boucle
aa = 100000

# On commence une boucle for pour N allant de 0 à 51 (range(52) donne les entiers de 0 inclus à 52 exclus)
for N in range(52):
    # Pour chaque valeur de N, on calcule la somme des trois appels à la fonction dist :
    # - dist(A, N) : le coût pour amener A à N
    # - dist(B, N) : le coût pour amener B à N
    # - dist(C, N) : le coût pour amener C à N
    # On utilise la fonction min pour mettre à jour aa si la valeur courante est plus petite que la précédente
    aa = min(aa, dist(A, N) + dist(B, N) + dist(C, N))

# Enfin, on affiche la valeur minimale trouvée pour aa
print(aa)