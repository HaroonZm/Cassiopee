def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b à l'aide de l'algorithme d'Euclide.

    Paramètres:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Retourne:
        int: Le PGCD de a et b.
    """
    # Continue tant que b n'est pas nul
    while b:
        # À chaque itération, remplace a par b et b par le reste de la division de a par b
        a, b = b, a % b
    # Lorsque b devient 0, a contient le PGCD
    return a

def solve():
    """
    Lit deux entiers a et b depuis l'entrée standard, puis effectue les opérations suivantes:
    - Si a et b sont égaux ou si a est divisible par b, affiche "0 1".
    - Si b est divisible par a, affiche "1 0".
    - Sinon, simplifie a et b par leur PGCD puis applique une variante de l'algorithme d'Euclide étendu
      pour déterminer deux coefficients d'une identité de Bézout, et affiche ces deux coefficients.

    Entrée:
        Deux entiers séparés par un espace (lus via input()).

    Sortie:
        Affiche une ligne de deux entiers séparés par un espace.
    """
    # Lit deux entiers depuis l'entrée standard
    a, b = map(int, input().split())

    # Si a et b sont égaux, ou si a est un multiple de b
    if a == b or a % b == 0:
        print(0, 1)
    # Si b est un multiple de a
    elif b % a == 0:
        print(1, 0)
    else:
        # Sinon, calcule le PGCD pour simplifier les deux nombres
        g = gcd(a, b)
        a //= g
        b //= g

        # Initialise les coefficients pour l'algorithme étendu d'Euclide.
        # coe[i] contient une paire [x, y] telle que x*a_original + y*b_original = valeur courante
        coe = [[1, 0], [0, 1]]

        # Applique l'algorithme d'Euclide étendu jusqu'à ce que b devienne 1
        while b != 1:
            # Calcule le quotient
            quo = a // b
            # Copie les coefficients précédents
            coe_d1 = coe[1]
            # Met à jour les coefficients en fonction des précédents et du quotient
            coe_d2 = [coe[0][0] - coe[1][0] * quo, coe[0][1] - coe[1][1] * quo]
            # Avance d'une étape dans la liste de coefficients
            coe = [coe_d1, coe_d2]
            # Met à jour a et b pour l'itération suivante
            a, b = b, a % b
        # Affiche les deux coefficients obtenus pour l'identité de Bézout
        print(*coe[1])

solve()