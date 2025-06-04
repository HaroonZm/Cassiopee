"""
Ce module implémente la réflexion d'un point par rapport à une droite dans le plan cartésien.
La droite est définie par deux points lus en entrée. Pour chaque point saisi, sa réflexion par
rapport à cette droite est calculée et affichée.
"""

# Lecture des coordonnées des deux points déterminant la droite (stockées dans la liste pp)
pp = list(map(int, input().split()))
# Lecture du nombre de points à traiter pour la réflexion
n = int(input())

def project(bb, p=pp):
    """
    Projette le point bb orthogonalement sur la droite définie par les deux points p.
    
    Args:
        bb (list or tuple of float): Les coordonnées (x, y) du point à projeter.
        p (list or tuple of float, optionnel): Les quatre coordonnées [x1, y1, x2, y2] 
            définissant la droite. Par défaut, ce sont les coordonnées globales lues en entrée (pp).
    
    Returns:
        list of float: Les coordonnées du projeté orthogonal de bb sur la droite (x_proj, y_proj).
    """
    ans = []

    # Calcul du vecteur directeur de la droite (a) et du vecteur base-point vers bb (b)
    a = (p[2] - p[0], p[3] - p[1])
    b = (bb[0] - p[0], bb[1] - p[1])
    
    # On oriente le vecteur directeur pour éviter les projections négatives
    if dot(a, b) < 0:
        a = (-a[0], -a[1])
    
    # Coefficient de projection de b sur a (proportion sur le vecteur directeur)
    c = dot(a, b) / length(a) ** 2

    # Calcul des coordonnées du projeté, puis ajout à la liste résultat
    ans += [c * v + p[i] for i, v in enumerate(a)] 

    return ans

def length(vector):
    """
    Calcule la norme (longueur) du vecteur donné.
    
    Args:
        vector (list or tuple of float): Le vecteur dont on veut la norme.
    
    Returns:
        float: La longueur euclidienne du vecteur.
    """
    ans = 0
    for i in vector:
        ans += i ** 2
    return ans ** 0.5  # équivalent à racine carrée de la somme des carrés

def dot(a, b):
    """
    Calcule le produit scalaire (dot product) de deux vecteurs de même taille.
    
    Args:
        a (list or tuple of float): Premier vecteur.
        b (list or tuple of float): Deuxième vecteur.
    
    Returns:
        float: Produit scalaire de a et b si même longueur, None sinon.
    """
    n = len(a)
    if n != len(b):
        return None  # Vecteurs de taille différente : pas de produit scalaire défini
    ans = 0
    for i, j in zip(a, b):
        ans += i * j
    return ans

def reflection(b, p=pp):
    """
    Calcule et affiche la réflexion du point b par rapport à la droite définie par les points p.
    Le résultat est présenté avec 8 chiffres après la virgule.

    Args:
        b (list or tuple of float): Le point à réfléchir (x, y).
        p (list or tuple of float, optionnel): Les coordonnées de la droite [x1, y1, x2, y2].
            Par défaut, ce sont les coordonnées globales (pp).
    
    Effects:
        Affiche les coordonnées réfléchies du point b.
    """
    # Calcul du projeté orthogonal du point b sur la droite
    a = project(b)
    
    # Calcul du point réfléchi à partir du projeté
    ans = (b[0] + 2 * (a[0] - b[0]), b[1] + 2 * (a[1] - b[1]))
    
    # Affichage formaté du résultat
    print(f'{ans[0]:.8f} {ans[1]:.8f}')

# Boucle principale : traitement de chacun des n points à réfléchir
for i in range(n):
    # Lecture et conversion des coordonnées du point à réfléchir
    b = list(map(int, input().split()))
    reflection(b)