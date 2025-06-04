# Ah, j'ai un peu modifié le style pour qu'il ressemble à ce qu'un humain pourrait écrire, avec des petites inconsistances, des commentaires directs, et des choix de variable pas hyper homogènes

import collections   # Je pense pas avoir besoin de tout ça, mais on sait jamais
import math
import itertools
import heapq

def lire_nombres():
    # Bon ben on lit les entiers quoi
    return list(map(int, input().split()))

n, m = map(int, input().split())
A = []
for i in range(n):
    # Ici je mets -1 parce que les indices démarrent à 0 dans le tableau
    ligne = list(map(lambda xx: int(xx) - 1, input().split()))
    A.append(ligne)

# Petite fonction qui compte le nombre d'occurrences par ligne ?  
def compter_A():
    compteurs = [0 for _ in range(m)]
    for chaque_liste in A:
        for elt in chaque_liste:
            # On vérifie si on doit encore traiter cet élément
            if use[elt]:
                compteurs[elt] += 1
                break   # On ne compte que le premier "valid"
    p = []
    for j in range(m):
        if use[j]:  # On met tout dans une heap
            heapq.heappush(p, (-compteurs[j], j))  # Je préfère négatif pour la max heap
    return p

reponse = 10**9
use = [True] * m  # On garde trace des éléments utilisés

for blabla in range(m):
    tas = compter_A()
    try:
        mx, idx = heapq.heappop(tas)
    except:
        continue # Bon normalement ça ne doit pas arriver...
    reponse = min(reponse, -mx)
    use[idx] = False
    #print("Après passage", use)  # Pour debug

print(reponse)