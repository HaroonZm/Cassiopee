"""
Ce script lit deux entiers du standard input représentant respectivement
le nombre d'éléments pairs (N_gu) et le nombre d'éléments impairs (M_ki).
Son but est de calculer le nombre de façons de choisir deux éléments
dont la somme est paire (c'est-à-dire soit deux pairs soit deux impairs),
en utilisant des fonctions de combinaison.

Fonctions utilitaires sont ajoutées avec des docstrings détaillées,
et des commentaires expliquent chaque étape du code.
"""

from math import factorial

def kumiawase_num(n, r):
    """
    Calcule le nombre de combinaisons possibles (nCr) pour choisir r éléments parmi n.
    Paramètres:
        n (int): Nombre total d'éléments disponibles.
        r (int): Nombre d'éléments à choisir.
    Retour:
        int: Le nombre de façons de choisir r éléments parmi n, ou 0 si n < r.
    """
    if n < r:
        # Impossible de choisir plus d'éléments qu'il n'en existe.
        return 0
    # Formule de combinaison : n! / (r! * (n-r)!)
    return factorial(n) // (factorial(r) * factorial(n - r))

def kumiawase_jufuku(n, r):
    """
    Calcule le nombre de combinaisons avec répétition possibles 
    pour choisir r éléments parmi n types (combinaison multiset).
    Paramètres:
        n (int): Nombre de types d'éléments.
        r (int): Nombre d'éléments à choisir (avec répétition).
    Retour:
        int: Le nombre de combinaisons avec répétition, ou 0 si n < r.
    """
    if n < r:
        # Impossible de choisir plus d'éléments qu'il n'en existe, même avec répétition.
        return 0
    # Formule de combinaison avec répétition : C(n+r-1, r)
    return kumiawase_num(n + r - 1, r)

# Lecture et initialisation des entrées utilisateur
# N_gu : nombre d'éléments pairs
# M_ki : nombre d'éléments impairs
N_gu, M_ki = map(int, input().split())

# Calcul du nombre de façons de choisir 2 éléments pairs (dont la somme sera paire)
gu_gu = kumiawase_num(N_gu, 2)
# Calcul du nombre de façons de choisir 2 éléments impairs (dont la somme sera aussi paire)
ki_ki = kumiawase_num(M_ki, 2)

# Affichage du résultat qui est la somme des deux possibilités ci-dessus
print(gu_gu + ki_ki)