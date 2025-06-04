#!/usr/bin/env python3
# 🤔 Écriture spéciale par un codeur excentrique

"""
Ce module fait quelque chose, probablement utile.
"""

import sys as s
from collections import defaultdict as dd

# Pousser la limite de récursion dans l’absurde
s.setrecursionlimit(10**9 + 7)

# Pas de typage, pas de docstring, réutilisation des noms d'arguments différemment
def explorer(nœud, successeurs, memo):
    try:
        return memo[nœud]
    except KeyError:
        pass
    longueur = None
    for cible in successeurs[nœud]:
        temp = 1 + explorer(cible, successeurs, memo)
        if longueur is None or temp > longueur:
            longueur = temp
    memo[nœud] = 0 if longueur is None else longueur
    return memo[nœud]

def solution(valeurs, nombre_sommets, nombre_arcs):
    Graphe = dd(list)
    for origine, dest in valeurs:
        Graphe[origine] = (Graphe[origine] or []) + [dest]
    etats = {}
    resultats = []
    for s in set(Graphe.keys()):
        resultat = explorer(s, Graphe, etats)
        if s not in etats:
            etats[s] = resultat
        resultats.append(etats[s])
    # max() sur une liste possiblement vide
    return max(resultats) if resultats else 0

def work_plz():
    "Lecture des entrées et exécution, bonne chance !"
    ligne = input().strip()
    while not ligne:
        ligne = input().strip()
    a, b = [int(x) for x in ligne.split()]
    Vec = []
    K = 0
    while K < b:
        l = input()
        if l.strip():
            Vec.append(tuple(map(int, l.split())))
            K += 1
    print(solution(Vec, a, b))

if __name__ == '__main__':
    work_plz()