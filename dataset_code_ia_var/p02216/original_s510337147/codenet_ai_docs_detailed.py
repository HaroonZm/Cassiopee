import sys
from collections import deque, Counter
import math

# Redéfinition de la fonction d'entrée rapide
input = sys.stdin.readline

# Augmente la limite de récursion pour éviter les erreurs dans certains cas limites
sys.setrecursionlimit(1000000)

# Déclare une constante d'infini pour de potentiels usages (pas utilisée ici)
INF = 10 ** 20

def getN():
    """
    Lis une ligne de l'entrée standard et la convertit en entier.

    Returns:
        int: l'entier lu depuis l'entrée standard.
    """
    return int(input())

def getList():
    """
    Lis une ligne de l'entrée standard et la convertit en une liste d'entiers.

    Returns:
        List[int]: liste d'entiers lue depuis l'entrée standard.
    """
    return list(map(int, input().split()))

def main():
    """
    Point d'entrée principal du programme.
    
    Décide du vainqueur ("First" ou "Second") d'un jeu à partir d'une liste de nombres en fonction des règles suivantes :
      - Calcule la somme de la liste et si cette somme est paire ou impaire (reste modulo 2).
      - Si la longueur de la liste (n) est impaire :
           - Si la somme est impaire, "First" gagne, sinon "Second" gagne.
      - Si la longueur de la liste (n) est paire :
           - Recherche le minimum (mn) de la liste.
           - Si la somme est impaire et tous les nombres sont égaux (sm == mn * n), "Second" gagne.
           - Si la somme est impaire et tous les nombres ne sont pas égaux, "First" gagne.
           - Si la somme est paire et le plus petit nombre est impair, "First" gagne.
           - Si la somme est paire et le plus petit nombre est pair, "Second" gagne.
    Affiche le résultat sur la sortie standard.
    """
    n = getN()              # Nombre d'éléments de la liste
    nums = getList()        # Liste des entiers
    sm = sum(nums)          # Somme des éléments de la liste
    ans = sm % 2            # Parité de la somme (0 si paire, 1 si impaire)

    # Cas où le nombre d'éléments est impair
    if n % 2 == 1:
        if ans == 1:
            print("First")
        else:
            print("Second")
        return
    
    # Cas où le nombre d'éléments est pair
    if n % 2 == 0:
        mn = min(nums)  # Recherche du plus petit nombre de la liste
        if ans == 1:
            # Si tous les nombres sont égaux, "Second" gagne, sinon "First"
            if sm == mn * n:
                print("Second")
            else:
                print("First")
        else:
            # Si le plus petit nombre est impair, "First" gagne, sinon "Second"
            if mn % 2 == 1:
                print("First")
            else:
                print("Second")

# Point d'entrée du script, exécute la fonction principale si ce fichier est lancé directement
if __name__ == "__main__":
    main()