import sys

# Augmente la limite de récursion pour permettre des appels récursifs profonds dans l'algorithme de GCD
sys.setrecursionlimit(10 ** 6)

# Fonctions utilitaires pour la lecture des entrées
int1 = lambda x: int(x) - 1  # Convertit en entier (base 0)
p2D = lambda x: print(*x, sep="\n")  # Affiche une liste ligne par ligne

def MI():
    """
    Lit une ligne de l'entrée standard et retourne un itérable de ses éléments convertis en int.
    Renvoie :
        map(int): Un itérateur de nombres entiers lus depuis l'entrée.
    """
    return map(int, sys.stdin.readline().split())

def LI():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers.
    Renvoie :
        list[int]: Une liste de nombres entiers lus depuis l'entrée.
    """
    return list(map(int, sys.stdin.readline().split()))

def LLI(rows_number):
    """
    Lit plusieurs lignes de l'entrée standard, chacune convertie en liste d'entiers.
    Args:
        rows_number (int): Le nombre de lignes à lire.
    Renvoie :
        list[list[int]]: Une liste contenant rows_number listes d'entiers.
    """
    return [LI() for _ in range(rows_number)]

def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) entre deux entiers,
    en utilisant un algorithme fondé sur l'arithmétique binaire (variant du PGCD d'Euclide).
    Args:
        a (int): Premier entier.
        b (int): Second entier.
    Renvoie :
        int: Le PGCD de a et b.
    """
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    k = a.bit_length() - b.bit_length()
    return gcd(b, a ^ (b << k))

def main():
    """
    Fonction principale du programme.
    Utilise l'arithmétique binaire pour gérer des entiers représentés comme coefficients d'un polynôme, calcule le PGCD binaire,
    puis détermine le nombre d'entiers possibles inférieurs à une valeur maximale donnée, en respectant certaines contraintes bit-à-bit.
    """
    md = 998244353  # Module pour le calcul du résultat final

    # Lecture des valeurs n (nombre d'éléments) et x (borne supérieure en binaire)
    n, x = input().split()
    x = int(x, 2)  # Conversion de x depuis la base binaire

    # Lecture de n chaînes binaires à stocker dans la liste aa
    aa = [input() for _ in range(int(n))]
    aa = [int(a, 2) for a in aa]  # Conversion de chaque chaîne en entier

    # Considérer les bits des nombres comme des coefficients de polynômes
    # Calculer le PGCD binaire sur tous les éléments de aa
    g = aa[0]
    for a in aa[1:]:
        g = gcd(g, a)

    # La solution possible se base sur le quotient de x avec le bit le plus significatif du PGCD
    ans = x >> (g.bit_length() - 1)
    s = 0

    # On ajuste s pour maximiser son alignement avec x tout en restant <= x
    while True:
        # Recherche le décalage possible en partant du bit de poids fort
        k = (x ^ s).bit_length() - g.bit_length()
        if k < 0:
            break
        s ^= g << k  # Ajuste s avec un GCD décalé

    # Si la valeur finale de s reste inférieure ou égale à x, on peut encore en ajouter une
    if s <= x:
        ans += 1

    # Affichage de la réponse modulo md
    print(ans % md)

# Point d'entrée du programme
main()