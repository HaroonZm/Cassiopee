import sys
readline = sys.stdin.readline
write = sys.stdout.write

def stern_brocot(p, n):
    """
    Trouve les fractions réduites les plus proches pour sqrt(p) dans l'arbre de Stern-Brocot.

    Plus précisément, détermine les fractions (rx/ry) < sqrt(p) < (lx/ly) les plus proches possible,
    où dénominateur et numérateur sont inférieurs ou égaux à n.

    Args:
        p (int): Le nombre dont on approche la racine carrée.
        n (int): La borne maximale pour le numérateur et le dénominateur.

    Returns:
        tuple: (lx, ly, rx, ry)
            (lx/ly) est la plus petite fraction supérieure à sqrt(p) (borne supérieure),
            (rx/ry) est la plus grande fraction inférieure à sqrt(p) (borne inférieure).
    """
    # Initialisation des bornes gauche (la/lb) et droite (ra/rb)
    la = 0
    lb = 1
    ra = 1
    rb = 0

    # lp/rp servent à déterminer si le parcours continue (1 = continuer, 0 = arrêter).
    lu = ru = 1

    # lx/ly = meilleure fraction supérieure <= n, rx/ry = meilleure fraction inférieure <= n
    lx = 0
    ly = 1
    rx = 1
    ry = 0

    # Parcours de l'arbre de Stern-Brocot par dichotomie stricte
    while lu or ru:
        # Fraction médiane
        ma = la + ra
        mb = lb + rb

        # Décide si on passe à droite (ma/mb < sqrt(p)) ou à gauche (ma/mb > sqrt(p))
        if p * mb**2 < ma**2:
            # La médiane est trop grande, restreindre la borne droite
            ra = ma
            rb = mb
            if ma <= n and mb <= n:
                # Si la fraction médiane est valide, on la prend comme meilleur borne supérieure
                rx = ma
                ry = mb
            else:
                # Sinon on arrête d'affiner cette borne
                lu = 0
        else:
            # La médiane est trop petite (ou pile), restreindre la borne gauche
            la = ma
            lb = mb
            if ma <= n and mb <= n:
                # Si la fraction est valide, on la prend comme meilleur borne inférieure
                lx = ma
                ly = mb
            else:
                # Sinon, on arrête d'affiner cette borne
                ru = 0
    return lx, ly, rx, ry

# Lecture des différentes instances du problème jusqu'à p == 0
while True:
    # Lecture et découpage de la ligne courante
    p, n = map(int, readline().split())
    if p == 0:
        # Fin d'entrée
        break
    # Calcul des deux fractions encadrant sqrt(p) avec bornes <= n
    lx, ly, rx, ry = stern_brocot(p, n)
    # Affichage dans le format demandé
    write("%d/%d %d/%d\n" % (rx, ry, lx, ly))