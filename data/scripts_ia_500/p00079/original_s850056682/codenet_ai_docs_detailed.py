def read():
    """
    Lit une ligne d'entrée standard contenant des nombres flottants séparés par des virgules,
    et retourne ces valeurs sous forme de liste de floats.
    
    Returns:
        list of float: Liste des nombres flottants lus depuis l'entrée standard.
    """
    # On lit une ligne de texte, on la découpe par les virgules, puis on convertit chaque valeur en float
    return list(map(float, input().split(",")))


def triArea(va, vb, vc):
    """
    Calcule l'aire du triangle défini par trois points dans le plan 2D.
    La formule utilisée est celle de la moitié du produit vectoriel entre deux vecteurs formés par ces points.
    
    Args:
        va (list or tuple of float): Coordonnées (x, y) du premier point.
        vb (list or tuple of float): Coordonnées (x, y) du deuxième point.
        vc (list or tuple of float): Coordonnées (x, y) du troisième point.
    
    Returns:
        float: Aire absolue du triangle formé par les points va, vb, vc.
    """
    # Calcul du déterminant formant le double de l'aire du triangle
    # |(va - vc) x (vb - vc)| / 2
    area = abs((va[0] - vc[0]) * (vb[1] - vc[1]) - (va[1] - vc[1]) * (vb[0] - vc[0])) / 2
    return area


# Lecture du premier point de référence (sommet fixe du polygone)
v1 = read()
# Lecture des deux premiers sommets consécutifs du polygone
va = read()
vb = read()
# Calcul initial de l'aire partielle en formant un triangle avec v1, va, et vb
s = triArea(v1, va, vb)

# Boucle infinie pour lire les points suivants du polygone jusqu'à la fin d'entrée
while True:
    try:
        # On décale les sommets : va devient l'ancien vb
        va = vb
        # On lit le nouveau sommet suivant
        vb = read()
        # On ajoute l'aire du triangle formé par v1, va, vb à l'aire totale
        s += triArea(v1, va, vb)
    except:
        # Fin de la lecture, on sort de la boucle
        break

# Affiche l'aire totale du polygone définie par les sommets lus
print(s)