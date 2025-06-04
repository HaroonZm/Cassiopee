def dist(x, y):
    """
    Calcule une mesure spéciale de la distance entre deux entiers x et y.
    
    Si x > y, la fonction retourne simplement x - y.
    Sinon (x <= y), elle retourne la moitié de la différence entre y et x (division entière),
    mais si la différence est impaire, elle ajoute 2 au résultat.

    Args:
        x (int): Premier entier.
        y (int): Deuxième entier.

    Returns:
        int: La "distance" calculée entre x et y selon la règle ci-dessus.
    """
    if x > y:
        # Si x est supérieur à y, distance directe.
        return x - y
    else:
        # Sinon, calcul de la moitié de la différence (y - x), ajustée pour impaire.
        d = y - x
        if d % 2 == 0:
            return d // 2
        else:
            return d // 2 + 2

# Lecture de l'entrée utilisateur : trois entiers séparés par des espaces.
A, B, C = list(map(int, input().split()))

# Initialisation d'une variable aa avec une valeur élevée qui sera minimisée plus tard.
aa = 100000

# Parcours de tous les entiers N de 0 à 51 compris pour tester chaque valeur possible pour minimiser la somme des distances.
for N in range(52):
    # On calcule la somme des "distances" entre A, B, C et le nombre courant N.
    current_sum = dist(A, N) + dist(B, N) + dist(C, N)
    # Mise à jour de aa si une plus petite somme est trouvée.
    aa = min(aa, current_sum)

# Affichage du résultat minimal trouvé.
print(aa)