import sys

# Import sys module to access standard input and set recursion limit
stdin = sys.stdin

# Increase maximum recursion limit to prevent stack overflow on large recursive calls
sys.setrecursionlimit(10 ** 7)

def li():
    """
    Lis une ligne depuis l'entrée standard, la divise selon les espaces,
    convertit chaque élément en int, et renvoie un itérable de ces entiers.
    """
    return map(int, stdin.readline().split())

def li_():
    """
    Lis une ligne depuis l'entrée standard, la divise selon les espaces,
    convertit chaque élément en int, puis soustrait 1 à chaque valeur.
    Retourne un itérable de ces valeurs pour le cas d'indexation à partir de zéro.
    """
    return map(lambda x: int(x) - 1, stdin.readline().split())

def lf():
    """
    Lis une ligne depuis l'entrée standard, la divise selon les espaces,
    convertit chaque élément en float, et renvoie un itérable de ces flottants.
    """
    return map(float, stdin.readline().split())

def ls():
    """
    Lis une ligne depuis l'entrée standard et la divise en une liste de chaînes par espace.
    """
    return stdin.readline().split()

def ns():
    """
    Lis une ligne depuis l'entrée standard, enlève le retour à la ligne final,
    et retourne la chaîne résultante.
    """
    return stdin.readline().rstrip()

def lc():
    """
    Lis une ligne depuis l'entrée standard (sans le retour à la ligne)
    et retourne la chaîne sous forme de liste de caractères.
    """
    return list(ns())

def ni():
    """
    Lis une ligne depuis l'entrée standard, la convertit en entier, puis la retourne.
    """
    return int(stdin.readline())

def nf():
    """
    Lis une ligne depuis l'entrée standard, la convertit en float, puis la retourne.
    """
    return float(stdin.readline())

from collections import defaultdict

# Lecture de la chaîne à traiter depuis l'entrée standard
s = ns()

# Création d'un dictionnaire comptant les occurrences de chaque caractère de la chaîne
dic = defaultdict(int)
for si in s:
    dic[si] += 1

# Vérification de la condition : chaque caractère doit apparaître exactement deux fois
ok = True
for _, v in dic.items():
    if v != 2:
        ok = False
        break

# Affichage du résultat en fonction de la vérification
print("Yes" if ok else "No")