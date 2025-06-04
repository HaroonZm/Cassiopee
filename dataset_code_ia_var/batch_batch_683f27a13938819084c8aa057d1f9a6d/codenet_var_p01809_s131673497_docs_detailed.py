def gcd(m, n):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers m et n
    en utilisant l'algorithme d'Euclide récursif.

    Args:
        m (int): Premier entier.
        n (int): Deuxième entier.

    Returns:
        int: Le plus grand commun diviseur de m et n.
    """
    r = m % n  # Reste de la division de m par n
    if r == 0:
        return n  # Si le reste est 0, le PGCD a été trouvé
    else:
        return gcd(n, r)  # On continue avec n et r


# Lecture des deux entiers p et q à partir de l'entrée standard
p, q = map(int, input().split())

# Simplification de la fraction p/q en divisant q par le PGCD de p et q
q //= gcd(p, q)

# Initialisation de variables :
# x est le dénominateur simplifié, y sera le résultat, et k le diviseur en cours
x = q
y = 1
k = 2

# Boucle pour trouver tous les facteurs premiers de x
while k * k <= x:
    if x % k == 0:
        # Si k divise x, on divise x par k autant de fois que possible
        while x % k == 0:
            x //= k
        # On multiplie y par ce facteur premier unique
        y *= k
    k += 1

# Si x > 1, il reste un dernier facteur premier à prendre en compte
y *= x

# Affichage du résultat final
print(y)