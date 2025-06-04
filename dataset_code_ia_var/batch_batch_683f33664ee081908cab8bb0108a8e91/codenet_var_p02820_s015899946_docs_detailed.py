import itertools
import math
import sys
import heapq
from collections import Counter
from collections import deque
from fractions import gcd

# Définition d'une très grande valeur pour l'infini
INF = 1 << 60

# Augmentation de la limite de récursion pour éviter les erreurs en cas de récursion profonde
sys.setrecursionlimit(10 ** 6)

def main():
    """
    Fonction principale qui lit les entrées, construit la séquence des coups
    à jouer pour maximiser le score au jeu de pierre-feuille-ciseaux selon
    certaines contraintes, et affiche le score maximal possible.

    Entrées :
    - n : nombre total de rounds
    - k : nombre de rounds consécutifs après lesquels un même coup est interdit
    - r, s, p : points pour vaincre respectivement 'pierre', 'ciseaux', 'feuille'
    - t : séquence des coups de l'adversaire sous forme de chaîne ('r', 's', 'p')

    Sortie :
    - Affiche le score maximal possible
    """
    # Lecture des paramètres n (nombre de coups), k (contrainte d'interdiction d'un même coup)
    n, k = map(int, input().split())
    
    # Lecture des scores associés : r (contre 'pierre'), s (contre 'ciseaux'), p (contre 'feuille')
    r, s, p = map(int, input().split())
    
    # Lecture de la séquence des coups adverses
    t = input()
    
    # Génération de la séquence optimale de coups à jouer contre l'adversaire
    a = create_optimal_moves(t)
    
    # Calcul du score initial sans tenir compte des contraintes
    ans = calculate_initial_score(a, r, s, p)
    
    # Ajustement du score pour respecter la règle d'interdiction (pas deux fois le même 'gagnant' à k d'intervalle)
    ans = adjust_for_constraints(a, n, k, r, s, p, ans)
    
    # Affichage du score final
    print(ans)

def create_optimal_moves(t):
    """
    Génère la séquence des coups optimaux maximisant le score contre la séquence de l'adversaire.
    Pour chaque coup de l'adversaire, on répond par le coup qui gagne contre lui.

    Args:
        t (str): Séquence des coups de l'adversaire ('r', 's', 'p')

    Returns:
        str: Séquence de coups optimaux
    """
    a = ""
    for i in t:
        if i == "r":
            a += "p"  # 'p' bat 'r'
        elif i == "s":
            a += "r"  # 'r' bat 's'
        else:
            a += "s"  # 's' bat 'p'
    return a

def calculate_initial_score(a, r, s, p):
    """
    Calcule le score initial pour la séquence de coups optimaux, sans tenir compte de la contrainte
    sur les coups répétés à intervalles k.

    Args:
        a (str): Séquence des coups joués
        r (int): Score pour 'r'
        s (int): Score pour 's'
        p (int): Score pour 'p'

    Returns:
        int: Score total initial
    """
    ans = 0
    for i in a:
        if i == "r":
            ans += r
        elif i == "s":
            ans += s
        else:
            ans += p
    return ans

def adjust_for_constraints(a, n, k, r, s, p, ans):
    """
    Ajuste le score pour respecter la contrainte qui interdit de jouer deux fois de suite le même
    coup gagnant espacés de k (si c'est le cas, il faut ignorer le deuxième gain).

    Args:
        a (str): Séquence initiale des coups joués
        n (int): Longueur de la séquence
        k (int): Contrainte d'espacement des coups identiques
        r (int): Score pour 'r'
        s (int): Score pour 's'
        p (int): Score pour 'p'
        ans (int): Score initial sans les contraintes

    Returns:
        int: Score ajusté prenant en compte la contrainte
    """
    # Pour pouvoir marquer les coups interdits, il faut un tableau mutable
    a = list(a)
    for i in range(k, n):
        # Si à k intervalles d'écart on retrouve le même coup, on annule le gain du second coup
        if a[i] == a[i - k]:
            if a[i] == "r":
                ans -= r
            elif a[i] == "s":
                ans -= s
            else:
                ans -= p
            # Marque ce coup comme utilisé/annulé en le remplaçant
            a[i] = "a"
    return ans

if __name__ == "__main__":
    main()