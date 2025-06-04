# Demande à l'utilisateur d'entrer une valeur, qui correspond généralement à un nombre entier.
n = input()
# Crée une liste 'ps' en utilisant une compréhension de liste.
# Pour chaque i dans la plage de n (ici 'xrange', utilisé en Python 2 pour générer un itérateur efficace),
# raw_input() demande une ligne de texte à l'utilisateur, qui est ensuite découpée avec split() pour séparer chaque nombre.
# map(int, ...) convertit chaque chaîne en entier.
# Ainsi, 'ps' est une liste de listes, chaque sous-liste contenant des entiers (typiquement des coordonnées).
ps = [map(int, raw_input().split()) for i in xrange(n)]

# Définit une fonction nommée 'intersection' qui prend 4 paramètres (chacun représentant un point dans le plan 2D).
# p1 et p2 sont les points d'un premier segment; q1 et q2 sont les points d'un deuxième segment.
def intersection(p1, p2, q1, q2):
    # Calcule la différence des coordonnées x entre le second et le premier point du premier segment.
    dx0 = p2[0] - p1[0]
    # Calcule la différence des coordonnées y entre le second et le premier point du premier segment.
    dy0 = p2[1] - p1[1]
    # Calcule la différence des coordonnées x entre le second et le premier point du second segment.
    dx1 = q2[0] - q1[0]
    # Calcule la différence des coordonnées y entre le second et le premier point du second segment.
    dy1 = q2[1] - q1[1]
    # Evalue quelques produits pour la résolution de l'intersection entre deux droites.
    # dy0*dx1 correspond au produit croisé pertinent du premier vecteur du premier segment et du second du deuxième segment.
    a = dy0*dx1
    b = dy1*dx0
    c = dx0*dx1
    d = dy0*dy1
    # Si a == b, cela signifie que les segments sont parallèles et donc, il n'y a pas d'intersection (ou elles sont confondues),
    # on retourne None dans ce cas.
    if a == b:
        return None
    # Calcule la coordonnée x du point d'intersection avec la formule trouvée par la résolution des équations paramétriques des deux segments.
    x = (a*p1[0] - b*q1[0] + c*(q1[1] - p1[1])) / float(a - b)
    # Même principe pour la coordonnée y, on utilise une formule équivalente adaptée à la coordonnée y.
    y = (b*p1[1] - a*q1[1] + d*(q1[0] - p1[0])) / float(b - a)
    # Retourne un tuple représentant le point d'intersection entre les deux segments.
    return x, y

# Définit une fonction 'cross' qui calcule le déterminant (produit vectoriel) de deux vecteurs AB et AC dans le plan.
# Cette valeur est positive si c est à gauche de la droite AB, négative si c est à droite, nulle si aligné.
def cross(a, b, c):
    # Calcule (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

# Déclare une fonction pour calculer l'aire d'un polygone à partir d'une liste de points (ps).
def calc_area(ps):
    # Calcule la somme pour chaque i de x_i * y_{i-1} - y_i * x_{i-1} (formule du polygone/shoelace theorem).
    # 'xrange(len(ps))' itère de 0 à len(ps)-1.
    # ps[i][0] accède à x_i, ps[i][1] à y_i
    # La notation ps[i-1] exploite que ps[-1] est le dernier élément de la liste, bouclant le polygone.
    return abs(
        sum(ps[i][0] * ps[i-1][1] - ps[i][1] * ps[i-1][0] for i in xrange(len(ps)))
    ) / 2.0

# Cette boucle for est exécutée pour chaque cas de test. L'utilisateur doit fournir un nombre de cas de test avec 'input()'.
for t in xrange(input()):
    # Initialisation d'une liste vide 'vs' destinée à contenir les sommets du nouveau polygone coupé.
    vs = []
    # Demande à l'utilisateur 4 entiers dans l'ordre x1, y1, x2, y2.
    # Ces valeurs décrivent les coordonnées de deux points formant une droite ou un segment.
    x1, y1, x2, y2 = map(int, raw_input().split())
    # Création de deux tuples représentant les deux points d'extrémité du segment séparateur.
    p1 = (x1, y1)
    p2 = (x2, y2)
    # Parcourt chaque côté du polygone initial en itérant sur les indices.
    for i in xrange(n):
        # q1 est le sommet précédent du polygone (si i==0, -1 donne le dernier sommet, réalisant la boucle).
        q1 = ps[i - 1]
        # q2 est le sommet courant.
        q2 = ps[i]
        # Calcule si le segment du polygone (q1,q2) croise le segment (p1,p2)
        # On utilise le signe du produit croisé pour vérifier si les points q1 et q2 sont de part et d'autre de la droite (p1,p2), ou dessus.
        if cross(p1, p2, q1) * cross(p1, p2, q2) <= 0:
            # Si c'est le cas, on calcule l'intersection entre les deux segments.
            r = intersection(p1, p2, q1, q2)
            # Si la fonction 'intersection' a retourné un point (c'est à dire, non None),
            # on l'ajoute à la liste des sommets.
            if r is not None:
                vs.append(r)
        # Si le point q2 est du "bon côté" ou sur la droite (p1,p2),
        # soit cross(p1,p2,q2) >= 0, alors on conserve q2 comme sommet du polygone résultant.
        if cross(p1, p2, q2) >= 0:
            vs.append(q2)
    # Après avoir collecté les sommets du polygone coupé, on affiche son aire.
    # Le format spécifique "%.09f" impose l'affichage d'un nombre à 9 chiffres après la virgule.
    print "%.09f" % calc_area(vs)