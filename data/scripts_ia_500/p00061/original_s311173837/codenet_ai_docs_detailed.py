#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def read_scores():
    """
    Lit les entrées standard ligne par ligne jusqu'à rencontrer une ligne
    commençant par '0,0'. Chaque ligne avant cette condition doit contenir
    deux entiers séparés par une virgule.

    Retourne:
        list of tuples: Une liste de tuples (id, point) où id et point sont des entiers.
    """
    scores = []
    while True:
        line = stdin.readline()
        if line.startswith('0,0'):
            break
        # Convertit la chaîne en tuple (id, point) d'entiers
        scores.append(tuple(int(s) for s in line.split(',')))
    return scores

def sort_scores_desc(scores):
    """
    Trie une liste de tuples (id, point) en fonction des points en ordre décroissant.

    Args:
        scores (list of tuples): Liste de tuples (id, point).

    Returns:
        list of tuples: Liste triée en fonction de point (décrémental).
    """
    # Trie par point, ordre décroissant (reverse=True)
    return sorted(scores, key=lambda id_point: id_point[1], reverse=True)

def compute_order_for_id(sorted_scores, query_id):
    """
    Calcule le classement (order) d'un joueur identifié par query_id basé sur la liste triée
    des scores. Le classement prend en compte les égalités (mêmes points -> même rang).

    Args:
        sorted_scores (list of tuples): Liste triée (id, point) par ordre décroissant de point.
        query_id (int): Identifiant du joueur recherché.

    Returns:
        int: Le rang du joueur (commence à 1 pour le meilleur score).
    """
    order = 0  # Rang actuel
    p = None   # Dernier point rencontré
    for id, point in sorted_scores:
        if p != point:
            p = point
            order += 1  # Nouveau rang pour un nouveau score
        if id == query_id:
            return order
    return None  # Si query_id non trouvé dans la liste

def main():
    """
    Fonction principale exécutant le programme :
    - Lit et stocke les scores.
    - Trie les scores.
    - Pour chaque identifiant lu en entrée, affiche le rang correspondant.
    """
    scores = read_scores()
    sorted_scores = sort_scores_desc(scores)

    for line in stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        order = compute_order_for_id(sorted_scores, n)
        if order is not None:
            print(order)

if __name__ == "__main__":
    main()