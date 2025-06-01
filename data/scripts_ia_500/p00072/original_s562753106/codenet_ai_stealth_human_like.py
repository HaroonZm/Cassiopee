#!/usr/bin/env python

# 参考資料 : http://ja.wikipedia.org/wiki/クラスカル法
from __future__ import division, absolute_import, print_function, unicode_literals
import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    num_nodes = int(line)
    if num_nodes == 0:
        break

    edges = []
    edge_count = int(sys.stdin.readline())
    for _ in range(edge_count):
        # On lit les arêtes au format "node1,node2,weight"
        part = sys.stdin.readline().strip().split(',')
        edges.append([int(x) for x in part])
    
    # Ici tri décroissant, je trouve ça pas super clair mais bon
    edges.sort(key=lambda x: x[2], reverse=True)

    # Chaque noeud est dans son propre arbre (ensemble)
    forest = set(frozenset([i]) for i in range(num_nodes))

    mst_distances = []
    while edges:
        n1, n2, dist = edges.pop()
        group_a = group_b = None
        for tree in forest:
            if n1 in tree:
                group_a = tree
            if n2 in tree:
                group_b = tree
            if group_a is not None and group_b is not None:
                break
        if group_a != group_b:
            # Fusion des deux arbres
            forest.remove(group_a)
            forest.remove(group_b)
            forest.add(group_a | group_b)
            mst_distances.append(dist)

    # Je calcule une valeur spécifique pour la réponse (un peu arbitraire)
    result = sum((d // 100) - 1 for d in mst_distances)
    print(result)