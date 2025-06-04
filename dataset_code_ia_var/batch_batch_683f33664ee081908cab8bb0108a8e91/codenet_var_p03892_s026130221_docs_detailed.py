def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) des deux entiers a et b en utilisant l'algorithme d'Euclide.

    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Returns:
        int: Le PGCD de a et b.
    """
    if b == 0:
        return a
    # Appel récursif avec b et le reste de la division de a par b
    return gcd(b, a % b)

# Lecture de quatre entiers sur une seule ligne séparés par des espaces
a, b, c, d = map(int, input().split())

# Calcul de la distance absolue entre les coordonnées
c = abs(c - a)
d = abs(d - b)

# Calcul du PGCD des deux distances
# On s'assure que le premier argument est le maximum pour éviter les erreurs de logique
g = gcd(max(c, d), min(c, d))

# Détermination du nombre de segments de longueur g dans chaque direction
j = int(c / g)
k = int(d / g)

# Calcul du résultat final : nombre minimal de pas à effectuer en diagonale puis tout droit
# (j + k - 1) donne le nombre total de segments moins la redondance du point de départ
result = (j + k - 1) * g

# Affichage du résultat
print(result)