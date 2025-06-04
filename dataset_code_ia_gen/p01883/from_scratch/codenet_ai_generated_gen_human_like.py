A = int(input())

# On cherche la plus petite chaîne la plus courte possible
# dont la distance de tri (nombre minimal d'échanges adjacents
# pour obtenir une chaîne équilibrée) est exactement A.

# On modélise la chaîne comme une séquence de paires (c) :
# la chaîne finale a N paires, donc longueur 2N.
# Le nombre de swaps minimal est la distance de tri à bulles
# entre la chaîne initiale et la chaîne équilibrée minimale.

# Le nombre minimal d'échanges pour rendre équilibrée la chaîne
# correspond au nombre d'inversions dans la séquence des parenthèses,
# ou plus précisément aux contestations dans la chaîne.

# Une construction clé est la suivante (trouvée par analyse combinatoire) :
# On choisit n, la plus petite longueur telle que n*(n-1)/2 >= A.
# Le nombre A correspond à la somme des entiers de 1 à n-1.

# Ensuite, on construit la chaîne en mettant :
# - n-1 parenthèses fermantes ')' au début,
# - puis une parenthèse ouvrante '(',
# - et ensuite un nombre k de parenthèses fermantes ')',
# - puis le reste de parenthèses ouvrantes '('.

# La valeur k est calculée pour valider que le nombre total d'inversions
# correspond exactement à A.

# Cette chaîne est la plus courte possible,
# et parmi celles minimales en lexicographique.

# Implémentation :

def solve(A):
    # Trouver n minimal tq n*(n-1)/2 >= A
    n = 1
    while n*(n-1)//2 < A:
        n += 1
    total = n*(n-1)//2
    diff = total - A
    # diff est le nombre de swaps "en excès" que l'on doit corriger
    # On place diff '(' au début après les n-1 ')'

    # Construction de la chaîne
    # Position : 
    # 0..(n-1 - diff -1) : ')'
    # Ensuite '('
    # Ensuite diff ')'
    # Ensuite (n -1) '('

    left_close = n - 1 - diff
    s = []
    s.extend(')' * left_close)
    s.append('(')
    s.extend(')' * diff)
    s.extend('(' * (n -1))
    return "".join(s)

print(solve(A))