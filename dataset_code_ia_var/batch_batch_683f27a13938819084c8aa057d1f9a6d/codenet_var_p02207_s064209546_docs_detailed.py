import sys

def read_input():
    """
    Lit les entrées du problème depuis stdin, construit les listes d'évènements et de requêtes.

    Returns:
        N (int): nombre d'évènements.
        E (list[list[int,int]]): liste des évènements sous forme [temps, valeur].
        QU (int): nombre de requêtes.
        Q (list[list[int,int]]): liste des requêtes sous forme [gauche, droite].
    """
    input = sys.stdin.readline
    N = int(input())  # Nombre d'évènements
    E = [list(map(int, input().split())) for _ in range(N)]  # Liste des évènements
    QU = int(input())  # Nombre de requêtes
    Q = [list(map(int, input().split())) for _ in range(QU)]  # Liste des requêtes
    return N, E, QU, Q

def coordinate_compression(E, Q):
    """
    Effectue la compression de coordonnées sur les temps et bornes des événements et requêtes.

    Args:
        E (list[list[int,int]]): événements [temps, valeur].
        Q (list[list[int,int]]): requêtes [gauche, droite].

    Returns:
        E (list[list[int,int]]): événements avec temps compressés.
        Q (list[list[int,int]]): requêtes avec bornes compressées.
        compression_dict (dict): dictionnaire de conversion de valeur originale à valeur compressée.
    """
    # On rassemble tous les temps et bornes pour la compression
    TIMELIST = []
    for t, a in E:
        TIMELIST.append(t)
    for l, r in Q:
        TIMELIST.append(l)
        TIMELIST.append(r)
    # Compression: dictionnaire val originale --> val compressée
    compression_dict = {a: ind for ind, a in enumerate(sorted(set(TIMELIST)))}
    # Met à jour E et Q avec valeurs compressées
    for i in range(len(E)):
        E[i][0] = compression_dict[E[i][0]]
    for i in range(len(Q)):
        Q[i] = [compression_dict[Q[i][0]], compression_dict[Q[i][1]]]
    return E, Q, compression_dict

def seg_function(x, y):
    """
    Fonction utilisée dans le segment tree, ici la multiplication.

    Args:
        x (float): première valeur.
        y (float): seconde valeur.

    Returns:
        float: x multiplié par y.
    """
    return x * y

def build_segment_tree(E, compression_dict):
    """
    Construit l'arbre segmentaire initialisé avec les valeurs issues des événements.

    Args:
        E (list[list[int,int]]): événements [temps compressé, valeur].
        compression_dict (dict): dictionnaire de compression de coordonnées.

    Returns:
        tuple:
            SEG (list[float]): tableau représentant le segment tree (1-indexé).
            seg_el (int): taille de base du segment tree (puissance de deux supérieure à nb de points).
    """
    # On veut que le segment tree a autant d'éléments que le nombre de points après compression
    n = len(compression_dict)
    seg_el = 1 << (n.bit_length())  # Next power of 2
    SEG = [1] * (2 * seg_el)  # Initialisation à 1 (élément neutre multiplicatif)
    # Place chaque évènement dans la feuille correspondante
    for t, a in E:
        SEG[t + seg_el] = 1 - 0.1 * a
    # Construit les valeurs internes du segment tree
    for i in range(seg_el - 1, 0, -1):
        SEG[i] = seg_function(SEG[i * 2], SEG[i * 2 + 1])
    return SEG, seg_el

def update(n, x, SEG, seg_el):
    """
    Met à jour la valeur en position n du segment tree avec x.

    Args:
        n (int): index à mettre à jour (compressé).
        x (float): nouvelle valeur à insérer.
        SEG (list[float]): tableau du segment tree.
        seg_el (int): taille de base du segment tree.
    """
    i = n + seg_el  # Position dans le segment tree
    SEG[i] = x  # Mise à jour de la feuille
    i >>= 1
    # Propagation de la mise à jour dans l'arbre
    while i != 0:
        SEG[i] = seg_function(SEG[i * 2], SEG[i * 2 + 1])
        i >>= 1

def getvalues(l, r, SEG, seg_el):
    """
    Calcule la valeur segmentée sur l'intervalle [l, r) à l'aide du seg_function.

    Args:
        l (int): borne gauche (compressée, incluse).
        r (int): borne droite (compressée, exclue).
        SEG (list[float]): tableau du segment tree.
        seg_el (int): taille de base du segment tree.

    Returns:
        float: valeur de la fonction segmentaire sur [l, r).
    """
    L = l + seg_el
    R = r + seg_el
    ANS = 1  # Neutre pour la multiplication
    # Parcours de l'intervalle de requête
    while L < R:
        if L & 1:
            ANS *= SEG[L]
            L += 1
        if R & 1:
            R -= 1
            ANS *= SEG[R]
        L >>= 1
        R >>= 1
    return ANS

def solve():
    """
    Fonction principale, lit les entrées, effectue la compression, construit le segment tree,
    puis répond aux requêtes en calculant la quantité demandée pour chaque intervalle.
    """
    N, E, QU, Q = read_input()
    E, Q, compression_dict = coordinate_compression(E, Q)
    SEG, seg_el = build_segment_tree(E, compression_dict)
    # Pour chaque requête, calcule le résultat et affiche-le
    for l, r in Q:
        res = getvalues(l, r, SEG, seg_el)
        print(int(10 ** 9 * res))

if __name__ == "__main__":
    solve()