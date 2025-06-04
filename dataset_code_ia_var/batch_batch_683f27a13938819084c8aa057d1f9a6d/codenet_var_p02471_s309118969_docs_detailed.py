def calc_gcd(x, y):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers x et y à l'aide de l'algorithme d'Euclide.

    Args:
        x (int): Premier entier.
        y (int): Deuxième entier.

    Returns:
        int: Le PGCD de x et y.
    """
    # On s'assure que x >= y pour simplifier l'algorithme
    if x < y:
        x, y = y, x

    # Boucle principale de l'algorithme d'Euclide
    while y > 0:
        x, y = y, x % y  # À chaque itération, x prend la valeur de y, y prend le reste de la division x//y

    # x est maintenant le PGCD
    return x

# Lecture des deux entiers a et b depuis l'entrée standard (séparés par un espace)
a, b = map(int, input().split())

# Calcul du PGCD de a et b
gcd = calc_gcd(a, b)

# Initialisation des coefficients pour la recherche de la solution particulière (méthode de l'algorithme étendu)
x1 = 1
y1 = 0
z1 = a_prime = a / gcd  # Coefficient associé à 'a' dans la division par le PGCD

x2 = 0
y2 = 1
z2 = b_prime = b / gcd  # Coefficient associé à 'b' dans la division par le PGCD

# Recherche d'une solution particulière à l'équation diophantienne a·x + b·y = gcd(a, b)
while z2 != 1:
    # Calcul du quotient entier q pour l'algorithme
    q = (z1 - (z1 % z2)) / z2

    # Mise à jour des coefficients selon l'algorithme d'Euclide étendu
    (x1, y1, z1), (x2, y2, z2) = (x2, y2, z2), (x1 - (q * x2), y1 - (q * y2), z1 - (q * z2))

# On a trouvé une solution particulière (x2, y2) telle que a'/b' sont premiers entre eux et a'*x2 + b'*y2 = 1

# Paramètre t pour la solution générale (ici t=0 pour la solution particulière)
t = 0
x = x2 + b_prime * t  # x = x2 + k·b'
y = y2 + a_prime * t  # y = y2 + k·a'

# Affichage de la solution particulière (seule une solution affichée, correspondant à t=0)
print(int(x), int(y))