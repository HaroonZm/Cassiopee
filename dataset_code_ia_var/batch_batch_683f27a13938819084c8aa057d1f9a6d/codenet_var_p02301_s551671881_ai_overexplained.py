# Cette fonction calcule la différence vectorielle entre deux points consécutifs dans une liste de points complexe
def diff(i):
    # On extrait les deux points (courant et suivant) depuis la liste 'points'
    # 'cp' est le point à l'indice i, 'np' est le point suivant à l'indice i+1
    cp, np = points[i:i + 2]
    # On retourne le vecteur allant de 'cp' à 'np' en soustrayant 'cp' à 'np'
    return np - cp

# Cette fonction calcule le produit vectoriel (cross product) de deux vecteurs du plan complexe
def cross(a, b):
    # En géométrie du plan, on peut représenter un vecteur par un nombre complexe : a = a.real + i*a.imag
    # Le produit vectoriel entre 'a' et 'b' est la différence du produit croisé des parties réelles et imaginaires
    # La formule devient (a.real * b.imag) - (a.imag * b.real)
    return a.real * b.imag - a.imag * b.real

# Cette fonction calcule la distance euclidienne (le diamètre courant) entre deux points donnés par leurs indices
def diameter(i, j):
    # On récupère les deux points complexes 'points[i]' et 'points[j]'
    # La distance euclidienne entre deux points complexes correspond à la valeur absolue de leur différence
    # 'abs(z)' retourne le module du nombre complexe 'z'
    return abs(points[i] - points[j])

# On lit un entier 'n' depuis l'entrée standard, qui représente le nombre de points du polygone
n = int(input())

# On crée une liste de tuples contenant les coordonnées (x, y) des points du polygone
# On lit 'n' lignes, chacune étant splittée en flottants (pour les coordonnées), puis on regroupe sous forme de tuples
t_points = [tuple(map(float, input().split())) for _ in range(n)]

# On trouve l'indice du point qui est le plus petit selon l'ordre lexicographique (x, puis y)
# 'key=lambda x: t_points[x]' utilise la comparaison des tuples pour choisir le plus petit
i = min(range(n), key=lambda x: t_points[x])

# On trouve l'indice du point qui est le plus grand selon l'ordre lexicographique (x, puis y)
j = max(range(n), key=lambda x: t_points[x])

# On transforme chaque point du polygone, défini par son tuple (x, y), en un nombre complexe 'x + i*y'
# Cela permet de simplifier les opérations vectorielles
points = [re + 1j * im for re, im in t_points]

# Pour faciliter le parcours circulaire du polygone, on recopie le premier point à la fin de la liste
# Ainsi, points[n] == points[0], ce qui évite d'avoir à traiter le débordement
points.append(points[0])

# On calcule un diamètre initial en utilisant les deux points extrêmes définis par les indices 'i' et 'j'
tentative_diameter = diameter(i, j)

# On initialise deux indices d'itération (pour les points opposés), 'it' et 'jt', à la position initiale de 'i' et 'j'
it, jt = i, j

# On entre dans une boucle infinie qui ne sera quittée que par un 'break' explicite
while True:
    # On compare les directions des bords partant de 'it' et 'jt' en utilisant leur produit vectoriel
    # diff(it) est le vecteur entre points[it] et points[it+1]
    # diff(jt) est le vecteur entre points[jt] et points[jt+1]
    # Si le produit vectoriel est positif ou nul, on avance 'jt' (le pointeur du point opposé)
    if cross(diff(it), diff(jt)) >= 0:
        # On avance jt d'une position, et on fait un modulo n pour tourner en boucle sur les indices (parce que le polygone est cyclique)
        jt = (jt + 1) % n
    else:
        # Si le produit vectoriel est strictement négatif, on avance 'it'
        it = (it + 1) % n
    # On actualise le diamètre maximal trouvé jusqu'à présent, en prenant la distance entre les nouveaux points it et jt
    tentative_diameter = max(tentative_diameter, diameter(it, jt))
    # Si l'on est revenu aux indices de départ, on arrête la boucle
    if it == i and jt == j:
        break

# On affiche le diamètre maximal trouvé (distance maximale entre deux points du polygone)
print(tentative_diameter)