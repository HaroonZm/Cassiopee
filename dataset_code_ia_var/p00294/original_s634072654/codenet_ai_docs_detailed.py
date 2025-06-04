"""
Ce script Python prend en entrée plusieurs paramètres, transforme et trie une liste d'entiers,
puis calcule une valeur minimale basée sur des conditions spécifiques.
Chaque fonction a été dotée d'une docstring complète, et les sections principales ont été commentées.
"""

import itertools as ite   # Import du module itertools pour des itérateurs efficaces (non utilisé dans ce code mais maintenu)
import math               # Import du module math pour des opérations mathématiques (non utilisé dans ce code mais maintenu)

# Définition d'une valeur infinie largement suffisante pour éviter le dépassement
INF = 10 ** 18

def read_input():
    """
    Lit les entrées utilisateur depuis l'entrée standard (compatible Python 2).

    Retourne:
        N (int): La valeur N entrée par l'utilisateur.
        M (int): La valeur M entrée par l'utilisateur.
        p (int): La valeur p entrée par l'utilisateur.
        ls (List[int]): Liste des valeurs transformées selon les règles du problème.
    """
    # Lecture et séparation des trois premiers entiers
    N, M, p = map(int, raw_input().split())

    ls = []
    # Lecture de M valeurs, transformation puis ajout à la liste.
    for i in range(M):
        # Pour chaque ligne, soustrait p puis prend le modulo N.
        val = (input() - p) % N
        ls.append(val)
    return N, M, p, ls

def compute_min_value(N, M, ls):
    """
    Calcule la réponse minimale basée sur les valeurs de la liste transformée.

    Args:
        N (int): Paramètre N du problème.
        M (int): Nombre de valeurs dans la liste.
        ls (List[int]): Liste d'entiers transformés.

    Retourne:
        int: La valeur minimale trouvée via les différents calculs, multipliée par 100.
    """
    # Trie la liste entière afin de faciliter les opérations ultérieures
    ls = sorted(ls)

    # Initialise la variable réponse avec un des deux cas extrêmes:
    # soit l'écart maximum vers la droite, soit le complément à gauche du minimum.
    ans = min(ls[-1], N - ls[0])

    # Pour chaque paire consécutive dans la liste triée, calcule deux longueurs,
    # puis actualise la réponse avec le minimum parmi plusieurs combinaisons possibles.
    for i in range(M - 1):
        len1 = ls[i]
        len2 = N - ls[i + 1]
        ans = min(ans, len1 * 2 + len2, len2 * 2 + len1)
    
    # Multiplie le résultat final par 100 (comme requis par l'énoncé)
    return ans * 100

def main():
    """
    Fonction principale qui orchestre la lecture des données, le calcul et l'affichage du résultat.
    """
    # Lecture des données d'entrée
    N, M, p, ls = read_input()
    # Calcul de la réponse minimale attendue
    result = compute_min_value(N, M, ls)
    # Affichage du résultat final
    print result

# Exécution du code principal si le script est lancé directement
if __name__ == "__main__":
    main()