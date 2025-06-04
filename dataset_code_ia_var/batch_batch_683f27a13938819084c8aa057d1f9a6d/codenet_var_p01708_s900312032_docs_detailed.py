digits = "-0123456789"

def cross_point(P, Q):
    """
    Calcule le point d'intersection de deux segments de droite définis par deux tuples P et Q.

    Arguments:
        P (tuple): Coordonnées du premier segment sous forme (x0, y0, x1, y1).
        Q (tuple): Coordonnées du second segment sous forme (x2, y2, x3, y3).

    Returns:
        tuple: Les coordonnées (x, y) du point d'intersection.
    """
    # Décomposition des tuples en coordonnées individuelles
    x0, y0, x1, y1 = P
    x2, y2, x3, y3 = Q
    # Calcul des vecteurs de direction des segments
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    # Calcul déterminant pour l'intersection
    s = (y0 - y2) * dx1 - (x0 - x2) * dy1
    sm = dx0 * dy1 - dy0 * dx1

    # Normalisation du signe
    if s < 0:
        s = -s
        sm = -sm

    # s == 0 veut dire segments sont alignés
    if s == 0:
        x = x0
        y = y0
    else:
        x = x0 + s * dx0 / sm
        y = y0 + s * dy0 / sm
    return x, y

def reflection(line, point):
    """
    Calcule le miroir d'un point par rapport à une droite.

    Arguments:
        line (tuple): Coordonnées de la droite sous forme (x0, y0, x1, y1).
        point (tuple): Coordonnées du point sous forme (p, q).

    Returns:
        tuple: Coordonnées (x, y) du point réfléchi.
    """
    # Extraction et translation pour que (x0, y0) soit à l'origine
    x0, y0, x1, y1 = line
    p, q = point
    x1 -= x0
    y1 -= y0
    p -= x0
    q -= y0

    # Calculs intermédiaires basés sur les produits scalaires et vectoriels
    cv = p * x1 + q * y1
    sv = p * y1 - q * x1
    cv2 = cv ** 2 - sv ** 2
    sv2 = 2 * cv * sv
    dd = (p ** 2 + q ** 2) * (x1 ** 2 + y1 ** 2)

    # Si la longueur est nulle, pas de réflexion possible
    if dd == 0:
        return x0 + p, y0 + q

    # Formule de réflexion complexe (inspiré des nombres complexes)
    x = x0 + (cv2 * p - sv2 * q) / dd
    y = y0 + (sv2 * p + cv2 * q) / dd
    return x, y

def parse(S):
    """
    Analyse et évalue une expression en géométrie de la forme "(point)@(point)", "(line)@(line)", etc.

    Arguments:
        S (str): La chaîne de caractères à analyser.

    Returns:
        tuple: Un tuple dont:
            - La première composante est 0 pour un point, 1 pour une droite,
            - Les composantes suivantes sont les coordonnées pertinentes.
    """
    # Ajout d'un symbole de fin de chaîne pour éviter les erreurs d'index
    S = S + "$"
    cur = 0

    def expr():
        """
        Analyse récursivement une expression géométrique à partir de la position courante dans la chaîne S.

        Returns:
            tuple: Le résultat analysé (voir parse).
        """
        nonlocal cur
        res = None
        # On attend des expressions entre parenthèses, éventuellement "@" imbriqués
        while S[cur] == '(':
            cur += 1  # Consomme '('
            if S[cur] in digits:
                # On a un point (x, y)
                x = number()
                cur += 1  # Consomme ','
                y = number()
                r = (0, x, y)
            else:
                # Expression récursive
                r = expr()
            cur += 1  # Consomme ')'

            if res is None:
                # Premier membre de l'expression
                res = r
            else:
                # Application de l'opérateur @ selon les types
                if res[0] == r[0] == 0:
                    # Cas (point)@(point) -> construit une droite
                    res = (1, res[1], res[2], r[1], r[2])
                elif res[0] == r[0] == 1:
                    # Cas (line)@(line) -> intersection de droites, produit un point
                    x, y = cross_point(res[1:], r[1:])
                    res = (0, x, y)
                else:
                    # (line)@(point) ou (point)@(line) -> réflexion du point par la droite
                    point, line = (res, r) if r[0] else (r, res)
                    x, y = reflection(line[1:], point[1:])
                    res = (0, x, y)
            # Si prochain symbole n'est pas '@', on sort de la boucle
            if S[cur] != '@':
                break
            cur += 1  # Consomme '@'
        return res

    def number():
        """
        Analyse un nombre entier à partir de la position courante dans la chaîne S.

        Returns:
            int: La valeur entière extraite.
        """
        nonlocal cur
        v = 0
        mns = 0
        if S[cur] == '-':
            mns = 1
            cur += 1  # Consomme '-'
        while S[cur] in digits:
            v = 10 * v + int(S[cur])
            cur += 1
        return -v if mns else v

    return expr()

def solve():
    """
    Lit une ligne de l'entrée standard, l'évalue avec "parse" et affiche le résultat formaté.

    Returns:
        bool: False si la chaîne lue est "#", True sinon.
    """
    s = input()
    if s == '#':
        return False
    res = parse(s)
    # Affiche les coordonnées du résultat avec 16 décimales
    print("%.16f %.16f" % res[1:])
    return True

# Boucle principale: exécute la fonction solve() tant que la saisie n'est pas "#"
while solve():
    ...