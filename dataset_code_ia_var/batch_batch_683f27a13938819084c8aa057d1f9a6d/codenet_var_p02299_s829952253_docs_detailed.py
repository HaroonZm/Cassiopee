def dot(a, b):
    """
    Calcule le produit scalaire (dot product) de deux nombres complexes considérés comme des points/vecteurs 2D.

    Paramètres:
        a (complex): Premier vecteur représenté par un nombre complexe.
        b (complex): Deuxième vecteur représenté par un nombre complexe.

    Retourne:
        float: Le produit scalaire de a et b.
    """
    # Produit scalaire : ax * bx + ay * by
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    """
    Calcule le produit vectoriel (cross product) de deux nombres complexes assimilés à des vecteurs 2D.

    Paramètres:
        a (complex): Premier vecteur représenté par un nombre complexe.
        b (complex): Deuxième vecteur représenté par un nombre complexe.

    Retourne:
        float: Le produit vectoriel de a et b (ax*by - ay*bx).
    """
    # Produit vectoriel : ax * by - ay * bx
    return a.real * b.imag - a.imag * b.real

# Lecture du nombre de sommets du polygone
n = int(input())
# Lecture des sommets du polygone, chaque sommet étant un nombre complexe (x + yj)
vertices = [complex(*map(int, input().split())) for _ in range(n)]
# Création de la liste des arêtes comme paires consécutives de sommets (bouclage à la fin)
edges = [(p0, p1) for p0, p1 in zip(vertices, vertices[1:] + [vertices[0]])]

# Lecture du nombre de requêtes à traiter
q = int(input())

while q:
    # On traite chaque requête séparément
    q -= 1
    # Lecture du point à tester, sous forme d'un nombre complexe
    p = complex(*map(int, input().split()))
    counter = 0  # Compteur pour le nombre de croisements du rayon horizontal vers la droite

    for p0, p1 in edges:
        # Vecteurs allant du point testé p vers les extrémités de l'arête courante
        a, b = p0 - p, p1 - p

        # On s'assure que a.imag <= b.imag pour simplifier le raisonnement
        if a.imag > b.imag:
            a, b = b, a

        # Calcul du produit vectoriel entre les vecteurs a et b
        crs = cross(a, b)

        # Test du croisement du segment avec le rayon horizontal (parité du nombre de croisements)
        if a.imag <= 0 < b.imag and crs < 0:
            counter += 1

        # Test si le point p est sur le segment [p0, p1]
        if crs == 0 and dot(a, b) <= 0:
            print(1)  # Le point est sur une arête du polygone
            break
    else:
        # Si on n'a pas cassé la boucle, on applique la règle de la parité pour déterminer la position
        # counter % 2 == 1 : intérieur, == 0 : extérieur
        print(2 if counter % 2 else 0)