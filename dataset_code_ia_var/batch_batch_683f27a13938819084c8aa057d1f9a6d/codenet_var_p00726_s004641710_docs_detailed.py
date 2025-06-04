#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

# Augmente la limite de récursion pour gérer de grandes profondeurs d'appels récursifs,
# nécessaire lors de l'évaluation d'expressions très imbriquées.
sys.setrecursionlimit(1000000)

def check(c):
    """
    Vérifie si le caractère spécifié est un chiffre (0-9).

    Args:
        c (str): Caractère à vérifier.

    Returns:
        bool: True si le caractère est un chiffre, False sinon.
    """
    return (ord(c) >= ord('0') and ord(c) <= ord('9'))

def check2(c):
    """
    Vérifie si le caractère spécifié est une lettre majuscule (A-Z).

    Args:
        c (str): Caractère à vérifier.

    Returns:
        bool: True si le caractère est une lettre majuscule, False sinon.
    """
    return (ord(c) >= ord('A') and ord(c) <= ord('Z'))

# Boucle principale pour traiter plusieurs entrées jusqu'à fermeture avec '0'
while True:
    # Lecture de l'expression et de la position cible (N)
    S1, S2 = raw_input().split()
    if S1 == '0':
        # Fin du programme si l'expression est '0'
        break
    N = int(S2)
    SS = ''
    flag = False

    # Étape 1 : Ajoute des parenthèses ouvertes après un chiffre suivi d'une lettre (hors '(')
    # Ceci rend explicite la structure de répétition dans l'expression.
    for i in range(len(S1) - 1):
        SS += S1[i]
        if check(S1[i]) and not check(S1[i + 1]) and S1[i + 1] != '(':
            SS += '('
            flag = True
        elif flag:
            SS += ')'
            flag = False
    SS += S1[len(S1) - 1]
    if flag:
        SS += ')'

    # Ajoute des parenthèses globale autour de l'expression modifiée
    S1 = '(' + SS + ')'

    # Étape 2 : Entoure chaque lettre majuscule de guillemets, en traitant les cas de concaténation
    # et d'imbrication pour assurer que chaque lettre soit bien une chaîne de caractères lors de l'évaluation.
    for i in range(26):
        c = chr(ord('A') + i)
        S1 = S1.replace('(' + c, '("' + c)
        S1 = S1.replace(c + ')', c + '")')
        S1 = S1.replace(')' + c, ')"' + c)
        S1 = S1.replace(c + '(', c + '"(')
        for j in range(10):
            c2 = str(j)
            S1 = S1.replace(c + c2, c + '"' + c2)

    # Retire les parenthèses globales
    S1 = S1[1 : -1]

    # Remplace chaque parenthèse ouverte par une virgule pour faciliter l'évaluation ultérieure
    S1 = S1.replace('(', ',')

    # Étape 3 : Ajoute des parenthèses ouvertes après tout non-chiffre suivi d'un chiffre
    SS = ''
    for i in range(len(S1) - 1):
        SS += S1[i]
        if not check(S1[i]) and check(S1[i + 1]):
            SS += '('
    SS += S1[len(S1) - 1]

    # Si l'expression commence par un chiffre, ajoute une parenthèse ouvrante initiale
    if check(S1[0]):
        SS = '(' + SS

    # Ajoute (1, ...) au début pour normaliser la structure d'expression (permet d'avoir un racine uniforme)
    S1 = '(1, ' + SS + ')'

    # Nettoie les structures syntaxiques pour conformité à la syntaxe d'évaluation en Python
    S1 = S1.replace(')(', '),(')
    S1 = S1.replace(')"', '),"')
    S1 = S1.replace('"(', '",(')

    # Évalue dynamiquement la structure et génère un arbre mixant tuples et chaînes de caractères
    hoge = eval(S1)

    # Initialisation des variables pour calcul et mappage mémoire
    ans = 0
    m = {}

    def func(obj):
        """
        Parcours récursivement l'expression structurée et calcule la longueur totale de la séquence générée.
        Remplit également un dictionnaire de mappage mémoire pour des sous-expressions afin d'éviter de multiples calculs.

        Args:
            obj (tuple or str): L'objet représentant une sous-expression ou une chaîne.

        Returns:
            int: La longueur de la séquence générée par cette sous-expression.
        """
        if type(obj) == type("hoge"):
            m[obj] = len(obj)
            return len(obj)
        num = obj[0]
        ret = 0
        for i in range(1, len(obj)):
            ret += num * func(obj[i])
        m[obj] = ret
        return ret

    def func2(obj, index):
        """
        Récupère récursivement le caractère à la position donnée dans la séquence déroulée sans générer toute la séquence.

        Args:
            obj (tuple or str): L'objet représentant une sous-expression ou une chaîne.
            index (int): La position cible dans la séquence finale.

        Returns:
            str: Le caractère à la position donnée ou '0' si non trouvé.
        """
        if type(obj) == type("hoge"):
            return obj[index]
        num = obj[0]
        S = m[obj]
        index %= S / num
        ret = 0
        for i in range(1, len(obj)):
            ret += m[obj[i]]
            if ret > index:
                ret -= m[obj[i]]
                return func2(obj[i], index - ret)
        return '0'

    # Calcule la longueur totale de la séquence
    func(hoge)

    # Si la position demandée est hors de portée, affiche '0'. Sinon, affiche le caractère à cette position.
    if N >= m[hoge]:
        print '0'
    else:
        print func2(hoge, N)