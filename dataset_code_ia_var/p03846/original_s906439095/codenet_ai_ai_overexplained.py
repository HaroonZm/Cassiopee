# Demande à l'utilisateur d'entrer un entier
N = int(input())  # N est la taille du tableau, ici on convertit la chaîne entrée en entier

# Définit une valeur de mod (modulo) souvent utilisée dans les problèmes de programmation compétitive pour éviter les dépassements de capacité
mod = 10 ** 9 + 7  # Cela signifie 10 puissance 9 plus 7, soit 1000000007

# Lit un tableau d'entiers de la saisie standard, les sépare et les convertit en entiers
A = list(map(int, input().split()))  # input().split() sépare l'entrée sur les espaces, map(int, ...) applique la conversion en entier à chaque élément

# Crée une liste B de taille N remplie de zéros. Elle servira à compter combien de fois chaque nombre de 0 à N-1 apparaît dans A
B = [0 for i in range(N)]  # Boucle qui répète N fois 0, donc B est une liste de N zéros

# Parcourt chaque élément de la liste A
for a in A:
    # Pour chaque valeur a dans A, incrémente le compteur à l'indice correspondant dans B
    B[a] += 1  # Cela signifie qu'on compte le nombre d'occurrences de chaque valeur de A

# Initialise un drapeau 'f' à 0. Ce drapeau servira à signaler certaines erreurs ou conditions de rejet
f = 0

# Vérifie si N est un nombre pair (puisque si N % 2 == 0 alors il est pair)
if N % 2 == 0:
    ans = 1  # Initialise la variable de réponse ans à 1. Elle servira à calculer le nombre de façons valides possibles
    # Parcourt les indices impairs de 1 jusqu'à N-1 avec un pas de 2 (1, 3, 5, ...)
    for i in range(1, N, 2):
        # Vérifie si la valeur d'occurrence à cet indice n'est pas égale à 2
        if B[i] != 2:
            # Si ce n'est pas égal à 2, met le drapeau f à 1 pour signaler un cas d'erreur et sort de la boucle
            f = 1
            break  # Quitte la boucle
        else:
            # Si c'est exactement 2, multiplie ans par 2 et prend le résultat modulo 'mod'
            ans = ans * 2 % mod  # Cela garantit que 'ans' ne dépasse jamais la valeur de mod
    # Après la boucle, si une erreur a été détectée (f == 1)
    if f == 1:
        print(0)  # Affiche 0 car la configuration n'est pas valide
    else:
        print(ans)  # Sinon, affiche le résultat trouvé
# Si N n'est pas pair, c'est-à-dire impair
else:
    ans = 1  # Initialise la variable réponse à 1
    # Vérifie que le nombre d'occurrences de 0 dans B doit être exactement 1
    if B[0] != 1:
        f = 1  # Si ce n'est pas le cas, signale une erreur via le drapeau f
    if f == 0:
        # Parcourt les indices pairs de 2 à N avec un pas de 2 (2, 4, 6, ..., N ou N-1)
        for i in range(2, N + 1, 2):
            # Vérifie si l'occurrence n'est pas exactement 2 à cet indice
            if B[i] != 2:
                f = 1  # Erreur détectée, signale via f
                break  # Interrompt la boucle
            else:
                # Sinon multiplie ans par 2 et prend le modulo 'mod'
                ans = ans * 2 % mod
    # Après les vérifications, si une erreur existe (f vaut 1)
    if f == 1:
        print(0)  # Affiche 0 car le cas n'est pas valide
    else:
        print(ans)  # Sinon, affiche le nombre de façons calculé