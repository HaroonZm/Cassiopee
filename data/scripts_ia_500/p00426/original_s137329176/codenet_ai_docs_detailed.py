from collections import deque
from math import log2

ans = []

while True:
    # Lecture de deux entiers N et M depuis l'entrée standard
    N, M = map(int, input().split())
    # Condition d'arrêt : si N=0 et M=0, on termine la boucle
    if (N, M) == (0, 0):
        break

    # Initialisation des entiers a, b, c qui représenteront des ensembles
    a, b, c = 0, 0, 0

    # Lecture des trois ensembles
    for i in range(3):
        A = list(map(int, input().split()))
        # Si le nombre d'éléments n'est pas nul
        if A[0] != 0:
            # Selon i, on met à jour a, b ou c avec un masque de bits
            if i == 0:
                for j in range(A[0]):
                    # Mise à 1 du bit correspondant à l'élément A[1+j]-1
                    a += 1 << (A[1 + j] - 1)
            elif i == 1:
                for j in range(A[0]):
                    b += 1 << (A[1 + j] - 1)
            else:
                for j in range(A[0]):
                    c += 1 << (A[1 + j] - 1)

    # Construction d'une file pour la recherche en largeur (BFS)
    # Chaque élément est un tuple : (compteur de mouvements, a, b, c, action précédente)
    d = deque([(0, a, b, c, '')])

    while len(d) > 0:
        # Extraction du premier élément de la file (FIFO)
        cnt, a, b, c, prev = d.popleft()

        # Si le compteur dépasse la limite M, on abandonne ce cas
        if cnt > M:
            ans.append(-1)  # Pas de solution dans M coups
            break

        # Condition d'arrêt : on veut que l'intersection des ensembles soit évitée
        # Si l'union de a et b est vide, ou b et c est vide, on a une solution
        if a + b == 0 or b + c == 0:
            ans.append(cnt)
            break

        # Calcul du bit de poids le plus élevé dans chacun des ensembles a, b, c
        # Ce bit représente la "valeur maximale" présente dans l'ensemble
        if a == 0:
            amax = -1
        else:
            amax = int(log2(a))
        if b == 0:
            bmax = -1
        else:
            bmax = int(log2(b))
        if c == 0:
            cmax = -1
        else:
            cmax = int(log2(c))

        # Application des règles de déplacement selon la valeur maximale et l'action précédente

        # Si la valeur maximale dans a est supérieure à celle dans b, et que le précédent n'était pas 'ba'
        # On effectue un déplacement de a vers b en décalant les bits
        if amax > bmax and prev != 'ba':
            d.append((cnt + 1,
                      a - (1 << amax),
                      b + (1 << amax),
                      c,
                      'ab'))

        # Inversement, si la valeur maximale dans a est inférieure à celle dans b, et que le précédent n'était pas 'ab'
        # Déplacement de b vers a
        elif amax < bmax and prev != 'ab':
            d.append((cnt + 1,
                      a + (1 << bmax),
                      b - (1 << bmax),
                      c,
                      'ba'))

        # De même, déplacements entre c et b selon leurs valeurs maximales et action précédente

        if cmax > bmax and prev != 'bc':
            d.append((cnt + 1,
                      a,
                      b + (1 << cmax),
                      c - (1 << cmax),
                      'cb'))
        elif cmax < bmax and prev != 'cb':
            d.append((cnt + 1,
                      a,
                      b - (1 << bmax),
                      c + (1 << bmax),
                      'bc'))

# Affichage de toutes les réponses accumulées, une par ligne
print(*ans, sep='\n')