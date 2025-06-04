import sys
from bisect import bisect as br
from collections import Counter

# Faster input reading for large data
readline = sys.stdin.readline

def check(A, B):
    """
    Effectue une série de vérifications sur deux séquences A et B pour déterminer 
    s'il est possible de transformer la séquence A en B sous certaines contraintes.

    Args:
        A (list of int): La première liste d'entiers.
        B (list of int): La seconde liste d'entiers.

    Returns:
        str: 'Yes' si la transformation est possible, 'No' sinon.
    """

    # On trie d'abord les deux listes pour faciliter la comparaison élément par élément
    SA = sorted(A)
    SB = sorted(B)

    # Première vérification : chaque élément de SA doit être <= correspondant dans SB
    # Si un élément de SA est strictement supérieur à SB, la transformation est impossible
    if any(a > b for a, b in zip(SA, SB)):
        return 'No'
    
    # Deuxième vérification : si A est déjà "inférieure ou égale" à B, c'est gagné
    # Cela vérifie la condition initiale sur les éléments correspondants
    if all(a <= b for a, b in zip(A, B)):
        return 'Yes'
    
    # Troisième vérification : on vérifie pour chaque position, si le nombre d'éléments
    # de SA <= SB[i] est strictement égal à i+1, sinon, transformation possible.
    # Cela teste une propriété de permutation.
    N = len(A)
    if any(br(SA, SB[i]) != i + 1 for i in range(N)):
        return 'Yes'
    
    # Quatrième vérification : si doublons dans A ou B, c'est possible
    if len(set(A)) != N or len(set(B)) != N:
        return 'Yes'

    # Cinquième vérification : on construit la permutation des indices reliant SA à SB via A/B
    # P[i] sera l'indice dans B qui correspond à l'élément trié position i de A
    # On mappe d'abord les valeurs de A et B à leurs indices finaux
    P = [None] * N
    Aidx = Counter()
    Bidx = Counter()

    # On enregistre pour chaque nombre de A (ou B) son dernier indice d'apparition
    for i in range(N):
        a = A[i]
        b = B[i]
        Aidx[a] = i
        Bidx[b] = i

    # On crée la permutation P en associant la position du i-ème élément trié de A à celle de B
    for i in range(N):
        sa = SA[i]
        sb = SB[i]
        P[Aidx[sa]] = Bidx[sb]

    # Parcours du cycle de permutations pour détecter si toute la permutation est cyclique
    # Si le cycle couvre toute la permutation (sans coupure), alors c'est 'No'
    # Sinon, c'est 'Yes'
    visited = set()
    vn = 0
    while vn not in visited:
        visited.add(vn)
        vn = P[vn]
    if len(visited) == N:
        return 'No'
    return 'Yes'

# Lecture des entrées standard
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

# Affichage du résultat selon le test sur A et B
print(check(A, B))