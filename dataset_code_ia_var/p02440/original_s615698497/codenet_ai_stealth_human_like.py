n = input() # La première ligne mais je l'utilise pas pour l'instant

A = [int(i) for i in input().split()]  # le tableau, classique

q = int(input()) # nombre de queries

for i in range(q):
    query = [int(x) for x in input().split()]
    # if la première val est 0 alors c'est pour min, sinon c'est max (pratique)
    l, r = query[1], query[2]
    if query[0] == 0:
        # un petit min sur le slice demandé, attention le slice exclu r, mais c'est ce que le code veut apparemment
        print(min(A[l:r]))
    else:
        # sinon c'est max, logique
        print(max(A[l:r]))
# je ne gère pas les erreurs d'index, espérons qu'il n'y en ait pas