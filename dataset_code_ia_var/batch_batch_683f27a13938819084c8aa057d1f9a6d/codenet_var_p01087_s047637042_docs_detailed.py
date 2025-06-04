from sys import setrecursionlimit

# Augmente la limite de récursion pour permettre des appels récursifs profonds
setrecursionlimit(10 ** 8)

def mul(A):
    """
    Calcule le produit de tous les éléments d'une liste.

    Args:
        A (list): Liste de nombres à multiplier.

    Returns:
        int: Le produit de tous les éléments de la liste.
    """
    res = 1
    for a in A:
        res *= a
    return res

# Dictionnaire associant les opérateurs à leurs fonctions Python respectives
O = {'+': sum, '*': mul}

class Source:
    """
    Classe représentant la source de caractères à lire séquentiellement.

    Attributes:
        S (str): La chaîne de caractères à analyser.
        pos (int): La position courante dans la chaîne.
    """
    def __init__(self, S, i=0):
        """
        Initialise la source.

        Args:
            S (str): La chaîne de caractères source.
            i (int, optional): Position de départ dans la chaîne. Par défaut à 0.
        """
        self.S = S
        self.pos = i

def peek(S):
    """
    Retourne le caractère courant de la source sans changer la position,
    ou 'a' si la fin est atteinte.

    Args:
        S (Source): L'objet Source à examiner.

    Returns:
        str: Le caractère courant ou 'a' en fin de chaîne.
    """
    return S.S[S.pos] if S.pos < len(S.S) else 'a'

def next(S):
    """
    Avance la position de la source d'un caractère.

    Args:
        S (Source): L'objet Source dont il faut avancer la position.
    """
    S.pos += 1

def level_off(S):
    """
    Consomme tous les caractères '.' consécutifs à la position courante
    et retourne leur nombre.

    Args:
        S (Source): L'objet Source à analyser.

    Returns:
        int: Le nombre de '.' consommés.
    """
    lv = 0
    while peek(S) == '.':
        lv += 1
        next(S)
    return lv

def level(S):
    """
    Détermine combien de '.' consécutifs sont présents à la position courante,
    sans changer la position de la source.

    Args:
        S (Source): L'objet Source à analyser.

    Returns:
        int: Le nombre de '.' consécutifs trouvés à la position courante.
    """
    i = S.pos
    lv = 0
    while peek(S) == '.':
        lv += 1
        next(S)

    S.pos = i
    return lv

def expr(S, lv, ope):
    """
    Évalue une expression à un certain niveau d'imbrication donnée.

    Args:
        S (Source): Objet Source contenant la chaîne à analyser.
        lv (int): Le niveau courant de points ('.').
        ope (function): Fonction opérateur à appliquer (+ ou *).

    Returns:
        int: Le résultat de l'évaluation de l'expression.
    """
    A = []
    while peek(S) != 'a' and level(S) == lv:
        level_off(S)
        A.append(factor(S, lv))
    return ope(A)

def factor(S, lv):
    """
    Évalue un facteur de l'expression à un niveau donné.

    Args:
        S (Source): Objet Source contenant la chaîne à analyser.
        lv (int): Le niveau courant d'ancrage avec les '.'.

    Returns:
        int: La valeur du facteur.
    """
    if peek(S) in O:
        ope = O[peek(S)]
        next(S)
        return expr(S, lv + 1, ope)
    return num(S)

def num(S):
    """
    Lit et renvoie le chiffre à la position courante, puis avance la source.

    Args:
        S (Source): Objet Source contenant la chaîne à analyser.

    Returns:
        int: La valeur lue.
    """
    res = int(peek(S))
    next(S)
    return res

# Boucle principale lisant les cas de test
while True:
    n = int(input())
    if n == 0:
        break
    S = []
    for i in range(n):
        S.append(input())
    # Concatène toutes les lignes en une seule chaîne et évalue l'expression
    print(expr(Source(''.join(S)), 0, O['+']))