def x():
    """
    Cherche le sous-tableau rectangulaire de la matrice `l` ayant la somme maximale possible.
    Utilise une généralisation en 2D de l'algorithme de Kadane.
    
    Retourne:
        int: La somme maximale trouvée parmi tous les sous-tableaux rectangulaires possibles.
    """
    m = -10**9  # Initialisation du maximum global avec une très petite valeur
    # On examine tous les intervalles de colonnes possibles [i, n-1]
    for i in N:
        p = [0] * n  # Initialisation du tableau temporaire de sommes sur les lignes
        for j in range(i, n):
            # On cumule les sommes pour chaque ligne dans le rectangle de colonnes [i, j]
            for k in N:
                p[k] += l[k][j]
            # On cherche la meilleure somme partielle dans le tableau réduit 1D p (entre les lignes)
            m = max(P(p), m)
    return m

def P(a):
    """
    Implémente l'algorithme de Kadane pour trouver la sous-séquence contiguë de somme maximale
    dans un tableau à une dimension.
    
    Args:
        a (list of int): Tableau d'entiers.
    
    Retourne:
        int: La somme maximale d'une sous-séquence contiguë de `a`.
    """
    m = -10**5  # Valeur initiale suffisamment négative pour supporter tous les cas
    c = 0       # Somme courante pour la sous-séquence considérée
    for x in N:
        c += a[x]      # On ajoute le nouvel élément à la somme courante
        m = max(c, m)  # On met à jour le maximum si besoin
        if c < 0:
            c = 0      # On recommence la somme si le total devient négatif
    return m

# Lecture de la taille de la matrice carrée
n = int(raw_input())

# On crée une liste d'indices de lignes et colonnes, pour itérations futures
N = range(n)

# Lecture de la matrice carrée l
l = []
for i in N:
    # Chaque ligne de la matrice est lue et convertie en liste d'entiers
    l.append(map(int, raw_input().split()))

# On lance le calcul et affiche le résultat
print x()